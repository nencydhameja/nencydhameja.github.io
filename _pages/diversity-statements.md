---
layout: single
title: "Diversity Statements in Faculty Hiring"
permalink: /diversity-statement/
author_profile: false
classes: wide
---

This project studies how requiring diversity statements affects faculty hiring
in economics and political science (2014–2024).

---

<style>
.embed-container{
  width: 100%;
  max-width: 1300px;
  margin: 0 auto;
  position: relative;
  border-radius: 12px;
  overflow: hidden;
}
.embed-container iframe{
  position: absolute;
  top: 0;
  left: 0;
  border: 0;
  transform-origin: 0 0;
}

/* Force wider content area on wide pages */
.layout--single.wide .page__inner-wrap,
.layout--splash .page__inner-wrap {
  max-width: 100% !important;
  padding: 0 20px !important;
}
</style>

<script>
function scaleAllEmbeds() {
  document.querySelectorAll('.embed-container').forEach(function(wrap) {
    var iframe = wrap.querySelector('iframe');
    if (!iframe) return;
    var nativeW = parseInt(iframe.dataset.width) || 1300;
    var nativeH = parseInt(iframe.dataset.height) || 500;
    var s = wrap.offsetWidth / nativeW;
    iframe.style.width = nativeW + 'px';
    iframe.style.height = nativeH + 'px';
    iframe.style.transform = 'scale(' + s + ')';
    wrap.style.height = (nativeH * s) + 'px';
  });
}
window.addEventListener('load', scaleAllEmbeds);
window.addEventListener('resize', scaleAllEmbeds);
</script>

<div class="embed-container">
  <iframe
    src="/assets/projects/diversity/treatment_trend.html"
    title="Treatment Trend"
    data-width="1300"
    data-height="650"
    loading="lazy"
    scrolling="no"
    allowfullscreen>
  </iframe>
</div>

<div class="embed-container" style="margin-top: 24px;">
  <iframe
    src="/assets/projects/diversity/div_state_map.html"
    title="Interactive Map"
    data-width="1300"
    data-height="500"
    loading="lazy"
    scrolling="no"
    allowfullscreen>
  </iframe>
</div>

<p style="text-align: right; margin-top: 4px;">
  <a href="/assets/projects/diversity/div_state_map.html" target="_blank" style="font-size: 13px; color: #636efa;">View full interactive map &rarr;</a>
</p>
