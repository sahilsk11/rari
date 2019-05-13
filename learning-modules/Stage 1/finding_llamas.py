import requests
import secret_stuff

# the top secret key. This is a unique identifier that tells Google who is accessing the API
key = secret_stuff.key()

# Path to the llama image
image_path = "llama.jpg"

img_string = secret_stuff.encode_img(image_path) # calls the function to encode the image. Don't worry about this.
max_results = 2

# these are the arguments we pass to the API. It follows the specific format the API wants the data in
payload = {"requests": [{"image": {"content": img_string}, "features": [{"type": "LABEL_DETECTION", "maxResults": max_results}]}]}

# sends the call to the API
r = requests.post("https://vision.googleapis.com/v1/images:annotate?key=" + key, json=payload)

response = r.json()

print(response)

#responses = secret_stuff.parse(response) # list of found objects
#print(responses)
