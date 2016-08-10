import json
# Takes in a path from raw input in the form: Level.sublevel.subsublevel
# and returns whether an element exists at that path
# Author: Pranav Harathi
# Date: 06-22-16

path_search_type = raw_input("Search by path or with multiple paths? (path/paths): ");
if(path_search_type == "path"): 
        path = raw_input("Enter the path you want to search: ");
        paths = [path]
elif(path_search_type == "pathset"):
        filename_paths = raw_input("Enter the name of the file containing the paths on separate lines (and nothing else): ")
        paths = [line.strip() for line in open(filename_paths)]

# reads in json to search from a file
filename = raw_input("Enter the name of the file containing the JSON: ");
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
                        starting_path = "OrderProductResponse.OrderProductResponseDetail.Product"
                        print "Analyzing data..."
                        print ""
                        break
                elif(starting_path_q == "n" or starting_path_q == "N"):
                                while path_confirm:
                                                starting_path = raw_input("Enter your starting path: (Level.sublevel.subsublevel... or nothing if you start from the top level)  ")
                                                if(starting_path == "" or starting_path == "nothing"):
                                                        starting_path_confirm = "Top-level starting path"
                                                else:
                                                        starting_path_confirm = starting_path
                                                while True:
                                                                confirmation = raw_input("Is this correct? \"" + starting_path_confirm + "\" (y/n)  ")
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
 

def check_path_exists(path, starting_path):
                path = path.strip();
                path_points = path.split(".");
 
                # starting path to json path
                current = json
                if(starting_path != ""):
                        for startpathpoint in starting_path.split("."):
                                current = current[startpathpoint]
 
                # checks if path exists
                success = True
                for point in path_points:
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
                                print "Path found: \t" + path
                else:
                                print "Not found: \t" + path
 
                return success
               
 
found = 0
for path in paths:
                if(check_path_exists(path, starting_path)):
                                found += 1
