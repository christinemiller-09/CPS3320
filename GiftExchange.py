#ask user how many people will be particiapting in gift exchange
#then ask for their first names and add it to a list
#randomly assign one person to another they cannot gift themsleves and no repeat
# finally have the list displyed lettering them know who is giving to whem in the gift exchange
import random
numPeople = int(input("How many people are gift exchanging? "))
givers =[]
recivers = []
#funtion to check the count that 1 giver and 1 reciver name only on the list
def doubleCheck(numPeople):
	for n in range(numPeople):
		if givers.count(givers[n]) > 1:
			givers.append(input("You entered "+ givers[n]+" name twice, enter new name."))
			givers.remove(givers[n])
		elif recivers.count(recivers[n])>1:
			recivers.remove(recivers[n])
			random.sample(givers,numPeople)


print("Please enter their names: ")
for i in range(numPeople):
	givers.append(input(" "))

for j in range(numPeople):
	recivers = random.sample(givers,numPeople)

once_over = True
while once_over :
	for l in range(numPeople):
		if givers[l] == recivers[l]:
			recivers = random.sample(givers,numPeople)
			once_over = True
# check to make sure giver isn't gifting themselves
	for m in range(numPeople):
		if not givers[m] == recivers[m]:
				once_over = False
	doubleCheck(numPeople)

print()
print("Gift Assignments..")
for k in range(numPeople):
	print(givers[k], " will buy a gift for ", recivers[k])
print()