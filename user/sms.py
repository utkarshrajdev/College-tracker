# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def sendsms(message,numbers) :
    account_sid = 'AC32e7a862a03bd60e140423339b71b27d'
    auth_token = '50734d971b63a79e20c81432339c035a'
    client = Client(account_sid, auth_token)
    for number in numbers :
        try : 
            message = client.messages \
                            .create(
                                body=message,
                                from_='+14179628324',
                                to="+91"+number
                            )
        except :
            message = client.messages \
                            .create(
                                body=message,
                                from_='+14179628324',
                                to="+91"+number
                            )
        print(message.sid)
