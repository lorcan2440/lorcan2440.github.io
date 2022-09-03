// Docs on event and context https://docs.netlify.com/functions/build/#code-your-function-2

const axios = require('axios');

const handler = async (event) => {
  try {
    
    const {q} = event.queryStringParameters;
    const API_SECRET = process.env.GOOGLE_MAPS_API_KEY;
    const url = "https://www.google.com/maps/embed/v1/place?key=${API_SECRET}&q=${q}";

    const iframe = <iframe
        width="720" height="480" style="border:0" loading="lazy" allowfullscreen
        referrerpolicy="no-referrer-when-downgrade" src="${url}"></iframe>

    console.log("Hello world!")

    return {
      statusCode: 200,
      body: iframe
    }
  } catch (error) {
    return { statusCode: 500, body: error.toString() }
  }
}

module.exports = { handler }
