var fs = require('fs')
fabric = require('fabric').fabric
// out = fs.createWriteStream(__dirname + '/output.png');


let jsonstr = fs.readFileSync(__dirname + '/generated_canvas.json', 'utf-8');
let json = JSON.parse(jsonstr);

var canvas = new fabric.StaticCanvas(null, { width: 2000, height: 2000 });

canvas.loadFromJSON(json, function () {

    //first render
  canvas.renderAll.bind(canvas);

  //save the canvas as SVG in server
  var svgoutput = canvas.toSVG();
  fs.writeFile("output.svg", svgoutput, function (err) {
    if (err) throw err;
  });
});