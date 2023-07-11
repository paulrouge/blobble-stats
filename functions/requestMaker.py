import requests, json
from functions.rpcMaker import rpcMaker
from config import config

# function that creates a request to be sent to the server with requests
def requestMaker(address, method, params):
    url = config.URL_ENDPOINT
    payload = json.dumps(rpcMaker(address, method, params))

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


