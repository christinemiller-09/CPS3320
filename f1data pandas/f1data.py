import pandas as pd
import random

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
#add all the necessary csv files related to f1 racing
data = pd.read_csv('drivers.csv',usecols = ['driverId','code','forename','surname'])
drivers = pd.read_csv('driver_standings.csv', usecols = ['driverStandingsId','raceId','driverId'])
results = pd.read_csv('results.csv', usecols = ['raceId', 'driverId', 'fastestLapTime'])
qualifying = pd.read_csv('qualifying.csv', usecols = ['raceId', 'driverId' ,'q1','q2','q3'])


merge = pd.merge(data,drivers, how = 'outer')
table = pd.merge(merge,results, how ='outer')
#merge the files into 1 data frame
df = pd.merge(merge,table)
df = pd.DataFrame(df)

# checks if both samples are same person
def playerPicker(df1,df2):
	if (df1.equals(df2)) == True:
	 		#change one of the samples
	 		df2new = small_sample.sample()
	 		sample1 = pd.merge(df1,df2new, how= "outer")
	 		print(sample1[['driverId','forename','surname']].to_string(index = False))
	 		return sample1['driverId'].tolist

	 		if(df2.equals(df2new)):
	 			#if matched again so a new sample will be randomized
	 			df3 = small_sample.sample()
	 			sample2 = pd.merge(df1,df3)
	 			print(sample2[['driverId','forename','surname']].to_string(index =False))
	 			return sample2['driverId'].tolist()

	elif (df1.equals(df2)) == False:
			sample = pd.merge(df1,df2, how = "outer")
			print(sample[['driverId','forename','surname']].to_string(index = False))
			return sample['driverId'].tolist()

		
if __name__ == "__main__":	
	print("Welcome to the simulation F1 race! How many races do you want to play?")
	races = int(input())
	round = 1
	w = 0
	l = 0
	while races != 0:
		print("Lap",round)
		#since the sample is so large for less redunancy from large list took smaller sample 
		small_sample = df.sample(100)
		df = pd.DataFrame(df)
		df1 = small_sample.sample()
		df2 = small_sample.sample()
		# subtracting the race
		races = races - 1
		#call function to get check if sample is duplicate
		choice = playerPicker(df1,df2)
		round = round + 1
		print("Who will win in the race? Please enter driverId number.")
		#user input of races
		win = int(input())
		# random winner
		choice = random.choice(choice)
		#who wins the race
		if win == choice :
			w = w + 1
		else:
			l = l + 1
		print("Wins",w, "Loses",l)
	# final score tally	
	if w > l:
		print("You are a winner!")
	else:
		print("You lost!")	
	