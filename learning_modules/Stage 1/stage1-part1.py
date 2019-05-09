import requests
import pprint

# the top secret key. This is a unique identifier that tells Google who is accessing the API
key = "AIzaSyAYhg5B10ji-Dv0FglIg-Xx3LDx8pOyoRk"

# Path to the llama image
# bonus! it's a .txt! this is because the API wants encoded images. More on this later.
image_path = "images/llama.txt"


# the API wants the image to be encoded in a special format. This function converts your image to the special format.
# Don't worry about this!
def encode_img(image_path):
    f = open(image_path)
    return f.read()


img_string = encode_img(image_path)

# these are the arguments we pass to the API. It follows the specific format the API wants the data in
payload = {
    "requests": [
        {
            "image": {
                "content": img_string
            },
            "features": [
                {
                    "type": "LABEL_DETECTION",
                    "maxResults": 2 # returns the 10 best labels for the images
                }
            ]
        }
    ]
}

# sends the call to the API
r = requests.post("https://vision.googleapis.com/v1/images:annotate?key=" + key, json=payload)

response = r.json()

print(response)