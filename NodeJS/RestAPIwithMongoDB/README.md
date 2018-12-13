# NodeJS_RestAPIwithMongoDB
A fully functional Node JS REST API built using mongodb for a ToDo note taking app.

Please have a look at the server folder

server.js - REST api methods for Todo Note taking app. Main file 

cofig/config.js  - Contains the configurations used for setting up the port and mongodb uri for rest api

db/mongoose.js - Setting up mongoose to interact with mongodb

models/Todo.js -  Todo model for the Todo API with attributes text, completed , completedAt

models/User.js - User model with email attribute for the Todo API

test/server.test.js - Test scripts to test the api(Get, Post, Patch, Delete)


This API doesnt implement security and authentication. Full REST api with authentication and security will be uploaded soon.
