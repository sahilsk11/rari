---
id: stage1part2
title: Part 2 - Recognizing Stop Signs
sidebar_label: Recognizing Stop Signs
---
Now that we can recognize llamas, it's time to recognize stop signs as well.

## Step 1: Recognizing Stop Signs
Now that we have written a script to use the Google Vision API to parse an image and determine what it's contents are, we can extend this code to recogize any object we want!

Since we don't care about llamas anymore let's adapt the code to parse an image of a stop sign.

Change line 9 to:

`image_path = "images/stopsign.png"`

This will now upload a picture of a stop sign.

### To-Do: Modify the code to find a stop sign instead of a llama
hint: when searching in your labels array, change the word "llama" to "stop sign"

### Solution
Change the word "llama" to stop sign and change the print statement.