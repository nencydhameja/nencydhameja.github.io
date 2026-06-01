#!/usr/bin/env python3
"""
Build spec-curve input CSV from the new long-format het battery.

Reads:
  ~/Projects/crime_property/chicago/output/00results/00het_battery/
      {OLS, GLS, GLS_Pctrl, GLS_Hurin_Pctrl}/het_nearfar_*.csv

Filters to one canonical headline slice and emits the legacy-schema CSV
that generate_charts.py:make_spec_curve() expects.

Default cell: prop_type='ALL_resid', est='GLS', pc='ctrl'
              (= the headline residential-tractmonth-demeaned + GLS+PC spec)

Output:
  ~/Projects/crime_property/chicago/output/00results/count_nearfar_crimetype_battery.csv
  (the schema generate_charts.py already knows how to read)
"""

import pandas as pd
from pathlib import Path
import re

CHICAGO = Path.home() / 'Projects' / 'crime_property' / 'chicago'
HET_DIR = CHICAGO / 'output' / '00results' / '00het_battery'
OUT_CSV = CHICAGO / 'output' / '00results' / 'count_nearfar_crimetype_battery.csv'

# Headline slice — what the spec curve renders by default.
TARGET_PROP_TYPE = 'ALL_resid'    # all properties, tract×month-demeaned
TARGET_EST       = 'GLS'          # GLS = Case-Shiller weighted (headline)
TARGET_PC        = 'ctrl'         # with persistence control

# crime_type rename: spec curve looks for 'total', files have 'total_spatial'
CRIME_RENAME = {
    'total_spatial':    'total',
    'total_spatial_dom':'domestic',
}

# test rename: spec curve expects 'perm_cum{n}_r{f}', files have 'cum_c{n}_r{f}'
TEST_RENAME_RE = re.compile(r'^cum_c(\d+)_r(\d+)$')

def rename_test(t: str) -> str:
    m = TEST_RENAME_RE.match(t)
    if m:
        return f'perm_cum{m.group(1)}_r{m.group(2)}'
    return t


def main():
    # ---- gather every het CSV across estimator subdirs ----
    csvs = []
    for subdir in ('OLS', 'GLS', 'GLS_Pctrl', 'GLS_Hurin_Pctrl'):
        csvs += list((HET_DIR / subdir).glob('het_nearfar_*.csv'))
    print(f"Found {len(csvs)} het CSVs")
    if not csvs:
        raise SystemExit("No het files found. Has the battery started writing yet?")

    dfs = []
    for p in csvs:
        try:
            d = pd.read_csv(p, on_bad_lines='skip', engine='python')
        except Exception as e:
            print(f"  WARN: skip {p.name}: {e}")
            continue
        # Drop the empty unnamed column created by the schema's stray double-comma
        d = d.loc[:, [c for c in d.columns if not str(c).startswith('Unnamed')]]
        dfs.append(d)

    df = pd.concat(dfs, ignore_index=True)
    print(f"  combined: {len(df):,} rows")
    print(f"  unique prop_type: {sorted(df['prop_type'].dropna().unique())}")
    print(f"  unique est:       {sorted(df['est'].dropna().unique())}")
    print(f"  unique pc:        {sorted(df['pc'].dropna().unique())}")
    print(f"  unique crime_type:{sorted(df['crime_type'].dropna().unique())}")

    # ---- filter to target cell ----
    mask = (
        (df['prop_type'] == TARGET_PROP_TYPE) &
        (df['est']       == TARGET_EST) &
        (df['pc']        == TARGET_PC)
    )
    sub = df[mask].copy()
    print(f"\n  rows in target cell ({TARGET_PROP_TYPE} × {TARGET_EST} × {TARGET_PC}): {len(sub):,}")

    if sub.empty:
        # Fallback: take whatever's available, warn loudly.
        print("  WARN: target cell empty. Falling back to first available "
              "(prop_type, est, pc) triple.")
        first = df[['prop_type','est','pc']].dropna().drop_duplicates().iloc[0]
        sub = df[
            (df['prop_type']==first['prop_type']) &
            (df['est']==first['est']) &
            (df['pc']==first['pc'])
        ].copy()
        print(f"  using fallback: {first.to_dict()} → {len(sub):,} rows")

    # ---- crime_type rename ----
    sub['crime_type'] = sub['crime_type'].replace(CRIME_RENAME)

    # ---- test token rename ----
    sub['test'] = sub['test'].astype(str).apply(rename_test)

    # ---- DROP wide-far specs (far ring = 0.5-1.0 mi) ----
    # These are the most-distant placebos / cumulative-far rings — excluded per
    # spec choice (too geographically diffuse to be a meaningful "far" comparison).
    n_before = len(sub)
    fd = sub['far_def'].astype(str)
    wide_far = fd.isin(['0.5-1.0', '0.50-1.00']) | fd.str.startswith('0.5')
    sub = sub[~wide_far].copy()
    print(f"\n  dropped wide-far (0.5-1.0 mi) rows: {n_before - len(sub):,} of {n_before:,}")

    # ---- emit only the columns spec curve needs ----
    keep = ['crime_type', 'test', 'window', 'fe_spec',
            'beta_near', 'se_near', 'p_near',
            'beta_far',  'se_far',  'p_far',
            'beta_diff', 'se_diff', 'p_diff', 'n']
    out = sub[[c for c in keep if c in sub.columns]].copy()

    # ---- coerce numeric columns + drop rows where parse failed
    # (defensive against any schema misalignment that lets text bleed in) ----
    num_cols = ['beta_near','se_near','p_near','beta_far','se_far','p_far',
                'beta_diff','se_diff','p_diff','n']
    for c in num_cols:
        if c in out.columns:
            out[c] = pd.to_numeric(out[c], errors='coerce')
    n_pre = len(out)
    out = out.dropna(subset=[c for c in ('beta_near','n') if c in out.columns]).copy()
    if len(out) < n_pre:
        print(f"  dropped {n_pre - len(out):,} rows with non-numeric beta_near/n")

    print(f"\n  output rows: {len(out):,}")
    print(f"  windows:   {sorted(out['window'].unique())}")
    print(f"  fe_specs:  {sorted(out['fe_spec'].unique())}")
    print(f"  crime_types: {sorted(out['crime_type'].unique())}")
    print(f"  test tokens (first 12): {sorted(out['test'].unique())[:12]}")

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT_CSV, index=False)
    print(f"\nSaved {OUT_CSV}")


if __name__ == '__main__':
    main()
