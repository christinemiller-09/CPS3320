import nltk
from nltk.chat.util import Chat,reflections
#(.*) for getting a specific response 
# %1 %2  use it in chatbot response

pairs = [
	[r"My name is (.*)", ["Hello %1, I am your vacation helper chatbot. If at any point you want to end this conversation respond quit. Do you want to go on vacation?"],],

	[r"yes", ["Well do you have money saved? Please respond with i do i have .. or i do not.."], ],

		[r"i do i have (.*)", ["Do you think %1 is enough? Please respond i think or i don't think so.."],],
	
		[r"i do not", ["Then I suggest we end this conversation and you go to work."],],
	
			[r"i think",["Well are you thinking of in this country or out of the country? Please respond i will be traveling.." ],],

			[r"i don't think so",["Well then start saving. Go to work."],],

				[r"i will be traveling in this country", ["What form of transportation will you use car, train, or plane? "],],
	
					[r"car", ["Roadtripping it huh, What where will you be going to? Please respond i will be going to ..."],],
	
						[r"i will be going to (.*)", ["Well %1 is nice, I suggest you have a long playlist, bring a friend, and lots of snacks. Bye!"],],
	
					[r'train', ["Oh man a train, like the Hogwarts Express? Where will you be taking a train to? Please respond i will be taking a train to .."],],
	
						[r"i will be taking a train to (.*)",[" %1 thats nice. I suggest you bring some entertainment maybe books or movies. Bye!"],],
	
					[r"plane", ["Where will you be going to on this plane ride? Please respond my plane trip will be taking me to .."],],

						[r"my plane trip will be taking me to (.*)",["%1 must be nice. I dont get to leave this state that I am in. Well seems like you should start to book your trip. Bye!"],],

				[r"i will be traveling out of the country",["Out of the country thats nice. Do you have a valid passport? Please respond it is valid or i'm not sure."],],

						[r"it is valid",["That's good to know, now what country were you thinking. Please respond with i was thinking "],],
	
	[r"i was thinking (.*)", ["Must be nice in the %1. I don't get to travel much these days. How long will you be away for? Please respond about # weeks"],],

			[r"about (.*) weeks", ["Wow, %1 weeks you have a lot of time. I don't get any days off. Well seems like you know what to do next. Book your trip."],],

	[r"i'm not sure", ["Well I suggest you stop talking to me and find out before continuing. Bye. "],],
	
	[r"no", ["Well then I suggest you go to work. Bye!"],],

	[r"bye", ["Take care."],],
	
		[r"(.*)", ["I do not know that %1. Please try again or quit."],]
	]

def vacayBot():
	print("Hello, what is your name? Please answer starting with my name is...")
	chat = Chat(pairs,reflections)
	chat.converse()


if __name__ == "__main__":
	vacayBot()
