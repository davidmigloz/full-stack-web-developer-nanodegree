from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC130c01770077cef69ef5bc6d8b9a8477"
auth_token  = "fcbc0a3c98c5790178fc32c912db832a"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Alba please?! I love you <3",
    to="+48530572694",    # Replace with your phone number
    from_="+48223073768") # Replace with your Twilio number
print message.sid
