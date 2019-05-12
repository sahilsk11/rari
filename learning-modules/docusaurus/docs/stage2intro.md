---
id: stage2
title: Welcome to Stage 2!
sidebar_label: Stage 2
---

By now, you have a vehicle that moves until it sees an image of a stop sign, and automatically stops.

#### However, as you have probably noticed. It's slow AF.

To be honest, I would be surprised in most cases if your car is able to stop before running into your stop sign.

We're going to fix that by exploring ways to streamline our algorithm.

As you may recall, here is everything going on in real-time:

1. The car takes an image as it moves (~3 sec)
2. The image is encoded into a String (~0.2 sec)
3. The new encoded image is uploaded to Google Vision API (~1 sec)
4. All of the results are searched through to find matching objects (< 1 sec)
5. We call the `esc` library to stop the vehicle if a stop sign is found

This process is extremely inefficient, and as you can see, is very slow. Let's jump into streamlining this process.

## Next Steps

In Stage 2, we introduce machine learning principles that will run on the car itself.

In our previous examples, we had to call Google's API to recognize images. However, the process of sending requests over WiFi to another server is too time consuming to do efficiently in real-time. In the following modules, we are going to learn how to do image recognition locally and faster than the Google API.

This project is about to get real. Strap in.

![takeoff](./../../img/doc-images/stage-2/original.gif)