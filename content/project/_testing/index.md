---
title: Uploading Media Tests
summary: Some tests on which kinds of content can be uploaded.
tags:
  - Web Design
date: "2020-09-02T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  caption: Photo by rawpixel on Unsplash
  focal_point: Smart

links:
  - icon: twitter
    icon_pack: fab
    name: Follow
    url: https://twitter.com/Nick_2440

url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: _testing

# Media and interaction
commentable: true
share: true
pager: true
show_related: true
profile: true

---

Main image with attribution.

---

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum. Sed ac faucibus dolor, scelerisque sollicitudin nisi. Cras purus urna, suscipit quis sapien eu, pulvinar tempor diam. Quisque risus orci, mollis id ante sit amet, gravida egestas nisl. Sed ac tempus magna. Proin in dui enim. Donec condimentum, sem id dapibus fringilla, tellus enim condimentum arcu, nec volutpat est felis vel metus. Vestibulum sit amet erat at nulla eleifend gravida.

Nullam vel molestie justo. Curabitur vitae efficitur leo. In hac habitasse platea dictumst. Sed pulvinar mauris dui, eget varius purus congue ac. Nulla euismod, lorem vel elementum dapibus, nunc justo porta mi, sed tempus est est vel tellus. Nam et enim eleifend, laoreet sem sit amet, elementum sem. Morbi ut leo congue, maximus velit ut, finibus arcu. In et libero cursus, rutrum risus non, molestie leo. Nullam congue quam et volutpat malesuada. Sed risus tortor, pulvinar et dictum nec, sodales non mi. Phasellus lacinia commodo laoreet. Nam mollis, erat in feugiat consectetur, purus eros egestas tellus, in auctor urna odio at nibh. Mauris imperdiet nisi ac magna convallis, at rhoncus ligula cursus.

Cras aliquam rhoncus ipsum, in hendrerit nunc mattis vitae. Duis vitae efficitur metus, ac tempus leo. Cras nec fringilla lacus. Quisque sit amet risus at ipsum pharetra commodo. Sed aliquam mauris at consequat eleifend. Praesent porta, augue sed viverra bibendum, neque ante euismod ante, in vehicula justo lorem ac eros. Suspendisse augue libero, venenatis eget tincidunt ut, malesuada at lorem. Donec vitae bibendum arcu. Aenean maximus nulla non pretium iaculis. Quisque imperdiet, nulla in pulvinar aliquet, velit quam ultrices quam, sit amet fringilla leo sem vel nunc. Mauris in lacinia lacus.

Suspendisse a tincidunt lacus. Curabitur at urna sagittis, dictum ante sit amet, euismod magna. Sed rutrum massa id tortor commodo, vitae elementum turpis tempus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean purus turpis, venenatis a ullamcorper nec, tincidunt et massa. Integer posuere quam rutrum arcu vehicula imperdiet. Mauris ullamcorper quam vitae purus congue, quis euismod magna eleifend. Vestibulum semper vel augue eget tincidunt. Fusce eget justo sodales, dapibus odio eu, ultrices lorem. Duis condimentum lorem id eros commodo, in facilisis mauris scelerisque. Morbi sed auctor leo. Nullam volutpat a lacus quis pharetra. Nulla congue rutrum magna a ornare.

Aliquam in turpis accumsan, malesuada nibh ut, hendrerit justo. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Quisque sed erat nec justo posuere suscipit. Donec ut efficitur arcu, in malesuada neque. Nunc dignissim nisl massa, id vulputate nunc pretium nec. Quisque eget urna in risus suscipit ultricies. Pellentesque odio odio, tincidunt in eleifend sed, posuere a diam. Nam gravida nisl convallis semper elementum. Morbi vitae felis faucibus, vulputate orci placerat, aliquet nisi. Aliquam erat volutpat. Maecenas sagittis pulvinar purus, sed porta quam laoreet at.

Blocks of text.

---

<div class="sketchfab-embed-wrapper"> <iframe title="Hatchet" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="720" height="480" src="https://sketchfab.com/models/997998bb3fd84908bfeed2f66fbd1d02/embed?autospin=1&ui_theme=dark&dnt=1"> </iframe> </div>

3D models (GLB, GLTF, etc) - using [SketchFab](https://help.sketchfab.com/hc/en-us/articles/203509907-Embedding-your-3D-models)

---

<iframe width="720" height="480" src="https://www.youtube-nocookie.com/embed/jjFSRDUvETQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

YouTube video - using [YouTube IFrame](https://developers.google.com/youtube/iframe_api_reference)

---

<iframe
  width="720" height="480" style="border:0" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"
  src="https://www.google.com/maps/embed/v1/place?key=AIzaSyAwWrgOOD7VH078D9MKygPbs3zYy63INSk
    &q=NUS+Singapore">
</iframe>

<!--
Docs: https://developers.google.com/maps/documentation/embed/get-started
Seems to be OK to show API key..?
https://stackoverflow.com/questions/46247295/how-do-i-create-environment-variables-to-protect-my-google-maps-api-keyor-any-o
If want to try hiding it see:
https://www.youtube.com/watch?v=m2Dr4L_Ab14
-->

Google Maps - using [Google Maps Embed API](https://developers.google.com/maps/documentation/embed/get-started)

---

<div id="adobe-dc-view" style="width: 720px; height: 985px"></div>
<script src="https://documentcloud.adobe.com/view-sdk/viewer.js"></script>
<script type="text/javascript">
	document.addEventListener("adobe_dc_view_sdk.ready", function(){
        if (location.hostname === "localhost" || location.hostname === "127.0.0.1") {
            apiKey = "6d36fa5703f24259ab52e4ddead85ca8";
            fileUrl = "http://localhost:1313/uploads/Lorcan%20Nicholls%20-%20CV.pdf"
        } else {
            apiKey = "109ff4b54f5448a9a9f90bbf0697471b"
            fileUrl = "https://lorcan.netlify.app/uploads/Lorcan%20Nicholls%20-%20CV.pdf"
        }
		var adobeDCView = new AdobeDC.View({clientId: apiKey, divId: "adobe-dc-view"});
		adobeDCView.previewFile({
			content: {location: {url: fileUrl}},
			metaData: {fileName: "Lorcan Nicholls - CV"}
		}, {embedMode: "IN_LINE", defaultViewMode: "FIT_PAGE"});
	});
</script>

<p>

<!--
Docs: https://developer.adobe.com/document-services/docs/overview/pdf-embed-api/howtos/
Need two api keys, one for local and one for production
-->

PDF - using [Adobe PDF Embed API](https://developer.adobe.com/document-services/docs/overview/pdf-embed-api/)

---

<iframe allowtransparency="true" width="720" height="480" src="//scratch.mit.edu/projects/175189448/embed?autostart=false"  frameborder="0" allowfullscreen></iframe>

Scratch project LOL

---

<iframe width="720" height="480" frameborder="0"
src="https://embed.molview.org/v1/?mode=balls&cid=2519&bg=gray"></iframe>

MolView

---

To try / keep in mind:

* [PowerPoint presentations](https://support.microsoft.com/en-us/office/embed-a-presentation-in-a-web-page-or-blog-19668a1d-2299-4af3-91e1-ae57af723a60#:~:text=Open%20your%20presentation%20in%20PowerPoint,Share%2C%20and%20then%20click%20Embed.&text=In%20the%20Embed%20box%2C%20under,Copy%2C%20and%20then%20click%20Close.)
* [Dash](https://dash.plotly.com/introduction) or [Bokeh](https://docs.bokeh.org/en/latest/) apps - find out if it's even possible
  
---

<div id="disqus_thread"></div>
<script>
    var disqus_config = function () {
    this.page.url = "https://lorcan.netlify.app/project/_testing/";  // Replace PAGE_URL with your page's canonical URL variable
    this.page.identifier = "12345"; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
    };
    (function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');
    s.src = 'https://https-lorcan-netlify-app.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
</script>

Disqus comments section

---

...which isn't fixed at the footer!