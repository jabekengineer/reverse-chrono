var express = require('express');

var app = express();

// http://expressjs.com/en/starter/static-files.html
app.use(express.static('public'));

// http://expressjs.com/en/starter/basic-routing.html
app.get("/", function (request, response) {
  response.sendFile(__dirname + '/views/index.html');
});

app.get("/test.py", function (request, response) {
  const { spawn } = require('child_process');
  const pyProg = spawn('python',['./public/py/test.py', 'hello' ]);
  pyProg.stdout.on('data', function(data) {
    // console.log(data.toString());
    response.write(data);
    response.end();
  });
})

// listen for requests :)
var listener = app.listen(process.env.PORT, function () {
  console.log('Your app is listening on port ' + listener.address().port);
});
