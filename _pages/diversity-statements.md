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
.plotly-container {
  width: 100%;
  margin: 0 auto;
}

/* Force wider content area on wide pages */
.layout--single.wide .page__inner-wrap,
.layout--splash .page__inner-wrap {
  max-width: 100% !important;
  padding: 0 20px !important;
}
</style>

<script src="https://cdn.plot.ly/plotly-2.35.2.min.js" charset="utf-8"></script>

<div class="plotly-container">
  <div id="treatment-trend" style="width:100%;"></div>
</div>

<div class="plotly-container" style="margin-top: 24px;">
  <div id="state-map" style="width:100%;"></div>
</div>

<p style="text-align: right; margin-top: 4px;">
  <a href="/assets/projects/diversity/div_state_map.html" target="_blank" style="font-size: 13px; color: #636efa;">View full interactive map &rarr;</a>
</p>

<script>
// Treatment Trend Chart
Plotly.newPlot("treatment-trend",
  [{"customdata":[[52,689],[73,666],[71,600],[103,576],[128,566],[150,559],[120,298],[223,515],[257,576],[190,462],[119,365]],"hovertemplate":"<b>Economics</b><br>Share: %{y:.1f}%<br>Treated: %{customdata[0]}<br>Total: %{customdata[1]}<extra></extra>","line":{"color":"#2563eb","width":3},"marker":{"size":10,"symbol":"circle"},"mode":"lines+markers","name":"Economics","x":["'14-'15","'15-'16","'16-'17","'17-'18","'18-'19","'19-'20","'20-'21","'21-'22","'22-'23","'23-'24","'24-'25"],"y":[7.5,11.0,11.8,17.9,22.6,26.8,40.3,43.3,44.6,41.1,32.6],"type":"scatter"},
   {"customdata":[[14,87],[105,1012],[246,1097],[222,1118],[298,1105],[284,809],[306,623],[569,1044],[587,1075],[258,485],[106,347]],"hovertemplate":"<b>Political Science</b><br>Share: %{y:.1f}%<br>Treated: %{customdata[0]}<br>Total: %{customdata[1]}<extra></extra>","line":{"color":"#dc2626","width":3},"marker":{"size":10,"symbol":"square"},"mode":"lines+markers","name":"Political Science","x":["'14-'15","'15-'16","'16-'17","'17-'18","'18-'19","'19-'20","'20-'21","'21-'22","'22-'23","'23-'24","'24-'25"],"y":[16.1,10.4,22.4,19.9,27.0,35.1,49.1,54.5,54.6,53.2,30.5],"type":"scatter"}],
  {"title":{"font":{"size":16},"text":"Share of Faculty Job Postings Requiring a Diversity Statement","x":0.5},"xaxis":{"title":{"text":"Academic Year"},"showgrid":false,"tickangle":0},"yaxis":{"title":{"text":"Share of Postings (%)"},"range":[0,65],"gridcolor":"rgba(200,200,200,0.3)"},"legend":{"x":0.02,"y":0.98,"bgcolor":"rgba(255,255,255,0.9)","bordercolor":"#ccc","borderwidth":1},"margin":{"l":60,"r":40,"t":80,"b":130},"hovermode":"x unified","plot_bgcolor":"white","paper_bgcolor":"white","annotations":[{"font":{"color":"gray","size":10},"showarrow":false,"text":"Dhameja, N. & Slichter, D. (2026). The Effect of Diversity Statements on Faculty Hiring.<br>Data: JOE (Economics) & APSA eJobs (Political Science).","x":0.5,"xanchor":"center","xref":"paper","y":-0.2,"yref":"paper"}]},
  {"responsive": true}
);

// State Map Chart
Plotly.newPlot("state-map",
  [{"colorscale":[[0.0,"rgb(247,251,255)"],[0.125,"rgb(222,235,247)"],[0.25,"rgb(198,219,239)"],[0.375,"rgb(158,202,225)"],[0.5,"rgb(107,174,214)"],[0.625,"rgb(66,146,198)"],[0.75,"rgb(33,113,181)"],[0.875,"rgb(8,81,156)"],[1.0,"rgb(8,48,107)"]],"customdata":[[1,7],[7,72],[0,27],[9,52],[249,551],[19,56],[38,127],[9,96],[13,24],[16,140],[34,176],[5,15],[36,66],[0,15],[92,314],[35,169],[3,28],[5,50],[4,56],[84,385],[23,109],[14,27],[57,146],[15,70],[20,79],[5,33],[1,10],[25,174],[0,9],[3,32],[15,32],[6,96],[4,14],[4,21],[100,404],[42,147],[2,28],[21,35],[83,284],[26,53],[2,41],[3,6],[9,90],[50,266],[8,47],[48,153],[9,21],[25,50],[17,80],[0,12],[2,8]],"hovertemplate":"%{location}<br>Prop: %{z:.3f}<br>Treated: %{customdata[0]:.0f}<br>Total: %{customdata[1]:.0f}<extra></extra>","locationmode":"USA-states","locations":["AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","HI","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VA","VT","WA","WI","WV","WY"],"showscale":false,"z":[0.1429,0.0972,0.0,0.1731,0.4519,0.3393,0.2992,0.0938,0.5417,0.1143,0.1932,0.3333,0.5455,0.0,0.2930,0.2071,0.1071,0.1,0.0714,0.2182,0.2110,0.5185,0.3904,0.2143,0.2532,0.1515,0.1,0.1437,0.0,0.0938,0.4688,0.0625,0.2857,0.1905,0.2475,0.2857,0.0714,0.6,0.2923,0.4906,0.0488,0.5,0.1,0.1880,0.1702,0.3137,0.4286,0.5,0.2125,0.0,0.25],"zmax":0.6909090909090909,"zmin":0,"type":"choropleth","geo":"geo"},
   {"colorbar":{"len":0.8,"thickness":15,"title":{"text":"Prop Treated"},"x":0.96},"colorscale":[[0.0,"rgb(247,251,255)"],[0.125,"rgb(222,235,247)"],[0.25,"rgb(198,219,239)"],[0.375,"rgb(158,202,225)"],[0.5,"rgb(107,174,214)"],[0.625,"rgb(66,146,198)"],[0.75,"rgb(33,113,181)"],[0.875,"rgb(8,81,156)"],[1.0,"rgb(8,48,107)"]],"customdata":[[9,79],[12,49],[0,4],[432,709],[69,110],[50,135],[69,235],[2,23],[70,243],[49,192],[0,2],[25,55],[4,20],[103,251],[54,200],[11,26],[25,73],[13,53],[179,348],[12,79],[38,55],[56,126],[21,44],[14,67],[5,34],[1,3],[66,222],[1,7],[6,9],[21,59],[25,215],[4,12],[10,19],[160,493],[84,252],[5,29],[25,43],[116,349],[34,66],[24,92],[5,11],[63,139],[89,370],[3,55],[131,303],[9,15],[33,69],[18,37],[1,8],[1,11]],"hovertemplate":"%{location}<br>Prop: %{z:.3f}<br>Treated: %{customdata[0]:.0f}<br>Total: %{customdata[1]:.0f}<extra></extra>","locationmode":"USA-states","locations":["AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","HI","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VA","VT","WA","WI","WV","WY"],"z":[0.1139,0.2449,0.0,0.6093,0.6273,0.3704,0.2936,0.0870,0.2881,0.2552,0.0,0.4545,0.2,0.4104,0.2700,0.4231,0.3425,0.2453,0.5144,0.1519,0.6909,0.4444,0.4773,0.2090,0.1471,0.3333,0.2973,0.1429,0.6667,0.3559,0.1163,0.3333,0.5263,0.3286,0.3333,0.1724,0.5814,0.3324,0.5152,0.2609,0.4545,0.4532,0.2405,0.0545,0.4323,0.6,0.4783,0.4865,0.125,0.0909],"zmax":0.6909090909090909,"zmin":0,"type":"choropleth","geo":"geo2"}],
  {"geo":{"domain":{"x":[0.0,0.45],"y":[0.05,1.0]},"scope":"usa"},"geo2":{"domain":{"x":[0.45,0.9],"y":[0.05,1.0]},"scope":"usa"},"title":{"text":"Share of Postings Requiring Diversity Statement by State (All Years)","x":0.5},"margin":{"l":20,"r":20,"t":80,"b":60},"height":500,"paper_bgcolor":"white","annotations":[{"font":{"size":14},"showarrow":false,"text":"Economics (JOE)","x":0.22,"xanchor":"center","xref":"paper","y":0.02,"yref":"paper"},{"font":{"size":14},"showarrow":false,"text":"Political Science (APSA)","x":0.67,"xanchor":"center","xref":"paper","y":0.02,"yref":"paper"},{"font":{"color":"gray","size":10},"showarrow":false,"text":"Dhameja, N. & Slichter, D. (2026). The Effect of Diversity Statement in Faculty Hiring. Data from JOE & APSA eJobs.","x":0.5,"xanchor":"center","xref":"paper","y":-0.08,"yref":"paper"}]},
  {"responsive": true}
);
</script>
