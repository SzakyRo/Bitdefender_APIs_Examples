import base64
import requests
import json

api_key = "your_api_key"
login_string = api_key + ":"
encoded_bytes = base64.b64encode(login_string.encode())
encoded_user_pass_sequence = str(encoded_bytes, 'utf-8')
authorization_header = "Basic " + encoded_user_pass_sequence

api_endpoint_url = "https://cloud.gravityzone.bitdefender.com/api/v1.0/jsonrpc/network"

request_data = {
    "params": {
        "parentId": "23b19c39b1a43d89367b32ce", #change this with your own Company ID
        "page": 1,
        "perPage": 100,
        "filters": {
            "type": {
                "companies": True,
                "computers": True
            },
            "depth": {
                "allItemsRecursively": True
            }
        },
        "options": {
            "companies": {
                "returnAllProducts": True
            },
            "endpoints": {
                "returnProductOutdated": True,
                "includeScanLogs": True
            }
        }
    },
    "jsonrpc": "2.0",
    "method": "getNetworkInventoryItems",
    "id": "301f7b05-ec02-481b-9ed6-c07b97de2b7b"
}

try:
    result = requests.post(api_endpoint_url, json=request_data, verify=True, headers={"Content-Type": "application/json", "Authorization": authorization_header})
    response = result.json()
    print(json.dumps(response, indent=4))
except Exception as e:
    print(f"An error occurred: {str(e)}")