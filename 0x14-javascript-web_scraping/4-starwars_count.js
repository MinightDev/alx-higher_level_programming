#!/usr/bin/node

const request = require('request');
const starWarsUri = process.argv[2];
let count = 0;

if (!starWarsUri) {
  console.error('Usage: ./script.js <Star Wars API URL>');
  process.exit(1);
}

request(starWarsUri, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    process.exit(1);
  }

  try {
    body = JSON.parse(body).results;

    for (let i = 0; i < body.length; ++i) {
      const characters = body[i].characters;

      for (let j = 0; j < characters.length; ++j) {
        const character = characters[j];
        const characterId = character.split('/')[5];

        if (characterId === '18') {
          count += 1;
        }
      }
    }

    console.log(count);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
    process.exit(1);
  }
});

