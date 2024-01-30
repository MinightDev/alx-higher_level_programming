#!/usr/bin/node

const request = require('request');

function getDataFrom(url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, _res, body) {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

function errorHandler(error) {
  console.log(error);
}

function printMovieCharacters(movieId) {
  const movieUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  getDataFrom(movieUrl)
    .then(JSON.parse, errorHandler)
    .then(function (response) {
      const characters = response.characters;
      const characterPromises = [];

      for (let i = 0; i < characters.length; ++i) {
        characterPromises.push(getDataFrom(characters[i]));
      }

      Promise.all(characterPromises)
        .then((results) => {
          for (let i = 0; i < results.length; ++i) {
            console.log(JSON.parse(results[i]).name);
          }
        })
        .catch(errorHandler);
    });
}

printMovieCharacters(process.argv[2]);

