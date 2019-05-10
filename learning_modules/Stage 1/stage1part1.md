# Welcome to Stage 1

This will be one of the easier modules of the project, hence it is first. Keep in mind that in this learning module, we will be prioritizing simplicity over efficiency! The program will be very slow and laggy, but establishing a strong understanding in this segment will help you a lot in future modules.
Additionally, understanding REST APIs is an invaluable skill in your programming career. I can almost guarantee your first internship will involve them.

### Background
Using the newly attached camera on your car, you are now able to capture still images. Processing these images using our own algorithms as an extremely complex process involving machine learning that we will visit in future models.

For now, we are going to hand off all our images to Google and have their algorithms parse our data and return what they find. All clear? Let's move on.


## Part 1: Parsing Llama Pics

![Llama time](/img/doc-images/stage-1/llama.jpg)

For this module, we're going to be working with our new friend, Ben.

As we said earlier, image processing can get pretty complex and writing our own scripts to do so involved machine learning. For this introductory module, we are going to use the Google Vision API to parse our images and tell us what's in them.

Once we do this, we can have our car analyze surroundings in real-time, and detect objects like stop signs or llamas on the road.

This may all sound complicated, but this is where the magic of the Google Vision API will come into play. Let's jump in.

## Step 0: What to Know

There are some key components I am going to assume you're familar with:
1. Using REST APIs
2. JSON notation
3. The difference between a llama and a stop sign

If any of these feel unfamiliar, I recommend going back and exploring some of the other topics I've published.

## Step 1: Sending Requests

To access Google's Vision API, we are going to use Python's requests library. This makes it very simple to access API's efficiently. Check it out:

`r = requests.get("test_url.projectcarbon.io", json=test_json)`

where `test_url` is the site for the API we are calling and `test_json` is a predefined JSON object with some arguments. Think of this like a method call: the URL specifies the method to run, and the arguments are the parameters. The `requests.get` runs the function that pulls the response from the server and stores it in the variable `r`.

Once this feels familiar, open up the starter code.

Start with line 8. Here, we are specifying the path to the image we want our API to parse.

Take a look at line 38:

![Line 38](/img/doc-images/stage-1/38.png)

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

## Step 3: Recognizing Stop Signs
Now that we have written a script to use the Google Vision API to parse an image and determine what it's contents are, we can extend this code to recogize any object we want!

Since we don't care about llamas anymore let's adapt the code to parse an image of a stop sign.

Change line 9 to:

`image_path = "images/stopsign.txt"`

This will now upload a picture of a stop sign.

### To-Do: Modify the code to find a stop sign instead of a llama
hint: when searching in your labels array, change the word "llama" to "stop sign"

### Solution
Change the word "llama" to stop sign and change the print statement!

* * *
### Congratulations!
If you did everything correctly, you have now successfully written and algorithm that can parse any image and check if the image contains an object. In our case, we are going to continue with the stop sign example, and now modify our car to stop moving if the camera sees a stop sign.