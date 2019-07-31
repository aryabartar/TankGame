import requests
import json

url = "https://api.sendinblue.com/v3/smtp/email"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'api-key': "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"
}


def reset_password(send_to, name, resetlink):
    payload = {
        "params": {"name": name, "resetlink": resetlink},
        "sender": {"name": "sNeeds", "email": 'noreply.sneeds@gmail.com'},
        "to": [{"email": send_to}],
        "replyTo": {'email': 'noreply.sneeds@gmail.com'},
        "templateId": 5,
    }
    json_data = json.dumps(payload)
    response = requests.request("POST", url, data=json_data, headers=headers)
    return response.text
