from django.test import TestCase

# Create your tests here.

import requests

url = "http://127.0.0.1/sentiment/"
#url = "http://localhost/sentiment/"

post_data = {"text": "I don't like this movie."}

def analysis(url, post_data):
    # Post the request and retrieve the response
    x = requests.get(url, params=post_data)

    return x.text

# Stress test the server with duplicated requests
for i in range(100):
    print(f"Request {i}: {analysis(url, post_data)}")