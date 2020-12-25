import requests

url = 'http://127.0.0.1:8000/api/books/'

print(requests.get(url).content)