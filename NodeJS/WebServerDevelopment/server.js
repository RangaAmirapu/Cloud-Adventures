// Loading the required modules

const express = require('express');
const hbs = require('hbs');
const fs = require('fs');

var app = express();

// Registering partials to use in view pages

hbs.registerPartials(__dirname + '/views/partials')
app.set('view engie', 'hbs');

// Adding Midleware

// Adding log file
app.use((req, res, next) => {
    var now = new Date().toString();
    var log = `${now}: ${req.method} ${req.url}`;
    fs.appendFile('server.log', log + '\n', (err) => {
        if (err) {
            console.log('Unable to write log file');
        }
    });
    next();
});

// Maintenance step if site has to be down

//app.use((req, res, next) => {
//    res.render('maintenance.hbs');
//})

// Allowing the app to use the public folder

app.use(express.static(__dirname + '/public'));

// Registering a helper to use in every page

hbs.registerHelper('GetCurrentYear', () => {
    return new Date().getFullYear();
});

hbs.registerHelper('Capitalize', (text) => {
    return text.toUpperCase();
});

// Configuring the app to serve according to the url

app.get('/', (req, res) => {
    res.render('home.hbs', {
        pageTitle: 'Home',
        name: 'Ranga'
    });
});

app.get('/about', (req, res) => {
    res.render('about.hbs', {
        pageTitle: 'About Page',
    });
});

app.get('/bad', (req, res) => {
    res.send({
      errorMessgae : 'Bad Request'
    });
});

// Configuring the app to listen on port 3000

app.listen(3000, () => {
    console.log("Node web server running on port 3000");
});