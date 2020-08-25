// Imports
const path = require("path");
const express = require("express");
const bodyParser = require("body-parser");

// Initialise the express server
const app = express();

// Initialise the body parser plugin
app.use(bodyParser.json());

// Initialise a GET request
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "index.html"));
});

app.get("/", sayHi);

//  Add a POST request
app.post("/add", (req, res) => {
    const { a, b } = req.body;
    res.send({
        result: parseInt(a) + parseInt(b)        
    });
});

// Listen on port 5000
app.listen(5000, () => {
    console.log('Server is running on port 5000')
})
