import timeit

start = timeit.default_timer()

import requests
import base64

#class variables
key = "AIzaSyAYhg5B10ji-Dv0FglIg-Xx3LDx8pOyoRk"


def encode_img(image_path):
    f = open(image_path)
    return f.read()


def post_image(image_path, num_results):
    img_string = encode_img(image_path)
    payload = {
        "requests": [
            {
                "image": {
                    "content": img_string
                },
                "features": [
                    {
                        "type": "LABEL_DETECTION",
                        "maxResults": num_results
                    }
                ]
            }
        ]
    }

    r = requests.post("https://vision.googleapis.com/v1/images:annotate?key=" + key, json=payload)
    if r.status_code == 200:
        return r.json()
    else:
        print(r.json())


def parse_labels(json_response):
    #print(json_response)
    try:
        response_obj = json_response["responses"][0]["labelAnnotations"]
        labels = []
        for annotation in response_obj:
            labels.append(annotation["description"])
        return labels
    except KeyError:
        print("Error: " + str(json_response))
        exit(0)

def is_stop_sign(file_path, num_responses=10):
    response = post_image(file_path, num_responses)
    labels = parse_labels(response)
    found = False
    for tag in labels:
        if tag.lower() == "stop sign":
            found = True
    return found


print(is_stop_sign("../images/stopsign.txt"))
end = timeit.default_timer()
print("Time elapsed: " + str(round((end - start) * 1000)) + " ms")
