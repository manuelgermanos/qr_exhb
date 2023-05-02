const express = require('express');
const router = express.Router();
const Item = require('./models/item');

router.route('/items').get((req, res) => {
  Item.find((err, items) => {
    if (err) {
      console.log(err);
    } else {
      res.json(items);
    }
  });
});

router.route('/items/:id').get((req, res) => {
  let id = req.params.id;
  Item.findById(id, (err, item) => {
    res.json(item);
  });
});

router.route('/items/add').post((req, res) => {
  let item = new Item(req.body);
  item.save()
    .then(item => {
      res.status(200).json({'item': 'item added successfully'});
    })
    .catch(err => {
      res.status(400).send('adding new item failed');
    });
});

module.exports = router;
