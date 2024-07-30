const request = require('request');

function printStarWarsCharacters(movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    characters.forEach((characterUrl) => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
          return;
        }
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  });
}

// Test the function
printStarWarsCharacters(process.argv[2]);
