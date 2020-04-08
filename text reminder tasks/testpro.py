from twilio.rest import Client
import datetime
import textmyself

#dictionary for the resident information, but in this case it is hardcoded and they are ficticious
residents = {"Garry Johnson" :{"street":"Green Lane", "phone":"+19082451550","ward":2},
			"Donlad Dolley":{"street": "Green Lane", "phone":"+19086697980", "ward": 2},
			"John Sweeney": {"street":"West 5th ave.", "phone":"+19082537450", "ward": 4},
			 "Steven Spiel":{"street":"West 5th ave.", "phone":"+19087654321","ward": 4},
			"Mario Pearson":{"street":"Chandler ave." ,"phone":"+19084160537", "ward": 5},
			 "Mary Smith":{"street":"East 3rd ave.","phone":"+19085509073", "ward": 3},
			"Stan Lee": {"street": "Locust St.","phone":"+19081435678", "ward": 1},
			"Haley Smith":{"street":"East 3rd ave.","phone":"+19082451846","ward": 3},
			 "Anthony Lopez":{"street":"Locust St.","phone":"+19085902953","ward": 1},
			 "Christine Milesr":{"street":"Pine St.", "phone":"+19085900573", "ward": 5}}

westside = "Green Lane", "West 5th ave."
eastside = "Locust St.", "East 3rd ave.", "Pine St.", "Chandler ave."
message ="Tomorrow is recycling remmeber to take out bottles and cans, place it on the curb for pickup"
garMessage = "Tomorrow is garbage, rememeber to take out your trash and place it on the curb."
left = "Alternate side parking, Please park on left side today."
right = "Alternate side parking, Please park on right side today."

#list for the set of phone numbers there needs to be three separate lists for each function
#in order to prevent duplicating messages
phone = []
phonenum = []
cellphone =[]
# function for garbage day message
def garbage():
	for i in residents:
		if residents[i].get('street') in eastside:
			if day == "Sunday" or day =="Wednesday":
				phone.append(residents[i].get('phone'))
		elif residents[i].get('street') in westside:
			if day == "Monday" or day == "Thursday":
				phone.append(residents[i].get('phone'))
	return phone
# function for recycling day message
def recycle():
	for i in residents:
		if 1 == residents[i].get('ward') and day == "Thursday":
			phonenum.append(residents[i].get('phone'))
		elif 2 == residents[i].get('ward') and day == "Wednesday":
			phonenum.append(residents[i].get('phone'))
		elif 3 == residents[i].get('ward') and day == "Tuesday":
			phonenum.append(residents[i].get('phone'))
		elif 4 == residents[i].get('ward') and day == "Monday":
			phonenum.append(residents[i].get('phone'))
		elif 5 == residents[i].get('ward') and day == "Sunday":
			phonenum.append(residents[i].get('phone'))	
	return phonenum
# function for alternate parking based on east or west side
def alternateparking():
	for i in residents:
		if residents[i].get('street') in eastside:
			if day == "Wednesday": 
				cellphone.append(residents[i].get('phone'))
			elif day == "Thursday":
				cellphone.append(residents[i].get('phone'))
		elif residents[i].get('street') in westside:
			if day == "Tuesday":
				cellphone.append(residents[i].get('phone'))
			elif day == "Friday":
				cellphone.append(residents[i].get('phone'))
	return cellphone

#this is to get the current day of the week to know which messages to send
day = datetime.datetime.now()
#this is to specify the day of the week 
day = day.strftime("%A")

# call function to return list that will send the text about garbage day
garbage()
if day != "Saturday":
	if day == "Monday" or day == "Thursday":
		textmyself.textmyself(garMessage,phone)
	elif day == "Sunday" or day == "Wednesday":
		textmyself.textmyself(garMessage,phone)

# call function to return list to send the text about recyling
recycle()
if day != "Saturday":
	if day != "Friday":
		textmyself.textmyself(message,phonenum)

#call function to return list of numbers to send the text about alternate side parking reminder
alternateparking()
if day != "Saturday":
	if day != "Monday" and day != "Thursday":
		if day == "Wednesday" or day =="Tuesday":
			textmyself.textmyself(left,cellphone)
		elif day == "Thursday" or day == "Friday":
			textmyself.textmyself(right,cellphone)


#this is for custom messages, ideally for emergency updates, accidents, crime, town meetings/events
resphone = []
question =input("What is the custom message?")
yn = input("Is that message correct? Are you sure you want to send? Respond y (yes) or n (no).")
if yn =="y":
	for i in residents:
		resphone.append(residents[i].get('phone'))
		textmyself.textmyself(question,resphone)
else:
	print("You responded no.")


