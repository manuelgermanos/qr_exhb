const mongoose = require('mongoose');

const circuitSchema = new mongoose.Schema({
  circuitId: Number,
  circuitRef: String,
  name: String,
  location: String,
  country: String,
  lat: Number,
  lng: Number,
  alt: Number,
  url: String
});

const seasonSchema = new mongoose.Schema({
    _id: {
      type: mongoose.Schema.Types.ObjectId,
      required: true
    },
    year: {
      type: Number,
      required: true
    },
    url: {
      type: String,
      required: true
    }
  });
  
  const driverSchema = new mongoose.Schema({
    driverId: {
      type: Number,
      required: true
    },
    driverRef: {
      type: String,
      required: true
    },
    number: String,
    code: String,
    forename: {
      type: String,
      required: true
    },
    surname: {
      type: String,
      required: true
    },
    dob: Date,
    nationality: String,
    url: String
  });

  const constructorSchema = new mongoose.Schema({
    _id: {
      type: mongoose.Schema.Types.ObjectId,
      required: true
    },
    constructorId: {
      type: Number,
      required: true
    },
    constructorRef: {
      type: String,
      required: true
    },
    name: {
      type: String,
      required: true
    },
    nationality: {
      type: String,
      required: true
    },
    url: {
      type: String,
      required: true
    }
  });
  
const Circuit = mongoose.model('circuit', circuitSchema);
const Season = mongoose.model('season', seasonSchema);
const Driver = mongoose.model('driver', driverSchema);
const Constructor = mongoose.model('constructor', constructorSchema);
  
module.exports = { Circuit, Season, Driver, Constructor };