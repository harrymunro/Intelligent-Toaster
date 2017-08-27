# Smart Toast
# Simplified in version 2 to only factor in toasting time

# Simulates the intelligent toaster

import random
import os.path
import numpy as np
import csv
from sklearn import linear_model

# Time of toasting


# User name
user = "Harry"

# Every time the toast is finished the user tells the toaster whether the toast was under-done, over-done or just right
# This data, along with the toast time and bread width is saved into the database along along with the users name
# A ML algorithm uses the database to determine the optimal toasting time for the given parameters in order to achieve "just-right" toast
# This means that we have a toaster that learns from user preferences

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

while True:
	toast_time = random.randint(30, 300)
	# Check whether CSV data file exists and read it, if not then create a default dataframe
	file_exists = os.path.isfile("toast2.csv") # returns True if file exists
	
	if file_exists == True and file_len('toast2.csv') > 5:
		with open('toast2.csv', 'rb') as csvfile:
			data = csv.reader(csvfile, delimiter=' ', quotechar='|')
			csvfile.close()
		# create input array
		first = np.loadtxt('toast2.csv', skiprows = 1, usecols = (2,))
		first = first.reshape(-1, 1)
		# create predictor array
		second = np.loadtxt('toast2.csv', skiprows = 1, usecols = (1,))
		second = second.reshape(-1, 1)
		
		blr = linear_model.LinearRegression()
		clf = blr.fit(first, second)
		toast_time = int(clf.predict(2))
	
	elif file_exists == False:
		with open('toast2.csv', 'a') as csvfile:
			data = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			data.writerow(['User', 'Toast_Time', 'Satisfaction'])
			csvfile.close()

	raw_input("\nPress enter to start toasting!")
	
	print "\nToasted bread for %d seconds." % toast_time
	
	x = True 
	while x == True:
		satisfaction = int(raw_input("\nHow was your toast?\n0.Vastly under-toasted\n1.Slightly under-toasted\n2.Just right\n3.Slightly burnt\n4.Badly burnt\nEnter the number and press enter: "))
		if satisfaction in (0, 1, 2, 3, 4):
			x = False
		else:
			print "That wasn't a correct option, please choose again.\n"
			
	x = True		
	
	with open('toast2.csv', 'a') as csvfile:
		data = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		data.writerow([user, toast_time, satisfaction])
		csvfile.close()
    		
	with open('toast2.csv', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			print row
		f.close()
