# create a function that gives each letter a specific score
# create another function that calculates the score of an entire word
letterOrWord = input("Enter a letter or word to find it's point value:")
letterOrWord = letterOrWord.lower()
score = 0
total = 0

def letterScore(letterOrWord):
	if letterOrWord in 'aeilnorstu':
		return 1
	elif letterOrWord in 'dg':
		return 2
	elif letterOrWord in 'bcmp':
		return 3	
	elif letterOrWord in "fhvwy":
		return 4
	elif letterOrWord in 'k':
		return 5
	elif letterOrWord in 'jx':
		return 8
	elif letterOrWord in 'qz':
		return 10
	else:
		return 0

def wordScore(letterOrWord):
	i = 0
	num = 0
	n = 0
	letterOrWord = list(letterOrWord)
	while i < len(letterOrWord):
		n = letterScore(letterOrWord[i])
		num+=n
		i+=1
	return num
	
if len(letterOrWord) == 1:
	score = letterScore(letterOrWord)
	print(" The letter " + letterOrWord + " is worth ", score , " point(s).")
else :
	total = wordScore(letterOrWord)
	print(" The word " + letterOrWord + " is worth ", total , " point(s).")
