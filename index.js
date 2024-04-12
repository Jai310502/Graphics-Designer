const fs = require('fs');
const fabric = require('fabric').fabric;

const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay));

// Read element properties from JSON file
const jsonstr = fs.readFileSync(__dirname + '/gpt4_response.json', 'utf-8');
const jsonData = JSON.parse(jsonstr);

const canvas = new fabric.Canvas('canvas', {
    width: 1024,
    height: 1024
});


// jsonData.Text_component_details_LIST.map(detail => {
//     const component = Object.keys(detail)[0];
//     const prop = detail[component];
//     const element = createDynamicText(prop.text, 512, parseInt(prop['location at y-axis']), 500, 50, prop.font_name, prop.font_weight, 'black', parseInt(prop.font_size), prop.font_style);
//     canvas.add(element);
//     canvas.renderAll();
// });

// Function to create canvas and render elements
async function createCanvas() {
    await sleep(3000)

    url = "https://cdn.discordapp.com/attachments/1222529795347185760/1228333564182003733/gd_superagi_98661_Generate_a_dynamic_and_energetic_logo_for_Fel_8d8e493b-566b-4143-bba4-9b833b1ecb66.png?ex=662ba9c7&is=661934c7&hm=947fca0ef3a75b08c4cdffd079eec96f0d98648de857ba511a8aebd6899f6518&"
    // load image
    fabric.Image.fromURL(url, function (img) {
        img.scaleToWidth(1024)
        img.scaleToHeight(1024)

        // Create text elements dynamically
        const textElements = jsonData.Text_component_details_LIST.map(detail => {
            const component = Object.keys(detail)[0];
            const prop = detail[component];
            return createDynamicText(prop.text, 512, parseInt(prop['location at y-axis']), 500, 50, prop.font_name, prop.font_weight, prop.font_colour, parseInt(prop.font_size), prop.font_style);
        });
        
        // Add image and text elements to a group
        const group = new fabric.Group([img, ...textElements], {});
        canvas.add(group);
        
        canvas.renderAll();

        // Save JSON
        const json = JSON.stringify(canvas);
        console.log(json);

        // Save SVG
        const svg = canvas.toSVG();
        fs.writeFileSync('output.svg', svg);
        console.log('SVG saved successfully.');
    });

    // Set the size of the canvas
    canvas.setDimensions({ width: 1024, height: 1024 });
};

// Function to create text with dynamic font size and centered horizontally
function createDynamicText(text, left, top, width, height, fontFamily, fontWeight, fill, fontSize, fontStyle = 'normal') {
    // TODO: 
    // Textbox or Text or IText

    console.log("INSIDE CREATE DYNAMIC TEXT")
    const textbox = new fabric.Text(text, {
        left: left,
        top: top,
        // width: width,
        // height: height,
        fontSize: fontSize,
        fontFamily: fontFamily,
        fontWeight: fontWeight,
        fill: fill,
        fontStyle: fontStyle,
        textAlign: 'center',
    });

    // Calculate and set the dynamic font size
    // const fontSize = findFontSize(text, fontFamily, fontWeight, width, height);

    // Calculate the actual width of the text
    const textWidth = getTextWidth(text, fontFamily, fontWeight, fontSize);

    // console.log(text)
    // console.log(textWidth)
    // console.log("left")
    // console.log(left - (textWidth / 2))

    // Adjust the left position to center the text horizontally
    textbox.set({
        // fontSize: fontSize,
        left: left - (textWidth / 2)
    });

    return textbox;
}

function getTextWidth(text, fontFamily, fontWeight, fontSize) {
    // const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");
    ctx.font = fontWeight + " " + fontSize + "px " + fontFamily;
    const width = ctx.measureText(text).width;
    return width;
}

function getTextHeight(text, fontFamily, fontWeight, fontSize) {
    // const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");
    ctx.font = fontWeight + " " + fontSize + "px " + fontFamily;
    // Returns the total line height
    return ctx.measureText('M').actualBoundingBoxAscent + ctx.measureText('M').actualBoundingBoxDescent;
}

function findFontSize(text, fontFamily, fontWeight, width, height) {
    const minSize = 1;
    const maxSize = 100;
    const fontSize = 50; // Default font size
    while (maxSize - minSize > 1) {
        fontSize = (minSize + maxSize) / 2; // Calculate the middle font size
        if (getTextWidth(text, fontFamily, fontWeight, fontSize) > width || getTextHeight(text, fontFamily, fontWeight, fontSize) > height) {
            maxSize = fontSize; // Adjust the max size
        } else {
            minSize = fontSize; // Adjust the min size
        }
    }
    return minSize; // Return the final font size
}




createCanvas();