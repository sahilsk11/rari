'''
This library contains functions that make it easier to analyze starter code. You're welcome to try to understand,
but it is not required.
'''
import base64

# OPTIONAL: the API wants the image to be encoded in a special format.
# This function converts your image to the special format.
# Don't worry about this!

def key():
    return "AIzaSyAYhg5B10ji-Dv0FglIg-Xx3LDx8pOyoRk"

def encode_img(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return str(encoded_string)[2:-1]

def parse(response):
    try:
        response_obj = response["responses"][0]["labelAnnotations"]
        labels = []
        for annotation in response_obj:
            labels.append(annotation["description"])
        return labels
    except KeyError:
        print("Error: " + str(response))