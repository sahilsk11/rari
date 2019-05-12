---
id: stage1part1
title: Part 1 - Recognizing Llamas
sidebar_label: Recognizing Llamas
---

## Background
Using the newly attached camera on your car, you are now able to capture still images. Modern image recognition uses machine-learning to parse images, but it's too complicated to write these algorithms on our own yet. Instead, we're going to use a pre-made Google algorithm to parse the images for us.


# Parsing Llama Pics

![Llama time](./../../img/doc-images/stage-1/llama.jpg)

For this module, we're going to be working with our new friend, Ben.

The very first algorithms we will create will be to recognize whether a given image contains a llama or not. Once we do this, we can apply the same code to detect objects like stop signs!

## Step 0: What to Know

There are some key components I am going to assume you're familiar with:
1. [Using REST APIs](https://medium.freecodecamp.org/what-is-an-api-in-english-please-b880a3214a82)
2. [JSON notation](https://www.w3schools.com/whatis/whatis_json.asp)
3. The difference between a llama and a stop sign

If any of these feel unfamiliar, click on them to read more.

## Step 1: Sending Requests

To access Google's Vision API, we are going to use Python's requests library. This makes it very simple to access API's efficiently. Check it out:

`r = requests.get("test_url.projectcarbon.io", json=test_json)`

where `test_url` is the site for the API we are calling and `test_json` is a predefined JSON object with some arguments. Think of this like a method call: the URL specifies the method to run, and the arguments are the parameters. The `requests.get` runs the function that pulls the response from the server and stores it in the variable `r`.

Once this feels familiar, open up the starter code.

Start with line 8. Here, we are specifying the path to the image we want our API to parse.

Take a look at line 38:

`r = requests.post("https://vision.googleapis.com/v1/images:annotate?key=" + key, json=payload)`

Look familiar?

This line accesses the API and passes the JSON object above. Don't worry too much about the syntax of the JSON object - just make sure you are comfortable with the idea that you can pass certain arguments to the API by specifying parameters in the JSON object.

Once that feels good, hit run. Congratulations! You just made your first call to the Google Vision API

## Step 2: Parsing Responses

If everything worked correctly, the program should have printed a JSON object. This is the response from the server. I've printed a simplified version here:

```
{'responses': [{'labelAnnotations': [{
    'description': 'Mammal',
    'mid': '/m/04rky',
    'score': 0.9890478,
    'topicality': 0.9890478,
    }, {
    'description': 'Llama',
    'mid': '/m/04ldz',
    'score': 0.98694533,
    'topicality': 0.98694533,
    }]}]}
```
It printed a dict with a key "responses" that contains an array that contains a dict... that contains an array...

Yeah, that's a pretty long object. Fortunately, it's easy enough to look at it and figure out what it's telling us. We can see that the program returned two labels: one with description "Mammal" with an accuracy of 0.989, and one with description "Llama" with accuracy 0.986. If you want to see more results, try changing "maxResults" in the JSON arguments on line 31.

Now, we want to parse the results into an array to see what the API found in a clean way.

### To-Do: Write a for loop that adds all the descriptions into an array
Hint: 
`labels = response["responses"][0]["labelAnnotations"]`

Will add the array contained in `labelAnnotations` to an array called labels. Now, write a for loop that can traverse `labels` and pull the descriptions.

### Solution

```
labels = json_response["responses"][0]["labelAnnotations"]
descriptions = []
for individual_description in labels:
    descriptions.append(individual_description["description"])
print(descriptions)
```

Now that we have all of the descriptions in an array, we can create another for loop that traverses our descriptions array and searches for different objects.

### To-Do: Write another for loop that searches the descriptions array for the word "llama" (case insensitive)
hint: use the `.lower()` method to convert a string to lowercase.

### Solution

```
for tag in labels:
    if tag.lower() == "llama":
        print("We found Ben")
```

