from graphics import*
from PIL import Image
import pyglet
# path location on of both alaphabet and number folder
# change based on Users/name/foldername/
path = '/Users/cmiller/Python/'

# dictionary for letters with associated picture by using google search
letters ={'a':'alphabet/A.png', 'b': 'alphabet/B.png',
		 'c': 'alphabet/C.png', 'd': 'alphabet/D.png',
		 'e': 'alphabet/E.png', 'f': 'alphabet/F.png',
		 'g': 'alphabet/G.png', 'h': 'alphabet/H.png', 
		 'i': 'alphabet/I.png', 'j': 'alphabet/J.png', 
		 'k': 'alphabet/K.png', 'l': 'alphabet/L.png', 
		 'm': 'alphabet/M.png', 'n': 'alphabet/N.png', 
		 'o': 'alphabet/O.png','p': 'alphabet/P.png', 
		 'q': 'alphabet/Q.png', 'r': 'alphabet/R.png',
		 's': 'alphabet/S.png', 't': 'alphabet/T.png', 
		 'u': 'alphabet/U.png','v': 'alphabet/V.png', 
		 'w': 'alphabet/w.png', 'x':'alphabet/X.png',
		 'y': 'alphabet/Y.png','z': 'alphabet/Z.png'}
		 
# dictionary for numbers 1 to 10 with pictures associated from google
number = {'1':"numbers/1.png",'2':"numbers/2.png",
		  '3':"numbers/3.png",'4':"numbers/4.png",
		  '5':"numbers/5.png",'6':"numbers/6.png",
	      '7':"numbers/7.png",'8':"numbers/8.png",
	      '9':"numbers/9.png",'10':"numbers/10.png"}

# this function to turn the set of letters and numbers based on user input into a loop creating the gif
def gifMaker(img):
	images = []
	images.append(img)  
	images[0].save('test.gif',
        save_all=True,
        append_images=images[1:],
        duration=5000,
        loop=0)

# function related to searching for the number to display based on input
def checkNum (number, key):
	n = split(key)
	i = 0
	size = (500,500)
	images = []
	if len(n) == 1:
			img = Image.open((path+number[key]))
			img = img.resize(size)
			gifMaker(img)
	elif len(n) == 2 and key == '10':
		if key in number.keys():
			img = Image.open((path+number[key]))
			img = img.resize(size)
			gifMaker(img)
	else:
		while i < len(key):
			if n[i] in number.keys():
				img = Image.open((path+ number[n[i]]))
				img = img.resize(size)
				images.append(img)
			images[0].save('test.gif',
             save_all=True,
             append_images=images[1:],
             duration=4000,
             loop=0)
			i=i+1
# splits the word into letters for the key to find in the dictionary
def split(word):
	return [char for char in word]

# function for the letters to be displayed based on input
def checkWord(letters,word):
	i = 0
	w = split(word)
	n = 0
	size = (500,500)
	images =[ ]
			# checkKey(letters, w[i])
	if len(w) == 1:
		if word in letters.keys():
	# Read image 
			img = Image.open((path+letters[word]))  
			img = img.resize(size)
			gifMaker(img)
	else:
		while i < len(word):		
			if w[i] in letters.keys():
				img = Image.open((path+letters[w[i]]))
				img = img.resize(size)
				images.append(img)
			images[0].save('test.gif',
	             save_all=True,
	             append_images=images[1:],
	             duration=5000,
	             loop=0)
			i=i+1

# this function displays the created gif frames in a new window to animate the created gif
def animategif(word):
	animation = pyglet.image.load_animation('test.gif')
	animSprite = pyglet.sprite.Sprite(animation)
	w = animSprite.width
	h = animSprite.height
	window = pyglet.window.Window(width=w, height=h)
	r,g,b,alpha = 0.5,0.5,0.8,0.5
	pyglet.gl.glClearColor(r,g,b,alpha)

	@window.event
	def on_draw():
	    window.clear()
	    window.set_caption(word)
	    animSprite.draw()


	pyglet.app.run()

# user input function to generate the gif by the response 
def user_input(response):
	if response == "w":
		word = input("Enter the word you would like to learn/translate in sign.")
		checkWord(letters,word)
		animategif(word)
		
	elif response == "n":
		num = input("Enter a number that you would like to learn or translate in sign.")
		checkNum(number,num)
		animategif(num)

	else:
		print(input("You did not enter the proper response. American Sign Langague learnin program is ending..."))

if __name__ =="__main__":
	response = input("Do you want to learn a word/letter or a number. Please repond with w (word/letter) or n (number).")	
	sign = True
	while sign == True:
		user_input(response)

		answer = input("Do you want you want to learn more? y (yes)/n(no)?")
		if answer =='y':
			response = input("Would you like to learn another w (word/letter) or n (number)? ")
			
		elif answer =='n':
			print("American Sign Language learning program is ending...")
			sign = False