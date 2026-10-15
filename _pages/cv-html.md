---
layout: archive
title: ""
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
    /* border: 0.5px solid rgba(26, 13, 171, 0.25); */
    border: 0.5px solid rgba(103, 36, 20, 0.2);
    padding: 1.5rem 2rem;
    border-radius: 2px;
    background:#fff
    
  }
  /* .cv-wrap a { color: #1a0dab; text-decoration: none; } */
  .cv-wrap a { color: #672414; text-decoration: none;}
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
  .cv-name {
  text-align: center;
  font-size: 18pt;
  font-weight: 600;
  font-variant: small-caps;
  letter-spacing: 0.08em;
  color: #111;
  margin-bottom: 0.5rem;
}
  .cv-years { display: grid; grid-template-columns: 3.2em 1fr; gap: 0.1rem 0.6rem; }
  .cv-years .cv-yr { font-weight: 600; }
  .cv-paper .cv-venue { display: block; }
  .cv-abstract { margin-top: 0.2rem; text-align: justify; }
  .cv-list { margin: 0.1rem 0 0.3rem 0; padding-left: 1.2em; }
  .cv-list li { margin-bottom: 0.15rem; }
  @media (max-width: 600px) {
    .cv-header-info { flex-direction: column; }
    .cv-address-right { text-align: left; }
    .cv-refs { grid-template-columns: 1fr; }
  }
</style>

<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<div class="cv-download" style="margin-bottom: 0.75rem; text-align: right;">
  <a href="/files/Nency_Dhameja_CV.pdf" class="btn btn--primary" target="_blank">Download CV as PDF</a>
</div>
<div class="cv-wrap">
<div class="cv-name">Nency Dhameja</div>

<div class="cv-updated">Last Updated: October 2026</div>

<div class="cv-header-info">
  <div>Department of Economics<br>Binghamton University<br>4400 Vestal Parkway East<br>Binghamton, NY 13902</div>
  <div class="cv-address-right">
    <span class="cv-email"><a href="mailto:ndhamej1@binghamton.edu">ndhamej1@binghamton.edu</a></span><br>
    <a href="https://nencydhameja.com">https://nencydhameja.com/</a>
  </div>
</div>

<section class="cv-section">
  <h2>Fields</h2>
  <div><strong>Primary:</strong> Urban and Regional Economics; Applied Microeconomics</div>
  <div><strong>Secondary:</strong> Applied Econometrics; Labor Economics; Computational Economics</div>
</section>

<section class="cv-section">
  <h2>Education</h2>
  <div class="cv-entry">
    <div class="cv-row"><span class="cv-left"><strong>Binghamton University, USA</strong></span><span class="cv-right">Aug 2021 – present</span></div>
    <div>Ph.D. in Economics (Expected May 2027)</div>
    <div>Committee: David Slichter (chair), Andreas Pape, Solomon W. Polachek, and Ivan Korolev</div>
  </div>
  <div class="cv-entry">
    <div class="cv-row"><span class="cv-left"><strong>SP Jain School of Management, Singapore</strong></span><span class="cv-right">Sep 2018 – Jul 2020</span></div>
    <div>Executive Master of Business Administration (EMBA) in Finance</div>
    <div>Thesis: Behavioral factors in stock markets</div>
  </div>
  <div class="cv-entry">
    <div class="cv-row"><span class="cv-left"><strong>Mahatma Gandhi Mission&rsquo;s College of Engineering &amp; Technology, India</strong></span><span class="cv-right">Oct 2001 – Jun 2005</span></div>
    <div>Bachelor of Technology in Electronics &amp; Telecommunications</div>
  </div>
</section>

<section class="cv-section">
  <h2>Research</h2>
  <div class="cv-sub">Job Market Paper</div>
  <div class="cv-paper">
    <a href="/files/Dhameja_Crime_House_Prices.pdf" target="_blank"><strong>When Does Crime Enter House Prices? Evidence from Chicago</strong></a>
    <div class="cv-abstract">I estimate how crime affects housing prices in Chicago. Although homebuyers presumably care about crime, most offenses have a near-zero effect on sale prices and asking rents. I argue that this is consistent with limited information: crime only changes buyers&rsquo; valuations if they learn of an incident and revise their expectations about future exposure. First, price effects are hyperlocal even though the predictive value of crimes is not. Second, price effects strengthen with agents&rsquo; local experience. Third, even within an offense, the effect depends on where at the property the incident occurred. These patterns are consistent with buyers responding to incidents they learn about rather than to the future crime those incidents predict.</div>
  </div>

  <div class="cv-sub">Publications</div>
  <div class="cv-paper">
    <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6752734"><strong>Causal Forests versus Penalized Splines for Heterogeneous Treatment Effects</strong></a> <em>(with Ivan Korolev and Abiodun Musbaudeen)</em>
    <span class="cv-venue"><em>Economics Letters</em>, 268 (2026), 113205.</span>
  </div>

  <div class="cv-sub">Consortium-Authored Publications</div>
  <div class="cv-paper">
    <a href="https://www.pnas.org/doi/10.1073/pnas.2524747123"><strong>AI-assisted teams outperform AI-led teams but not human-only teams in assessing research reproducibility in quantitative social science</strong></a> <em>(Brodeur et al.)</em>
    <span class="cv-venue"><em>Proceedings of the National Academy of Sciences</em>, 123(22) (2026), e2524747123.</span>
  </div>

  <div class="cv-sub">Working Papers</div>
  <div class="cv-paper">
    <strong>The Effects of Diversity Statements in Faculty Hiring</strong> <em>(with David Slichter)</em>
  </div>
  <div class="cv-paper">
    <strong>Cashing the Credit: Anomalous Billing and Firm Dynamics in Italy&rsquo;s Superbonus 110%</strong> <em>(with Marcello Graziano, Maurizio Fiaschetti, and Cristina Connolly)</em>
  </div>
  <div class="cv-paper">
    <a href="https://chriszosh1.github.io/files/Agent-BasedEconometrics_MC_Zosh_et_al.pdf"><strong>Monte-Carlo Tests for Identification and Validation of Stochastic Agent-Based Models</strong></a> <em>(with Christopher Zosh, Yixin Ren, Andreas Pape)</em>
    <span class="cv-venue">Revise &amp; Resubmit, <em>Journal of Artificial Societies and Social Simulation</em> (JASSS)</span>
  </div>

  <div class="cv-sub">Work in Progress</div>
  <div class="cv-paper">
    <strong>Social Context in the Schelling Model using LLMs</strong> <em>(with Andreas Pape, Srikanth Iyer, Yixin Ren, Christopher Zosh, Mohammed Mahinur Alam, Carl Lipo)</em>
  </div>
  <div class="cv-paper">
    <strong>Food Swamps, Obesity, and Metabolic Risks</strong>
  </div>
</section>

<section class="cv-section">
  <h2>Grants and Awards</h2>
  <div>Graduate Student Research Fund, Binghamton University (2026), for MLS transaction data</div>
  <div>Dean&rsquo;s List (Term II, III), SP Jain School of Management, 2019–2020</div>
</section>

<section class="cv-section">
  <h2>Research Affiliations</h2>
  <div><a href="https://www.i4replication.org/about">Fellow, Institute for Replication</a>, since 2026</div>
</section>

<section class="cv-section">
  <h2>Conference Presentations</h2>
  <div class="cv-years">
    <span class="cv-yr">2027</span><span>American Economic Association (AEA), Jan (Scheduled)</span>
    <span class="cv-yr">2026</span><span>Southern Economic Association (SEA), Nov (Scheduled)<br>Western Economic Association International (WEAI), Jul<br>Society for the Advancement of Behavioral Economics (SABE), Jun<br>American Society of Health Economists (ASHEcon), Jun<br>Midwest Economics Association (MEA), Mar<br>American Economic Association (AEA), Jan</span>
    <span class="cv-yr">2025</span><span>Southern Economic Association (SEA), Nov<br>Western Economic Association International (WEAI), Jun<br>Finger Lakes (FLX) Economics of Education Conference, Jun<br>Eastern Economic Association (EEA), Feb</span>
    <span class="cv-yr">2024</span><span>Eastern Economic Association (EEA), Feb</span>
  </div>
</section>

<section class="cv-section">
  <h2>Online Presentations</h2>
  <div class="cv-years">
    <span class="cv-yr">2026</span><span>Canadian Economics Association (CEA), May</span>
    <span class="cv-yr">2025</span><span>American Political Science Association (APSA), Feb</span>
  </div>
</section>

<section class="cv-section">
  <h2>Poster Presentations</h2>
  <div class="cv-years">
    <span class="cv-yr">2026</span><span>Society for Causal Inference (SCI), May</span>
    <span class="cv-yr">2025</span><span>Association for Public Policy Analysis &amp; Management (APPAM), Nov</span>
  </div>
</section>

<section class="cv-section">
  <h2>Teaching</h2>
  <div class="cv-row"><span class="cv-left"><strong>Binghamton University, NY</strong></span><span class="cv-right">2022 – present</span></div>
  <div class="cv-sub">Instructor</div>
  <div>Economics of Poverty and Discrimination (ECON 144), Winter 2026. Sole instructor</div>
  <div class="cv-sub">Teaching Assistant</div>
  <div class="cv-years">
    <span class="cv-yr">2026</span><span>Macroeconomic Theory (ECON 362, Fall, current)<br>Introduction to Econometrics (ECON 466, Fall, current)<br>Economics of Education (ECON 448, Spring)</span>
    <span class="cv-yr">2025</span><span>Behavioral Economics (ECON 483C, Fall)<br>Agent-Based Modeling with Python (ECON 570/670, Spring)</span>
    <span class="cv-yr">2024</span><span>Forecasting (ECON 476, Fall)<br>Introduction to Econometrics (ECON 466, Fall)<br>Econometrics (ECON 616, Spring)</span>
    <span class="cv-yr">2023</span><span>Economic Development of Latin America (ECON 483, Fall)<br>U.S. Financial Systems: Markets and Institutions (ECON 350, Spring)</span>
    <span class="cv-yr">2022</span><span>Economics of Corporations (ECON 454, Fall)</span>
  </div>
  <div class="cv-sub">Teaching Simulations</div>
  <div><a href="/econlab/">Open-access interactive simulations for economics and statistics</a></div>
</section>

<section class="cv-section">
  <h2>Service</h2>
  <div>Session Discussant, Western Economic Association International (2026)</div>
  <div>Conference Volunteer, Society for Causal Inference Annual Conference (2026)</div>
  <div>Session Discussant, Midwest Economics Association Annual Meeting (2026)</div>
  <div>Session Chair and Discussant, American Political Science Association (2025)</div>
  <div>Session Discussant, Eastern Economic Association Annual Conference (2024)</div>
</section>

<section class="cv-section">
  <h2>Additional Training &amp; Workshops</h2>
  <div class="cv-sub">Supplementary Methods Training</div>
  <ul class="cv-list">
    <li>Advanced Confounding Adjustment, Harvard T.H. Chan School of Public Health, 2026</li>
    <li>Causal Inference Workshop (Advanced), Northwestern University, 2025</li>
    <li>Causal Inference Workshop (Main), Northwestern University, 2025</li>
  </ul>
  <div class="cv-sub">Pedagogical Workshops/Conferences</div>
  <ul class="cv-list">
    <li>Conference on Teaching and Research in Economic Education (CTREE), AEA, 2026</li>
    <li>TeachECONference (CTaLE), 2026</li>
  </ul>
</section>

<section class="cv-section">
  <h2>Professional Experience</h2>
  <div class="cv-entry">
    <div class="cv-row"><span class="cv-left"><strong>Data Analyst</strong>, Graduate Admissions Office, Binghamton University</span><span class="cv-right">Aug 2021 – Aug 2022</span></div>
  </div>
  <div class="cv-entry">
    <div class="cv-row"><span class="cv-left"><strong>Industry</strong>, India &amp; Singapore</span><span class="cv-right">Jun 2005 – Aug 2021</span></div>
    <div>Sixteen years in software engineering, business analysis, and project management at Accenture, Grab, Jones Lang LaSalle, Agilent Technologies, and CSC (now DXC Technology). JLL Pinnacle Award, 2017; Agilent Technologies Appreciation Award for Innovation, 2008, and Outstanding Individual and Team Performance Awards, 2009–2011.</div>
  </div>
</section>

<section class="cv-section">
  <h2>Computational Skills</h2>
  <div><strong>Methods:</strong> panel methods; causal inference; spatial data construction; agent-based modeling (including LLM agents); machine learning (causal forests, gradient boosting)</div>
  <div><strong>Spatial data analysis:</strong> large-scale geocoding and spatial matching; spatial econometrics</div>
  <div><strong>Software:</strong> Stata, R, Python, SQL, Git, QGIS</div>
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
      <a href="https://www.binghamton.edu/apps/directory/person/profile/apape">Dr. Andreas Pape</a><br>
      Associate Professor of Economics<br>
      Binghamton University<br>
      <span class="cv-ref-email"><a href="mailto:apape@binghamton.edu">apape@binghamton.edu</a></span>
    </div>
    <div class="cv-ref">
      <a href="https://bingweb.binghamton.edu/~polachek/">Dr. Solomon W. Polachek</a><br>
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

</div>
<div class="cv-download" style="margin-top: 0.75rem; text-align: right;">
  <a href="/files/Nency_Dhameja_CV.pdf" class="btn btn--primary" target="_blank">Download CV as PDF</a>
</div>
