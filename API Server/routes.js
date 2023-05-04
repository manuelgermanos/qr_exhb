const express = require('express');

const router = express.Router()

module.exports = router;

//Post Method
router.post('/post', (req, res) => {
    res.send('Post API')
})

//Get all Method
router.get('/getAll', (req, res) => {
    res.send('Get All API')
})

//Get by ID Method
const circuit = require('./models');
const drivers = require('./models');
const season = require('./models');
const constructor = require('./models');

router.get('/circuits/names', async (req, res) => {
    try {
      const circuits = await circuit.find({}, 'name'); // find all circuits and return only their name field
      const circuitNames = circuits.map(circuit => circuit.name); // map the circuits to an array of their names
      res.send(circuitNames); // send the array of circuit names as the response
    } catch (error) {
      console.error(error);
      res.status(500).send('Internal Server Error');
    }
  });

 // Import the Mongoose model for drivers

// router.get('/getOne/:id', async (req, res) => {
//   try {
//     const drivers = await drivers.find({ driverId: 3 }, 'forename surname'); // Find all drivers with driverID 3 and return only their forename and surname
//     res.send(drivers);
//   } catch (error) {
//     console.log(error);
//     res.status(500).send('Internal Server Error');
//   }
// });

module.exports = router;


//Update by ID Method
router.patch('/update/:id', (req, res) => {
    res.send('Update by ID API')
})

//Delete by ID Method
router.delete('/delete/:id', (req, res) => {
    res.send('Delete by ID API')
})