import requests


def sendMessage(message):

    url = 'http://localhost:5005/webhooks/rest/webhook'
    data = '''{
      "sender": "Rasa2",
      "message": "'''+message+''''"
    }'''

    return requests.post(url, data=data)
