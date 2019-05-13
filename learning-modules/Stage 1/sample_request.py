import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
# this url points to an API that returns some random data about a user

r = requests.get(url)

json = r.json() #decodes r into a JSON object that we can understand

print(json)