import adal
import requests
import json

tenant = "" #your tenant id /
client_id = "" #your client id /
client_secret = "" #your client secret /

authority = "https://login.microsoftonline.com/" + tenant
RESOURCE = "https://graph.microsoft.com"

context = adal.AuthenticationContext(authority)
token = context.acquire_token_with_client_credentials(
   RESOURCE,
   client_id,
   client_secret
   )

access_token = token['accessToken']
def send_post_request(url, payload):
    headers = {"Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"}
    payload = {
        "activityGroupNames": ["Malicious URLs"],
        "confidence": 8,
        "description": "Malicious URL Indicator",
        "expirationDateTime": "2023-12-31T23:59:59Z",
        "killChain": None,
        "lastReportedDateTime": None,
        "tags": ["Malicious"],
        "targetProduct": "Microsoft Defender ATP",
        "threatType": "URL",
        "tlpLevel": "green",
        "url": line,
        "Ti Action": "Block",
        "Action": "Block"
    }

    response = requests.post(url, json=payload, headers=headers)
    # Process the response
    if response.status_code == 200 or 201:
        print(f"Success: {json.dumps(payload)},{response.text}, {response.status_code}")
    else:
        print(f"Failed: {json.dumps(payload)}, {response.text}, {response.status_code}")

# Open the text file
with open('urls.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()
    # Send POST requests for each line
    for line in lines:
        # Construct the JSON payload
        payload = {'url': line.strip()}
        # Specify the URL to send the request to
        url = "https://graph.microsoft.com/beta/security/tiIndicators"
        # Send the POST request with the JSON payload
        send_post_request(url, payload)
