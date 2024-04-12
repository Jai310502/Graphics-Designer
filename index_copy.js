// Get the image URL and JSON data
var imageUrl = "";
var jsonData = {}

document.getElementById('fileInput').addEventListener('change', function selectedFileChanged() {
    if (this.files.length === 0) {
        console.log('No file selected.');
        return;
    }

    const reader = new FileReader();
    reader.onload = function fileReadCompleted() {
        // when the reader is done, the content is in reader.result.
        jsonData = JSON.parse(reader.result);
        console.log(typeof jsonData);
        console.log(jsonData);

        const canvas = new fabric.Canvas('canvas')

        // canvas.loadFromJSON(jsonData, function() {
        //     canvas.renderAll(); 
        // },function(o,object){
        //     console.log(o,object)
        // })
        // const ctx = canvas.getContext("2d");

        // Extracting URL
        // const imageUrl = jsonData.url;
        // console.log("Image URL:", imageUrl);

        // // Extracting Text Component Details
        // const textComponentDetails = jsonData.Text_component_details_LIST[0];
        // console.log("Text Component Details:", textComponentDetails);

        // // Extracting Title
        // const title = textComponentDetails.Title;
        // console.log("Title:", title);

        // // Extracting Venue
        // const venue = textComponentDetails.Venue;
        // console.log("Venue:", venue);

        // // Extracting Time
        // const time = textComponentDetails.Time;
        // console.log("Time:", time);

        // // Extracting Date
        // const date = textComponentDetails.Date;
        // console.log("Date:", date);

        // // Extracting Asset Component Details
        // const assetComponentDetails = jsonData.Asset_component_details_LIST;
        // console.log("Asset Component Details:", assetComponentDetails);

        // // Looping through Asset Component Details
        // assetComponentDetails.forEach(function(assetComponent) {
        //     // Extracting URL
        //     const assetUrl = assetComponent.url;
        //     console.log("Asset URL:", assetUrl);

        //     // Extracting Component Name
        //     const componentName = assetComponent.component_name;
        //     console.log("Component Name:", componentName);

        //     // Extracting Component Description
        //     const componentDescription = assetComponent.component_description;
        //     console.log("Component Description:", componentDescription);

        //     // Extracting Component Location
        //     const componentLocation = assetComponent.component_location;
        //     console.log("Component Location:", componentLocation);

        //     // Extracting Thought on Location
        //     const thoughtOnLocation = assetComponent.thought_on_location;
        //     console.log("Thought on Location:", thoughtOnLocation);
        // });

        imageUrl = jsonData.url

        var logo1;
        var logo2;
        var fg_img;
        var fg_img_2;
        var logo1_url = "https://static-00.iconduck.com/assets.00/openai-icon-2021x2048-4rpe5x7n.png"
        var logo2_url = "https://www.freepnglogos.com/uploads/google-logo-png/google-logo-png-webinar-optimizing-for-success-google-business-webinar-13.png"

        var fg_url = "https://cdn.discordapp.com/attachments/1222529795347185760/1227567080522514442/gd_superagi_98661_Musical_Instrument._There_will_be_a_black_pla_6ce3d9d8-b0f1-4d33-8e59-924ba472f31d.png?ex=6628dfef&is=66166aef&hm=76d9578f039a4068a8df31077522738674359408733d662340a28af25930013c&"
        var fg_url_2 = "https://cdn.discordapp.com/attachments/1222529795347185760/1227519918014992414/gd_superagi_98661_Splash_of_color._The_splash_of_color_should_b_19d31349-ecbb-42d4-9d72-a67ef0ca0e5c.png?ex=6628b402&is=66163f02&hm=87dcfc5da8a2d0384690f2b6b6d005d2b0a747081e43a959353ea4f6e6dffc6b&"

        const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay))

        async function load_logos() {
            // await sleep(5000);
            fabric.Image.fromURL(logo1_url, function (img) {
                img.set({
                    left: 20,
                    top: 40
                })
                img.scaleToWidth(120);
                img.scaleToHeight(120);

                logo1 = img

            });

            fabric.Image.fromURL(logo2_url, function (img) {
                img.set({
                    left: 628,
                    top: 40
                })
                img.scaleToWidth(120);
                img.scaleToHeight(120);

                logo2 = img
            })
            
            fabric.Image.fromURL(fg_url, function (img) {
                img.set({
                    left: 384,
                    top: 384
                })
                img.scaleToWidth(384);
                img.scaleToHeight(384);

                fg_img = img
            })

            fabric.Image.fromURL(fg_url_2, function (img) {
                img.set({
                    left: 0,
                    top: 0
                })
                img.scaleToWidth(768);
                img.scaleToHeight(384);

                fg_img_2 = img
            })
        }

        load_logos();



        // // load image
        async function finalRender() {
            await sleep(3000)
            fabric.Image.fromURL(imageUrl, function (img) {
                var t1 = createDynamicText('Winter Music Conference Pool Party', img.width / 2, 100, 500, 150, 'Helvetica Bold', 'normal', '#FFFFFF', 48);
                // var t2 = createDynamicText('THE BEST IN BUSINESS', img.width/2, 420, 230, 64, 'Lato', 'normal', '#FFFFFF', 40);
                var t3 = createDynamicText('Talkatora Stadium, Delhi', img.width / 2, 1340, 300, 50, 'Lato', 'normal', '#FFFFFF', 36);
                var t4 = createDynamicText('25th February 2024, 8 PM', img.width / 2, 1380, 300, 50, 'Lato', 'normal', '#FFFFFF', 36);
                // var t5 = createDynamicText('Featuring: Sunidhi Chauhan', img.width / 2, 220, 668, 50, 'Helvetica', 'normal', '#FFFFFF', 36);
                var t6 = createDynamicText('Friday', img.width / 2, 1200, 668, 50, 'Helevetica', 'normal', '#FFFFFF', 28);


                
                // Add image and text to a group
                var group = new fabric.Group([img, t1, t2, t3, t4], {
                    // left: 50,
                    // top: 50,
                });

                canvas.add(group);

                canvas.renderAll();

                // Save JSON
                var json = JSON.stringify(canvas);
                console.log(json);
            });

            // Set the size of the canvas
            canvas.setDimensions({ width: 2000, height: 2000 });
        };

        finalRender();
    }

    
    reader.readAsText(this.files[0]);
});

// Function to create text with dynamic font size and centered horizontally
function createDynamicText(text, left, top, width, height, fontFamily, fontWeight, fill, fontSize, fontStyle = 'normal') {
    // TODO: 
    // Textbox or Text or IText

    var textbox = new fabric.Text(text, {
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
    // var fontSize = findFontSize(text, fontFamily, fontWeight, width, height);

    // Calculate the actual width of the text
    var textWidth = getTextWidth(text, fontFamily, fontWeight, fontSize);

    console.log(text)
    console.log(textWidth)
    console.log("left")
    console.log(left - (textWidth / 2))

    // Adjust the left position to center the text horizontally
    textbox.set({
        // fontSize: fontSize,
        left: left - (textWidth / 2)
    });

    return textbox;
}

function getTextWidth(text, fontFamily, fontWeight, fontSize) {
    var canvas = document.createElement("canvas");
    var ctx = canvas.getContext("2d");
    ctx.font = fontWeight + " " + fontSize + "px " + fontFamily;
    var width = ctx.measureText(text).width;
    return width;
}

function getTextHeight(text, fontFamily, fontWeight, fontSize) {
    var canvas = document.createElement("canvas");
    var ctx = canvas.getContext("2d");
    ctx.font = fontWeight + " " + fontSize + "px " + fontFamily;
    // Returns the total line height
    return ctx.measureText('M').actualBoundingBoxAscent + ctx.measureText('M').actualBoundingBoxDescent;
}

function findFontSize(text, fontFamily, fontWeight, width, height) {
    var minSize = 1;
    var maxSize = 100;
    var fontSize = 50; // Default font size
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





