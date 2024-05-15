#CLI main file for CLIUNIApp
# university 
# student_system
# student_course
# admin system


#import 

def display_university_menu():
    print("The University System")
    print("Please choose an option:")
    print("(A) Admin")
    print("(S) Student")
    print("(X) Exit")

def display_student_menu():
    print("The Student System")
    print("Please choose an option:")
    print("(L) Login")
    print("(R) Register")
    print("(X) Exit")

def display_student_course_menu():
    print("The Student Course System")
    print("Please choose an option:")
    print("(C) Change Password")
    print("(E) Enroll in Subject")
    print("(R) Remove Subject")
    print("(S) Show Enrolled Subjects")
    print("(X) Exit")

def display_admin_menu():
    print("The Admin System")
    print("Please choose an option:")
    print("(C) Clear Database File")
    print("(G) Group Students")
    print("(P) Partition Students")
    print("(R) Remove Student")
    print("(S) Show Students")
    print("(X) Exit")

def validate_email(email):
    # Email pattern validation logic here
    # Return True if email is valid, False otherwise
    # You can use regular expressions for email pattern matching
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_pattern, email)

def register_student():
    email = input("Enter email: ")
    password = input("Enter password: ")

    if validate_email(email):
        # Check if student already exists in the database
        # Add code to check if student already exists in the database
        # If student does not exist, register the student by storing data in "students.data" file
        with open("students.data", "a") as file:
            file.write(f"{email},{password}\n")
        print("Registration successful!")
    else:
        print("Invalid email format. Please try again.")

def login_student():
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Check if student exists in the database
    # Add code to check if student exists in the database
    # If student exists, login the student and perform actions in the student course menu

    # Simulating login by printing a success message
    print(f"Login successful! Welcome, {email}.")

def handle_student_course_choice(choice):
    if choice == 'C':
        print("Changing password...")
        # Add code to change student's password
       # student.new_password = input("Enter new password: ")
       # student.updatePassword(student.new_password)
    elif choice == 'E':
        print("Enrolling in subject...")
        # Add code to enroll student in a subject
    elif choice == 'R':
        print("Removing subject...")
        # Add code to remove subject from student's enrollment list
    elif choice == 'S':
        print("Showing enrolled subjects...")
        # Add code to show enrolled subjects and grades for the student
    elif choice == 'X':
        print("Exiting Student Course System...")
    else:
        print("Invalid choice. Please try again.")

def handle_admin_choice(choice):
    if choice == 'C':
        print("Clearing database file...")
        # Add code to clear the "students.data" file
    elif choice == 'G':
        print("Grouping students...")
        # Add code to group students based on grades
    elif choice == 'P':
        print("Partitioning students...")
        # Add code to show pass/fail distribution of students
    elif choice == 'R':
        print("Removing student...")
        # Add code to remove a student from the database
    elif choice == 'S':
        print("Showing students...")
        # Add code to show all students from the database
    elif choice == 'X':
        print("Exiting Admin System...")
    else:
        print("Invalid choice. Please try again.")

def main():
    while True:
        display_university_menu()
        university_choice = input("Enter your choice: ").upper()
        
        if university_choice == 'A':
            display_admin_menu()
            admin_choice = input("Enter your choice: ").upper()
            handle_admin_choice(admin_choice)
        elif university_choice == 'S':
            display_student_menu()
            student_choice = input("Enter your choice: ").upper()
            
            if student_choice == 'L':
                login_student()
                display_student_course_menu()
                student_course_choice = input("Enter your choice: ").upper()
                handle_student_course_choice(student_course_choice)
            elif student_choice == 'R':
                register_student()
            elif student_choice == 'X':
                print("Exiting Student System...")
                break
            else:
                print("Invalid choice. Please try again.")
        elif university_choice == 'X':
            print("Exiting University System...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
