#!/usr/bin/env python3
"""
Consolidate per-prop_type/crime_type het CSVs into per-estimator master files
that make_spec_explorer() in generate_charts.py expects.

For each estimator subdir under 00het_battery/:
  Read all het_nearfar_*.csv files
  Concatenate into ONE DataFrame
  Normalize prop_type labels: ALL_resid / ALL_nonresid → All
  Normalize crime_type:       total_spatial → total
  Drop wide-far (0.5-1.0 mi) rows
  Coerce numeric columns; drop rows that fail
  Save as {EST}/{EST}_master.csv

Input:  ~/Projects/.../00het_battery/{OLS, GLS, GLS_Pctrl, GLS_Hurin_Pctrl}/het_nearfar_*.csv
Output: ~/Projects/.../00het_battery/{EST}/{EST}_master.csv
"""

import pandas as pd
from pathlib import Path
import re

CHICAGO = Path.home() / 'Projects' / 'crime_property' / 'chicago'
HET_DIR = CHICAGO / 'output' / '00results' / '00het_battery'

ESTIMATORS = ['OLS', 'OLS_Pctrl', 'GLS', 'GLS_Pctrl', 'GLS_Hurin_Pctrl', 'Hurin', 'Hurin_Pctrl']

PROP_TYPE_RENAME = {}   # keep raw labels (ALL_resid, ALL_nonresid, SF, Condo, Multi, Townhouse)
CRIME_RENAME = {
    # Keep total_spatial as-is (it's the canonical "total minus domestic" variable).
    # total_spatial_dom collapses naturally to 'domestic' (the domestic-only slice).
    'total_spatial_dom': 'domestic',
}

NUM_COLS = ['beta_near','se_near','p_near','beta_far','se_far','p_far',
            'beta_diff','se_diff','p_diff','n']


def consolidate(est_dir: Path) -> int:
    csvs = sorted(est_dir.glob('het_nearfar_*.csv'))
    if not csvs:
        return 0
    out = est_dir / f'{est_dir.name}_master.csv'

    dfs = []
    for p in csvs:
        try:
            d = pd.read_csv(p, on_bad_lines='skip', engine='python')
        except Exception as e:
            print(f"    skip {p.name}: {e}")
            continue
        d = d.loc[:, [c for c in d.columns if not str(c).startswith('Unnamed')]]
        dfs.append(d)

    df = pd.concat(dfs, ignore_index=True)

    # ── Fix shifted post-side rows ─────────────────────────────────────────
    # Some rows have a column-shift: se_diff slot holds p_diff, p_diff slot
    # holds n, n slot holds eq_stage1, etc. Detect via p_diff > 1 (impossible
    # for a real p-value) and realign.
    if 'p_diff' in df.columns:
        df['p_diff'] = pd.to_numeric(df['p_diff'], errors='coerce')
        shifted = df['p_diff'] > 1
        if shifted.any():
            print(f"    realigning {int(shifted.sum())} shifted rows in {est_dir.name}")
            # Save old values then shift
            old_se_diff   = df.loc[shifted, 'se_diff'].copy() if 'se_diff' in df.columns else None
            old_p_diff    = df.loc[shifted, 'p_diff'].copy()
            old_n         = df.loc[shifted, 'n'].copy() if 'n' in df.columns else None
            old_eq_stage1 = df.loc[shifted, 'eq_stage1'].copy() if 'eq_stage1' in df.columns else None
            # Realign: shift columns RIGHT by 1 starting at se_diff
            if 'p_diff' in df.columns and old_se_diff is not None:
                df.loc[shifted, 'p_diff'] = pd.to_numeric(old_se_diff, errors='coerce')
            if 'n' in df.columns:
                df.loc[shifted, 'n'] = old_p_diff
            if 'eq_stage1' in df.columns and old_n is not None:
                df.loc[shifted, 'eq_stage1'] = old_n
            if 'eq_stage2' in df.columns and old_eq_stage1 is not None:
                df.loc[shifted, 'eq_stage2'] = old_eq_stage1
            if 'se_diff' in df.columns:
                # se_diff was lost during the shift. Approximate as
                # sqrt(se_near² + se_far²) — an overestimate (assumes independence)
                # but closer to truth than NaN/0/1.
                sn = pd.to_numeric(df.loc[shifted, 'se_near'], errors='coerce')
                sf = pd.to_numeric(df.loc[shifted, 'se_far'],  errors='coerce')
                df.loc[shifted, 'se_diff'] = ((sn**2 + sf**2)**0.5)

    # Drop wide-far (0.5-1.0 mi)
    if 'far_def' in df.columns:
        fd = df['far_def'].astype(str)
        df = df[~(fd.isin(['0.5-1.0','0.50-1.00']) | fd.str.startswith('0.5'))].copy()

    # Coerce numerics + drop rows where parse failed
    for c in NUM_COLS:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')
    # Only require numeric beta_near; the 'n' column is often shifted by the
    # source CSV's double-comma artifact on post-side rows. Build counts come
    # from len(merged) downstream, so a garbage 'n' column doesn't matter.
    df = df.dropna(subset=[c for c in ('beta_near',) if c in df.columns]).copy()

    # Drop rows where p-values fall outside [0, 1] — these are shifted-column
    # corruption (p_diff slot holds something else, like a sample-size value).
    for pcol in ('p_near', 'p_far', 'p_diff'):
        if pcol in df.columns:
            mask = (df[pcol] >= 0) & (df[pcol] <= 1)
            df = df[mask | df[pcol].isna()].copy()

    # Normalize labels
    if 'prop_type' in df.columns:
        df['prop_type'] = df['prop_type'].replace(PROP_TYPE_RENAME)
    if 'crime_type' in df.columns:
        df['crime_type'] = df['crime_type'].replace(CRIME_RENAME)

    df.to_csv(out, index=False)
    return len(df)


def main():
    for est in ESTIMATORS:
        est_dir = HET_DIR / est
        if not est_dir.exists():
            continue
        n = consolidate(est_dir)
        print(f"{est:<20s}  {n:>6} rows → {est}_master.csv")
        if n > 0:
            df = pd.read_csv(est_dir / f'{est}_master.csv')
            print(f"  prop_types: {sorted(df['prop_type'].dropna().unique())}")
            print(f"  crime_types: {sorted(df['crime_type'].dropna().unique())}")
            print(f"  fe_specs:   {sorted(df['fe_spec'].dropna().unique())}")
            print(f"  windows:    {sorted(df['window'].dropna().unique())}")
            print(f"  sides:      {sorted(df['side'].dropna().unique())}")


if __name__ == '__main__':
    main()
