import json

#function to transform the original json using generated json and write it to transformed_json
def transform_json(original_json, generated_json):
    for obj in original_json["objects"]:
        for inner_obj in obj["objects"]:
            if inner_obj["type"] == "text":
                if inner_obj["text"] == "brand_name":
                    inner_obj["text"] = generated_json["brand_name"]
                    inner_obj["fontFamily"] = generated_json["brand_name_properties"]["Font"]
                    inner_obj["fontSize"] = int(''.join(filter(str.isdigit, generated_json["brand_name_properties"]["Size"])))
                    inner_obj["fontWeight"] = "bold" if generated_json["brand_name_properties"]["Bold"] else "normal"
                    inner_obj["fontStyle"] = "italic" if generated_json["brand_name_properties"]["Italics"] else "normal"
                    inner_obj["fill"] = generated_json["brand_name_properties"]["Color"]
                elif inner_obj["text"] == "subtext":
                    inner_obj["text"] = generated_json["subtext"]
                    inner_obj["fontFamily"] = generated_json["subtext_properties"]["Font"]
                    inner_obj["fontSize"] = int(''.join(filter(str.isdigit, generated_json["subtext_properties"]["Size"])))
                    inner_obj["fontWeight"] = "bold" if generated_json["subtext_properties"]["Bold"] else "normal"
                    inner_obj["fontStyle"] = "italic" if generated_json["subtext_properties"]["Italics"] else "normal"
                    inner_obj["fill"] = generated_json["subtext_properties"]["Color"]

    with open('transformed_json.json', 'w') as f:
        json.dump(original_json, f, indent=4)

# Load original and generated json
with open('original.json', 'r') as f:
    original_json = json.load(f)

with open('gen.json', 'r') as f:
    generated_json = json.load(f)

# Transform the original json using the generated json
transform_json(original_json, generated_json)


