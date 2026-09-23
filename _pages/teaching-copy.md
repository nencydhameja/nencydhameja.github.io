---
layout: archive
title: ""
permalink: /teaching-copy/
author_profile: true
---

<meta name="shinylive:serviceworker_dir" content="/">
<script src="/econlab/stats-course/site_libs/quarto-contrib/shinylive-0.9.1/shinylive/load-shinylive-sw.js" type="module"></script>
<script src="/econlab/stats-course/site_libs/quarto-contrib/shinylive-0.9.1/shinylive/run-python-blocks.js" type="module"></script>
<link href="/econlab/stats-course/site_libs/quarto-contrib/shinylive-0.9.1/shinylive/shinylive.css" rel="stylesheet">
<link href="/econlab/stats-course/site_libs/quarto-contrib/shinylive-quarto-css/shinylive-quarto.css" rel="stylesheet">

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

  /* NEW: two shinylive simulations side by side in one row */
  .sim-row {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));  /* minmax(0,…) stops the long <pre> code from blowing out the column width */
    gap: 1.2rem;
    align-items: start;
    margin: 1.3rem 0 1.1rem;
  }
  .sim-cell { min-width: 0; overflow: hidden; }
  /* render the app WIDE on the CONTAINER (so sliders + plots sit side by side, plots on the right),
     then zoom the whole thing down to fit the cell (zoom shrinks the box too, no whitespace) */
  .sim-clip { width: 900px; zoom: 0.44; }
  .sim-clip iframe { width: 100% !important; height: 470px !important; max-width: none !important; border: 0; }
  .sim-head {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 1rem;
    margin: 0 0 0.4rem;
  }
  /* Stack back to one per row on narrow screens */
  @media (max-width: 900px) {
    .sim-row { grid-template-columns: 1fr; }
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
  I build browser-based teaching simulations that let students experiment with the models directly.
  Explore them in my
  <a href="/econlab/" style="color:#185FA5;text-decoration:none;">EconLab</a>.
</p>

<div class="sim-row" markdown="0">

<div class="sim-cell">
<div class="sim-head"><span style="font-size:15px;font-weight:500;color:#1a1a18;">Central Limit Theorem <span style="color:#888780;font-weight:400;">Statistics</span></span><a href="/econlab/stats-course/simulations.html" target="_blank" rel="noopener" style="font-size:12px;color:#185FA5;text-decoration:none;white-space:nowrap;">Full notes &#8599;</a></div>
<div class="sim-clip"><pre class="shinylive-r" data-engine="r"><code>#| standalone: true
#| viewerHeight: 460

library(shiny)

# ---------------------------------------------------------------------------
# Helper: draw a single random sample from the chosen distribution
# ---------------------------------------------------------------------------
draw_sample &lt;- function(n, dist) {
  switch(dist,
    "Uniform(0, 1)"      = runif(n),
    "Exponential(1)"     = rexp(n, rate = 1),
    "Right-skewed"       = rchisq(n, df = 3),
    "Bimodal"            = {
      k &lt;- rbinom(n, 1, 0.5)
      k * rnorm(n, mean = -2, sd = 0.6) + (1 - k) * rnorm(n, mean = 2, sd = 0.6)
    },
    "Bernoulli(0.3)"     = rbinom(n, size = 1, prob = 0.3),
    runif(n)
  )
}

# Theoretical mean &amp; sd of each population distribution
pop_params &lt;- list(
  "Uniform(0, 1)"  = list(mu = 0.5, sigma = sqrt(1 / 12)),
  "Exponential(1)" = list(mu = 1,   sigma = 1),
  "Right-skewed"   = list(mu = 3,   sigma = sqrt(6)),
  "Bimodal"        = list(mu = 0,   sigma = sqrt(0.6^2 + 4)),
  "Bernoulli(0.3)" = list(mu = 0.3, sigma = sqrt(0.3 * 0.7))
)

# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------
ui &lt;- fluidPage(
  tags$head(tags$style(HTML("
    .stats-box {
      background: #eaf2f8; border-radius: 6px; padding: 14px;
      margin-top: 12px; font-size: 14px; line-height: 1.8;
    }
    .stats-box b { color: #2c3e50; }
  "))),

  sidebarLayout(
    sidebarPanel(
      width = 3,

      selectInput("dist", "Population distribution:",
                  choices = names(pop_params)),

      sliderInput("n", "Sample size (n):",
                  min = 1, max = 200, value = 5, step = 1),

      sliderInput("reps", "Number of samples:",
                  min = 100, max = 3000, value = 1000, step = 100),

      actionButton("resample", "Draw new samples",
                   class = "btn-primary", width = "100%"),

      uiOutput("stats_box")
    ),

    mainPanel(
      width = 9,
      fluidRow(
        column(6, plotOutput("parent_plot", height = "230px")),
        column(6, plotOutput("sampling_plot", height = "230px"))
      )
    )
  )
)

# ---------------------------------------------------------------------------
# Server
# ---------------------------------------------------------------------------
server &lt;- function(input, output, session) {

  sim &lt;- reactive({
    input$resample
    n    &lt;- input$n
    reps &lt;- input$reps
    dist &lt;- input$dist

    means &lt;- replicate(reps, mean(draw_sample(n, dist)))

    params &lt;- pop_params[[dist]]
    theo_mu &lt;- params$mu
    theo_se &lt;- params$sigma / sqrt(n)

    list(means = means, dist = dist, n = n, reps = reps,
         theo_mu = theo_mu, theo_se = theo_se)
  })

  output$parent_plot &lt;- renderPlot({
    dist &lt;- input$dist
    big  &lt;- draw_sample(10000, dist)

    par(mar = c(4.5, 4, 3, 1))
    hist(big, breaks = 60, probability = TRUE,
         col = "#d5e8d4", border = "#82b366",
         main = paste("True Population:", dist),
         xlab = "x", ylab = "Density")
  })

  output$sampling_plot &lt;- renderPlot({
    s &lt;- sim()

    par(mar = c(4.5, 4, 3, 1))
    hist(s$means, breaks = 40, probability = TRUE,
         col = "#dae8fc", border = "#6c8ebf",
         main = paste0("Sampling Distribution of the Mean (n = ", s$n, ")"),
         xlab = "Sample mean", ylab = "Density")

    x_seq &lt;- seq(min(s$means), max(s$means), length.out = 300)
    lines(x_seq, dnorm(x_seq, mean = s$theo_mu, sd = s$theo_se),
          col = "#e74c3c", lwd = 2.5)

    abline(v = s$theo_mu, lty = 2, lwd = 2, col = "#2c3e50")

    legend("topright",
           legend = c("Normal approximation", "Theoretical mean"),
           col    = c("#e74c3c", "#2c3e50"),
           lwd    = c(2.5, 2),
           lty    = c(1, 2),
           bty    = "n", cex = 0.9)
  })

  output$stats_box &lt;- renderUI({
    s &lt;- sim()
    tags$div(class = "stats-box",
      HTML(paste0(
        "&lt;b&gt;Theoretical mean:&lt;/b&gt; ",   round(s$theo_mu, 4), "&lt;br&gt;",
        "&lt;b&gt;Observed mean:&lt;/b&gt; ",      round(mean(s$means), 4), "&lt;br&gt;",
        "&lt;b&gt;Theoretical SE:&lt;/b&gt; ",     round(s$theo_se, 4), "&lt;br&gt;",
        "&lt;b&gt;Observed SD:&lt;/b&gt; ",        round(sd(s$means), 4)
      ))
    )
  })
}

shinyApp(ui, server)</code></pre></div>
</div>

<div class="sim-cell">
<div class="sim-head"><span style="font-size:15px;font-weight:500;color:#1a1a18;">Consumer Choice <span style="color:#888780;font-weight:400;">Intermediate Micro</span></span><a href="/econlab/intermediate-micro/choice.html" target="_blank" rel="noopener" style="font-size:12px;color:#185FA5;text-decoration:none;white-space:nowrap;">Full notes &#8599;</a></div>
<div class="sim-clip"><pre class="shinylive-r" data-engine="r"><code>#| standalone: true
#| viewerHeight: 460

library(shiny)

ui &lt;- fluidPage(
  titlePanel("Cobb-Douglas Consumer"),

  sidebarLayout(
    sidebarPanel(
      width = 4,
      sliderInput("a", "Cobb-Douglas exponent a:",
                  min = 0.5, max = 4, value = 1, step = 0.25),
      sliderInput("b", "Cobb-Douglas exponent b:",
                  min = 0.5, max = 4, value = 1, step = 0.25),
      sliderInput("m",  "Income (m):",            min =  20, max = 200, value = 100, step = 10),
      sliderInput("p1", "Price of good 1 (p₁):",  min =   1, max =  20, value =   5, step = 1),
      sliderInput("p2", "Price of good 2 (p₂):",  min =   1, max =  20, value =   5, step = 1),
      hr(),
      checkboxInput("show_other_ics",
                    "Show a ladder of indifference curves",
                    value = TRUE),
      htmlOutput("readout")
    ),
    mainPanel(
      width = 8,
      plotOutput("choice_plot", height = "300px")
    )
  )
)

server &lt;- function(input, output, session) {

  bundle &lt;- reactive({
    a &lt;- input$a; b &lt;- input$b
    m &lt;- input$m; p1 &lt;- input$p1; p2 &lt;- input$p2
    x1 &lt;- a * m / ((a + b) * p1)
    x2 &lt;- b * m / ((a + b) * p2)
    u_opt &lt;- x1^a * x2^b
    list(a = a, b = b, m = m, p1 = p1, p2 = p2,
         x1 = x1, x2 = x2, u_opt = u_opt)
  })

  output$choice_plot &lt;- renderPlot({
    s &lt;- bundle()
    x1_int &lt;- s$m / s$p1
    x2_int &lt;- s$m / s$p2

    xmax &lt;- max(40, x1_int) * 1.05
    ymax &lt;- max(40, x2_int) * 1.05

    par(mar = c(4.2, 4.5, 1, 1))
    plot(NA, xlim = c(0, xmax), ylim = c(0, ymax),
         xlab = expression(x[1]), ylab = expression(x[2]), main = "")

    # Indifference curves: x_1^a x_2^b = U =&gt; x_2 = (U / x_1^a)^(1/b)
    ic_x &lt;- seq(0.1, xmax * 1.5, length.out = 600)
    ic_y_opt &lt;- (s$u_opt / ic_x^s$a)^(1 / s$b)

    if (isTRUE(input$show_other_ics)) {
      for (frac in c(0.5, 0.75, 1.25)) {
        u &lt;- s$u_opt * frac
        y &lt;- (u / ic_x^s$a)^(1 / s$b)
        lines(ic_x, y, col = adjustcolor("#7f8c8d", 0.5), lwd = 1.2, lty = 3)
      }
    }

    lines(ic_x, ic_y_opt, col = "#27ae60", lwd = 2.4)

    polygon(c(0, x1_int, 0), c(0, 0, x2_int),
            col = adjustcolor("#3498db", 0.12), border = NA)
    segments(0, x2_int, x1_int, 0, col = "#185FA5", lwd = 3)

    points(s$x1, s$x2, pch = 19, col = "#c0392b", cex = 1.8)
    text(s$x1, s$x2, sprintf("  (%.1f, %.1f)", s$x1, s$x2),
         pos = 4, col = "#c0392b", cex = 1.0)

    legend("topright",
           legend = c("Budget line", "Indifference curve through optimum",
                      if (isTRUE(input$show_other_ics)) "Other indifference curves" else NULL,
                      "Optimal bundle (x₁*, x₂*)"),
           col    = c("#185FA5", "#27ae60",
                      if (isTRUE(input$show_other_ics)) "#7f8c8d" else NULL,
                      "#c0392b"),
           lwd    = c(3, 2.4, if (isTRUE(input$show_other_ics)) 1.2 else NULL, NA),
           lty    = c(1, 1, if (isTRUE(input$show_other_ics)) 3 else NULL, NA),
           pch    = c(NA, NA, if (isTRUE(input$show_other_ics)) NA else NULL, 19),
           bty = "n", cex = 0.9)
  })

  output$readout &lt;- renderUI({
    s &lt;- bundle()
    share1 &lt;- s$a / (s$a + s$b)
    share2 &lt;- s$b / (s$a + s$b)
    HTML(sprintf(paste(
      "&lt;div style='margin-top:10px;font-size:13px;line-height:1.7;'&gt;",
      "&lt;b&gt;Ordinary demand:&lt;/b&gt; x₁* = %.2f, x₂* = %.2f&lt;br&gt;",
      "&lt;b&gt;Spending on good 1:&lt;/b&gt; p₁·x₁* = %.1f (%.0f%% of income)&lt;br&gt;",
      "&lt;b&gt;Spending on good 2:&lt;/b&gt; p₂·x₂* = %.1f (%.0f%% of income)&lt;br&gt;",
      "&lt;b&gt;MRS at optimum:&lt;/b&gt; %.2f &amp;nbsp; &lt;b&gt;p₁/p₂:&lt;/b&gt; %.2f&lt;br&gt;",
      "&lt;b&gt;Utility achieved:&lt;/b&gt; %.2f",
      "&lt;/div&gt;"
    ),
    s$x1, s$x2,
    s$p1 * s$x1, 100 * share1,
    s$p2 * s$x2, 100 * share2,
    (s$a / s$b) * (s$x2 / s$x1),
    s$p1 / s$p2, s$u_opt))
  })
}

shinyApp(ui, server)</code></pre></div>
</div>



<div class="sim-cell">
<div class="sim-head"><span style="font-size:15px;font-weight:500;color:#1a1a18;">Regression Discontinuity <span style="color:#888780;font-weight:400;">Causal Inference</span></span><a href="/econlab/causal-inference/rdd.html" target="_blank" rel="noopener" style="font-size:12px;color:#185FA5;text-decoration:none;white-space:nowrap;">Full notes &#8599;</a></div>
<div class="sim-clip"><pre class="shinylive-r" data-engine="r"><code>#| standalone: true
#| viewerHeight: 460

library(shiny)

ui &lt;- fluidPage(
  tags$head(tags$style(HTML("
    .stats-box {
      background: #f0f4f8; border-radius: 6px; padding: 14px;
      margin-top: 12px; font-size: 14px; line-height: 1.9;
    }
    .stats-box b { color: #2c3e50; }
    .good { color: #27ae60; font-weight: bold; }
    .bad  { color: #e74c3c; font-weight: bold; }
  "))),

  sidebarLayout(
    sidebarPanel(
      width = 3,

      sliderInput("n", "Sample size:",
                  min = 200, max = 2000, value = 500, step = 100),

      sliderInput("tau", "True treatment effect:",
                  min = 0, max = 5, value = 2, step = 0.25),

      sliderInput("sigma", "Noise (SD):",
                  min = 0.5, max = 4, value = 1.5, step = 0.25),

      sliderInput("bw", "Bandwidth around cutoff:",
                  min = 0.05, max = 0.5, value = 0.2, step = 0.05),

      selectInput("curve", "True relationship:",
                  choices = c("Linear" = "linear",
                              "Quadratic" = "quad",
                              "Flat" = "flat")),

      actionButton("go", "New draw", class = "btn-primary", width = "100%"),

      uiOutput("results")
    ),

    mainPanel(
      width = 9,
      plotOutput("rdd_plot", height = "480px")
    )
  )
)

server &lt;- function(input, output, session) {

  dat &lt;- reactive({
    input$go
    n     &lt;- input$n
    tau   &lt;- input$tau
    sigma &lt;- input$sigma
    bw    &lt;- input$bw
    curve &lt;- input$curve

    # Running variable: uniform on [0, 1], cutoff at 0.5
    x &lt;- runif(n)
    cutoff &lt;- 0.5
    treat &lt;- as.numeric(x &gt;= cutoff)

    # Potential outcome (smooth function of x)
    if (curve == "linear") {
      mu &lt;- 2 + 1.5 * x
    } else if (curve == "quad") {
      mu &lt;- 2 + 3 * (x - 0.5)^2
    } else {
      mu &lt;- rep(3, n)
    }

    y &lt;- mu + tau * treat + rnorm(n, sd = sigma)

    # Local linear regression within bandwidth
    in_bw &lt;- abs(x - cutoff) &lt;= bw
    x_bw &lt;- x[in_bw]
    y_bw &lt;- y[in_bw]
    t_bw &lt;- treat[in_bw]

    # Separate regressions left and right
    left  &lt;- x_bw &lt; cutoff
    right &lt;- x_bw &gt;= cutoff

    if (sum(left) &gt; 2 &amp;&amp; sum(right) &gt; 2) {
      fit_l &lt;- lm(y_bw[left] ~ x_bw[left])
      fit_r &lt;- lm(y_bw[right] ~ x_bw[right])

      # Predicted values at cutoff
      pred_l &lt;- coef(fit_l)[1] + coef(fit_l)[2] * cutoff
      pred_r &lt;- coef(fit_r)[1] + coef(fit_r)[2] * cutoff

      rdd_est &lt;- pred_r - pred_l

      # Fitted lines for plotting
      xseq_l &lt;- seq(cutoff - bw, cutoff, length.out = 100)
      xseq_r &lt;- seq(cutoff, cutoff + bw, length.out = 100)
      yhat_l &lt;- coef(fit_l)[1] + coef(fit_l)[2] * xseq_l
      yhat_r &lt;- coef(fit_r)[1] + coef(fit_r)[2] * xseq_r
    } else {
      rdd_est &lt;- NA
      xseq_l &lt;- xseq_r &lt;- yhat_l &lt;- yhat_r &lt;- NULL
      pred_l &lt;- pred_r &lt;- NA
    }

    list(x = x, y = y, treat = treat, cutoff = cutoff,
         bw = bw, in_bw = in_bw, rdd_est = rdd_est,
         tau = tau, sigma = sigma,
         xseq_l = xseq_l, xseq_r = xseq_r,
         yhat_l = yhat_l, yhat_r = yhat_r,
         pred_l = pred_l, pred_r = pred_r)
  })

  output$rdd_plot &lt;- renderPlot({
    d &lt;- dat()
    par(mar = c(4.5, 4.5, 3, 1))

    # Color by treatment
    cols &lt;- ifelse(d$treat == 1, adjustcolor("#3498db", 0.25),
                   adjustcolor("#e74c3c", 0.25))

    # Dim points outside bandwidth
    cols[!d$in_bw] &lt;- adjustcolor("gray70", 0.15)

    plot(d$x, d$y, pch = 16, cex = 0.5, col = cols,
         xlab = "Running variable (X)", ylab = "Outcome (Y)",
         main = "Regression Discontinuity Design")

    # Cutoff line
    abline(v = d$cutoff, lty = 2, col = "gray40", lwd = 1.5)

    # Bandwidth shading
    rect(d$cutoff - d$bw, par("usr")[3],
         d$cutoff + d$bw, par("usr")[4],
         col = adjustcolor("#f39c12", 0.08), border = NA)

    # Local linear fits
    if (!is.null(d$xseq_l)) {
      lines(d$xseq_l, d$yhat_l, col = "#e74c3c", lwd = 3)
      lines(d$xseq_r, d$yhat_r, col = "#3498db", lwd = 3)

      # Jump arrow
      arrows(d$cutoff + 0.01, d$pred_l, d$cutoff + 0.01, d$pred_r,
             code = 3, lwd = 2.5, col = "#27ae60", length = 0.1)

      text(d$cutoff + 0.03,
           (d$pred_l + d$pred_r) / 2,
           paste0("Jump = ", round(d$rdd_est, 2)),
           col = "#27ae60", cex = 0.95, adj = 0, font = 2)
    }

    text(d$cutoff, par("usr")[4] * 0.98, "Cutoff",
         col = "gray40", cex = 0.8, pos = 4)

    legend("topleft", bty = "n", cex = 0.85,
           legend = c("Control (below cutoff)", "Treated (above cutoff)",
                      "Estimation window"),
           pch = c(16, 16, 15),
           col = c("#e74c3c", "#3498db", adjustcolor("#f39c12", 0.3)))
  })

  output$results &lt;- renderUI({
    d &lt;- dat()
    if (is.na(d$rdd_est)) {
      return(tags$div(class = "stats-box",
        HTML("&lt;b&gt;Not enough observations in bandwidth.&lt;/b&gt; Widen it.")))
    }

    bias &lt;- d$rdd_est - d$tau
    tags$div(class = "stats-box",
      HTML(paste0(
        "&lt;b&gt;True effect:&lt;/b&gt; ", d$tau, "&lt;br&gt;",
        "&lt;b&gt;RDD estimate:&lt;/b&gt; ", round(d$rdd_est, 3), "&lt;br&gt;",
        "&lt;b&gt;Bias:&lt;/b&gt; &lt;span class='", ifelse(abs(bias) &lt; 0.3, "good", "bad"), "'&gt;",
        round(bias, 3), "&lt;/span&gt;&lt;br&gt;",
        "&lt;hr style='margin:6px 0'&gt;",
        "&lt;small&gt;Bandwidth: &amp;plusmn;", d$bw, " around cutoff&lt;/small&gt;"
      ))
    )
  })
}

shinyApp(ui, server)</code></pre></div>
</div>

<div class="sim-cell">
<div class="sim-head"><span style="font-size:15px;font-weight:500;color:#1a1a18;">Monocentric City <span style="color:#888780;font-weight:400;">Urban Economics</span></span><a href="/econlab/urban-econ/monocentric-city.html" target="_blank" rel="noopener" style="font-size:12px;color:#185FA5;text-decoration:none;white-space:nowrap;">Full notes &#8599;</a></div>
<div class="sim-clip"><pre class="shinylive-r" data-engine="r"><code>#| standalone: true
#| viewerHeight: 460

library(shiny)

ui &lt;- fluidPage(
  tags$head(tags$style(HTML("
    .stats-box {
      background: #f0f4f8; border-radius: 6px; padding: 14px;
      margin-top: 12px; font-size: 14px; line-height: 1.9;
    }
    .stats-box b { color: #2c3e50; }
    .good { color: #27ae60; font-weight: bold; }
    .bad  { color: #e74c3c; font-weight: bold; }
    .info-box {
      background: #eaf2f8; border-radius: 6px; padding: 14px;
      margin-top: 12px; font-size: 13px; line-height: 1.8;
    }
    .info-box b { color: #2c3e50; }
  "))),

  sidebarLayout(
    sidebarPanel(
      width = 3,

      sliderInput("transport", "Transport cost ($/mile):",
                  min = 50, max = 500, value = 200, step = 25),

      sliderInput("income", "Wage/income ($1000s):",
                  min = 20, max = 120, value = 60, step = 5),

      sliderInput("ag_rent", "Agricultural rent ($/acre):",
                  min = 50, max = 500, value = 100, step = 25),

      sliderInput("pop", "Population (thousands):",
                  min = 50, max = 1000, value = 300, step = 25),

      actionButton("go", "Update city", class = "btn-primary", width = "100%"),

      uiOutput("info")
    ),

    mainPanel(
      width = 9,
      fluidRow(
        column(4, plotOutput("rent_plot", height = "400px")),
        column(4, plotOutput("density_plot", height = "400px")),
        column(4, plotOutput("city_plot", height = "400px"))
      )
    )
  )
)

server &lt;- function(input, output, session) {

  city &lt;- reactive({
    input$go
    t_cost  &lt;- input$transport
    income  &lt;- input$income * 1000
    r_ag    &lt;- input$ag_rent
    pop     &lt;- input$pop * 1000

    # CBD rent determined by population pressure and income
    # Higher pop and income push CBD rent up
    r_cbd &lt;- r_ag + sqrt(pop * income * t_cost) * 0.01

    # City radius: where rent = agricultural rent
    d_star &lt;- (r_cbd - r_ag) / t_cost

    # Ensure reasonable bounds
    d_star &lt;- max(d_star, 0.1)

    # Distance vector
    d &lt;- seq(0, d_star * 1.3, length.out = 200)

    # Rent gradient
    rent &lt;- pmax(r_cbd - t_cost * d, r_ag)

    # Population density declines with distance (proportional to rent)
    density_cbd &lt;- pop / (pi * d_star^2) * 2
    density &lt;- density_cbd * pmax(1 - d / d_star, 0)

    # Total area
    area &lt;- pi * d_star^2

    # Average rent (within city)
    avg_rent &lt;- (r_cbd + r_ag) / 2

    list(d = d, rent = rent, density = density,
         d_star = d_star, r_cbd = r_cbd, r_ag = r_ag,
         area = area, avg_rent = avg_rent, t_cost = t_cost,
         density_cbd = density_cbd)
  })

  output$rent_plot &lt;- renderPlot({
    c &lt;- city()
    par(mar = c(4.5, 4.5, 3, 1))
    plot(c$d, c$rent, type = "l", lwd = 3, col = "#2c3e50",
         xlab = "Distance from CBD (miles)",
         ylab = "Rent ($/acre)",
         main = "Rent Gradient")
    abline(h = c$r_ag, lty = 2, col = "#e74c3c", lwd = 2)
    abline(v = c$d_star, lty = 3, col = "#7f8c8d", lwd = 1.5)
    text(c$d_star, c$r_cbd * 0.9,
         paste0("City edge\nd* = ", round(c$d_star, 1), " mi"),
         pos = 4, cex = 0.8, col = "#7f8c8d")
    legend("topright", bty = "n", cex = 0.85,
           legend = c("Rent gradient", "Agricultural rent"),
           col = c("#2c3e50", "#e74c3c"), lwd = c(3, 2), lty = c(1, 2))
  })

  output$density_plot &lt;- renderPlot({
    c &lt;- city()
    par(mar = c(4.5, 4.5, 3, 1))
    d_city &lt;- c$d[c$d &lt;= c$d_star]
    dens_city &lt;- c$density[seq_along(d_city)]
    plot(d_city, dens_city, type = "l", lwd = 3, col = "#3498db",
         xlab = "Distance from CBD (miles)",
         ylab = "Population density (per sq mi)",
         main = "Population Density")
    polygon(c(d_city, rev(d_city)),
            c(dens_city, rep(0, length(d_city))),
            col = adjustcolor("#3498db", 0.2), border = NA)
    abline(v = c$d_star, lty = 3, col = "#7f8c8d", lwd = 1.5)
  })

  output$city_plot &lt;- renderPlot({
    c &lt;- city()
    par(mar = c(1, 1, 3, 1))
    theta &lt;- seq(0, 2 * pi, length.out = 100)
    r_max &lt;- c$d_star * 1.3

    plot(NULL, xlim = c(-r_max, r_max), ylim = c(-r_max, r_max),
         xlab = "", ylab = "", main = "City Footprint",
         asp = 1, axes = FALSE)

    # Fill city area
    polygon(c$d_star * cos(theta), c$d_star * sin(theta),
            col = adjustcolor("#e74c3c", 0.15), border = "#e74c3c", lwd = 2)

    # CBD point
    points(0, 0, pch = 19, cex = 2, col = "#2c3e50")
    text(0, 0, "CBD", pos = 3, cex = 0.9, col = "#2c3e50", font = 2)

    # Radius line
    segments(0, 0, c$d_star, 0, lwd = 2, col = "#e74c3c", lty = 2)
    text(c$d_star / 2, -c$d_star * 0.12,
         paste0(round(c$d_star, 1), " mi"), cex = 0.85, col = "#e74c3c")
  })

  output$info &lt;- renderUI({
    c &lt;- city()
    tags$div(class = "info-box",
      HTML(paste0(
        "&lt;b&gt;City radius:&lt;/b&gt; ", round(c$d_star, 1), " miles&lt;br&gt;",
        "&lt;b&gt;CBD rent:&lt;/b&gt; $", format(round(c$r_cbd), big.mark = ","), "/acre&lt;br&gt;",
        "&lt;b&gt;Avg rent:&lt;/b&gt; $", format(round(c$avg_rent), big.mark = ","), "/acre&lt;br&gt;",
        "&lt;b&gt;City area:&lt;/b&gt; ", format(round(c$area, 1), big.mark = ","), " sq mi"
      ))
    )
  })
}

shinyApp(ui, server)</code></pre></div>
</div>

</div>
