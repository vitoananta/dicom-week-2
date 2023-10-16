let data_path = './data/volume/';
data_path = './Phantoms/Manekin-01/A/Z01';
data_path = './Phantoms/Phantom Test 02/A/Z21';

var daikon = require('./daikon-min.js');
var fs = require('fs');

function toArrayBuffer(buffer) {
    var ab = new ArrayBuffer(buffer.length);
    var view = new Uint8Array(ab);
    for (var i = 0; i < buffer.length; ++i) {
        view[i] = buffer[i];
    }
    return ab;
}

var name = data_path;
var buf = fs.readFileSync(name);

// parse DICOM file
var image = daikon.Series.parseImage(new DataView(toArrayBuffer(buf)));

const data = image.getInterpretedData();
// console.log('data: ' + data);
const imageNumber = image.getImageNumber();
const imageRow = image.getRows();
const imageCol = image.getCols();
const imageWW = image.getWindowWidth();
const imageWC = image.getWindowCenter();

const shape = {
    slice: imageNumber,
    rows: imageRow,
    cols: imageCol,
}

const wwwc = [imageWW, imageWC]

function WWWC(shape, data, wwwc) {
    const [x, y, z] = [shape.slice, shape.rows, shape.cols];
    const size = y * z;
    const appliedArray = new Float32Array(size);
    for (let i = 0; i < size; i++) {
        const newValue = ((data[i] - (wwwc[1] - 0.5)) / (wwwc[0]) + 0.5) * 255;
        if (newValue > 255 || newValue < 0) {
            appliedArray[i] = 0;
        } else {
            appliedArray[i] = newValue;
        }
    }
    return appliedArray;
}

const appliedArray = WWWC(shape, data, wwwc);
console.log(appliedArray);

// Write the appliedArray to a CSV file
const csvData = appliedArray.join(',');
fs.writeFileSync('appliedArray.csv', csvData);