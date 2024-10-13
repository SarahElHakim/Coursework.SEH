# Ask user how many students are registering.
num_students = int(input("How many students are registering?"))

# Open the file that will register student ID.
with open ("reg_form.txt", "a+") as file:
    # Repeat for every student.
    for i in range(0,num_students):
        # Ask for ID number.
        id_number = input("Enter student ID number ")
        # Add ID to the file.
        file.write(id_number + "  ................ \n")