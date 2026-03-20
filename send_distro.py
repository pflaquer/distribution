import os, requests, json

# 1. Auth with MS Graph
token_url = f"https://login.microsoftonline.com{os.environ['TENANT_ID']}/oauth2/v2.0/token"
res = requests.post(token_url, data={
    'client_id': os.environ['CLIENT_ID'],
    'client_secret': os.environ['CLIENT_SECRET'],
    'grant_type': 'client_credentials',
    'scope': 'https://graph.microsoft.com'
})
token = res.json().get('access_token')

# 2. Send Distribution Email
payload = json.loads(os.environ['ECN_DATA'])
email_body = {
    "message": {
        "subject": f"ECN Released: {payload['subject']}",
        "body": {"contentType": "Text", "content": "The ECN has been fully signed."},
        "toRecipients": [{"emailAddress": {"address": "eng-distro@company.com"}}]
    }
}
requests.post("https://graph.microsoft.com", 
              headers={'Authorization': f'Bearer {token}'}, json=email_body)
