
#Python function to validate password based on some predefined criteria
def validate_pswd(password):
    upper = False
    lower = False
    num = False
    char = False

    for ele in password:
        if not ele.isalnum():
            char = True
        elif ele.isupper():
            upper = True
        elif ele.islower():
            lower = True
        elif ele.isdigit():
            num = True

    if upper and lower and num and len(password) > 7 and char:
        return True
    else:
        return False

psw = input("Please enter your password: ")

if validate_pswd(psw):
    print("Password is valid.")
else:
    print("Password must be at least 8 characters long, alphanumeric with at least a special character, an uppercase letter, a lowercase letter, and a number.")

# verifying age of registrants
#import datetime for age calculation

from datetime import datetime
def validate_age(dob_year):
    today = datetime.today()

    dob = datetime.strptime(dob_year, '%m/%d/%y')

    age = today - dob
    # print(age.days)
    if int(age.days) >= 18 * 365:
        return True
    else:
        return False

dob_year = input("Enter the year of your birth (YYYY): ")
if validate_age(dob_year):
    print("You are qualified.")
else:
    print("You are not qualified.")

def uname_pswd_match(uname, pswd, filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # print(line)
            fields = line.split(",")
            if fields[0] == uname and fields[1].strip() == pswd:
                return True
    return False
# Example Usage:
filepath = "username_password_list.txt"
print("Correct filepath")
#uname_pswd_match("Biden", "Password@1", filepath)
if uname_pswd_match("Biden", "Password@1", filepath):
    print("Entry is a match")
else:
    print("Username and/or password is/are not correct")