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
.map-embed{
  width: 100%;
  max-width: 1300px;
  margin: 0 auto;
  /* scale trick: container height = 500/1300 = 38.46% of width */
  padding-bottom: 38.46%;
  position: relative;
  border-radius: 12px;
  overflow: hidden;
}
.map-embed iframe{
  position: absolute;
  top: 0;
  left: 0;
  width: 1300px;
  height: 500px;
  border: 0;
  transform-origin: 0 0;
}

/* Force wider content area on wide pages */
.layout--single.wide .page__inner-wrap,
.layout--splash .page__inner-wrap {
  max-width: 1600px !important;
}
</style>

<script>
function scaleIframe() {
  var wrap = document.querySelector('.map-embed');
  var iframe = wrap && wrap.querySelector('iframe');
  if (!wrap || !iframe) return;
  var s = wrap.offsetWidth / 1300;
  iframe.style.transform = 'scale(' + s + ')';
  wrap.style.height = (500 * s) + 'px';
  wrap.style.paddingBottom = '0';
}
window.addEventListener('load', scaleIframe);
window.addEventListener('resize', scaleIframe);
</script>

<div class="map-embed">
  <iframe
    src="/assets/projects/diversity/div_state_map.html"
    title="Interactive Map"
    loading="lazy"
    scrolling="no"
    allowfullscreen>
  </iframe>
</div>
