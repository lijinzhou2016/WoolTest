import requests


def get():
    return requests.get("http://118.24.52.95:5010/get").text