#!/usr/bin/node

const request = require('request');

// Check if the movie ID is passed as an argument
if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to get the film details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    // Parse the movie details
    const filmData = JSON.parse(body);

    // Extract the character URLs
    const characters = filmData.characters;

    // Create an array of promises to fetch each character's name
    const promises = characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (err, res, characterBody) => {
          if (err) {
            reject(new Error(err)); // Ensure rejection reason is an Error
          } else if (res.statusCode === 200) {
            const characterData = JSON.parse(characterBody);
            resolve(characterData.name); // Resolve the character name
          } else {
            reject(new Error(`Failed to retrieve character at ${characterUrl}`)); // Ensure rejection reason is an Error
          }
        });
      });
    });

    // Wait for all character requests to complete and print them in order
    Promise.all(promises)
      .then((characterNames) => {
        characterNames.forEach((name) => console.log(name));
      })
      .catch((err) => console.error('Error:', err.message)); // Log error message
  } else {
    console.error(`Failed to retrieve movie. Status code: ${response.statusCode}`);
  }
});
