---
id: stage1part2
title: Part 2 - Recognizing Stop Signs
sidebar_label: Recognizing Stop Signs
---
Now that we can recognize llamas, it's time to recognize stop signs as well.

## Step 1: Recognizing Stop Signs
Now that we have written a script to use the Google Vision API to parse an image and determine what it's contents are, we can extend this code to recogize any object we want!

Since we don't care about llamas anymore let's adapt the code to parse an image of a stop sign.

Change line 8 to:

`image_path = "stopsign.png"`

This will now upload a picture of a stop sign.

### To-Do: Modify the code to find a stop sign instead of a llama
hint: when searching in your responses array, change the word "llama" to "stop sign"

### Solution

```
for i in range(0, len(responses))
    if responses[i] == "stop sign":
        print("We found a stop sign")
```

## Step 2: Make it a function

It will be significantly easier to reuse this code in later modules if we convert this code into a function.

### To-Do: Write a function with one parameter (the path to an image) that tells you if the image contains a stop sign.

It should follow something similar to:

```
def is_stop_sign(path_to_image):
    #code
```

and return `True` or `False`.

#### Hint: Everything after line 9 should be included in the function

### Solution

```
def is_stop_sign(path_to_image):
    img_string = secret_stuff.encode_img(path_to_image)
    max_results = 2
    
    payload = {"requests": [{"image": {"content": img_string}, "features": [{"type": "LABEL_DETECTION", "maxResults": max_results}]}]}
    
    r = requests.post("https://vision.googleapis.com/v1/images:annotate?key=" + key, json=payload)
    response = r.json()
        
    responses = secret_stuff.parse(response)
    
    for i in range(0, len(responses)):
        if responses[i] == "stop sign":
            return True
    return False
```

