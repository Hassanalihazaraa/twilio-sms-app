from twilio.rest import Client
from credientials import account_sid, auth_token, my_number, my_twilio

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hi, It is my first twilio message",
    from_=my_twilio,
    to=my_number
)

print(message.sid)
