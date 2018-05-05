# In this challenge, you get to be the boss. You oversee hundreds of employees across the country developing 
# Tuna 2.0, a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, 
# and self-adulation. The company recently decided to purchase a new HR system, and unfortunately for you, the
# new system requires employee records be stored completely differently.

# Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required 
# format. Your script will need to do the following:

        # Import the employee_data1.csv and employee_data2.csv files, which currently holds employee records like the below:
                # Emp ID,Name,DOB,SSN,State
                # 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
                # 15,Samantha Lara,1993-09-08,848-80-7526,Colorado
                # 411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania

        # Then convert and export the data to use the following format instead:
                # Emp ID,First Name,Last Name,DOB,SSN,State
                # 214,Sarah,Simpson,12/04/1985,***-**-8166,FL
                # 15,Samantha,Lara,09/08/1993,***-**-7526,CO
                # 411,Stacy,Charles,12/20/1957,***-**-8526,PA

# In summary, the required conversions are as follows:

# 1) The Name column should be split into separate First Name and Last Name columns.

# 2) The DOB data should be re-written into MM/DD/YYYY format.

# 3) The SSN data should be re-written such that the first five numbers are hidden from view.

# 4) The State data should be re-written as simple two-letter abbreviations.

# Special Hint: You may find this link to be helpful—Python Dictionary for State Abbreviations.

#Program: 
#Import the library that you want to use for this program
import csv as csv
import os as os
import us_state_abbrev

#Import two csv files that you are going to modify

#file_path1 = os.path.join("/Users/kh/Desktop/BOOTCAMP/Week3/Homework3/python-challenge/Pyboss", "employee_data", "employee_data1.csv")
#file_path2 = os.path.join("/Users/kh/Desktop/BOOTCAMP/Week3/Homework3/python-challenge/Pyboss", "employee_data", "employee_data2.csv")

# https://code.tutsplus.com/tutorials/quick-tip-how-to-make-changes-to-multiple-files-within-a-directory-using-python--cms-26452


#operating in my current directory 
# http://www.pythonforbeginners.com/code-snippets-source-code/python-os-listdir-and-endswith
os.chdir(".")

#reading all of the files in a directory which I got from here:
directorylist = os.listdir("employee_data")

#For all of the files in the above directory, do the following
for x in os.listdir("employee_data"):
    if x.endswith(".csv"):
    #An empty list for me to write to later
        new_data = []

        #Now we are going to read the first csv file, opening the employee data dir with x as the file name.
        with open(os.path.join("employee_data", x)) as csvfile:
            
            readthis = csv.DictReader(csvfile)
            #For each of the rows in the readthis file, I made the row headers variables.
            for row in readthis:
                Emp_DI = row["Emp ID"]
                name = row["Name"]
                DOB = row["DOB"]
                SSN = row["SSN"] 
                State = row["State"]

                #I need to split the Name row so I can get the first and last name
            
                First_Name = name.split()[0]
                Last_Name = name.split()[1]

                # I need to replace the state spelled out with the state abbreviation. I called the US state abbreviation program.
                newstatename = us_state_abbrev.us_state_abbrev[State]
                row["State"] = newstatename
            
                #The DOB data should be re-written into MM/DD/YYYY format. Its currently written like "1985-12-04"
                DOB.split("-")
                year_DOB = DOB[0:4]
                month_DOB = DOB[5:7]
                day_DOB = DOB[8:]

                new_birthday =f"{month_DOB}/{day_DOB}/{year_DOB}"

                #The SSN data should be re-written such that the first five numbers are hidden from view. Should read like ***-**-8166. 
                # Currently written as 282-01-8166
                Last_four = SSN[7:]
                new_SSN = f"***-**-{Last_four}"

                #Add the new csv keys to the blank list as the top. 
                new_data.append(
                        {
                            "Emp_ID": row["Emp ID"],
                            "First_Name": First_Name,
                            "Last_Name": Last_Name,
                            "DOB": new_birthday,
                            "SSN": new_SSN,
                            "State": row["State"]
                            }
                            )
        # Grab the filename from the original path
        _, filename = os.path.split(x)

        # Write updated data to csv file
        csvpath = os.path.join("output", filename)
        with open(csvpath, "w") as csvfile:
            fieldnames = ["Emp_ID", "First_Name", "Last_Name", "DOB", "SSN", "State"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_data)                