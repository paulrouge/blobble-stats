#  function that creates a rpc request to be sent to the server with requests
def rpcMaker(address, method, params):
    return {
        "jsonrpc": "2.0",
        "method": "icx_call",
        "id": 1234,
        "params": {
            "from": "hx" + 40 * "0",
            "to": address,
            "dataType": "call",
            "data": {
                "method": method,
                "params": params
            }
        }
    }