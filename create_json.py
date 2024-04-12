import json

def create_canvas_json(num_images, num_texts, img_properties, text_properties):
    canvas_json = {
        "version": "5.3.0",
        "objects": [
            {
                "type": "group",
                "version": "5.3.0",
                "originX": "left",
                "originY": "top",
                "left": 50,
                "top": 50,
                "width": 1024,
                "height": 1024,
                "fill": "rgb(0,0,0)",
                "stroke": None,
                "strokeWidth": 0,
                "strokeDashArray": None,
                "strokeLineCap": "butt",
                "strokeDashOffset": 0,
                "strokeLineJoin": "miter",
                "strokeUniform": False,
                "strokeMiterLimit": 4,
                "scaleX": 1,
                "scaleY": 1,
                "angle": 0,
                "flipX": False,
                "flipY": False,
                "opacity": 1,
                "shadow": None,
                "visible": True,
                "backgroundColor": "",
                "fillRule": "nonzero",
                "paintFirst": "fill",
                "globalCompositeOperation": "source-over",
                "skewX": 0,
                "skewY": 0,
                "objects": []
            }
        ]
    }

    for i in range(num_images):
        image_obj = {
            "type": "image",
            "version": "5.3.0",
            "originX": "left",
            "originY": "top",
            "left": -512,
            "top": -512,
            "width": 1024,
            "height": 1024,
            "fill": "rgb(0,0,0)",
            "stroke": None,
            "strokeWidth": 0,
            "strokeDashArray": None,
            "strokeLineCap": "butt",
            "strokeDashOffset": 0,
            "strokeLineJoin": "miter",
            "strokeUniform": False,
            "strokeMiterLimit": 4,
            "scaleX": 1,
            "scaleY": 1,
            "angle": 0,
            "flipX": False,
            "flipY": False,
            "opacity": 1,
            "shadow": None,
            "visible": True,
            "backgroundColor": "",
            "fillRule": "nonzero",
            "paintFirst": "fill",
            "globalCompositeOperation": "source-over",
            "skewX": 0,
            "skewY": 0,
            "cropX": 0,
            "cropY": 0,
            "src": "",
            "crossOrigin": None,
            "filters": []
        }

        print("IMAGE PROPERTUES SIZE", len(img_properties))
        for i in range(len(img_properties)):
            image_obj["left"] = img_properties[i]["left"]
            image_obj["top"] = img_properties[i]["top"]
            image_obj["width"] = img_properties[i]["width"]
            image_obj["height"] = img_properties[i]["height"]
            image_obj["src"] = img_properties[i]["src"]

            canvas_json["objects"][0]["objects"].append(image_obj.copy())

    for i in range(num_texts):
        text_obj = {
            "type": "text",
            "version": "5.3.0",
            "originX": "left",
            "originY": "top",
            "left": -107,
            "top": -412,
            "width": 178.39,
            "height": 33.9,
            "fill": "white",
            "stroke": None,
            "strokeWidth": 1,
            "strokeDashArray": None,
            "strokeLineCap": "butt",
            "strokeDashOffset": 0,
            "strokeLineJoin": "miter",
            "strokeUniform": False,
            "strokeMiterLimit": 4,
            "scaleX": 1,
            "scaleY": 1,
            "angle": 0,
            "flipX": False,
            "flipY": False,
            "opacity": 1,
            "shadow": None,
            "visible": True,
            "backgroundColor": "",
            "fillRule": "nonzero",
            "paintFirst": "fill",
            "globalCompositeOperation": "source-over",
            "skewX": 0,
            "skewY": 0,
            "fontFamily": "Sans-serif",
            "fontWeight": "bold",
            "fontSize": 30,
            "text": "brand_name",
            "underline": False,
            "overline": False,
            "linethrough": False,
            "textAlign": "left",
            "fontStyle": "normal",
            "lineHeight": 1.16,
            "textBackgroundColor": "",
            "charSpacing": 0,
            "styles": [],
            "direction": "ltr",
            "path": None,
            "pathStartOffset": 0,
            "pathSide": "left",
            "pathAlign": "baseline"
        }

    print("TEXT PROPERTUES SIZE", len(text_properties))
    for i in range(len(text_properties)):

        text_obj["left"] = text_properties[i]["left"]
        text_obj["top"] = text_properties[i]["top"]
        text_obj["width"] = text_properties[i]["width"]
        text_obj["height"] = text_properties[i]["height"]
        text_obj["fill"] = text_properties[i]["fill"]
        text_obj["text"] = text_properties[i]["text"]

        canvas_json["objects"][0]["objects"].append(text_obj.copy())

    return canvas_json

# Example: Create a canvas JSON with 2 image objects and 1 text object
# num_images = 1
# num_texts = 2
img_properties = [
    {
        "left": -445.68,
        "top": -768,
        "width": 768,
        "height": 1536,
        "src": "https://cdn.discordapp.com/attachments/1222529795347185760/1226958933097320651/gd_superagi_98661_A_poster_with_Background_Component_background_064e65af-f809-46d8-aa6a-c2837e9dcfde.png?ex=6626a98d&is=6614348d&hm=2960834465c914d39d387ec17a21552ace68f3e319f072b07fb0176ba6cbe0d0&"
    }
]

text_properties = [
    {
        "left": -395.49,
        "top": -358,
        "width": 668,
        "height": 99.89,
        "fill": "#FFFFFF",
        "text": "Laugh out Loud"
    },
    {
        "left": -395.49,
        "top": -558,
        "width": 668,
        "height": 99.89,
        "fill": "magenta",
        "text": "Don't Laugh out Loud",
    }
]

new_canvas_json = create_canvas_json(num_images=len(img_properties), num_texts=len(text_properties), img_properties=img_properties, text_properties=text_properties)

# Convert the JSON to a string and print it
new_canvas_json_str = json.dumps(new_canvas_json, indent=4)

# Write the JSON to a file
with open('generated_canvas.json', 'w') as file:
    json.dump(new_canvas_json, file, indent=4)

print(new_canvas_json_str)