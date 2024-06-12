### My [Portfoilio Website](https://lorcan.netlify.app/)!

I've migrated from GitHub Pages to Netlify.

[![Netlify Status](https://api.netlify.com/api/v1/badges/a7579a4e-5d8d-4c2c-bc46-715c727d6fc7/deploy-status)](https://app.netlify.com/sites/lorcan/deploys)

#### Info

**Built with:** Hugo Academic Theme (starter-hugo-academic), Wowchemy

Helpful docs:

 - [Page Builder](https://wowchemy.com/docs/getting-started/page-builder/)
 - [Customisation](https://wowchemy.com/docs/getting-started/customization/)

To build and run the website:

```bash
$ hugo server
```

### Troubleshooting

"Error: from config: failed to resolve output format "headers" from site config"
- Go to `C:\Users\lnick\AppData\Local\Temp`
- Delete `hugo_cache`
- or just run `$ rmdir C:\Users\lnick\AppData\Local\Temp\hugo_cache`

How to fix not uploading to github:
- Take out data book and delete `local` folder
- `$ cd C:\Users\lnick\Documents\Personal\Programming\Projects`
- `$ git clone https://github.com/lorcan2440/lorcan2440.github.io.git`
- Put data book back into `static/uploads`
- Push to github
