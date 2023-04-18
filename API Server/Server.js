const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const mongoose = require('mongoose');

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(cors());

mongoose.connect('mongodb+srv://admin:admin@coe416database.qlhbx66.mongodb.net/test', { useNewUrlParser: true });

const MongoClient = require('mongodb').MongoClient;
const uri = 'mongodb+srv://admin:admin@coe416database.qlhbx66.mongodb.net/test'; // Replace with your MongoDB URI
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

client.connect((err) => {
    if (err) {
      console.error('Failed to connect to MongoDB:', err);
      return;
    }
    console.log('Connected to MongoDB');
    
    // Your database operations go here
});  

const collection = client.db('f1').collection('drivers');

app.get('/documents', (req, res) => {
  collection.find().toArray((err, docs) => {
    if (err) {
      console.error('Failed to retrieve documents:', err);
      res.status(500).send('Failed to retrieve documents');
      return;
    }
    res.send(docs);
  });
});


const connection = mongoose.connection;
connection.once('open', () => {
  console.log('MongoDB database connection established successfully');
});

app.listen(port, () => {
  console.log(`Server is running on port: ${port}`);
});

process.on('SIGINT', () => {
    console.log('Shutting down server');
    client.close();
    process.exit();
  });
  
