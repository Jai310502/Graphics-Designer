import os
import json
import rich
import base64
from openai import OpenAI
from anthropic import Anthropic
import google.generativeai as genai
from dotenv import load_dotenv

# import PIL.Image

# img = PIL.Image.open('image.png')
# img

load_dotenv()

client = OpenAI()
client.api_key = os.environ["OPENAI_API_KEY"]

anthroClient = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def compiledInput(maintext, subtext, placeOfEvent, timingOfEvent, contactDetails):
    input = {
                "title" : str(maintext),
                "tagline": str(subtext),
                "placeOfEvent": str(placeOfEvent),
                "timingOfEvent": str(timingOfEvent),
                "contactDetails": str(contactDetails)
    }
    return str(input)

def claudeCall(system_prompt, user_input = None):
    prompt = system_prompt
    messages = [
        {
            "role": "user",
            "content": str(prompt)
        }
    ]

    if user_input != None:
        messages.append(
            {
                "role": "user",
                "content": str(user_input)
            }
        )
    response = anthroClient.messages.create(
        max_tokens= 2048,
        messages = messages,
        model = "claude-3-opus-20240229"
    )

    return response.content

def geminiCall(prompt):
    model = genai.GenerativeModel('gemini-pro')
    # model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(str(prompt))
    return response.text

def gpt4call(system_prompt, user_input = None):

    prompt = system_prompt
    # prompt = prompt.replace('{image_description}', img_desc)
    # input = compiledInput(maintext, subtext, placeOfEvent, timingOfEvent, contactDetails)
    # prompt = prompt.replace('{poster_elements}', str(input))

    messages = [
        {
            "role": "system",
            "content": str(prompt)
        }
    ]
    if user_input:
        messages.append({
            "role": "user",
            "content": str(user_input)
        })
    response = client.chat.completions.create(
        model = "gpt-4-0125-preview",
        response_format= {'type': 'json_object'},
        messages= messages,
        temperature=0.9
    )

    text_response = json.loads(response.choices[0].message.content)
    return text_response

# def midjourney(prompt, user_input):
#     with open("prompts/midJourney.txt") as journeyText:
#         prompt = journeyText.read()
    
def gpt4visioncall(img_url, maintext, subtext, placeOfEvent, timingOfEvent, contactDetails):
    with open("prompts/imgDescription.txt") as fileVision:
        prompt = fileVision.read()
    # input = {
    #             "title" : str(maintext),
    #             "tagline": str(subtext),
    #             "placeOfEvent": str(placeOfEvent),
    #             "timingOfEvent": str(timingOfEvent),
    #             "contactDetails": str(contactDetails)
    #         }
    # prompt = prompt.replace('{poster_elements}', str(input))
    """
    with open(image_path, "rb") as image_file:
        img = base64.b64encode(image_file.read()).decode('utf-8')
    """
    # txt = {
    #         maintext: str(maintext),
    #         subtext: str(subtext),
    #         placeOfEvent: str(placeOfEvent),
    #         timeOfEvent: str(timeOfEvent),
    #         contactDetails: str(contactDetails)
    #     } # include when using logoPosition.txt prompt + "brand_name: " + str(brand_name) + "\nsubtext: " + str(subtext)
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": str(prompt) #+ str(txt)
                },
                {
                    "type": "image_url",
                    "image_url":{
                        "url": str(img_url)
                    }
                }
            ]
        }
    ]

    response = client.chat.completions.create(
        model = "gpt-4-vision-preview",
        messages= messages,
        #response_format= {"type": "json_object"},
        temperature = 0.9
    )

    vision_response = response.choices[0].message.content
    return vision_response

# user_input = 'Online Wellness Coaching Logo Design: Create a logo for "MindfulWell", an online wellness coaching service offering personalized support for mental health, stress management, and holistic well-being. Utilize elements like serene symbols, wellness icons, or peaceful color schemes. Download in JPG format.'

# brand_name, subtext = gpt4call(user_input)

#img_path = "C:\Contlo\gdFabric\logo_images\Greencycle.png"
#brand_name = "GreenCycle"
#subtext = "Let the planet breathe"
#user_input = 'Post Malone Concert Poster Design: Create a poster for "Posty Night", a musical concert organised by Coke Studio in JLN Stadium, Delhi, on 20th April 2024 from 7pm. Tagline should be "The World will watch" The poster should convey a high energy environment and portray the event as larger than life. There should be visual elements like a large number of lights and a huge crowd. Tickets can be purchased from BookMyShow.com. For additional details, contact studio@cocacola.com.'
# img_desc = """[
#                         {
#                             "COMPONENT_NAME":"Background Circle",
#                             "COMPONENT_DESCRIPTION":"A large red circle dominates the background, centered horizontally.",
#                             "COMPONENT_LOCATION":"Centered at approx. (384, 768) with a radius of approx. 730 pixels",
#                             "COMPONENT_COLOUR_CODE":"#E53B44"
#                         },
#                         {
#                             "COMPONENT_NAME":"Silhouette",
#                             "COMPONENT_DESCRIPTION":"Silhouette of a person in profile at a microphone, against the circle.",
#                             "COMPONENT_LOCATION":"Centered at approx. (384, 520), extends roughly from (192, 240) to (576, 800)",
#                             "COMPONENT_COLOUR_CODE":"#000000"
#                         },
#                         {
#                             "COMPONENT_NAME":"Splatter Effect",
#                             "COMPONENT_DESCRIPTION":"Abstract red splatter effect across the bottom, resembling a reflection.",
#                             "COMPONENT_LOCATION":"Occupies the lower third of the image, below approx. (0, 1024)",
#                             "COMPONENT_COLOUR_CODE":"#E53B44"
#                         },
#                         {
#                             "COMPONENT_NAME":"Foreground Reflection",
#                             "COMPONENT_DESCRIPTION":"A dark, stylized reflection of the silhouette in the splatter effect.",
#                             "COMPONENT_LOCATION":"Centered at approx. (384, 1300), extends from the bottom to (384, 1100)",
#                             "COMPONENT_COLOUR_CODE":"#000000"
#                         }
#     ]"""
# #result = gpt4call(user_input) #gpt4visioncall(img_path, brand_name, subtext)
# img_url = "https://cdn.discordapp.com/attachments/1222529795347185760/1226840498749181972/gd_superagi_98661_Poster_of_an_comedy_event_with_logo_of_a_pers_fb9d9e96-94f2-4f8e-8186-f9b7d28d012b.png?ex=66263b40&is=6613c640&hm=67dc3108e0162f352a6977c12a3df6a21971e5e9538e8ddceb31deb10bd231f0&"
# maintext = "Music for Generations"
# subtext = "The best in business"
# placeOfEvent = "Talkatora Stadium, Delhi"
# timingOfEvent = "8pm, 24 APR"
# contactDetails = "www.musegen.com"
# result = gpt4call(img_desc, maintext, subtext, placeOfEvent, timingOfEvent, contactDetails)
# print(result)

###################################################################################################################

user_input = input("Please input your request for the logo: ")
# sys_prompt_file = open("prompts/inputParsing.txt", "r")
sys_prompt_file = open("prompts/logo_input_parsing.txt", "r")
sys_prompt = sys_prompt_file.read()
event_details = gpt4call(sys_prompt, user_input)
sys_prompt_file.close()

with open("prompts/logo_llm_element_placer.txt") as design_prompt_file:
    design_prompt = design_prompt_file.read()
rich.print_json(data = event_details)

design_prompt = design_prompt.replace(r'{title}', str(event_details["title"]))
design_prompt = design_prompt.replace(r'{tagline}', str(event_details["tagline"]))
# design_prompt = design_prompt.replace(r'{venue}', str(event_details["venue"]))
# design_prompt = design_prompt.replace(r'{timing}', str(event_details["time"]))
# design_prompt = design_prompt.replace(r'{artist}', str(event_details["artists"]))
# design_prompt = design_prompt.replace(r'{desc}', str(event_details["event_description"]))

print(design_prompt)

final_results = gpt4call(design_prompt)

with open('gpt4_response.json', 'w') as f:
    json.dump(final_results, f, indent=4)

rich.print_json(data = final_results)
design_prompt_file.close()
############################################################################################################

# prompt_file = open("prompts/llmElementPlacer.txt")
# prompt = prompt_file.read()


# # improved_gemini_prompt_file = open("prompts/gemini_improvement.txt")
# # improved_gemini_prompt = improved_gemini_prompt_file.read()
# # result = geminiCall(improved_gemini_prompt)

# result = geminiCall(prompt)
# # result = claudeCall(prompt)
# print(result)
#rich.print_json(data = result)