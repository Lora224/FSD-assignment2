#regex patterns for email and password validation
#save registered users in student.data
#when logging in , the program should read the data from the file a nd verify the student credentials

import re
#email must end with university.com
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
password_pattern = r'^(?=.*[A-Z])[A-Za-z]{6,}[0-9]{3,}$'

# Example usage:
email = "example@example.com"
if re.match(email_pattern, email):
    print("Valid email")
else:
    print("Invalid email")
password = "Password123"
if re.match(password_pattern, password):
    print("Valid password")
else:
    print("Invalid password")
    
    