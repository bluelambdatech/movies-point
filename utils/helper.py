import bcrypt
import re


# Define a PasswordValidator class to encapsulate the password validation logic
class PasswordValidator:
    def __init__(self):
        # Define special characters used for password validation
        self.special_chars = '[@_!#$%^&*()-+{/?}|>:;<"~`]'

    # Method to validate the password
    def validate_password(self):
        # Display password requirements to the user
        print("Password must meet the following requirements:")
        print("- Must be at least 8 characters")
        print("- Have an uppercase letter")
        print("- Have a lowercase letter")
        print("- Have a special character")
        print("- Have a numeric character\n")

        #         regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        #         count = 0
        #         while count != 5:

        #             email = input("Enter your email: ")

        #             try:
        #                 count += 1
        #                 assert re.fullmatch(regex, email), "You entered an invalid email address"

        #             except AssertionError as e:
        #                 print(f"\nEmail issue: {e}")

        #             else:
        #                 print(f"Your email is:  {email}\n\n")

        #                 break

        while True:
            # Prompt the user to enter a password
            pwd = input("Enter your password: ")

            try:
                # Check password length
                assert len(pwd) >= 8, "Password length is less than 8 characters"
                # Check if all characters are ASCII
                assert pwd.isascii(), "Check your character types"
                # Check for at least one uppercase letter
                assert any(char.isupper() for char in pwd), "No upper case letters"
                # Check for at least one lowercase letter
                assert any(char.islower() for char in pwd), "No lower case letters"
                # Check for at least one numeric character
                assert any(char.isnumeric() for char in pwd), "No numeric character"
                # Check for at least one special character
                assert any(char in self.special_chars for char in pwd), "No special character"

            except AssertionError as e:
                # If any assertion fails, print an error message
                print(f"\nPassword issue: {e}")

            else:
                # If all checks pass, prompt the user to confirm the password
                repeat = input("Confirm your password: ")

                try:
                    # Check if the confirmation matches the original password
                    assert repeat == pwd, "There is a mismatch"
                except AssertionError as e:
                    # If confirmation fails, print an error message
                    print(e)
                else:
                    # If confirmation passes, hash the password using bcrypt
                    encoded_pwd = pwd.encode()
                    salt = bcrypt.gensalt()
                    hashed_pwd = bcrypt.hashpw(encoded_pwd, salt)

                    # Return a success message with the hashed password
                    return f"\nYour hashed password was appropriately set as {hashed_pwd}"


if __name__ == "__main__":
    # Create an instance of the PasswordValidator class
    password_validator = PasswordValidator()

    # Call the validate_password method to initiate the password validation process
    result = password_validator.validate_password()
    password_validator

    # Print the result at the end
    print(result)