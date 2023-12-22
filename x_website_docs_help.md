https://wowchemy.com/docs/getting-started/page-builder/
https://wowchemy.com/docs/getting-started/customization/

How to hide API keys in Netlify
https://www.youtube.com/watch?v=m2Dr4L_Ab14

Adobe PDF Embed API
https://developer.adobe.com/console/projects/988909/4566206088344831837/overview

Example of hiding Google Maps API Keys
https://github.com/netlify/code-examples/blob/master/function_examples/token-hider/README.md

How to fix local site building:
"Error: from config: failed to resolve output format "headers" from site config"
- Go to C:\Users\lnick\AppData\Local\Temp
- Delete hugo_cache
- or just run $ rmdir C:\Users\lnick\AppData\Local\Temp\hugo_cache

How to fix not uploading to github:
- Take out data book and delete local folder
- $ cd C:\Users\lnick\Documents\Personal\Programming\Projects
- $ git clone https://github.com/lorcan2440/lorcan2440.github.io.git
- Put data book back into static/uploads
- Push to github

How to run and update website
- $ hugo server