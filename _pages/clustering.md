---
layout: single
title: "Why Standard Errors Change"
permalink: /clustering/
author_profile: false
classes: wide
---

<style>
.page {
  float: none !important;
  width: 100% !important;
  margin-left: 0 !important;
  margin-right: 0 !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
}
.note-container {
  max-width: 820px;
  margin: 0 auto;
}
.concept-box {
  background: rgba(255,255,255,0.85);
  border-left: 4px solid #2563eb;
  border-radius: 8px;
  padding: 18px 22px;
  margin: 1.5rem 0;
}
.concept-box h3 {
  margin-top: 0;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 1rem 0;
}
th, td {
  border: 1px solid #d1d5db;
  padding: 8px 14px;
  text-align: left;
}
th {
  background: #f3f4f6;
}
</style>

<div class="note-container">

OLS assumes:

$$E[u_i \, u_j] = 0 \quad \text{for } i \neq j$$

But in panel or spatial data, **that is false.**

Observations are correlated within:
- The same property
- The same census tract
- The same county
- The same time period
- The same firm
- The same school

If you ignore that, your SEs are **too small** &rarr; false significance.

**Clustering corrects this.**

---

## Intuition

If shocks are correlated within group \\(g\\):

$$u_{ig} = \underbrace{\text{common component}}_{\text{shared within cluster}} + \underbrace{\text{idiosyncratic}}_{\text{independent across obs.}}$$

Then treating observations as independent **overcounts information.**

Clustering says: *treat each cluster as the unit of independent variation.*

---

## What Happens When You Change Cluster Level?

Suppose you estimate:

$$\ln P_{it} = \beta \, \text{Shock}_{it} + \text{FE} + u_{it}$$

Now consider clustering at:

<div class="concept-box">
<h3>1. Property (PIN)</h3>
Allows arbitrary serial correlation within property over time.<br>
SE usually <strong>&uarr;</strong> relative to naive.
</div>

<div class="concept-box">
<h3>2. Census Tract</h3>
Allows correlation across different properties in same tract.<br>
If crime shocks spill over spatially, this matters.<br>
SE likely <strong>&uarr;</strong> further.
</div>

<div class="concept-box">
<h3>3. County</h3>
Allows even broader spatial correlation.<br>
SE <strong>&uarr;</strong> more.
</div>

<div class="concept-box" style="border-left-color: #dc2626;">
<h3>4. No Clustering</h3>
Assumes independence.<br>
SE smallest. <strong>Usually wrong.</strong>
</div>

---

## Why Larger Clusters Often Increase SE

Because:

$$\text{Var}(\hat{\beta}) \;\propto\; \frac{1}{G}$$

where \\(G\\) = number of independent clusters (not \\(N\\)).

| Cluster Level | # Clusters | SE |
|---|---|---|
| Property | Many | Smaller |
| Tract | Fewer | Larger |
| County | Few | Largest |

The effective sample size becomes \\(G\\), not \\(N\\).

---

## Key Principle

<div class="concept-box" style="border-left-color: #f59e0b; background: rgba(255,243,220,0.7);">
You should cluster at the level where the <strong>identifying variation is correlated.</strong>
</div>

---

## In the Crime&ndash;Housing Context

The setting uses:
- Spatial kernel exposure
- Properties within tracts
- Crime shocks at neighborhood level

Errors are likely correlated within:
- **Census tract**
- Possibly community area
- Possibly time &times; area

So **clustering at tract** is reasonable.

</div>
