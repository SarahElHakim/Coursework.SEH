# Create empty list for lines.
lines = []

try:
    # Open the file in the directory.
    with open("./Code Files/Input/Task file/DOB.txt", "r") as file:
        # Store each line as a list element.
        for line in file:
            # Separate the words in the line.
            lines.append(line.split(" "))

    # Print the Name header.
    print("Name")

    # Loop through each line.
    for line in lines:
        # Print the name.
        name = " ".join(line[0:2])
        print(name)

    # Print the Birthdate header.
    print("\nBirthdate")

    # Loop through each line.
    for line in lines:
        # Print the birthdate.
        # Asked for help after I kept getting extra lines between each birthdate printed 
        # and the solution I was given was .replace.
        birthdate = " ".join(line[2:5]).replace("\n", "") 
        print(birthdate)
except FileNotFoundError:
    # In case the file does not exist error.
    print("The file does not exist.")