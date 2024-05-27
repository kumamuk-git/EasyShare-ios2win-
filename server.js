const express = require('express');
let open;

import('open').then((module) => {
    open = module.default;
});

const app = express();
const port = 8080;

app.use(express.json());

app.post('/', async (req, res) => {

    const url = req.body.url;
    if (url) {  // urlが存在し、空でないことを確認
        if(open){
          await open(url);
          res.send('OK');
        }
        else{
          res.send('open module is not loaded yet');
        }
    } else {
        res.send('URL is not provided in the request body');
    }
});

app.listen(port, '0.0.0.0', () => {
  
});
