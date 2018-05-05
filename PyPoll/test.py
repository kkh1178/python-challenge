#Import the library that you want to use for this program
import csv as csv
import os as os


#Import two csv files that you are going to modify

file_path1 = os.path.join("/Users/kh/Desktop/BOOTCAMP/Week3/Homework3/python-challenge/PyPoll", "raw_data", "election_data_1.csv")
file_path2 = os.path.join("/Users/kh/Desktop/BOOTCAMP/Week3/Homework3/python-challenge/PyPoll", "raw_data", "election_data_2.csv")
#file_path2 = os.path.join("/Users/kh/Desktop/BOOTCAMP/Week3/Homework3/python-challenge/Pyboss", "employee_data", "employee_data2.csv")
#Starting the vote counter, unique candidates dictionary
perc = {}
unique_candidates = {}
countvote = 0
#http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
file = open("results.txt", "w") 

with open(file_path1) as csvfile:
    readthis = csv.DictReader(csvfile)
    
    #For each of the rows in the readthis file, I made the row headers variables.
    for row in readthis:
        voter_ID = row["Voter ID"]
        county = row["County"]
        candidate = row["Candidate"]
        
        #For each time you go thru the loop, add a number to the counter
        countvote = countvote + 1
        
        #Calculate a complete list of candidates who received votes:
 
        # For all of the candidates, if you see if add one, 
        # if you haven't seen it, start at zero and add one
        # I got this from: http://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python
        # but removed the forloop cuz it was counting all of the letters! 
        unique_candidates[candidate] = unique_candidates.get(candidate, 0) + 1
        number_votes = unique_candidates
    
    print(f"{countvote} is the total number of votes.")
    file.write(f"{countvote} is the total number of votes.\n")
    #The percentage of votes each candidate won
        
    for k, v in unique_candidates.items():
        file.write(f"{k}: {v/countvote:.2%}, ({v})\n")
        print(f"{k}: {v/countvote:.2%}, ({v})")

    print(f"{max(unique_candidates, key=unique_candidates.get)} is the winner.")
    file.write(f"{max(unique_candidates, key=unique_candidates.get)} is the winner.\n")
    


