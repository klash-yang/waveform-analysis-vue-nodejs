const express = require('express')
const app = express()
const port = 3000

const {
    spawn
} = require('child_process');

var workerProcess = (req, res) => {
    var dataToSend;
    console.log('received request');
    // spawn new child process to call the python script
    const python = spawn('python', ['./get_data.py']);
    // collect data from script
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        // console.log(JSON.parse(data.toString()));
        res.json(JSON.parse(data.toString()));
    });
    // in close event we are sure that stream from child process is close
}

// workerProcess();

app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });

app.get('/', workerProcess);

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))