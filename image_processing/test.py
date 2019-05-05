import base64

f = open("stopsign.png", "rb")
image_content = f.read()
str = str(base64.b64encode(image_content))
print(str[2:])
