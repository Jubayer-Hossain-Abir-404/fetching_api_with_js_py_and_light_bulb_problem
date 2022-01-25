// Fetching API Data
let baseUrl = 'https://gorest.co.in/public/v1/users';

// Json response
fetch(baseUrl).then(response => response.json())
.then(json => {
    // Here stringifying the json data for showcasing the response in the browser
    document.write(JSON.stringify(json));
})