from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "sid"
# Your Auth Token from twilio.com/console
auth_token  = "token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+number", 
    from_="+34955160731",
    body="Hola Putxi Putxi! Eres tan Putxi!")

print(message.sid)