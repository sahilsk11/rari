---
id: stage1part1
title: Part 1 - Recognizing Llamas
sidebar_label: Recognizing Llamas
---

## Background
Using the newly attached camera on your car, you are now able to capture still images. Modern image recognition uses machine-learning to parse images, but it's too complicated to write these algorithms on our own yet. Instead, we're going to use a pre-made Google algorithm to parse the images for us.

Unfortunately, this is one of the longest modules of the project, but simply because we tried to simplify everything as much as possible. We recommend doing one part at a time!

# Parsing Llama Pics

![Llama time](./../../img/doc-images/stage-1/llama.jpg)

For this module, we're going to be working with our new friend, Ben.

The very first algorithms we will create will be to recognize whether a given image contains a llama or not. Once we do this, we can apply the same code to detect objects like stop signs!

## Step 1: HTML Requests and APIs

#### Note: APIs are among the most important topics in computer science today! Understanding them can help tremendously in securing an internship earlier!

Browsers and programs are always communicating information with each other. For example, your browser sent a request to Rari servers to pull this article and display it on your computer.

These interactions (between servers and websites) are done through *HTML requests*. Basically, the computer sends a request to a server, and the server responds with data.

We can use HTML requests to gain access to all kinds of data, beyond just web pages. To do this, we often take advantage of APIs, or application programming interfaces. Think of an API as a robot that is the bridge between you and the server. It is the API's job to simplify the data returned by the server into a format we can use.

For example, we can send an HTML request to an online weather API, and that API will respond with weather!

#### Note: don't get lost in terminology! Some of these terms may sound confusing, but will get cleared up as soon as you start using them!

![api](../../img/doc-images/stage-1/api.png)

In the APIs we will use, the format the data is returned in is called JSON (javascript object notation). Again, don't worry about terminology! Just know that JSON is a format that we can easily write programs to decode.

##### Remember JSON! Once again, this is one of key topics in modern computer science.

If this is still unclear, check out some of our other resources on APIs. If you kinda get the idea, keep going! This stuff is much easier understood once you do it.


## Step 2: Using Python's Request Library

Python has a library that makes HTML requests super easy. To make a request to an API, we can write:

`r = requests.get("sample.com")`

When we do this, the response from the API is stored in the variable `r` which we can easily decode.

### To-do: Try out Python's request library

Open `sample_request.py` from the starter code. Click run.

It will print some data about a user in JSON format. It's that simple!

## Step 3: Using Google Vision API

Google has a public API where they allow anyone to send a picture, and they will respond with the objects found in the picture. This API is called the Google Vision API.

Remember our friend Ben from the beginning of the module? We are going to use the picture of him as a sample. 

### To-do: Upload the image of Ben to the Google Vision API

Open up `finding_llamas.py` from the starter code.

This is a pretty long program, but at it's core, it is simply and API call. Let's break this down.

On line 23, we see a large chunk of code. This defines some parameters that the Google Vision API needs to work. Don't worry about this now!

On line 27 we see the core of the program. This makes the request to the Google server, and it responds with data about the image we uploaded.

If you try running the program, you can see it prints some JSON data about what the Google API found.


## Step 4: Parsing Responses

If everything worked correctly, the program should have printed the following:

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

Parsing JSON objects in Python is extremely simple. However, since it isn't important to the course, we leave it up to you to learn. For now, we give you the method to pull the objects from the JSON object.

Uncomment line 23 to try it.

##### Note: to change the number of objects recognized, change the `max_results` variable on line 11.


## To-Do: Write a script that will determine if the image has a llama

Now that we have all of the recognized objects in an array, write a for loop that will iterate through all of the labels and determine if the image contains a llama.

#### Hint: find out if the word "llama" is in the list called `responses`

### Solution

```
for i in range(0, len(responses))
    if responses[i] == "llama":
        print("We found Ben")
```

Phew, that was a long module. But now, you are capable of using APIs and requests to find data, and can utilize the Google Vision API to determine a list of objects found in an image. 

This is a tricky module! If any of it is confusing, reach out. It gets easier from here (sorta)!

Onwards!