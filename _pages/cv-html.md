---
layout: archive
title: "CV"
permalink: /cv-html/
author_profile: true
---

<style>
  .archive {
    width: 80%;
    margin: 0 auto;
    float: none;
    padding-right: 0;
  }
  @media (min-width: 80em) {
    .archive { width: 70%; }
  }

  .cv-wrap {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 10.5pt;
    line-height: 1.5;
    color: #111;
    border: 0.5px solid rgba(26, 13, 171, 0.25);
    padding: 1.5rem 2rem;
    border-radius: 2px;
  }
  .cv-wrap a { color: #1a0dab; text-decoration: none; }
  .cv-wrap a:hover { text-decoration: underline; }

  .cv-header-info {
    display: flex;
    justify-content: space-between;
    margin-bottom: 1.2rem;
  }
  .cv-address-right { text-align: right; }
  .cv-email { font-family: 'Courier New', monospace; font-size: 10pt; }

  .cv-updated {
    text-align: right;
    font-style: italic;
    font-size: 10pt;
    color: #444;
    margin-bottom: 0.5rem;
  }

  .cv-section { margin-bottom: 1.1rem; }

  .cv-section h2 {
    font-size: 13pt;
    font-weight: 600;
    font-variant: small-caps;
    letter-spacing: 0.05em;
    border-bottom: 0.5px solid #555;
    padding-bottom: 2px;
    margin-bottom: 7px;
    margin-top: 0;
  }

  .cv-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 1rem;
  }
  .cv-left { flex: 1; min-width: 0; }
  .cv-right { white-space: nowrap; flex-shrink: 0; }

  .cv-entry { margin-bottom: 0.45rem; }

  .cv-sub { font-weight: 600; margin: 0.6rem 0 0.25rem; }
  .cv-paper { margin-bottom: 0.5rem; padding-left: 1em; }

  .cv-refs {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.8rem 1rem;
  }
  .cv-ref { font-size: 10.5pt; line-height: 1.6; }
  .cv-ref a { font-weight: 600; }
  .cv-ref .cv-ref-email { font-family: 'Courier New', monospace; font-size: 9.5pt; }
  .cv-ref .cv-ref-email a { font-weight: normal; }

  .cv-download { margin-top: 1.5rem; }

  @media (max-width: 600px) {
    .cv-header-info { flex-direction: column; }
    .cv-address-right { text-align: left; }
    .cv-refs { grid-template-columns: 1fr; }
  }
</style>

<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">

<div class="cv-wrap">

<div class="cv-updated">Last Updated: <script>document.write(new Date().toLocaleDateString('en-US',{month:'long',day:'numeric',year:'numeric'}))</script></div>

<div class="cv-header-info">
  <div>4400 Vestal Pkwy E,<br>Binghamton, NY 13902</div>
  <div class="cv-address-right">
    <span class="cv-email">ndhamej1@binghamton.edu</span><br>
    <a href="https://nencydhameja.com">https://nencydhameja.com/</a>
  </div>
</div>

<section class="cv-section">
  <h2>Fields of Interest</h2>
  <p>Applied Microeconomics (Urban, Labor, Health, Behavioral), Computational Methods</p>
</section>

<section class="cv-section">
  <h2>Education</h2>
  <div class="cv-entry">
    <div class="cv-row"><span class="cv-left"><strong>Binghamton University, USA</strong></span><span class="cv-right">Aug 2021 – present</span></div>
    <div>Ph.D. in Economics (Expected May 2027)</div>
  </div>
  <div class="cv-entry">
    <div class="cv-row"><span class="cv-left"><strong>SP Jain School of Management, Singapore</strong></span><span class="cv-right">Sep 2018 – Jul 2020</span></div>
    <div>Master of Business Administration in Finance</div>
    <div>Dean's List</div>
  </div>
  <div class="cv-entry">
    <div class="cv-row"><span class="cv-left"><strong>Mahatma Gandhi Mission's CoET, India</strong></span><span class="cv-right">Sep 2001 – May 2005</span></div>
    <div>Bachelor of Technology in Electronics &amp; Telecommunications</div>
  </div>
</section>

<section class="cv-section">
  <h2>Research</h2>
  <div class="cv-sub">Job Market Paper</div>
  <div class="cv-entry">
    <strong>Salience, Attention, and Memory: Crime Capitalization in Housing Prices</strong><br>
    Uses repeat-sales panel data and spatial-temporal kernel estimation to identify the causal impact of localized crime shocks via a near-far difference-in-differences design with property fixed effects.
  </div>

  <div class="cv-sub">Working Papers</div>
  <div class="cv-paper">
    <strong>The Effect of Diversity Statements in Faculty Hiring</strong> <em>(with David Slichter)</em><br>
    Uses nationwide faculty job posting data and staggered difference-in-differences to estimate the causal impact of diversity statement requirements on faculty hiring composition and representation outcomes.
  </div>
  <div class="cv-paper">
    <a href="https://chriszosh1.github.io/files/Agent-BasedEconometrics_MC_Zosh_et_al.pdf"><strong>Monte Carlo Diagnostics for Agent-Based Models</strong></a> <em>(with Christopher Zosh, Yixin Ren, Andreas Pape)</em><br>
    Develops simulation-based inference methods for estimating parameters and uncertainty in stochastic agent-based economic models.
  </div>
  <div class="cv-paper">
    <a href="https://chriszosh1.github.io/files/Social_Context_and_LLM_Segregation.pdf"><strong>Social Context in the Schelling Model using LLMs</strong></a> <em>(with Andreas Pape, Srikanth Iyer, Carl Lipo, Yixin Ren, Christopher Zosh)</em><br>
    Embeds large language models as decision-making agents in a Schelling segregation framework to study how social context shapes residential sorting.
  </div>

  <div class="cv-sub">Work in Progress</div>
  <div class="cv-paper">
    <strong>Food Swamps, Obesity, and Metabolic Risks</strong><br>
    Exploits within-tract variation in dollar store entry using continuous-treatment difference-in-differences and entropy balancing to estimate causal effects on obesity.
  </div>
</section>

<section class="cv-section">
  <h2>Employment</h2>
  <div class="cv-entry"><strong>Binghamton University</strong></div>
  <div class="cv-entry">
    <div class="cv-row"><span class="cv-left"><em>Instructor</em> &mdash; Economic Poverty &amp; Discrimination</span><span class="cv-right">Winter 2026</span></div>
  </div>
  <div class="cv-entry">
    <div class="cv-row"><span class="cv-left"><em>Teaching Assistant</em></span><span class="cv-right">Aug 2022 – present</span></div>
    <div>Courses: Econometrics (undergraduate and graduate), Behavioral Economics, Economics of Education, Agent-Based Modeling (Python), Forecasting, Economic Development of Latin America, U.S. Financial Markets &amp; Institutions, Economics of Corporations.</div>
  </div>
  <div class="cv-entry">
    <div class="cv-row"><span class="cv-left"><em>Data Analyst</em>, Graduate Admissions Office</span><span class="cv-right">Aug 2021 – Aug 2022</span></div>
    <div>Created and maintained daily, weekly, and monthly reports for the Graduate Admissions Office.</div>
  </div>
  <div class="cv-entry">
    <em>Prior industry experience:</em> Software engineering and management roles at Grab, Accenture, Jones Lang LaSalle, and Agilent Technologies (2005–2021).
  </div>
</section>

<section class="cv-section">
  <h2>Conference Presentations</h2>
  <div class="cv-entry"><strong>2026</strong><br>
  ASSA Annual Meeting, Jan 2026; Northeast Regional Conference on Complex Systems (NERCCS), Online, Mar 2026; Midwest Economics Association (MEA), Mar 2026; American Society of Health Economists (ASHEcon), Jun 2026; Society for the Advancement of Behavioral Economics (SABE), Jun 2026; Western Economic Association International (WEAI), Jun 2026.</div>
  <div class="cv-entry"><strong>2025</strong><br>
  Eastern Economic Association (EEA), Feb 2025; American Political Science Association (APSA), Online, Feb 2025; FLX Economics of Education Conference, Jun 2025; Western Economic Association International (WEAI), Jun 2025; Southern Economic Association (SEA), Nov 2025.</div>
  <div class="cv-entry"><strong>2024</strong><br>
  Eastern Economic Association (EEA), Feb 2024.</div>
</section>

<section class="cv-section">
  <h2>Poster Presentations</h2>
  <p>Association for Public Policy Analysis &amp; Management (APPAM), Seattle, Nov 2025.</p>
</section>

<section class="cv-section">
  <h2>Professional Service</h2>
  <div>Session Discussant, Midwest Economics Association Annual Meeting (2026)</div>
  <div>Conference Volunteer, Society for Causal Inference Annual Conference (2026)</div>
  <div>Session Chair and Discussant, American Political Science Association (2025)</div>
  <div>Session Discussant, Eastern Economic Association Annual Conference (2024)</div>
</section>

<section class="cv-section">
  <h2>Professional Development</h2>
  <div>Northwestern University, Causal Inference Workshop (Main &amp; Advanced), 2025</div>
  <div>Harvard University, CausalLab Workshop, Scheduled, Summer 2026</div>
</section>

<section class="cv-section">
  <h2>Research Methods and Technical Skills</h2>
  <p>Causal inference (difference-in-differences, event studies, IV, entropy balancing, continuous treatments); spatial methods (kernel estimation, exposure measures); simulation and agent-based modeling (including LLM agent simulations); machine learning (LASSO, Random Forest, XGBoost).</p>
  <p style="margin-top:0.4rem;"><strong>Programming:</strong> Python, Stata, R, SQL.</p>
</section>

<section class="cv-section">
  <h2>Languages</h2>
  <p>English (Fluent), Hindi (Native)</p>
</section>

<section class="cv-section">
  <h2>References</h2>
  <div class="cv-refs">
    <div class="cv-ref">
      <a href="https://sites.google.com/site/slichterdavid/home">Dr. David Slichter</a><br>
      Associate Professor of Economics<br>
      Binghamton University<br>
      <span class="cv-ref-email"><a href="mailto:slichter@binghamton.edu">slichter@binghamton.edu</a></span>
    </div>
    <div class="cv-ref">
      <a href="https://andreasduuspape.com/">Dr. Andreas Pape</a><br>
      Associate Professor of Economics<br>
      Binghamton University<br>
      <span class="cv-ref-email"><a href="mailto:apape@binghamton.edu">apape@binghamton.edu</a></span>
    </div>
    <div class="cv-ref">
      <a href="https://www.binghamton.edu/economics/people/polachek-solomon.html">Dr. Solomon W. Polachek</a><br>
      Distinguished Professor of Economics<br>
      Binghamton University<br>
      <span class="cv-ref-email"><a href="mailto:polachek@binghamton.edu">polachek@binghamton.edu</a></span>
    </div>
    <div class="cv-ref">
      <a href="https://sites.google.com/view/ivan-korolev/home">Dr. Ivan Korolev</a><br>
      Assistant Professor of Economics<br>
      Binghamton University<br>
      <span class="cv-ref-email"><a href="mailto:ikorolev@binghamton.edu">ikorolev@binghamton.edu</a></span>
    </div>
  </div>
</section>

<div class="cv-download">
 <a href="/files/Nency_Dhameja_CV_2026.pdf" class="btn btn--primary" target="_blank">Download CV as PDF</a>
</div>

</div>
