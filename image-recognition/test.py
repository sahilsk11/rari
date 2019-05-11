import base64

with open("stopsign.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
print(str(encoded_string)[2:-1])