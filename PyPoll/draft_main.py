# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration 
# isn't what it used to be.)

# You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). Each dataset is composed of three 
# columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates 
# each of the following:

        # 1) The total number of votes cast

        # 2) A complete list of candidates who received votes

        # 3) The percentage of votes each candidate won

        # 4) The total number of votes each candidate won

        # 5) The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:
        # Election Results
        # -------------------------
        # Total Votes: 620100
        # -------------------------
        # Rogers: 36.0% (223236)
        # Gomez: 54.0% (334854)
        # Brentwood: 4.0% (24804)
        # Higgins: 6.0% (37206)
        # -------------------------
        # Winner: Gomez
        # -------------------------
# Your final script must be able to handle any such similarly-structured dataset in the future 
# (i.e you have zero intentions of living in this hillbilly town -- so your script needs to work without massive re-writes). 
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Create a Python script that analyzes votes and calculates the following:

import os as os
import csv as csv

#operating in my current directory 
os.chdir(".")

#reading all of the files in a directory which I got from here:
directorylist = os.listdir("raw_data")

#For all of the files in the above directory, do the following
for x in os.listdir("raw_data"):
    
    #Starting the vote counter
    countvote = 0

    if x.endswith(".csv"):
    #An empty list for me to write to later
        new_data = []
        
        #Now we are going to read the first csv file, opening the employee data dir with x as the file name.
        with open(os.path.join("raw_data", x)) as csvfile:
            readthis = csv.DictReader(csvfile)
            
            #For each of the rows in the readthis file, I made the row headers variables.
            for row in readthis:
                voter_ID = row["Voter ID"]
                county = row["County"]
                candidate = row["Candidate"]
                
                #For each time you go thru the loop, add a number to the counter
                countvote = countvote + 1
                
                

                #Calculate a complete list of candidates who received votes
        print(countvote)
