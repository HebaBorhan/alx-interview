#!/usr/bin/node

const request = require('request');

// Check if the movie ID is passed as an argument
if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];

// Make a request to the Star Wars API for the specific movie
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    // Parse the response body into a JSON object
    const filmData = JSON.parse(body);

    // Extract the list of character URLs from the "characters" field
    const characters = filmData.characters;

    // Fetch the name of each character
    characters.forEach((characterUrl) => {
      request(characterUrl, (err, res, characterBody) => {
        if (err) {
          console.error('Error:', err);
          return;
        }

        if (res.statusCode === 200) {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        }
      });
    });
  } else {
    console.error(`Failed to retrieve movie. Status code: ${response.statusCode}`);
  }
});
