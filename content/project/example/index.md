---
title: Uploading Media Tests
summary: Some tests on which kinds of content can be uploaded.
tags:
  - Design
date: '2022-09-03T00:00:00Z'

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  caption: Photo by rawpixel on Unsplash
  focal_point: Smart

links:
  - icon: twitter
    icon_pack: fab
    name: Follow
    url: https://twitter.com/georgecushen
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: example

---

Main image with attribution.

---

<div class="sketchfab-embed-wrapper"> <iframe title="Hatchet" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="720" height="480" src="https://sketchfab.com/models/997998bb3fd84908bfeed2f66fbd1d02/embed?autospin=1&ui_theme=dark&dnt=1"> </iframe> </div>

3D models (GLB, GLTF, etc) - using [SketchFab](https://help.sketchfab.com/hc/en-us/articles/203509907-Embedding-your-3D-models)

---

<iframe width="720" height="480" src="https://www.youtube-nocookie.com/embed/jjFSRDUvETQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

YouTube video - using [YouTube IFrame](https://developers.google.com/youtube/iframe_api_reference)

---

<iframe
  width="720" height="480" style="border:0" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"
  src="https://www.google.com/maps/embed/v1/place?key=${GOOGLE_MAPS_API_KEY}
    &q=NUS+Singapore">
</iframe>

Google Maps - using [Google Maps Embed API](https://developers.google.com/maps/documentation/embed/get-started)

---

<div id="adobe-dc-view" style="width: 720px;"></div>
<script src="https://documentcloud.adobe.com/view-sdk/viewer.js"></script>
<script type="text/javascript">
	document.addEventListener("adobe_dc_view_sdk.ready", function(){ 
		var adobeDCView = new AdobeDC.View({clientId: "${ADOBE_PDF_EMBED_API_KEY}", divId: "adobe-dc-view"});
		adobeDCView.previewFile({
			content:{location: {url: "https://lorcan.netlify.app/uploads/Lorcan%20Nicholls%20-%20CV.pdf"}},
			metaData:{fileName: "Lorcan Nicholls - CV"}
		}, {embedMode: "IN_LINE"});
	});
</script>

PDF - using [Adobe PDF Embed API](https://developer.adobe.com/document-services/docs/overview/pdf-embed-api/)

---

<iframe allowtransparency="true" width="720" height="480"  src="//scratch.mit.edu/projects/175189448/embed?autostart=false"  frameborder="0" allowfullscreen></iframe>

Scratch project LOL

