"""
Generate interactive Plotly charts for the crime-salience project page.

Outputs 4 standalone HTML files:
  - spatial_decay.html   (dropdown: window)
  - time_decay.html      (dropdown: view toggle)
  - crimetype_heatmap.html (side-by-side dropdowns: window + FE spec)
  - spec_curve.html      (mirror-style, 624 specs)
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────────
DATA_DIR = Path.home() / "Projects" / "crime_property" / "chicago" / "output" / "00results"
OUT_DIR = Path(__file__).parent

MAIN_CSV = DATA_DIR / "all_nearfar_stata_results.csv"
CRIME_CSV = DATA_DIR / "count_nearfar_crimetype_battery.csv"
POST_CSV = DATA_DIR / "post_sale_fixed_results.csv"

# ── Styling ──────────────────────────────────────────────────────────────────
RUST = "#672414"
TEXT_COLOR = "#1a1a18"
GRID_COLOR = "#d3d1c7"
BG_COLOR = "#ffffff"
GRAY = "#888780"
FONT = "Inter, sans-serif"
SIG_COLOR = RUST
NONSIG_COLOR = "#c4c0b8"

PLOTLY_CONFIG = {"displayModeBar": False, "responsive": True}

CRIME_LABELS = {
    "burglary": "Burglary", "disorder": "Disorder",
    "dom_battery": "Dom. Battery", "domestic": "Domestic",
    "drugvice": "Drug/Vice", "homicide": "Homicide",
    "nondom_assault": "Non-Dom. Assault", "nondom_violent": "Non-Dom. Violent",
    "property": "Property", "robbery": "Robbery",
    "sex_offenses": "Sex Offenses", "total": "Total Crime", "violent": "Violent",
}

FE_LABELS = {
    "PIN_CAM": "Tract×Month", "PIN_YM": "PIN×Year-Month",
    "PIN_CAY_YM": "Tract×Yr+YM", "PIN_TM": "Tract×Month (alt)",
}

FE_COLORS = {
    "PIN_CAM": RUST, "PIN_YM": "#2c5f8a",
    "PIN_CAY_YM": "#5a7d3a", "PIN_TM": "#8a6c2c",
}


def write_html(fig, filename):
    fig.write_html(
        OUT_DIR / filename, include_plotlyjs="cdn",
        full_html=True, config=PLOTLY_CONFIG,
    )
    print(f"  ✓ {filename}")


# ── Load data ────────────────────────────────────────────────────────────────
print("Loading data...")
df_main = pd.read_csv(MAIN_CSV)
df_crime = pd.read_csv(CRIME_CSV)
df_post = pd.read_csv(POST_CSV)


# ══════════════════════════════════════════════════════════════════════════════
# Chart A: Spatial Decay — dropdown for window
# ══════════════════════════════════════════════════════════════════════════════
def make_spatial_decay():
    print("Generating spatial_decay.html...")

    ring_order = ["near", "expanded", "near15", "near20", "mid", "donut", "far", "far25"]
    ring_labels = {
        "near": "Near (0.05mi)", "expanded": "Expanded (0.10mi)",
        "near15": "Near15 (0.15mi)", "near20": "Near20 (0.20mi)",
        "mid": "Mid (0.22mi)", "donut": "Donut (0.25mi)",
        "far": "Far (0.27mi)", "far25": "Far25 (0.30mi)",
    }
    ring_dist = {
        "near": 0.05, "expanded": 0.10, "near15": 0.15, "near20": 0.20,
        "mid": 0.22, "donut": 0.25, "far": 0.27, "far25": 0.30,
    }

    fe_specs = ["PIN_CAM", "PIN_YM"]
    windows = ["60d", "90d", "120d", "180d", "240d", "360d"]
    default_w = "180d"

    fig = go.Figure()
    traces_per_w = {}
    idx = 0

    for window in windows:
        mask = (df_main["section"] == "dilution") & (df_main["window"] == window)
        d = df_main[mask].copy()
        vis = window == default_w
        start = idx

        for spec in fe_specs:
            sub = d[(d["fe_spec"] == spec) & (d["ring"].isin(ring_order))].copy()
            sub["ri"] = sub["ring"].map({r: i for i, r in enumerate(ring_order)})
            sub = sub.sort_values("ri")

            x = [ring_labels.get(r, r) for r in sub["ring"]]
            y = sub["beta"].values * 100
            se = sub["se"].values * 100

            hover = [
                f"<b>{ring_labels.get(r,r)}</b><br>β: {b:.4f}%<br>SE: {s:.4f}%<br>p: {p:.4f}<br>N: {int(n):,}"
                for r, b, s, p, n in zip(sub["ring"], y, se, sub["p_val"], sub["n_obs"])
            ]

            c = FE_COLORS[spec]
            rgba = f"rgba({int(c[1:3],16)},{int(c[3:5],16)},{int(c[5:7],16)},0.10)"

            # CI band
            fig.add_trace(go.Scatter(
                x=x + x[::-1], y=list(y + 1.96*se) + list((y - 1.96*se)[::-1]),
                fill="toself", fillcolor=rgba, line=dict(color="rgba(0,0,0,0)"),
                showlegend=False, hoverinfo="skip", visible=vis,
            ))
            idx += 1

            # Line
            fig.add_trace(go.Scatter(
                x=x, y=y, mode="lines+markers",
                name=FE_LABELS[spec], line=dict(color=c, width=2.5),
                marker=dict(size=7, color=c),
                hovertemplate="%{customdata}<extra></extra>", customdata=hover,
                visible=vis, showlegend=vis,
            ))
            idx += 1

        traces_per_w[window] = (start, idx)

    fig.add_hline(y=0, line_dash="dot", line_color=GRAY, line_width=1)

    total = idx
    buttons = []
    for w in windows:
        s, e = traces_per_w[w]
        vis = [False]*total
        sl = [False]*total
        for i in range(s, e):
            vis[i] = True
            if i % 2 == 1:
                sl[i] = True
        buttons.append(dict(label=w, method="update",
            args=[{"visible": vis, "showlegend": sl},
                  {"title.text": f"Spatial Decay ({w} window)"}]))

    fig.update_layout(
        font=dict(family=FONT, color=TEXT_COLOR, size=13),
        paper_bgcolor=BG_COLOR, plot_bgcolor=BG_COLOR,
        margin=dict(l=60, r=30, t=80, b=50),
        title=dict(text=f"Spatial Decay ({default_w} window)", font=dict(size=16)),
        xaxis=dict(gridcolor=GRID_COLOR, zeroline=False),
        yaxis=dict(gridcolor=GRID_COLOR, zeroline=True, zerolinecolor=GRID_COLOR,
                   title="Effect on Log Sale Price (%)"),
        xaxis_title="Distance Ring",
        legend=dict(x=0.98, y=0.02, xanchor="right", yanchor="bottom",
                    bgcolor="rgba(255,255,255,0.8)", bordercolor=GRID_COLOR, borderwidth=0.5),
        height=460,
        hoverlabel=dict(bgcolor="white", font_size=12, font_family=FONT, bordercolor=GRID_COLOR),
        updatemenus=[dict(
            type="dropdown", x=0.0, y=1.14, xanchor="left", yanchor="top",
            bgcolor="white", bordercolor=GRID_COLOR, borderwidth=0.5, font=dict(size=12),
            buttons=buttons, active=windows.index(default_w),
        )],
        annotations=[dict(text="Window:", x=-0.02, y=1.17, xref="paper", yref="paper",
                          showarrow=False, font=dict(size=11, color=GRAY))],
    )

    write_html(fig, "spatial_decay.html")


# ══════════════════════════════════════════════════════════════════════════════
# Chart B: Time Decay
# ══════════════════════════════════════════════════════════════════════════════
def make_time_decay():
    print("Generating time_decay.html...")

    window_order = ["60d", "90d", "120d", "180d", "240d", "360d"]
    wl = {w: w.replace("d", " days") for w in window_order}
    fe_specs = ["PIN_CAM", "PIN_YM", "PIN_CAY_YM", "PIN_TM"]

    fig = go.Figure()

    # All FE specs — near ring
    for spec in fe_specs:
        mask = (df_main["section"] == "main") & (df_main["ring"] == "near") & (df_main["fe_spec"] == spec)
        sub = df_main[mask].copy()
        sub = sub[sub["window"].isin(window_order)]
        sub["wi"] = sub["window"].map({w: i for i, w in enumerate(window_order)})
        sub = sub.sort_values("wi")

        x = [wl[w] for w in sub["window"]]
        y = sub["beta"].values * 100
        se = sub["se"].values * 100

        hover = [
            f"<b>{wl[w]}</b><br>FE: {FE_LABELS[spec]}<br>β: {b:.4f}%<br>SE: {s:.4f}%<br>p: {p:.4f}<br>N: {int(n):,}"
            for w, b, s, p, n in zip(sub["window"], y, se, sub["p_val"], sub["n_obs"])
        ]

        fig.add_trace(go.Scatter(
            x=x, y=y, mode="lines+markers",
            name=FE_LABELS[spec], line=dict(color=FE_COLORS[spec], width=2.5),
            marker=dict(size=7, color=FE_COLORS[spec]),
            error_y=dict(type="data", array=1.96*se, visible=True,
                         color=FE_COLORS[spec], thickness=1.5, width=4),
            hovertemplate="%{customdata}<extra></extra>", customdata=hover,
        ))

    # Near vs far (hidden)
    for ring, color, name in [("near", RUST, "Near (0.05mi)"), ("far", NONSIG_COLOR, "Far (0.27mi)")]:
        mask = (df_main["section"] == "main") & (df_main["ring"] == ring) & (df_main["fe_spec"] == "PIN_CAM")
        sub = df_main[mask].copy()
        sub = sub[sub["window"].isin(window_order)]
        sub["wi"] = sub["window"].map({w: i for i, w in enumerate(window_order)})
        sub = sub.sort_values("wi")

        x = [wl[w] for w in sub["window"]]
        y = sub["beta"].values * 100
        se = sub["se"].values * 100

        hover = [
            f"<b>{name}</b> — {wl[w]}<br>β: {b:.4f}%<br>SE: {s:.4f}%<br>p: {p:.4f}"
            for w, b, s, p in zip(sub["window"], y, se, sub["p_val"])
        ]

        fig.add_trace(go.Scatter(
            x=x, y=y, mode="lines+markers", name=name,
            line=dict(color=color, width=2.5), marker=dict(size=7, color=color),
            error_y=dict(type="data", array=1.96*se, visible=True, color=color, thickness=1.5, width=4),
            hovertemplate="%{customdata}<extra></extra>", customdata=hover,
            visible=False,
        ))

    fig.add_hline(y=0, line_dash="dot", line_color=GRAY, line_width=1)

    n_fe = len(fe_specs)
    buttons = [
        dict(label="All FE specs", method="update",
             args=[{"visible": [True]*n_fe + [False, False]},
                   {"title.text": "Time Decay: Near-Crime Effect Across FE Specs"}]),
        dict(label="Near vs Far", method="update",
             args=[{"visible": [False]*n_fe + [True, True]},
                   {"title.text": "Time Decay: Near vs Far (Tract×Month FE)"}]),
    ]

    fig.update_layout(
        font=dict(family=FONT, color=TEXT_COLOR, size=13),
        paper_bgcolor=BG_COLOR, plot_bgcolor=BG_COLOR,
        margin=dict(l=60, r=30, t=80, b=50),
        title=dict(text="Time Decay: Near-Crime Effect Across FE Specs", font=dict(size=16)),
        xaxis=dict(gridcolor=GRID_COLOR, zeroline=False, title="Time Window"),
        yaxis=dict(gridcolor=GRID_COLOR, zeroline=True, zerolinecolor=GRID_COLOR,
                   title="Effect on Log Sale Price (%)"),
        legend=dict(x=0.98, y=0.02, xanchor="right", yanchor="bottom",
                    bgcolor="rgba(255,255,255,0.8)", bordercolor=GRID_COLOR, borderwidth=0.5),
        height=460,
        hoverlabel=dict(bgcolor="white", font_size=12, font_family=FONT, bordercolor=GRID_COLOR),
        updatemenus=[dict(
            type="dropdown", x=0.0, y=1.14, xanchor="left", yanchor="top",
            bgcolor="white", bordercolor=GRID_COLOR, borderwidth=0.5, font=dict(size=12),
            buttons=buttons, active=0,
        )],
        annotations=[dict(text="View:", x=-0.02, y=1.17, xref="paper", yref="paper",
                          showarrow=False, font=dict(size=11, color=GRAY))],
    )

    write_html(fig, "time_decay.html")


# ══════════════════════════════════════════════════════════════════════════════
# Chart C: Crime Type — SIDE-BY-SIDE dropdowns for window + FE spec
# ══════════════════════════════════════════════════════════════════════════════
def make_crimetype_heatmap():
    print("Generating crimetype_heatmap.html...")

    windows = [f"{m}m" for m in range(1, 13)]
    fe_specs = ["PIN_CAM", "PIN_YM", "PIN_CAY_YM", "PIN_TM"]
    default_w = "6m"
    default_fe = "PIN_CAM"

    # Build one trace per (window, fe_spec) combo
    fig = go.Figure()
    combo_idx = {}
    idx = 0

    for w in windows:
        for fe in fe_specs:
            mask = (df_crime["test"] == "main") & (df_crime["fe_spec"] == fe) & (df_crime["window"] == w)
            d = df_crime[mask].copy()
            d["abs_beta"] = d["beta_near"].abs()
            d = d.sort_values("abs_beta", ascending=True)

            y_labels = [CRIME_LABELS.get(c, c) for c in d["crime_type"]]
            betas = d["beta_near"].values * 100
            ses = d["se_near"].values * 100
            pvals = d["p_near"].values

            hover = [
                f"<b>{CRIME_LABELS.get(c,c)}</b><br>Window: {w} | FE: {FE_LABELS[fe]}<br>"
                f"β: {b:.4f}%<br>SE: {s:.4f}%<br>p: {p:.4f}<br>N: {int(n):,}"
                for c, b, s, p, n in zip(d["crime_type"], betas, ses, pvals, d["n"])
            ]

            vis = (w == default_w and fe == default_fe)

            fig.add_trace(go.Bar(
                y=y_labels, x=betas, orientation="h",
                marker=dict(color=[SIG_COLOR if p < 0.05 else NONSIG_COLOR for p in pvals]),
                error_x=dict(type="data", array=1.96*ses, visible=True,
                             color=TEXT_COLOR, thickness=1, width=3),
                hovertemplate="%{customdata}<extra></extra>", customdata=hover,
                visible=vis, showlegend=False,
            ))
            combo_idx[(w, fe)] = idx
            idx += 1

    fig.add_vline(x=0, line_dash="dot", line_color=GRAY, line_width=1)

    total = idx

    # Window dropdown
    w_buttons = []
    for w in windows:
        vis = [False] * total
        for fe in fe_specs:
            vis[combo_idx[(w, fe)]] = True
        w_buttons.append(dict(label=w, method="restyle",
            args=[{"visible": vis}]))

    # FE spec dropdown
    fe_buttons = []
    for fe in fe_specs:
        vis = [False] * total
        for w in windows:
            vis[combo_idx[(w, fe)]] = True
        fe_buttons.append(dict(label=FE_LABELS[fe], method="restyle",
            args=[{"visible": vis}]))

    # Since Plotly can't do independent dual dropdowns natively with restyle
    # (each overrides the other), use JavaScript post-processing.
    # Instead, build with combined buttons approach:
    # Two rows of buttons side by side using updatemenus

    # Actually, let's use a cleaner approach: window buttons + FE buttons
    # where window buttons assume default FE and FE buttons assume default window
    # This is the standard Plotly pattern for side-by-side filters.

    # Rebuild: each dropdown sets visibility for its default counterpart
    w_buttons2 = []
    for w in windows:
        vis = [False] * total
        # Show only the default FE for this window
        # We'll use JS to handle cross-filtering
        vis[combo_idx[(w, default_fe)]] = True
        w_buttons2.append(dict(label=w, method="update",
            args=[{"visible": vis},
                  {"title.text": f"Crime Type Effects ({w}, {FE_LABELS[default_fe]})"}]))

    fe_buttons2 = []
    for fe in fe_specs:
        vis = [False] * total
        vis[combo_idx[(default_w, fe)]] = True
        fe_buttons2.append(dict(label=FE_LABELS[fe], method="update",
            args=[{"visible": vis},
                  {"title.text": f"Crime Type Effects ({default_w}, {FE_LABELS[fe]})"}]))

    fig.update_layout(
        font=dict(family=FONT, color=TEXT_COLOR, size=13),
        paper_bgcolor=BG_COLOR, plot_bgcolor=BG_COLOR,
        margin=dict(l=130, r=30, t=90, b=50),
        title=dict(text=f"Crime Type Effects ({default_w}, {FE_LABELS[default_fe]})",
                   font=dict(size=16)),
        xaxis=dict(gridcolor=GRID_COLOR, zeroline=False, title="Effect on Log Sale Price (%)"),
        yaxis=dict(gridcolor=GRID_COLOR),
        height=520,
        hoverlabel=dict(bgcolor="white", font_size=12, font_family=FONT, bordercolor=GRID_COLOR),
        updatemenus=[
            dict(
                type="dropdown", x=0.0, y=1.13, xanchor="left", yanchor="top",
                bgcolor="white", bordercolor=GRID_COLOR, borderwidth=0.5, font=dict(size=12),
                buttons=w_buttons2, active=windows.index(default_w),
            ),
            dict(
                type="dropdown", x=0.22, y=1.13, xanchor="left", yanchor="top",
                bgcolor="white", bordercolor=GRID_COLOR, borderwidth=0.5, font=dict(size=12),
                buttons=fe_buttons2, active=fe_specs.index(default_fe),
            ),
        ],
        annotations=[
            dict(text="Window:", x=-0.02, y=1.16, xref="paper", yref="paper",
                 showarrow=False, font=dict(size=11, color=GRAY)),
            dict(text="FE:", x=0.20, y=1.16, xref="paper", yref="paper",
                 showarrow=False, font=dict(size=11, color=GRAY)),
        ],
    )

    write_html(fig, "crimetype_heatmap.html")


# ══════════════════════════════════════════════════════════════════════════════
# Chart D: Specification Curve — 3-panel vertical mirror (matched pre/post)
# ══════════════════════════════════════════════════════════════════════════════
def make_spec_curve():
    print("Generating spec_curve.html...")
    import re

    C_PRE  = "#1f4e79"   # blue  — significant in main only (clean)
    C_BOTH = "#e8a0a0"   # pink  — significant in both main and placebo (placebo failed)
    C_POST = "#7dba99"   # muted green — placebo panel default (only used when post sig but pre not)
    # The decision rule in plotting code: blue if pre-only-sig, pink if both-sig, gray if neither.

    ring_names = {
        'r1': '0-0.05', 'r2': '0.05-0.10', 'r3': '0.10-0.15', 'r4': '0.15-0.20',
        'r5': '0.20-0.25', 'r6': '0.25-0.30', 'r7': '0.30-0.35',
        'r8': '0.35-0.40', 'r9': '0.40-0.50',
        'r10a': '0.50-0.75', 'r10b': '0.75-1.00',
        'cum2': '0-0.10', 'cum3': '0-0.15', 'cum4': '0-0.20',
    }

    battery = df_crime
    post_all_df = df_post

    COLS = ['window', 'fe_spec', 'beta_near', 'se_near', 'p_near']

    # --- 1. Main near-far ---
    pre_main = battery[(battery['crime_type'] == 'total') & (battery['test'] == 'main')][
        COLS].copy()
    pre_main['match_key'] = 'main_' + pre_main['window'] + '_' + pre_main['fe_spec']
    pre_main['near_def'] = '0-0.05'
    pre_main['far_def'] = '0.20-0.30'

    post_main = post_all_df[post_all_df['test'] == 'post_sale_fixed'][COLS].copy()
    post_main['match_key'] = 'main_' + post_main['window'] + '_' + post_main['fe_spec']

    # --- 2. Band permutations ---
    pre_perm_list, post_perm_list = [], []
    for n in range(1, 5):
        for f in range(5, 10):
            pre_t = f'perm_r{n}_r{f}'
            post_t = f'ps_perm_r{n}_r{f}'
            pre_sub = battery[(battery['crime_type'] == 'total') & (battery['test'] == pre_t)][
                COLS].copy()
            pre_sub['match_key'] = pre_t + '_' + pre_sub['window'] + '_' + pre_sub['fe_spec']
            pre_sub['near_def'] = ring_names[f'r{n}']
            pre_sub['far_def'] = ring_names[f'r{f}']
            pre_perm_list.append(pre_sub)
            post_sub = post_all_df[post_all_df['test'] == post_t][COLS].copy()
            post_sub['match_key'] = pre_t + '_' + post_sub['window'] + '_' + post_sub['fe_spec']
            post_perm_list.append(post_sub)

    # --- 2b. Cumulative near ---
    for cn in [2, 3, 4]:
        for f in range(5, 10):
            pre_t = f'perm_cum{cn}_r{f}'
            post_t = f'ps_perm_cum{cn}_r{f}'
            pre_sub = battery[(battery['crime_type'] == 'total') & (battery['test'] == pre_t)][
                COLS].copy()
            if len(pre_sub) == 0:
                continue
            pre_sub['match_key'] = pre_t + '_' + pre_sub['window'] + '_' + pre_sub['fe_spec']
            pre_sub['near_def'] = ring_names[f'cum{cn}']
            pre_sub['far_def'] = ring_names[f'r{f}']
            pre_perm_list.append(pre_sub)
            post_sub = post_all_df[post_all_df['test'] == post_t][COLS].copy()
            post_sub['match_key'] = pre_t + '_' + post_sub['window'] + '_' + post_sub['fe_spec']
            post_perm_list.append(post_sub)

    # --- 3. Distance placebos ---
    pre_dist_list, post_dist_list = [], []
    for pre_t, post_t in [('dist_mid', 'ps_dist_mid'), ('dist_donut', 'ps_dist_donut'),
                           ('dist_far25', 'ps_dist_far25'), ('dist_distant', 'ps_dist_distant'),
                           ('dist_true', 'ps_dist_true')]:
        pre_sub = battery[(battery['crime_type'] == 'total') & (battery['test'] == pre_t)][
            COLS].copy()
        pre_sub['match_key'] = pre_t + '_' + pre_sub['window'] + '_' + pre_sub['fe_spec']
        pre_sub['near_def'] = 'dist_plac'
        pre_sub['far_def'] = pre_t
        pre_dist_list.append(pre_sub)
        post_sub = post_all_df[post_all_df['test'] == post_t][COLS].copy()
        post_sub['match_key'] = pre_t + '_' + post_sub['window'] + '_' + post_sub['fe_spec']
        post_dist_list.append(post_sub)

    # --- 4. Shock (main_shock) matched to post_sale_fixed (windows 2m-12m) ---
    pre_shock = battery[(battery['crime_type'] == 'total') & (battery['test'] == 'main_shock')][
        COLS].copy()
    pre_shock['match_key'] = 'shock_' + pre_shock['window'] + '_' + pre_shock['fe_spec']
    pre_shock['near_def'] = '0-0.05'
    pre_shock['far_def'] = '0.20-0.30'

    post_shock = post_all_df[post_all_df['test'] == 'post_sale_fixed'].copy()
    post_shock = post_shock[post_shock['window'] != '1m'][COLS].copy()
    post_shock['match_key'] = 'shock_' + post_shock['window'] + '_' + post_shock['fe_spec']

    # Combine and merge
    pre_all = pd.concat([pre_main] + pre_perm_list + pre_dist_list + [pre_shock], ignore_index=True)
    post_all_matched = pd.concat([post_main] + post_perm_list + post_dist_list + [post_shock], ignore_index=True)
    merged = pre_all.merge(post_all_matched, on='match_key', suffixes=('_pre', '_post'))

    for s in ['_pre', '_post']:
        merged[f'beta_pct{s}'] = merged[f'beta_near{s}'] * 100
        merged[f'se_pct{s}'] = merged[f'se_near{s}'] * 100
    merged['sig_pre'] = merged['p_near_pre'] < 0.05
    merged['sig_post'] = merged['p_near_post'] < 0.05

    # Sort by pre-sale beta
    df = merged.sort_values('beta_pct_pre').reset_index(drop=True)
    df['spec_id'] = range(len(df))

    # Parse near/far ring definitions
    def parse_near_far(key):
        m = re.match(r'perm_(r\d|cum\d)_(r\d)_', key)
        if m:
            return ring_names.get(m.group(1), m.group(1)), ring_names.get(m.group(2), m.group(2))
        if key.startswith('main_'):
            return '0-0.05', '0.20-0.30'
        if key.startswith('dist_'):
            return 'dist_plac', 'dist_plac'
        return None, None

    parsed = df['match_key'].apply(lambda k: pd.Series(parse_near_far(k), index=['nr', 'fr']))
    df['nr'] = parsed['nr']
    df['fr'] = parsed['fr']

    n_specs = len(df)
    n_sig_pre = int(df['sig_pre'].sum())
    n_sig_post = int(df['sig_post'].sum())
    print(f"  {n_specs} matched pairs (pre sig: {n_sig_pre}, post sig: {n_sig_post})")

    # ── Build 3-panel figure: top=pre-sale, middle=indicators, bottom=placebo ──
    fig = make_subplots(
        rows=3, cols=1,
        row_heights=[0.32, 0.36, 0.32],
        vertical_spacing=0.03,
        shared_xaxes=True,
    )

    x = df['spec_id'].tolist()

    # ── Row 1 (top): Post-Crime Sale (actual) — split sig / non-sig ──
    def make_hover(df_sub, n_specs, suffix='', is_post=False):
        panel = ' (placebo)' if is_post else ''
        beta_col = 'beta_pct_post' if is_post else 'beta_pct_pre'
        se_col = 'se_pct_post' if is_post else 'se_pct_pre'
        p_col = 'p_near_post' if is_post else 'p_near_pre'
        return [
            f"<b>Spec #{int(r.spec_id)+1}/{n_specs}{panel}</b><br>"
            f"FE: {FE_LABELS.get(r.fe_spec_pre, r.fe_spec_pre)}<br>"
            f"Window: {r.window_pre}<br>"
            f"Near: {r.near_def}<br>Far: {r.far_def}<br>"
            f"β: {getattr(r, beta_col):.4f}%<br>SE: {getattr(r, se_col):.4f}%<br>"
            f"p: {getattr(r, p_col):.4f}"
            for _, r in df_sub.iterrows()
        ]

    df_pre_nonsig = df[~df['sig_pre']]
    df_pre_sig = df[df['sig_pre']]

    # Non-significant: faded
    if len(df_pre_nonsig) > 0:
        fig.add_trace(go.Scatter(
            x=df_pre_nonsig['spec_id'].tolist(), y=df_pre_nonsig['beta_pct_pre'].tolist(),
            mode='markers',
            marker=dict(size=3, color=C_PRE, opacity=0.3),
            error_y=dict(type='data', array=(1.96 * df_pre_nonsig['se_pct_pre']).tolist(),
                         visible=True, color='rgba(31,78,121,0.15)', thickness=0.5, width=0),
            hovertemplate='%{customdata}<extra></extra>',
            customdata=make_hover(df_pre_nonsig, n_specs),
            showlegend=False,
        ), row=1, col=1)

    # Significant: bright, full opacity
    if len(df_pre_sig) > 0:
        fig.add_trace(go.Scatter(
            x=df_pre_sig['spec_id'].tolist(), y=df_pre_sig['beta_pct_pre'].tolist(),
            mode='markers',
            marker=dict(size=5, color=C_PRE, opacity=1.0),
            error_y=dict(type='data', array=(1.96 * df_pre_sig['se_pct_pre']).tolist(),
                         visible=True, color='rgba(31,78,121,0.5)', thickness=1, width=0),
            hovertemplate='%{customdata}<extra></extra>',
            customdata=make_hover(df_pre_sig, n_specs),
            showlegend=False,
        ), row=1, col=1)

    fig.add_hline(y=0, line_dash='dot', line_color='black', line_width=0.8, row=1, col=1)

    # ── Row 3 (bottom): Post-Sale Crime (placebo) — split sig / non-sig ──
    df_post_nonsig = df[~df['sig_post']]
    df_post_sig = df[df['sig_post']]

    # Non-significant: faded muted green
    if len(df_post_nonsig) > 0:
        fig.add_trace(go.Scatter(
            x=df_post_nonsig['spec_id'].tolist(), y=df_post_nonsig['beta_pct_post'].tolist(),
            mode='markers',
            marker=dict(size=3, color=C_POST, opacity=0.3, symbol='square'),
            error_y=dict(type='data', array=(1.96 * df_post_nonsig['se_pct_post']).tolist(),
                         visible=True, color='rgba(125,186,153,0.15)', thickness=0.5, width=0),
            hovertemplate='%{customdata}<extra></extra>',
            customdata=make_hover(df_post_nonsig, n_specs, is_post=True),
            showlegend=False,
        ), row=3, col=1)

    # Significant: bright green, full opacity
    if len(df_post_sig) > 0:
        fig.add_trace(go.Scatter(
            x=df_post_sig['spec_id'].tolist(), y=df_post_sig['beta_pct_post'].tolist(),
            mode='markers',
            marker=dict(size=7, color='#27ae60', opacity=1.0, symbol='square'),
            error_y=dict(type='data', array=(1.96 * df_post_sig['se_pct_post']).tolist(),
                         visible=True, color='rgba(39,174,96,0.5)', thickness=1, width=0),
            hovertemplate='%{customdata}<extra></extra>',
            customdata=make_hover(df_post_sig, n_specs, is_post=True),
            showlegend=False,
        ), row=3, col=1)

    fig.add_hline(y=0, line_dash='dot', line_color='black', line_width=0.8, row=3, col=1)

    # ── Row 2 (middle): indicator dots ──
    # Categories: FE, Window, Near ring, Far ring
    cats_order = [
        ('FE', {
            'Tract×Month': lambda r: r['fe_spec_pre'] == 'PIN_CAM',
            'Tract×Yr+YM': lambda r: r['fe_spec_pre'] == 'PIN_CAY_YM',
            'Tract×Month (alt)': lambda r: r['fe_spec_pre'] == 'PIN_TM',
        }),
        ('Window', {
            '2m': lambda r: r['window_pre'] == '2m',
            '4m': lambda r: r['window_pre'] == '4m',
            '6m': lambda r: r['window_pre'] == '6m',
            '8m': lambda r: r['window_pre'] == '8m',
            '12m': lambda r: r['window_pre'] == '12m',
            'other': lambda r: r['window_pre'] in ['1m','3m','5m','7m','9m','10m','11m'],
        }),
        ('Near ring', {
            '0-0.05': lambda r: r['nr'] == '0-0.05',
            '0.05-0.10': lambda r: r['nr'] == '0.05-0.10',
            '0.10-0.15': lambda r: r['nr'] == '0.10-0.15',
            '0.15-0.20': lambda r: r['nr'] == '0.15-0.20',
            '0-0.10 (cum)': lambda r: r['nr'] == '0-0.10',
            '0-0.15 (cum)': lambda r: r['nr'] == '0-0.15',
            '0-0.20 (cum)': lambda r: r['nr'] == '0-0.20',
            'dist placebo': lambda r: r['nr'] == 'dist_plac',
        }),
        ('Far ring', {
            '0.20-0.25': lambda r: r['fr'] == '0.20-0.25',
            '0.25-0.30': lambda r: r['fr'] == '0.25-0.30',
            '0.30-0.35': lambda r: r['fr'] == '0.30-0.35',
            '0.35-0.40': lambda r: r['fr'] == '0.35-0.40',
            '0.40-0.50': lambda r: r['fr'] == '0.40-0.50',
            '0.50-0.75': lambda r: r['fr'] == '0.50-0.75',
            '0.75-1.00': lambda r: r['fr'] == '0.75-1.00',
            '0.20-0.30': lambda r: r['fr'] == '0.20-0.30',
            'dist placebo': lambda r: r['fr'] == 'dist_plac',
        }),
    ]

    y_pos = 0
    y_labels_bot = []
    y_positions_bot = []
    cat_boundaries = []

    for cat_name, options in cats_order:
        cat_start = y_pos
        for opt_name, cond_fn in options.items():
            active_mask = df.apply(cond_fn, axis=1)

            pre_only = active_mask & df['sig_pre'] & ~df['sig_post']
            post_only = active_mask & df['sig_post'] & ~df['sig_pre']
            both_sig = active_mask & df['sig_pre'] & df['sig_post']
            neither = active_mask & ~df['sig_pre'] & ~df['sig_post']

            # Gray (neither sig)
            ids = df.loc[neither, 'spec_id'].values
            if len(ids) > 0:
                fig.add_trace(go.Scatter(
                    x=ids.tolist(), y=[y_pos]*len(ids), mode='markers',
                    marker=dict(size=3, color='gray', opacity=0.2, symbol='square'),
                    showlegend=False, hoverinfo='skip',
                ), row=2, col=1)

            # Blue (pre sig only)
            ids = df.loc[pre_only, 'spec_id'].values
            if len(ids) > 0:
                fig.add_trace(go.Scatter(
                    x=ids.tolist(), y=[y_pos]*len(ids), mode='markers',
                    marker=dict(size=4, color=C_PRE, opacity=0.85, symbol='square'),
                    showlegend=False, hoverinfo='skip',
                ), row=2, col=1)

            # Green (post sig only)
            ids = df.loc[post_only, 'spec_id'].values
            if len(ids) > 0:
                fig.add_trace(go.Scatter(
                    x=ids.tolist(), y=[y_pos]*len(ids), mode='markers',
                    marker=dict(size=4, color=C_POST, opacity=0.85, symbol='square'),
                    showlegend=False, hoverinfo='skip',
                ), row=2, col=1)

            # Red (both sig)
            ids = df.loc[both_sig, 'spec_id'].values
            if len(ids) > 0:
                fig.add_trace(go.Scatter(
                    x=ids.tolist(), y=[y_pos]*len(ids), mode='markers',
                    marker=dict(size=5, color=C_BOTH, opacity=0.9, symbol='square'),
                    showlegend=False, hoverinfo='skip',
                ), row=2, col=1)

            y_labels_bot.append(opt_name)
            y_positions_bot.append(y_pos)
            y_pos += 1
        cat_boundaries.append((cat_start, y_pos - 1, cat_name))
        y_pos += 0.6

    # Category separator lines
    for start, end, name in cat_boundaries:
        if start > 0:
            fig.add_hline(y=start - 0.3, line_color=GRID_COLOR, line_width=0.5, row=2, col=1)

    # Row guide lines
    for yp in y_positions_bot:
        fig.add_hline(y=yp, line_color='rgba(200,200,200,0.2)', line_width=0.2, row=2, col=1)

    # Symmetric y-limits for top and bottom coefficient panels
    ymax_pre = max(abs(df['beta_pct_pre'].min()), abs(df['beta_pct_pre'].max())) * 1.15
    ymax_post = max(abs(df['beta_pct_post'].min()), abs(df['beta_pct_post'].max())) * 1.15
    ymax = max(ymax_pre, ymax_post)

    # Category label annotations (right side of indicator panel = row 2 = y2)
    cat_annotations = []
    for start, end, name in cat_boundaries:
        cat_annotations.append(dict(
            text=f'<b>{name}</b>', x=1.01, y=((start + end) / 2),
            xref='paper', yref='y2', showarrow=False,
            font=dict(size=9, color=GRAY), xanchor='left', yanchor='middle',
        ))

    fig.update_layout(
        font=dict(family=FONT, color=TEXT_COLOR, size=12),
        paper_bgcolor=BG_COLOR, plot_bgcolor=BG_COLOR,
        margin=dict(l=100, r=80, t=70, b=40),
        height=900,
        hoverlabel=dict(bgcolor='white', font_size=11, font_family=FONT, bordercolor=GRID_COLOR),
        showlegend=False,
        annotations=[
            dict(text=f'<b style="color:{C_PRE}">Post-Crime Sale</b> — {n_sig_pre}/{n_specs} significant at 5%',
                 x=0, y=1.06, xref='paper', yref='paper', showarrow=False,
                 font=dict(size=13, color=C_PRE), xanchor='left'),
            dict(text=f'<b style="color:{C_POST}">Post-Sale Crime (placebo)</b> — {n_sig_post}/{n_specs} significant',
                 x=0, y=-0.02, xref='paper', yref='paper', showarrow=False,
                 font=dict(size=13, color=C_POST), xanchor='left'),
        ] + cat_annotations,
    )

    # Row 1 (top): pre-sale coefficients
    fig.update_xaxes(showticklabels=False, showgrid=False, zeroline=False, row=1, col=1)
    fig.update_yaxes(title_text='β_near (%)', gridcolor=GRID_COLOR, zeroline=True,
                     zerolinecolor=GRID_COLOR, range=[-ymax, ymax], row=1, col=1)

    # Row 2 (middle): indicator dots
    fig.update_xaxes(showticklabels=False, showgrid=False, zeroline=False, row=2, col=1)
    fig.update_yaxes(
        tickmode='array', tickvals=y_positions_bot, ticktext=y_labels_bot,
        tickfont=dict(size=7.5), gridcolor='rgba(0,0,0,0)', zeroline=False,
        autorange='reversed', row=2, col=1,
    )

    # Row 3 (bottom): placebo coefficients
    fig.update_xaxes(showticklabels=False, showgrid=False, zeroline=False, row=3, col=1)
    fig.update_yaxes(title_text='β_near (%)', gridcolor=GRID_COLOR, zeroline=True,
                     zerolinecolor=GRID_COLOR, range=[-ymax, ymax], row=3, col=1)

    write_html(fig, 'spec_curve.html')


# ══════════════════════════════════════════════════════════════════════════════
# Chart E: Specification Curve Explorer — interactive multi-model comparison
# ══════════════════════════════════════════════════════════════════════════════
def make_spec_explorer():
    print("Generating spec_explorer.html...")
    import json
    import re

    # ── Dimension labels (expanded for new het_battery) ───────────────────
    fe_list = ['PIN_CAM', 'PIN_YM', 'PIN_CAY_YM', 'PIN_TM']
    window_list = ['1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', '10m', '11m', '12m']
    near_ring_list = [
        '0-0.05', '0.05-0.10', '0.10-0.15', '0.15-0.20', '0.20-0.25', '0.25-0.30',
        '0-0.10', '0-0.15', '0-0.20', '0-0.25', '0-0.30', '0.35-0.40',
    ]
    far_ring_list = [
        '0.15-0.20', '0.20-0.25', '0.25-0.30', '0.30-0.35', '0.35-0.40',
        '0.40-0.50', '0.20-0.30',
    ]

    fe_idx_map = {v: i for i, v in enumerate(fe_list)}
    win_idx_map = {v: i for i, v in enumerate(window_list)}
    near_idx_map = {v: i for i, v in enumerate(near_ring_list)}
    far_idx_map = {v: i for i, v in enumerate(far_ring_list)}

    prop_types = ['ALL_nonresid', 'ALL_resid', 'SF', 'Condo', 'Multi', 'Townhouse']
    crime_types_old = ['total', 'drugvice', 'disorder', 'property', 'violent', 'domestic']
    # The new het master files contain multiple crime_types per file — loop over them.
    NEW_CRIME_TYPES = ['total_spatial', 'violent']
    NEW_CRIME_TYPE = 'total_spatial'  # kept for blocks (OLS/GLS/Heckman) not yet refactored

    # ── Helper: build entry dict from a filtered dataframe ────────────────
    def build_entry(pre, post_df=None):
        pre = pre.copy()
        # Drop 0.50-1.00 far ring specs (too distant, picks up spatial sorting)
        pre = pre[pre['far_def'] != '0.50-1.00']
        if post_df is not None:
            post_df = post_df[post_df['far_def'] != '0.50-1.00']
        pre['fe_idx'] = pre['fe_spec'].map(fe_idx_map)
        pre['win_idx'] = pre['window'].map(win_idx_map)
        pre['near_idx'] = pre['near_def'].map(near_idx_map)
        pre['far_idx'] = pre['far_def'].map(far_idx_map)

        # Drop rows with unmapped values
        pre = pre.dropna(subset=['fe_idx', 'win_idx', 'near_idx', 'far_idx'])
        pre = pre.sort_values('beta_near').reset_index(drop=True)

        has_post = post_df is not None and len(post_df) > 0
        if has_post:
            post_df = post_df.copy()
            merged = pre.merge(
                post_df[['test', 'window', 'fe_spec', 'beta_near', 'se_near', 'p_near',
                         'beta_diff', 'se_diff', 'p_diff']],
                on=['test', 'window', 'fe_spec'], suffixes=('', '_post'), how='left',
            )
        else:
            merged = pre

        n_specs = len(merged)
        if n_specs == 0:
            return None
        n_pre_sig = int((merged['p_near'] < 0.05).sum())
        n_pre_sig_d = int((merged['p_diff'] < 0.05).sum())

        entry = {
            'b':  (merged['beta_near'] * 100).round(4).tolist(),
            's':  (merged['se_near'] * 100).round(4).tolist(),
            'p':  merged['p_near'].round(6).tolist(),
            'bd': (merged['beta_diff'] * 100).round(4).tolist(),
            'sd': (merged['se_diff'] * 100).round(4).tolist(),
            'pd': merged['p_diff'].round(6).tolist(),
            'fi': merged['fe_idx'].astype(int).tolist(),
            'wi': merged['win_idx'].astype(int).tolist(),
            'ni': merged['near_idx'].astype(int).tolist(),
            'ri': merged['far_idx'].astype(int).tolist(),
            'ns': n_specs,
            'np': n_pre_sig,
            'npd': n_pre_sig_d,
            'hp': has_post,
        }

        if has_post and 'beta_near_post' in merged.columns:
            merged['beta_near_post'] = merged['beta_near_post'].fillna(0)
            merged['se_near_post'] = merged['se_near_post'].fillna(1)
            merged['p_near_post'] = merged['p_near_post'].fillna(1)
            merged['beta_diff_post'] = merged.get('beta_diff_post', pd.Series([0]*n_specs)).fillna(0)
            merged['se_diff_post'] = merged.get('se_diff_post', pd.Series([1]*n_specs)).fillna(1)
            merged['p_diff_post'] = merged.get('p_diff_post', pd.Series([1]*n_specs)).fillna(1)
            entry['bp']  = (merged['beta_near_post'] * 100).round(4).tolist()
            entry['sp']  = (merged['se_near_post'] * 100).round(4).tolist()
            entry['pp']  = merged['p_near_post'].round(6).tolist()
            entry['nps'] = int((merged['p_near_post'] < 0.05).sum())
            entry['bpd'] = (merged['beta_diff_post'] * 100).round(4).tolist()
            entry['spd'] = (merged['se_diff_post'] * 100).round(4).tolist()
            entry['ppd'] = merged['p_diff_post'].round(6).tolist()
            entry['npsd'] = int((merged['p_diff_post'] < 0.05).sum())

        return entry

    # ── Load new het_battery (total_spatial, all prop types) ──────────────
    HET_DIR = DATA_DIR / '00het_battery'
    all_data = {}

    # OLS Standard + OLS Persistence Control (from new het_battery)
    ols_path = HET_DIR / 'OLS' / 'OLS_master.csv'
    ols_pc_path = HET_DIR / 'OLS_Pctrl' / 'OLS_Pctrl_master.csv'

    if ols_path.exists():
        print("  Loading het_battery OLS...")
        df_ols = pd.read_csv(ols_path)
        df_ols = df_ols[df_ols['crime_type'] == NEW_CRIME_TYPE]
        df_ols_pc = pd.read_csv(ols_pc_path) if ols_pc_path.exists() else None
        if df_ols_pc is not None:
            df_ols_pc = df_ols_pc[df_ols_pc['crime_type'] == NEW_CRIME_TYPE]

        ts_data = {}
        for pt in prop_types:
            pt_data = {}

            # OLS Standard
            pre = df_ols[(df_ols['prop_type'] == pt) & (df_ols['side'] == 'main')]
            post = df_ols[(df_ols['prop_type'] == pt) & (df_ols['side'] == 'post')]
            entry = build_entry(pre, post)
            if entry:
                pt_data['OLS_none'] = entry
                print(f"    total/{pt}/OLS_none: {entry['ns']} specs, pre sig: {entry['np']}, post sig: {entry.get('nps','n/a')}")

            # OLS Persistence Control (drop 0.40-0.50 far ring — inflated placebo)
            if df_ols_pc is not None:
                pre = df_ols_pc[(df_ols_pc['prop_type'] == pt) & (df_ols_pc['side'] == 'main')]
                pre = pre[pre['far_def'] != '0.40-0.50']
                post = df_ols_pc[(df_ols_pc['prop_type'] == pt) & (df_ols_pc['side'] == 'post')]
                post = post[post['far_def'] != '0.40-0.50']
                entry = build_entry(pre, post)
                if entry:
                    pt_data['OLS_pc'] = entry
                    print(f"    total/{pt}/OLS_pc: {entry['ns']} specs, pre sig: {entry['np']}, post sig: {entry.get('nps','n/a')}")

            if pt_data:
                ts_data[pt] = pt_data

        all_data[NEW_CRIME_TYPE] = ts_data

    # GLS Standard (Case-Shiller) (from het_battery)
    gls_path = HET_DIR / 'GLS' / 'GLS_master.csv'
    if gls_path.exists():
        print("  Loading het_battery GLS (Case-Shiller)...")
        df_gls = pd.read_csv(gls_path)
        df_gls = df_gls[df_gls['crime_type'] == NEW_CRIME_TYPE]
        for pt in prop_types:
            pre = df_gls[(df_gls['prop_type'] == pt) & (df_gls['side'] == 'main')]
            post = df_gls[(df_gls['prop_type'] == pt) & (df_gls['side'] == 'post')]
            entry = build_entry(pre, post)
            if entry:
                if NEW_CRIME_TYPE not in all_data:
                    all_data[NEW_CRIME_TYPE] = {}
                if pt not in all_data[NEW_CRIME_TYPE]:
                    all_data[NEW_CRIME_TYPE][pt] = {}
                all_data[NEW_CRIME_TYPE][pt]['GLS_none'] = entry
                print(f"    total/{pt}/GLS_none: {entry['ns']} specs, pre sig: {entry['np']}, post sig: {entry.get('nps','n/a')}")

    # GLS + Persistence Control (Case-Shiller + PC) (from het_battery)
    gls_pc_path = HET_DIR / 'GLS_Pctrl' / 'GLS_Pctrl_master.csv'
    if gls_pc_path.exists():
        print("  Loading het_battery GLS+PC (Case-Shiller + Persistence Control)...")
        df_gls_pc_all = pd.read_csv(gls_pc_path)
        for ct in NEW_CRIME_TYPES:
            df_gls_pc = df_gls_pc_all[df_gls_pc_all['crime_type'] == ct]
            # 1-month window is noisy for rare crimes — drop for violent.
            if ct == 'violent':
                df_gls_pc = df_gls_pc[df_gls_pc['window'] != '1m']
            for pt in prop_types:
                pre = df_gls_pc[(df_gls_pc['prop_type'] == pt) & (df_gls_pc['side'] == 'main')]
                post = df_gls_pc[(df_gls_pc['prop_type'] == pt) & (df_gls_pc['side'] == 'post')]
                entry = build_entry(pre, post)
                if entry:
                    if ct not in all_data:
                        all_data[ct] = {}
                    if pt not in all_data[ct]:
                        all_data[ct][pt] = {}
                    all_data[ct][pt]['GLS_pc'] = entry
                    print(f"    {ct}/{pt}/GLS_pc: {entry['ns']} specs, pre sig: {entry['np']}, post sig: {entry.get('nps','n/a')}")

    # OLS + Heckman (Hurin) (from het_battery)
    hurin_path = HET_DIR / 'Hurin' / 'Hurin_master.csv'
    if hurin_path.exists():
        print("  Loading het_battery Hurin (OLS+Heckman)...")
        df_hurin = pd.read_csv(hurin_path)
        for pt in prop_types:
            pre = df_hurin[(df_hurin['prop_type'] == pt) & (df_hurin['side'] == 'main')]
            post = df_hurin[(df_hurin['prop_type'] == pt) & (df_hurin['side'] == 'post')]
            entry = build_entry(pre, post)
            if entry:
                if NEW_CRIME_TYPE not in all_data:
                    all_data[NEW_CRIME_TYPE] = {}
                if pt not in all_data[NEW_CRIME_TYPE]:
                    all_data[NEW_CRIME_TYPE][pt] = {}
                all_data[NEW_CRIME_TYPE][pt]['OLS_none_heckman'] = entry
                print(f"    total/{pt}/OLS_none_heckman: {entry['ns']} specs, pre sig: {entry['np']}, post sig: {entry.get('nps','n/a')}")

    # OLS + Heckman + Persistence Control (Hurin_Pctrl) (from het_battery)
    hurin_pc_path = HET_DIR / 'Hurin_Pctrl' / 'Hurin_Pctrl_master.csv'
    if hurin_pc_path.exists():
        print("  Loading het_battery Hurin_Pctrl (OLS+Heckman+PC)...")
        df_hurin_pc = pd.read_csv(hurin_pc_path)
        for pt in prop_types:
            pre = df_hurin_pc[(df_hurin_pc['prop_type'] == pt) & (df_hurin_pc['side'] == 'main')]
            post = df_hurin_pc[(df_hurin_pc['prop_type'] == pt) & (df_hurin_pc['side'] == 'post')]
            entry = build_entry(pre, post)
            if entry:
                if NEW_CRIME_TYPE not in all_data:
                    all_data[NEW_CRIME_TYPE] = {}
                if pt not in all_data[NEW_CRIME_TYPE]:
                    all_data[NEW_CRIME_TYPE][pt] = {}
                all_data[NEW_CRIME_TYPE][pt]['OLS_pc_heckman'] = entry
                print(f"    total/{pt}/OLS_pc_heckman: {entry['ns']} specs, pre sig: {entry['np']}, post sig: {entry.get('nps','n/a')}")

    # GLS + Heckman (GLS_Hurin) (from het_battery)
    gls_hurin_path = HET_DIR / 'GLS_Hurin' / 'GLS_Hurin_master.csv'
    if gls_hurin_path.exists():
        print("  Loading het_battery GLS_Hurin (GLS+Heckman)...")
        df_gls_hurin = pd.read_csv(gls_hurin_path)
        for pt in prop_types:
            pre = df_gls_hurin[(df_gls_hurin['prop_type'] == pt) & (df_gls_hurin['side'] == 'main')]
            post = df_gls_hurin[(df_gls_hurin['prop_type'] == pt) & (df_gls_hurin['side'] == 'post')]
            entry = build_entry(pre, post)
            if entry:
                if NEW_CRIME_TYPE not in all_data:
                    all_data[NEW_CRIME_TYPE] = {}
                if pt not in all_data[NEW_CRIME_TYPE]:
                    all_data[NEW_CRIME_TYPE][pt] = {}
                all_data[NEW_CRIME_TYPE][pt]['GLS_none_heckman'] = entry
                print(f"    total/{pt}/GLS_none_heckman: {entry['ns']} specs, pre sig: {entry['np']}, post sig: {entry.get('nps','n/a')}")

    # GLS + Heckman + Persistence Control (GLS_Hurin_Pctrl) (from het_battery)
    gls_hurin_pc_path = HET_DIR / 'GLS_Hurin_Pctrl' / 'GLS_Hurin_Pctrl_master.csv'
    if gls_hurin_pc_path.exists():
        print("  Loading het_battery GLS_Hurin_Pctrl (GLS+Heckman+PC)...")
        df_gls_hurin_pc = pd.read_csv(gls_hurin_pc_path)
        for pt in prop_types:
            pre = df_gls_hurin_pc[(df_gls_hurin_pc['prop_type'] == pt) & (df_gls_hurin_pc['side'] == 'main')]
            post = df_gls_hurin_pc[(df_gls_hurin_pc['prop_type'] == pt) & (df_gls_hurin_pc['side'] == 'post')]
            entry = build_entry(pre, post)
            if entry:
                if NEW_CRIME_TYPE not in all_data:
                    all_data[NEW_CRIME_TYPE] = {}
                if pt not in all_data[NEW_CRIME_TYPE]:
                    all_data[NEW_CRIME_TYPE][pt] = {}
                all_data[NEW_CRIME_TYPE][pt]['GLS_pc_heckman'] = entry
                print(f"    total/{pt}/GLS_pc_heckman: {entry['ns']} specs, pre sig: {entry['np']}, post sig: {entry.get('nps','n/a')}")

    # ── Load old spec_battery_4way for crime type heterogeneity ───────────
    ring_names_old = {
        'r1': '0-0.05', 'r2': '0.05-0.10', 'r3': '0.10-0.15', 'r4': '0.15-0.20',
        'r5': '0.20-0.25', 'r6': '0.25-0.30', 'r7': '0.30-0.35',
        'r8': '0.35-0.40', 'r9': '0.40-0.50',
        'c2': '0-0.10 (cum)', 'c3': '0-0.15 (cum)', 'c4': '0-0.20 (cum)',
    }
    # Map old ring names to new near_ring_list (cum names differ)
    old_near_map = {
        '0-0.05': '0-0.05', '0.05-0.10': '0.05-0.10', '0.10-0.15': '0.10-0.15',
        '0.15-0.20': '0.15-0.20', '0-0.10 (cum)': '0-0.10', '0-0.15 (cum)': '0-0.15',
        '0-0.20 (cum)': '0-0.20', 'dist placebo': '0.35-0.40',
    }
    old_far_map = {
        '0.20-0.25': '0.20-0.25', '0.25-0.30': '0.25-0.30', '0.30-0.35': '0.30-0.35',
        '0.35-0.40': '0.35-0.40', '0.40-0.50': '0.40-0.50', '0.20-0.30': '0.20-0.30',
        'dist placebo': '0.50-1.00',
    }

    def parse_test_old(test):
        if test == 'main':
            return '0-0.05', '0.20-0.30'
        if test.startswith('dist_'):
            return '0.35-0.40', '0.50-1.00'
        m = re.match(r'perm_(r\d|c\d)_(r\d)', test)
        if m:
            nr = ring_names_old.get(m.group(1), m.group(1))
            fr = ring_names_old.get(m.group(2), m.group(2))
            nr = old_near_map.get(nr, nr)
            fr = old_far_map.get(fr, fr)
            return nr, fr
        return test, test

    for ct in crime_types_old:
        if ct == 'total' and 'total' in all_data:
            continue  # already loaded from het_battery

        csv_path = DATA_DIR / f'spec_battery_4way_{ct}.csv'
        if not csv_path.exists():
            print(f"  SKIP {ct} — file not found")
            continue
        df_bat = pd.read_csv(csv_path, encoding='latin-1')

        ct_data = {}
        # Only OLS for now
        for mk in ['OLS_none']:
            est, pc = mk.split('_', 1)
            pre = df_bat[(df_bat['est'] == est) & (df_bat['pc'] == pc)
                         & (df_bat['side'] == 'main')].copy()
            pre['near_def'] = pre['test'].apply(lambda t: parse_test_old(t)[0])
            pre['far_def'] = pre['test'].apply(lambda t: parse_test_old(t)[1])
            has_post = 'post' in df_bat['side'].values
            post = None
            if has_post:
                post = df_bat[(df_bat['est'] == est) & (df_bat['pc'] == pc)
                              & (df_bat['side'] == 'post')].copy()
                post['near_def'] = post['test'].apply(lambda t: parse_test_old(t)[0])
                post['far_def'] = post['test'].apply(lambda t: parse_test_old(t)[1])
            entry = build_entry(pre, post)
            if entry:
                if 'All' not in ct_data:
                    ct_data['All'] = {}
                ct_data['All'][mk] = entry
                print(f"  {ct}/All/{mk}: {entry['ns']} specs, pre sig: {entry['np']}")

        if ct_data:
            all_data[ct] = ct_data

    data_json = json.dumps(all_data, separators=(',', ':'))

    # ── HTML template ──────────────────────────────────────────────────────
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Results</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',system-ui,sans-serif;background:#f8f7f4;color:#1a1a18}

.explorer{display:flex;height:100vh}

.sidebar{
  width:190px;min-width:190px;padding:24px 16px;
  background:#fff;border-right:1px solid #d3d1c7;
  position:fixed;top:0;left:0;height:100vh;overflow-y:auto;z-index:10;
}
.sidebar h2{font-size:15px;font-weight:600;margin-bottom:16px;color:#672414}
.sidebar h3{
  font-size:11px;font-weight:500;text-transform:uppercase;
  letter-spacing:.08em;color:#888780;margin-bottom:8px;margin-top:20px;
}
.sidebar h3:first-of-type{margin-top:0}
.sidebar .section-heading{
  font-size:10px;font-weight:600;text-transform:uppercase;
  letter-spacing:.06em;color:#672414;margin-top:24px;margin-bottom:4px;
  padding-bottom:4px;border-bottom:1px solid #e8e6df;
}
.sidebar .section-heading:first-of-type{margin-top:0}
.sidebar select{
  width:100%;padding:8px 10px;border:1px solid #d3d1c7;border-radius:6px;
  font-size:13px;font-family:inherit;background:#fff;color:#1a1a18;
  cursor:pointer;outline:none;
}
.sidebar select:focus{border-color:#672414}
.sidebar label{
  display:flex;align-items:center;gap:8px;padding:6px 0;
  font-size:13px;cursor:pointer;color:#1a1a18;
}
.sidebar label input{cursor:pointer}
.cdot{display:inline-block;width:10px;height:10px;border-radius:2px}
.model-group-label{
  font-size:12px;font-weight:600;color:#1a1a18;margin-top:10px;margin-bottom:1px;
}
.model-group{position:relative}
.info-i{
  font-size:10px;color:#b4b2a9;cursor:pointer;margin-left:4px;
  border:1px solid #d3d1c7;border-radius:50%;width:14px;height:14px;
  display:inline-flex;align-items:center;justify-content:center;
  vertical-align:middle;line-height:1;
}
.info-i:hover{color:#672414;border-color:#672414}
.model-tip{
  display:none;position:fixed;z-index:30;
  width:240px;background:#fff;border:1px solid #d3d1c7;border-radius:8px;
  padding:10px 12px;font-size:10.5px;color:#4a4a46;line-height:1.5;
  box-shadow:0 4px 14px rgba(0,0,0,.08);text-align:justify;
}
.model-tip.open{display:block}
.model-tip::before{
  content:'';position:absolute;left:-6px;top:10px;
  width:10px;height:10px;background:#fff;border-left:1px solid #d3d1c7;
  border-bottom:1px solid #d3d1c7;transform:rotate(45deg);
}
.model-sub{padding-left:14px}
.model-sub label{font-size:12px;padding:4px 0}

.card{
  background:#fff;border:1px solid #d3d1c7;border-radius:10px;
  margin-bottom:24px;overflow:hidden;
}
.card-title{padding:14px 20px;font-size:14px;font-weight:500;border-bottom:1px solid #eae8e0}
.card-plot{width:100%}
.card-footer{
  padding:10px 20px;font-size:12px;color:#888780;
  border-top:1px solid #eae8e0;background:#fafaf7;
}

.legend-row{display:flex;gap:14px;margin-top:18px;flex-wrap:wrap}
.legend-item{display:flex;align-items:center;gap:4px;font-size:11px;color:#888780}
.legend-sw{width:8px;height:8px;border-radius:1px}

.topnav{
  position:fixed;top:0;left:190px;right:0;z-index:15;
  height:44px;background:#fff;border-bottom:1px solid #d3d1c7;
  display:flex;align-items:center;padding:0 32px;gap:0;
}
.topnav-item{
  font-size:12px;font-weight:500;color:#888780;cursor:pointer;
  padding:12px 16px;border:none;background:none;font-family:inherit;
  position:relative;letter-spacing:.02em;
}
.topnav-item:hover{color:#672414}
.topnav-item.active{color:#672414}
.topnav-item.active::after{
  content:'';position:absolute;bottom:0;left:16px;right:16px;
  height:2px;background:#672414;border-radius:1px;
}
.topnav-sep{
  width:1px;height:16px;background:#e8e6df;
}

.info-panel{
  display:none;position:fixed;top:44px;left:190px;z-index:14;
  width:420px;background:#fff;border:1px solid #d3d1c7;border-radius:0 0 10px 10px;
  padding:20px 24px;font-size:12.5px;color:#4a4a46;line-height:1.7;
  box-shadow:0 4px 12px rgba(0,0,0,.06);max-height:50vh;overflow-y:auto;
}
.info-panel.open{display:block}
.info-panel h4{
  font-size:13px;font-weight:600;color:#672414;margin:0 0 8px;
}
.info-panel p{margin:0 0 8px}
.info-panel p:last-child{margin-bottom:0}
.info-panel ul{margin:4px 0 8px 18px;padding:0}
.info-panel li{margin-bottom:4px}

.display{margin-left:190px;flex:1;padding:24px 32px;padding-top:68px;overflow-y:auto}
.tab-frame{display:none;width:100%;height:calc(100vh - 68px)}
.tab-frame iframe{width:100%;height:100%;border:none;}

@media(max-width:700px){
  .sidebar{width:180px;min-width:180px;padding:16px 14px}
  .topnav{left:180px;padding:0 16px}
  .info-panel{left:180px;padding:16px}
  .display{margin-left:180px;padding:16px;padding-top:60px}
}
</style>
</head>
<body>
<script>
var EMBED=new URLSearchParams(window.location.search).has('embed');
if(EMBED){document.documentElement.classList.add('embed-mode');}
</script>
<style>.embed-mode .topnav{display:none!important} .embed-mode .display{padding-top:24px!important} .embed-mode .tab-frame{display:none!important} .embed-mode #rq-hero{display:none!important}</style>
<div class="topnav" id="spec-topnav">
  <button class="topnav-item active" onclick="showTab('results')" style="font-weight:600;">Results</button>
  <div class="topnav-sep"></div>
  <button class="topnav-item" onclick="showTab('data')">Data</button>
  <div class="topnav-sep"></div>
  <button class="topnav-item" onclick="showTab('ident')">Model</button>
  <div class="topnav-sep"></div>
  <button class="topnav-item" onclick="showTab('geo')">Geography</button>
  <div class="topnav-sep"></div>
  <button class="topnav-item" onclick="showTab('robust')">Robustness</button>
</div>

<div class="explorer">
  <div class="sidebar">
    <div class="section-heading">Treatment (crime) heterogeneity</div>
    <h3>Crime Type</h3>
    <select id="crime-select" onchange="render()">
      <option value="total_spatial">Total Spatial Crime</option>
      <option value="violent">Violent</option>
      <option value="property" disabled>Property (coming soon)</option>
      <option value="disorder" disabled>Disorder (coming soon)</option>
      <option value="drugvice" disabled>Drug/Vice (coming soon)</option>
      <option value="domestic" disabled>Domestic placebo (coming soon)</option>
      <option value="nonspatial" disabled>Non-Spatial placebo (coming soon)</option>
    </select>

    <div class="section-heading">Outcome (property) heterogeneity</div>
    <h3>Property Type</h3>
    <select id="prop-select" onchange="render()">
      <option value="ALL_nonresid">All Properties</option>
      <option value="ALL_resid">All (residential subset)</option>
      <option value="SF">Single-Family</option>
      <option value="Condo">Condo</option>
      <option value="Multi">Multi-Unit</option>
      <option value="Townhouse">Townhouse</option>
    </select>

    <h3>Specification</h3>
    <div class="model-group">
      <div class="model-group-label">Estimator <span class="info-i" onclick="toggleTip(event,'tip-het')">i</span></div>
      <div class="model-tip" id="tip-het">Repeat-sales error variance grows with holding period between sales. GLS downweights long-gap pairs.</div>
      <div class="model-sub">
        <label style="opacity:0.4"><input type="checkbox" class="ax-het" value="OLS" disabled onchange="render()">
          <span class="cdot" style="background:#1f4e79"></span> OLS <em style="font-size:10px;color:#888">(coming soon)</em></label>
        <label><input type="checkbox" class="ax-het" value="GLS" checked onchange="render()">
          <span class="cdot" style="background:#1f4e79"></span> Case-Shiller GLS</label>
      </div>
    </div>
    <div class="model-group">
      <div class="model-group-label">Persistence <span class="info-i" onclick="toggleTip(event,'tip-pc')">i</span></div>
      <div class="model-tip" id="tip-pc">Crime is persistent&mdash;high-crime tracts stay high-crime. Controls for historical crime counts to separate persistent from transitory capitalization.</div>
      <div class="model-sub">
        <label style="opacity:0.4"><input type="checkbox" class="ax-pc" value="none" disabled onchange="render()">
          Standard <em style="font-size:10px;color:#888">(coming soon)</em></label>
        <label><input type="checkbox" class="ax-pc" value="pc" checked onchange="render()">
          Persistence Controlled</label>
      </div>
    </div>
    <div class="model-group">
      <div class="model-group-label">Selection Correction <span class="info-i" onclick="toggleTip(event,'tip-sel')">i</span></div>
      <div class="model-tip" id="tip-sel">Repeat sales requires two transactions. Properties that sell infrequently may differ systematically. Heckman corrects for non-random selection into the repeat-sales sample.</div>
      <div class="model-sub">
        <label><input type="checkbox" class="ax-sel" value="none" checked onchange="render()">
          None</label>
        <label style="opacity:0.4"><input type="checkbox" class="ax-sel" value="heckman" disabled onchange="render()">
          Heckman (&lambda;) <em style="font-size:10px;color:#888">(coming soon)</em></label>
      </div>
    </div>

    <div class="legend-row">
      <div class="legend-item"><span class="legend-sw" style="background:#c8c6be"></span> Not sig.</div>
      <div class="legend-item"><span class="legend-sw" style="background:#1f4e79"></span> Main sig.</div>
      <div class="legend-item"><span class="legend-sw" style="background:#27ae60"></span> Placebo sig.</div>
      <div class="legend-item"><span class="legend-sw" style="background:#e8a0a0"></span> Both</div>
    </div>
  </div>

  <div class="display">
    <div id="results-content">
    <div id="rq-hero">
    <p style="font-size:11px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:#888780;margin:0 0 6px;">Research Question</p>
    <p style="font-size:17px;color:#1a1a18;line-height:1.6;margin:0 0 20px;font-family:'Lora',Georgia,serif;">
      How does the salience of crime drive its capitalization into residential property values?
    </p>
    <div style="display:flex;gap:14px;margin-bottom:24px;">
      <div style="flex:1;background:#fff;border-left:3px solid #8B2F1A;border-top:.5px solid #d3d1c7;border-right:.5px solid #d3d1c7;border-bottom:.5px solid #d3d1c7;border-radius:0 10px 10px 0;padding:12px 16px;">
        <div style="font-size:10px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:#b4b2a9;margin-bottom:2px;">Hyperlocal</div>
        <div style="font-size:24px;font-weight:500;color:#672414;font-family:'Lora',Georgia,serif;line-height:1.2;">&minus;0.10%</div>
        <div style="font-size:12px;color:#5f5e5a;margin-top:2px;line-height:1.4;">near &minus; far differential (&delta;) per crime</div>
      </div>
      <div style="flex:1;background:#fff;border-left:3px solid #8B2F1A;border-top:.5px solid #d3d1c7;border-right:.5px solid #d3d1c7;border-bottom:.5px solid #d3d1c7;border-radius:0 10px 10px 0;padding:12px 16px;">
        <div style="font-size:10px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:#b4b2a9;margin-bottom:2px;">Ignored far</div>
        <div style="font-size:24px;font-weight:500;color:#672414;font-family:'Lora',Georgia,serif;line-height:1.2;">0%</div>
        <div style="font-size:12px;color:#5f5e5a;margin-top:2px;line-height:1.4;">Far crime predicts near crime (p &lt; 0.01) but is priced at zero</div>
      </div>
      <div style="flex:1;background:#fff;border-left:3px solid #8B2F1A;border-top:.5px solid #d3d1c7;border-right:.5px solid #d3d1c7;border-bottom:.5px solid #d3d1c7;border-radius:0 10px 10px 0;padding:12px 16px;">
        <div style="font-size:10px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:#b4b2a9;margin-bottom:2px;">Crime type</div>
        <div style="font-size:24px;font-weight:500;color:#672414;font-family:'Lora',Georgia,serif;line-height:1.2;">&mdash;</div>
        <div style="font-size:12px;color:#5f5e5a;margin-top:2px;line-height:1.4;">coming</div>
      </div>
    </div>
    </div>
    <h2 style="text-align:left;font-size:16px;font-weight:500;color:#672414;font-family:'Lora',Georgia,serif;margin:0 0 16px">Results</h2>
    <div id="display"></div>
    </div>
    <div class="tab-frame" id="frame-data"><iframe src="data_descriptives.html"></iframe></div>
    <div class="tab-frame" id="frame-ident"><iframe src="identification.html"></iframe></div>
    <div class="tab-frame" id="frame-geo"><iframe src="geography.html"></iframe></div>
    <div class="tab-frame" id="frame-robust"><iframe src="robustness.html"></iframe></div>
  </div>
</div>

<script>
function toggleTip(e,id){
  e.stopPropagation();
  var tips = document.querySelectorAll('.model-tip');
  var target = document.getElementById(id);
  var isOpen = target.classList.contains('open');
  tips.forEach(function(t){t.classList.remove('open')});
  if(!isOpen){
    var btn = e.currentTarget;
    var r = btn.getBoundingClientRect();
    target.style.left = (r.right + 12) + 'px';
    target.style.top = (r.top - 4) + 'px';
    target.classList.add('open');
  }
}
document.addEventListener('click',function(){
  document.querySelectorAll('.model-tip').forEach(function(t){t.classList.remove('open')});
});

function showTab(id){
  var frames = document.querySelectorAll('.tab-frame');
  var btns = document.querySelectorAll('.topnav-item');
  var results = document.getElementById('results-content');
  var sidebarInner = document.querySelectorAll('.sidebar > *');
  frames.forEach(function(f){f.style.display='none'});
  btns.forEach(function(b){b.classList.remove('active')});
  if(id==='results'){
    results.style.display='block';
    btns[0].classList.add('active');
    sidebarInner.forEach(function(el){el.style.visibility='visible'});
  } else {
    results.style.display='none';
    var frame = document.getElementById('frame-'+id);
    if(frame) frame.style.display='block';
    event.currentTarget.classList.add('active');
    sidebarInner.forEach(function(el){el.style.visibility='hidden'});
  }
}

var DATA = __DATA_PLACEHOLDER__;

var HET_LABELS = {OLS:'OLS', GLS:'Case-Shiller GLS'};
var PC_LABELS = {none:'Standard', pc:'Persistence Controlled'};
var SEL_LABELS = {none:'', heckman:'Heckman'};
var PT_LABELS = {All:'All Properties',ALL_nonresid:'All Properties',ALL_resid:'All (residential subset)',SF:'Single-Family',Condo:'Condo',Multi:'Multi-Unit',Townhouse:'Townhouse'};

function modelLabel(het,pc,sel){
  var parts = [];
  if(sel!=='none') parts.push(SEL_LABELS[sel]);
  parts.push(HET_LABELS[het]);
  parts.push(PC_LABELS[pc]);
  return parts.join(' \\u2014 ');
}

var MC = {
  OLS_none:'#1f4e79', OLS_pc:'#5b9bd5',
  GLS_none:'#2e7d6e', GLS_pc:'#1f4e79',
  OLS_none_heckman:'#2e75b6', OLS_pc_heckman:'#9dc3e6',
  GLS_none_heckman:'#3a9485', GLS_pc_heckman:'#8ecfc3'
};

function modelKey(het,pc,sel){
  if(sel==='none') return het+'_'+pc;
  return het+'_'+pc+'_'+sel;
}
function modelColor(het,pc,sel){
  var k = modelKey(het,pc,sel);
  return MC[k] || '#888';
}

/* backward compat */
var ML = {OLS_none:'OLS \\u2014 Standard',OLS_pc:'OLS \\u2014 Persistence Controlled',
           GLS_none:'Case-Shiller GLS \\u2014 Standard',GLS_pc:'Case-Shiller GLS \\u2014 Persistence Controlled'};
var CL = {total:'Total Spatial Crime',total_spatial:'Total Spatial Crime',drugvice:'Drug/Vice',disorder:'Disorder',
           property:'Property',violent:'Violent',domestic:'Domestic',nonspatial:'Non-Spatial'};

var FL = ['PIN+CA\\u00d7Mo','PIN+YM','PIN+CA\\u00d7Yr+YM','PIN+Tract\\u00d7Mo'];
var WL = ['1m','2m','3m','4m','5m','6m','7m','8m','9m','10m','11m','12m'];
var NL = ['0-0.05','0.05-0.10','0.10-0.15','0.15-0.20','0.20-0.25','0.25-0.30',
           '0-0.10','0-0.15','0-0.20','0-0.25','0-0.30','0.35-0.40'];
var RL = ['0.15-0.20','0.20-0.25','0.25-0.30','0.30-0.35','0.35-0.40',
           '0.40-0.50','0.20-0.30'];

var CATS = [
  {name:'FE',        labels:FL, key:'fi'},
  {name:'Window',    labels:WL, key:'wi'},
  {name:'Near ring', labels:NL, key:'ni'},
  {name:'Far ring',  labels:RL, key:'ri'}
];

/* compute indicator-panel y layout */
function indLayout(){
  var y=0, pos={}, tv=[], tt=[], bounds=[];
  CATS.forEach(function(cat,ci){
    var start=y;
    cat.labels.forEach(function(lbl,oi){
      pos[ci+'_'+oi]=y; tv.push(y); tt.push(lbl); y++;
    });
    bounds.push({s:start,e:y-1,name:cat.name});
    y+=0.6;
  });
  return {pos:pos,tv:tv,tt:tt,bounds:bounds};
}
var IND = indLayout();

function rgba(hex,a){
  var r=parseInt(hex.slice(1,3),16),g=parseInt(hex.slice(3,5),16),
      b=parseInt(hex.slice(5,7),16);
  return 'rgba('+r+','+g+','+b+','+a+')';
}

function render(){
  var ct = document.getElementById('crime-select').value;
  var pt = document.getElementById('prop-select').value;
  var isDelta = true;
  var disp = document.getElementById('display');

  /* purge old plots */
  var oldPlots = disp.querySelectorAll('.card-plot');
  for(var i=0;i<oldPlots.length;i++) Plotly.purge(oldPlots[i]);
  disp.innerHTML = '';

  /* check data availability */
  if(!DATA[ct] || !DATA[ct][pt]) {
    disp.innerHTML = '<p style="color:#888;font-size:13px;padding:20px 0;">Coming soon — this combination has not been computed yet.</p>';
    return;
  }

  /* read model axes and compute all combinations */
  var hets=[], pcs=[], sels=[];
  document.querySelectorAll('.ax-het:checked').forEach(function(e){hets.push(e.value)});
  document.querySelectorAll('.ax-pc:checked').forEach(function(e){pcs.push(e.value)});
  document.querySelectorAll('.ax-sel:checked').forEach(function(e){sels.push(e.value)});

  var checked = [];
  hets.forEach(function(h){pcs.forEach(function(p){sels.forEach(function(s){
    checked.push({het:h,pc:p,sel:s,mk:modelKey(h,p,s)});
  })})});

  checked.forEach(function(combo){
    var mk = combo.mk;
    if(!DATA[ct][pt][mk]) return;
    var d = DATA[ct][pt][mk];
    var n = d.ns, color = modelColor(combo.het,combo.pc,combo.sel), hasPost = d.hp;

    /* pick arrays based on metric */
    var preB = isDelta ? d.bd : d.b;
    var preS = isDelta ? d.sd : d.s;
    var preP = isDelta ? d.pd : d.p;
    var postB = isDelta ? (d.bpd||null) : (d.bp||null);
    var postS = isDelta ? (d.spd||null) : (d.sp||null);
    var postP = isDelta ? (d.ppd||null) : (d.pp||null);
    var nPreSig = isDelta ? d.npd : d.np;
    var nPostSig = isDelta ? (d.npsd!=null?d.npsd:null) : (d.nps!=null?d.nps:null);

    /* sort order by selected metric pre-sale beta */
    var ord = Array.from({length:n},function(_,i){return i});
    ord.sort(function(a,b){return preB[a]-preB[b]});

    /* card DOM */
    var card = document.createElement('div'); card.className='card';
    var title = document.createElement('div'); title.className='card-title';
    var metLabel = isDelta ? ' (\\u03b4)' : '';
    var ptLabel = pt !== 'All' ? ' \\u2014 '+PT_LABELS[pt] : '';
    title.innerHTML = '<span style="color:'+color+'">&#9632;</span> '+modelLabel(combo.het,combo.pc,combo.sel)+' \\u2014 '+CL[ct]+ptLabel+metLabel;
    card.appendChild(title);

    var plotDiv = document.createElement('div'); plotDiv.className='card-plot';
    card.appendChild(plotDiv);

    var footer = document.createElement('div'); footer.className='card-footer';
    var ft = 'Main: '+nPreSig+'/'+n+' sig ('+Math.round(100*nPreSig/n)+'%)';
    if(hasPost && nPostSig!=null) ft += ' | Placebo: '+nPostSig+'/'+n+' sig ('+Math.round(100*nPostSig/n)+'%)';
    footer.textContent = ft;
    card.appendChild(footer);
    disp.appendChild(card);

    /* ── build traces ── */
    var traces = [];

    /* Row 1: pre-sale coefficients (sorted by selected metric) */
    var preCleanX=[],preCleanY=[],preCleanE=[],preCleanH=[];
    var preBothX=[],preBothY=[],preBothE=[],preBothH=[];
    var preNsX=[],preNsY=[],preNsE=[],preNsH=[];
    for(var xi=0;xi<n;xi++){
      var j = ord[xi];
      var sig = preP[j]<0.05;
      var sigPost = (hasPost && postP) ? postP[j]<0.05 : false;
      var hov = '<b>Spec '+(xi+1)+'/'+n+'</b><br>'+
        'FE: '+FL[d.fi[j]]+'<br>Window: '+WL[d.wi[j]]+'<br>'+
        'Near: '+NL[d.ni[j]]+'<br>Far: '+RL[d.ri[j]]+'<br>'+
        (isDelta?'\\u03b4':'\\u03b2')+': '+preB[j].toFixed(4)+'%<br>SE: '+preS[j].toFixed(4)+'%<br>p: '+preP[j].toFixed(4);
      if(sig && sigPost){preBothX.push(xi);preBothY.push(preB[j]);preBothE.push(1.96*preS[j]);preBothH.push(hov);}
      else if(sig){preCleanX.push(xi);preCleanY.push(preB[j]);preCleanE.push(1.96*preS[j]);preCleanH.push(hov);}
      else{preNsX.push(xi);preNsY.push(preB[j]);preNsE.push(1.96*preS[j]);preNsH.push(hov);}
    }

    if(preNsX.length>0) traces.push({
      x:preNsX,y:preNsY,
      error_y:{type:'data',array:preNsE,visible:true,color:'rgba(160,158,150,0.25)',thickness:0.3,width:0},
      mode:'markers',marker:{size:3,color:'#a0a098',opacity:0.45},
      hovertemplate:'%{customdata}<extra></extra>',customdata:preNsH,
      hoverlabel:{bgcolor:'#faf9f7',bordercolor:'#d3d1c7',font:{size:11,family:'Inter',color:'#b4b2a9'}},
      showlegend:false,xaxis:'x',yaxis:'y'
    });
    if(preCleanX.length>0) traces.push({
      x:preCleanX,y:preCleanY,
      error_y:{type:'data',array:preCleanE,visible:true,color:rgba(color,0.5),thickness:1,width:2},
      mode:'markers',marker:{size:5,color:color,opacity:1.0},
      hovertemplate:'%{customdata}<extra></extra>',customdata:preCleanH,
      hoverlabel:{bgcolor:'white',bordercolor:'#672414',font:{size:11,family:'Inter',color:'#672414'}},
      showlegend:false,xaxis:'x',yaxis:'y'
    });
    if(preBothX.length>0) traces.push({
      x:preBothX,y:preBothY,
      error_y:{type:'data',array:preBothE,visible:true,color:'rgba(232,160,160,0.3)',thickness:0.5,width:1},
      mode:'markers',marker:{size:3,color:'#e8a0a0',opacity:0.8},
      hovertemplate:'%{customdata}<extra></extra>',customdata:preBothH,
      hoverlabel:{bgcolor:'white',bordercolor:'#d3d1c7',font:{size:11,family:'Inter',color:'#4a4a46'}},
      showlegend:false,xaxis:'x',yaxis:'y'
    });

    /* Row 2: indicator dots (using same sort order) */
    var dots = {none:{x:[],y:[]},pre:{x:[],y:[]},post:{x:[],y:[]},both:{x:[],y:[]}};
    for(var xi=0;xi<n;xi++){
      var j = ord[xi];
      var sp = preP[j]<0.05;
      var spo = (hasPost && postP) ? postP[j]<0.05 : false;
      var g = (sp&&spo)?'both':sp?'pre':spo?'post':'none';
      dots[g].x.push(xi); dots[g].y.push(IND.pos['0_'+d.fi[j]]);
      dots[g].x.push(xi); dots[g].y.push(IND.pos['1_'+d.wi[j]]);
      dots[g].x.push(xi); dots[g].y.push(IND.pos['2_'+d.ni[j]]);
      dots[g].x.push(xi); dots[g].y.push(IND.pos['3_'+d.ri[j]]);
    }
    var dS = {
      none:{color:'gray',opacity:0.2,size:3},
      pre:{color:color,opacity:0.85,size:4},
      post:{color:'#27ae60',opacity:0.85,size:4},
      both:{color:'#e8a0a0',opacity:0.9,size:5}
    };
    ['none','pre','post','both'].forEach(function(g){
      if(dots[g].x.length>0) traces.push({
        x:dots[g].x,y:dots[g].y,mode:'markers',
        marker:{size:dS[g].size,color:dS[g].color,opacity:dS[g].opacity,symbol:'square'},
        showlegend:false,hoverinfo:'skip',xaxis:'x2',yaxis:'y2'
      });
    });

    /* Row 3: post-sale placebo (if exists) — green/gray scheme, distinct from main. */
    if(hasPost && postB){
      var postSigX=[],postSigY=[],postSigE=[],postSigH=[];
      var postNsX=[],postNsY=[],postNsE=[],postNsH=[];
      for(var xi=0;xi<n;xi++){
        var j = ord[xi];
        var sig = postP[j]<0.05;
        var hov = '<b>Spec '+(xi+1)+'/'+n+' (placebo)</b><br>'+
          'FE: '+FL[d.fi[j]]+'<br>Window: '+WL[d.wi[j]]+'<br>'+
          'Near: '+NL[d.ni[j]]+'<br>Far: '+RL[d.ri[j]]+'<br>'+
          (isDelta?'\\u03b4':'\\u03b2')+': '+postB[j].toFixed(4)+'%<br>SE: '+postS[j].toFixed(4)+'%<br>p: '+postP[j].toFixed(4);
        if(sig){postSigX.push(xi);postSigY.push(postB[j]);postSigE.push(1.96*postS[j]);postSigH.push(hov);}
        else{postNsX.push(xi);postNsY.push(postB[j]);postNsE.push(1.96*postS[j]);postNsH.push(hov);}
      }
      if(postNsX.length>0) traces.push({
        x:postNsX,y:postNsY,
        error_y:{type:'data',array:postNsE,visible:true,color:'rgba(160,158,150,0.25)',thickness:0.3,width:0},
        mode:'markers',marker:{size:3,color:'#a0a098',opacity:0.45},
        hovertemplate:'%{customdata}<extra></extra>',customdata:postNsH,
        hoverlabel:{bgcolor:'#faf9f7',bordercolor:'#d3d1c7',font:{size:11,family:'Inter',color:'#b4b2a9'}},
        showlegend:false,xaxis:'x3',yaxis:'y3'
      });
      if(postSigX.length>0) traces.push({
        x:postSigX,y:postSigY,
        error_y:{type:'data',array:postSigE,visible:true,color:'rgba(125,186,153,0.5)',thickness:1,width:2},
        mode:'markers',marker:{size:5,color:'#7dba99',opacity:1.0},
        hovertemplate:'%{customdata}<extra></extra>',customdata:postSigH,
        hoverlabel:{bgcolor:'white',bordercolor:'#7dba99',font:{size:11,family:'Inter',color:'#1a1a18'}},
        showlegend:false,xaxis:'x3',yaxis:'y3'
      });
    }

    /* y-axis range (symmetric, shared between pre and post) */
    var ymxP = 0;
    for(var i=0;i<n;i++) ymxP = Math.max(ymxP, Math.abs(preB[i]));
    var ymx = ymxP * 1.15;
    if(hasPost && postB){
      var ymxQ = 0;
      for(var i=0;i<n;i++) ymxQ = Math.max(ymxQ, Math.abs(postB[i]));
      ymx = Math.max(ymx, ymxQ * 1.15);
    }
    if(ymx < 0.01) ymx = 0.05;

    /* ── layout ── */
    var shapes = [{
      type:'line',x0:-10,x1:n+10,y0:0,y1:0,
      xref:'x',yref:'y',line:{color:'black',width:0.8,dash:'dot'}
    }];

    /* category separator lines */
    IND.bounds.forEach(function(bd){
      if(bd.s>0) shapes.push({
        type:'line',x0:-10,x1:n+10,y0:bd.s-0.3,y1:bd.s-0.3,
        xref:'x2',yref:'y2',line:{color:'#d3d1c7',width:0.5}
      });
    });

    /* category label annotations */
    var anns = IND.bounds.map(function(bd){
      return {text:'<b>'+bd.name+'</b>',x:1.01,y:(bd.s+bd.e)/2,
        xref:'paper',yref:'y2',showarrow:false,
        font:{size:9,color:'#888780'},xanchor:'left',yanchor:'middle'};
    });

    /* pre-sale header annotation */
    anns.push({text:'<b>Main (sale after crime) \u2014 '+nPreSig+'/'+n+' sig ('+Math.round(100*nPreSig/n)+'%)</b>',
      x:0.47,y:0.98,xref:'paper',yref:'paper',showarrow:false,
      font:{size:10,color:color},xanchor:'center',yanchor:'bottom'});

    var lay = {
      height: hasPost ? 650 : 500,
      showlegend:false,
      margin:{l:60,r:55,t:10,b:20},
      font:{family:'Inter,sans-serif',size:12,color:'#1a1a18'},
      paper_bgcolor:'#fff',plot_bgcolor:'#fff',
      hoverlabel:{bgcolor:'white',font:{size:11,family:'Inter'},bordercolor:'#d3d1c7'},
      xaxis: {domain:[0,0.94],showticklabels:false,showgrid:false,zeroline:false,anchor:'y'},
      xaxis2:{domain:[0,0.94],showticklabels:false,showgrid:false,zeroline:false,anchor:'y2',matches:'x'},
      yaxis: {
        domain:hasPost?[0.52,1.0]:[0.42,1.0],anchor:'x',
        title:{text:isDelta?'\\u03b4\\u00d7100  (% \\u0394 price)':'\\u03b2_near\\u00d7100  (% \\u0394 price)',font:{size:11}},
        gridcolor:'#d3d1c7',zeroline:false,range:[-ymx,ymx]
      },
      yaxis2:{
        domain:hasPost?[0.18,0.50]:[0.0,0.40],anchor:'x2',
        tickmode:'array',tickvals:IND.tv,ticktext:IND.tt,
        tickfont:{size:7.5},gridcolor:'rgba(0,0,0,0)',zeroline:false,
        autorange:'reversed'
      },
      shapes:shapes,
      annotations:anns
    };

    if(hasPost){
      lay.xaxis3 = {domain:[0,0.94],showticklabels:false,showgrid:false,zeroline:false,anchor:'y3',matches:'x'};
      lay.yaxis3 = {
        domain:[0.0,0.15],anchor:'x3',
        title:{text:'Placebo: '+(isDelta?'\\u03b4\\u00d7100  (% \\u0394 price)':'\\u03b2_near\\u00d7100  (% \\u0394 price)'),font:{size:11}},
        gridcolor:'#d3d1c7',zeroline:false,range:[-ymx,ymx]
      };
      shapes.push({
        type:'line',x0:-10,x1:n+10,y0:0,y1:0,
        xref:'x3',yref:'y3',line:{color:'black',width:0.8,dash:'dot'}
      });
      anns.push({text:'<b>Placebo (sale before crime) \u2014 '+nPostSig+'/'+n+' sig ('+Math.round(100*nPostSig/n)+'%)</b>',x:0.47,y:0.16,
        xref:'paper',yref:'paper',showarrow:false,
        font:{size:10,color:'#27ae60'},xanchor:'center'});
    }

    Plotly.newPlot(plotDiv, traces, lay, {displayModeBar:false,responsive:true});
  });

  /* Multi-unit caveat — show only when Multi + PC is selected */
  var pcChecked = document.querySelectorAll('.ax-pc:checked');
  var hasPc = false;
  pcChecked.forEach(function(e){if(e.value==='pc') hasPc=true;});
  if(pt === 'Multi' && hasPc){
    var caveat = document.createElement('div');
    caveat.style.cssText = 'margin-top:24px;padding:16px 20px;background:#fff;border:1px solid #d3d1c7;border-left:3px solid #e67e73;border-radius:0 8px 8px 0;font-size:12px;color:#4a4a46;line-height:1.7;';
    caveat.innerHTML = '<strong style="color:#b03a2e;">Interpretation note (2\u20136 unit multifamily)</strong><br>' +
      'The salience mechanism predicts no near\u2013far gradient for buyers who do not form prices through direct property observation. ' +
      'Investor-driven multifamily transactions, characterized by professional underwriting rather than consumer salience, ' +
      'fail the near\u2013far placebo discipline (post-sale placebo significance rate exceeds pre-sale rate in several specifications, ' +
      'indicating spatial trajectory confounding rather than causal hyperlocal capitalization). ' +
      'This is consistent with the salience mechanism not applying to professional investor markets, ' +
      'though we cannot cleanly distinguish \u2018no salience effect\u2019 from \u2018identification failure.\u2019';
    disp.appendChild(caveat);
  }
}

render();
</script>
</body>
</html>'''

    html = html.replace('__DATA_PLACEHOLDER__', data_json)
    (OUT_DIR / 'spec_explorer.html').write_text(html)
    print("  ✓ spec_explorer.html")


# ── Run all ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    make_spatial_decay()
    make_time_decay()
    make_crimetype_heatmap()
    make_spec_curve()
    make_spec_explorer()
    print("\nDone!")
