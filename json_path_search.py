import json
# Takes in a path from raw input in the form: Level.sublevel.subsublevel
# and returns whether an element exists at that path
# Author: Pranav Harathi
# Date: 06-22-16

"""
path = raw_input("Enter the path you want to search: ");
#path = "Organization.Linkage.ShareOwner.ShareHoldingPercentage"
path = path.strip();
path_points = path.split(".");
"""

filename_paths = raw_input("Enter the name of the file containing the paths on separate lines (and nothing else): ")
paths = [line.strip() for line in open(filename_paths)]

# reads in json to search from a file
filename = raw_input("Enter the name of the file containing the JSON: ");
#filename = "jsontest2.json"
jsonfile = open(filename, "r");
jsonstring = jsonfile.read().strip();

# converts string to json
json = json.loads(jsonstring);

starting_path = ""
path_confirm = True
# Confirm starting path
while path_confirm:
	starting_path_q = raw_input("Is your starting path \"OrderProductResponse.OrderProductResponseDetail.Product\"? (y/n)  ")
	if(starting_path_q == "y" or starting_path_q == "Y"):
		print "Analyzing data..."
		print ""
		break
	elif(starting_path_q == "n" or starting_path_q == "N"):
		while path_confirm:
			starting_path = raw_input("Enter your starting path: (Level.sublevel.subsublevel...)  ")
			while True:
				confirmation = raw_input("Is this correct? " + starting_path + " (y/n)  ")
				if(confirmation == "y" or confirmation == "Y"):
					print "Analyzing data..."
					print ""
					path_confirm = False
					break
				elif(confirmation == "n" or confirmation == "N"):
					break
				else:
					print "Invalid input"
	else:
		print "Invalid input"

if(starting_path == ""):
	starting_path = "OrderProductResponse.OrderProductResponseDetail.Product"

def check_path_exists(path):
	path = path.strip();
	path_points = path.split(".");

	# starting path to json path
	current = json
	for startpathpoint in starting_path.split("."):
		current = current[startpathpoint]

	# checks if path exists
	success = True
	#current = json["OrderProductResponse"]["OrderProductResponseDetail"]["Product"]
	for point in path_points:
		#print point
		if type(current) is list:        # if it is a list, iterate until the next json object is found
			#print current
			check = None    # reference for next current
			for element in current:
				if(point in element):   # if point is in element, then we stop
					check = element[point]
					break
			if(check is None):    #this is true if we iterated and none of the elements had it
				success = False
				break
			else:
				current = check  	
				continue
		else:
			#print "not a list"
			if(point in current):
				current = current[point]
			else:
				success = False
				break

	if(success):
		print "Path found!"
	else:
		print "Not found :("

for path in paths:
	check_path_exists(path)


