import smtplib  # Import the smtplib module to handle sending emails
import datetime as dt  # Import datetime module to work with dates
import random  # Import random module to randomly select items
import pandas  # Import pandas module for data manipulation

# Get the current date and time
now = dt.datetime.now()
current_month = now.month  # Get the current month
current_day = now.day  # Get the current day
birthday_date = (current_month, current_day)  # Create a tuple for the current date (month, day)

# Load birthday data from a CSV file into a pandas DataFrame
data = pandas.read_csv("100_Projects/project32_Birthday_Email/birthdays.csv")

# Create a dictionary with (month, day) as keys and a string of person details as values
birthdays_dict = {
    (row['month'], row['day']): f"{row['name']},{row['email']},{row['year']},{row['month']},{row['day']}"
    for _, row in data.iterrows()  # Iterate over each row in the DataFrame
}

# Check if today matches anyone's birthday in the dictionary
if birthday_date in birthdays_dict.keys():
    # Get the details of the person whose birthday it is today
    person_details = birthdays_dict[birthday_date]
    
    # Split the details string into a list of individual attributes
    details_list = person_details.split(',')
    
    person_name = details_list[0]  # First element is the person's name
    person_email = details_list[1]  # Second element is the person's email

    # Define file paths for the birthday letter templates
    file1 = "100_Projects/project32_Birthday_Email/letter_templates/letter_1.txt"
    file2 = '100_Projects/project32_Birthday_Email/letter_templates/letter_2.txt'
    file3 = '100_Projects/project32_Birthday_Email/letter_templates/letter_3.txt'

    # Open all three letter template files at the same time
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'r') as f3:
        # Read the content of each file into separate variables
        content1 = f1.read()  # Read content of letter_1.txt
        content2 = f2.read()  # Read content of letter_2.txt
        content3 = f3.read()  # Read content of letter_3.txt
        
        # Store the letters in a tuple
        letter_templates = (content1, content2, content3)
        
        # Randomly select one letter template from the tuple
        random_letter = random.choice(letter_templates)
        
        # Replace the placeholder [NAME] in the selected letter with the actual person's name
        letter = random_letter.replace("[NAME]", person_name)

        # Set up email details
        my_email = person_email  # Set the sender email address
        password = "qlfc sufc diro bfqy"  # Set the password for the email account

        # Use the SMTP protocol to send the email
        with smtplib.SMTP("smtp.gmail.com") as connection:  # Connect to Gmail's SMTP server
            connection.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            connection.login(user=my_email, password=password)  # Log in to the email account
            
            # Send the email
            connection.sendmail(
                from_addr=my_email,  # Email sender
                to_addrs=my_email,  # Email recipient (can be changed to another address)
                msg=f"Subject: Happy Birthday!!\n\n {letter}"  # Create the email message with a subject and body
            )
    
# Print a message indicating that the email has been sent
print("Email sent")