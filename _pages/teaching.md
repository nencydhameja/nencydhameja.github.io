---
layout: archive
title: ""
permalink: /teaching/
author_profile: true
---

<style>
  body, .page, #main { background: #f7f6f3 !important; }  /* CHANGED: warm page bg so white panels pop (homepage stays white) */

  .talk-section { margin-bottom: 0.35rem; }

  .year-card {
    /* background: #f7f6f3; */
    background: #fff;
    border: 0.5px solid #d3d1c7;
    border-radius: 0;
    overflow: hidden;
    margin-bottom: 0.35rem;
    max-width: 580px;
  }

  .year-card-header {
    padding: 0.2rem 1.1rem;
    /* background: #ede9e0; */
    background: #fff;
    border-bottom: 0.5px solid #d3d1c7;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #888780;
    font-size: 10px;
  }

  .talk-row {
    display: grid;
    grid-template-columns: 96px 1fr auto;  /* CHANGED: term+year label (96px) + course name + right column for the small course number (where the term used to be) */
    column-gap: 1.1rem;
    align-items: baseline;
    padding: 0.26rem 1.2rem;
    border-bottom: 0.5px solid #f1efe8;
  }
  .talk-year { font-size: 12px; font-weight: 400; color: #8a8880; }  /* CHANGED: term+year, no longer bold (was font-weight 600) */
  .talk-num { font-size: 8.5px; color: #a7a59c; letter-spacing: 0.02em; text-align: right; white-space: nowrap; }  /* CHANGED: small course number in right column (where the term column used to be) */

  .talk-row:last-child { border-bottom: none; }

  .talk-name {
    font-size: 11px;          /* CHANGED: was 12.5px -> 11px, smaller course text */
    font-weight: 500;
    color: #1a1a18;
  }

  .talk-abbr {
    font-size: 11px;          /* CHANGED: was 12.5px -> 11px */
    font-weight: 400;
    color: #888780;
  }
  .talk-name .talk-abbr { font-size: 8.5px; color: #a7a59c; letter-spacing: 0.02em; }  /* CHANGED: was 10px -> 8.5px, smaller inline course number */

  .talk-meta {
    display: flex;
    gap: 1.25rem;
    flex-shrink: 0;
    align-items: baseline;
  }

  .talk-location { font-size: 11.5px; color: #5f5e5a; text-align: right; white-space: nowrap; }

  .talk-date {
    font-size: 12px;
    color: #b4b2a9;
    min-width: 54px;
    text-align: right;
  }

  .section-title {
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #888780;
    margin: 1rem 0 0.3rem;
  }

  .page-heading {
    font-size: 19px;
    font-weight: 600;
    color: #1a1a18;
    margin: 1.5rem 0 0.9rem;
    padding-bottom: 0.3rem;
    border-bottom: 1px solid #d3d1c7;
    display: block;   /* full width — matches its OWN section's content (e.g. the wider simulations grid) */
  }
  .page-heading:first-of-type { margin-top: 0.5rem; max-width: 580px; }   /* CHANGED: Courses Taught underline capped to 580px to match the courses card; the general (Teaching Tools) heading stays full-width to match the simulations grid */

  .page-intro {
    font-size: 14.5px;
    color: #5f5e5a;
    line-height: 1.55;
    margin: -0.3rem 0 1.1rem;
  }

  /* One simulation per row, natural size */
  .demo-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.9rem;
    margin-bottom: 1.1rem;
  }
  .demo-card {
    border: 0.5px solid #d3d1c7;
    border-radius: 0;
    overflow: hidden;
    background: #fff;
  }
  .demo-card-header {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 1rem;
    padding: 0.5rem 1.1rem;
    background: #fff;
    border-bottom: 0.5px solid #d3d1c7;
  }
  .demo-title { font-size: 14.5px; font-weight: 500; color: #1a1a18; }
  .demo-title .talk-abbr { font-weight: 400; color: #888780; }
  .demo-open { font-size: 12px; color: #185FA5; text-decoration: none; white-space: nowrap; }
  /* Viewport clips the scaled iframe; the iframe renders large then is
     zoomed out so the whole widget fits inside a half-width card. */
  .demo-viewport {
    height: 330px;
    overflow: hidden;
    border: 0;
  }
  .demo-frame {
    width: 182%;
    height: 600px;
    transform: scale(0.55);
    transform-origin: top left;
    border: 0;
    display: block;
  }
  .demo-more {
    font-size: 13.5px;
    color: #5f5e5a;
    margin: 0.2rem 0 0.4rem;
    line-height: 1.6;
  }
  .demo-more a { color: #185FA5; text-decoration: none; }
  .demo-launch {
    width: 100%;
    height: 100%;               /* CHANGED: was 430px -> fill the 330px viewport so the placeholder matches the loaded sim height */
    border: 0;
    background: #f7f6f3;
    color: #185FA5;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.35rem;
    transition: background 0.15s ease;
  }
  .demo-launch:hover { background: #ece7dd; }
  /* CHANGED: placeholder shown until the lazy-loaded sim iframe is injected */
  .demo-ph {
    display: flex;
    width: 100%;
    height: 100%;
    align-items: center;
    justify-content: center;
    background: #f7f6f3;
    color: #a7a59c;
    font-size: 12.5px;
  }
  .demo-launch small { color: #888780; font-weight: 400; font-size: 11.5px; }
  .demo-spin { font-weight: 500; }
  .demo-link {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding: 0.7rem 1.1rem;
    border: 0.5px solid #d3d1c7;
    background: #fff;
    text-decoration: none;
    transition: background 0.15s ease;
  }
  .demo-link:hover { background: #f7f6f3; }
  .dl-title { font-size: 14px; font-weight: 500; color: #1a1a18; }
  .dl-title small { color: #888780; font-weight: 400; font-size: 11.5px; margin-left: 0.45rem; }
  .dl-cta { font-size: 12.5px; color: #185FA5; white-space: nowrap; }
  /* CHANGED: demos now open the standalone sim in a new tab (iframe-embedded shinylive is unreliable on GitHub Pages) */
  .demo-launch-card { display: block; text-decoration: none; }
  .demo-launch-card .demo-launch { min-height: 128px; }
</style>

<div class="page-heading">Courses Taught</div>

<div class="section-title">Instructor — Binghamton University, NY, USA</div>
<div class="talk-section">
  <div class="year-card">
    <div class="talk-row"><span class="talk-year">Winter 2026</span><span class="talk-name">Economic Poverty &amp; Discrimination</span><span class="talk-num">ECON 144</span></div>
  </div>
</div>

<div class="section-title">Teaching Assistant — Binghamton University, NY, USA</div>
<div class="talk-section">
  <div class="year-card">
    <div class="talk-row"><span class="talk-year">Fall 2026</span><span class="talk-name">Introduction to Econometrics</span><span class="talk-num">ECON 466</span></div>
    <div class="talk-row"><span class="talk-year"></span><span class="talk-name">Macroeconomic Theory</span><span class="talk-num">ECON 362</span></div>
    <div class="talk-row"><span class="talk-year">Spring 2026</span><span class="talk-name">Economics of Education</span><span class="talk-num">ECON 448</span></div>
    <div class="talk-row"><span class="talk-year">Fall 2025</span><span class="talk-name">Behavioral Economics</span><span class="talk-num">ECON 483C</span></div>
    <div class="talk-row"><span class="talk-year">Spring 2025</span><span class="talk-name">Agent-Based Modeling (Python)</span><span class="talk-num">ECON 570/670</span></div>
    <div class="talk-row"><span class="talk-year">Fall 2024</span><span class="talk-name">Forecasting</span><span class="talk-num">ECON 476</span></div>
    <div class="talk-row"><span class="talk-year"></span><span class="talk-name">Introduction to Econometrics</span><span class="talk-num">ECON 466</span></div>
    <div class="talk-row"><span class="talk-year">Spring 2024</span><span class="talk-name">Econometrics</span><span class="talk-num">ECON 616</span></div>
    <div class="talk-row"><span class="talk-year">Fall 2023</span><span class="talk-name">Economic Development of Latin America</span><span class="talk-num">ECON 483</span></div>
    <div class="talk-row"><span class="talk-year">Spring 2023</span><span class="talk-name">U.S. Financial Systems: Markets &amp; Institutions</span><span class="talk-num">ECON 350</span></div>
    <div class="talk-row"><span class="talk-year">Fall 2022</span><span class="talk-name">Economics of Corporations</span><span class="talk-num">ECON 454</span></div>
  </div>
</div>

<div class="page-heading">Teaching Tools &amp; Simulations</div>
<p class="page-intro">
  I build browser-based teaching simulations that run entirely in the browser (no installs), so
  students can experiment with the models directly. Explore them in my
  <a href="/econlab/" style="color:#185FA5;text-decoration:none;">Econ&nbsp;Lab</a>.
</p>

<!-- Simulation cards hidden for now (they live in Econ Lab); uncomment to show them here
<div class="demo-grid">
<a class="demo-card demo-launch-card" href="/econlab/stats-course/simulations.html" target="_blank" rel="noopener">
  <div class="demo-card-header">
    <span class="demo-title">Central Limit Theorem <span class="talk-abbr">Statistics</span></span>
    <span class="demo-open">Launch &#8599;</span>
  </div>
  <div class="demo-launch"><span class="demo-spin">Open interactive simulation</span><small>runs in your browser</small></div>
</a>
<a class="demo-card demo-launch-card" href="/econlab/intermediate-micro/choice.html" target="_blank" rel="noopener">
  <div class="demo-card-header">
    <span class="demo-title">Consumer Choice <span class="talk-abbr">Intermediate Micro</span></span>
    <span class="demo-open">Launch &#8599;</span>
  </div>
  <div class="demo-launch"><span class="demo-spin">Open interactive simulation</span><small>runs in your browser</small></div>
</a>
</div>
-->
