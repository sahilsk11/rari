## Understanding APIs
APIs, or an Application Programming Interface, is a fancy term for software that allows programs to communicate with each other. Typically, a user will call an API from their program that sends a request to a server somewhere. That server will parse the message and send an appropriate response, usually in a format called JSON (we'll come back to this). The API simply handles the requests and sends the response.

For most of the APIs used in Rari (and everywhere else), the server responds in _JSON_ or Javascript Object Notation. It sounds fancy, but it just follows this format:

`{"key":"value"}`

Each JSON object has curly braces, and the inside contains one or more key. Each key corresponds to a value, which can be one of the following:
1. A String
2. A number (int)
3. A list (array)
4. Another JSON object

Here's another sample JSON object

`{"sample_json":"hello world!","woah_another!":[1, 2, 3],"you_can_nest?":{"nested_json":"here's the value"}}`

If you're interested in learning more about JSON, I recommend reading more online. This is one of the most important skills to learn for internships!
* * *


#### Warning: 
At this point, I recommend pausing and making sure the concepts of API calls and JSON make sense. If this is your first time using these, I recommend starting off with another API. The Google Vision API is a bit tricky to start with for beginners, but if you're confident, then let's go!

## Step 2: Setting up the Google Vision API
As I said earlier, we're handing off all our images a Google server to parse and tell us what is in our images. Getting started with the API can be a bit tricky, but I've simplified the process a bit to get started.

#### Step 2a. Go to the [Google Vision API Website](https://cloud.google.com/vision/)
I recommend taking a random image on your laptop and uploading it to the "Try the API" section. This gives you a bit of an idea on what kind of data we are processing. Play around with it!

#### Step 2b. Using the starter code

Since configuring your own Google account API can be a little tricky, I've configured the starter code to include everything already.