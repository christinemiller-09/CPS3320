# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = account id from twilio
auth_token = specific token given by twilio
twilionumber = number goes here

def textmyself(message, phone):
	client = Client(account_sid, auth_token)
	for number in range(len(phone)):
		client.messages.create(
	   		body = message,
	    	from_= twilionumber,
	   	 	to = phone[number])