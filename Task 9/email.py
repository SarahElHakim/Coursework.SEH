
# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email:
    # Initialise the instance variables for each email.
    def __init__(self, address, subject, content):
        self.address = address
        self.subject = subject
        self.content = content
        self.has_been_read = False
    
    # Changes the 'has_been_read' instance variable for a specific object from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Functions --- #
inbox = []

def populate_inbox():
    # Create 3 sample emails and add it to the inbox list.
    email_1 = Email("masupport@company.com", "support", "Thank you for your enquiry. We will get back to you shortly.")
    email_2 = Email("jenna@company.com", "On Leave", "I am on leave at the moment. Will get back to you as soon as I am back.")
    email_3 = Email("feedback@company.com", "Feedback", "Let us know how we did.")
    inbox.append(email_1)
    inbox.append(email_2)
    inbox.append(email_3)


def list_emails():
    # Prints each email's subject line
    # alongside its corresponding index number,
    # regardless of whether the email has been read.
    for index, email in enumerate(inbox):
        print(f"{index} {email.subject}")


def read_email(index):
    # Displays the email_address, subject_line, and email_content attributes for the selected email.
    print(inbox[index].address)
    print(inbox[index].subject)
    print(inbox[index].content)

    # Set 'has_been_read' instance variable to True using the 'mark_as_read()' method.
    inbox[index].mark_as_read()

    print(f"\nEmail from {inbox[index].address} marked as read. \n")

def view_unread_emails():
    # Displays all unread Email object subject lines along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    for index, email in enumerate(inbox):
        if (not email.has_been_read):
            print(f"{index} {email.subject}")

# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.
populate_inbox()

print("Emails:")
list_emails()

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(input(
        """\nWould you like to:
        1. Read an email
        2. View unread emails
        3. Quit application

        Enter selection: """
    ))

    if user_choice == 1:
        emailIndex = int(input("Enter the index of the email you would like to read"))
        read_email(emailIndex)
    elif user_choice == 2:
        view_unread_emails()
    elif user_choice == 3:
        exit()
    else:
        print("Oops - incorrect input.")
