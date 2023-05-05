require('dotenv').config();

const express = require('express');
const mongoose = require('mongoose');
const app = express();
const routes = require('./routes');
app.use('/api', routes)
const circuit = require('./models');
const drivers = require('./models');
const season = require('./models');
const constructor = require('./models');

const mongoString = process.env.DATABASE_URL //we are storing the string into a variable called mongoString.

mongoose.connect(mongoString);
const database = mongoose.connection // connect the database to our server using Mongoose.

database.on('error', (error) => {
    console.log(error)
})



database.once('connected', () => {
    console.log('Database Connected');
})

// throw a success or an error message depending on whether our database connection is successful or fails.

//database.on means it will connect to the database, and throws any error if the connection fails. And database.once means it will run only one time. If it is successful, it will show a message that says Database Connected.

app.use(express.json());

app.listen(3000, () => {
    console.log(`Server Started at ${3000}`)
})
