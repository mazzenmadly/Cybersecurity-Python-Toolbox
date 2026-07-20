import re

def evaluate_password_strength(password):
  

    # Rule 1: The password must be at least 8 characters long.
    if len(password) < 8:
        return "Non-compliant", "The given password did not pass the following criteria:\n- Your password must be at least 8 characters long."

    # Rule 2: The password must contain at least one digit.
    if not re.search(r'\d', password):
        return "Non-compliant", "The given password did not pass the following criteria:\n- Your password must contain at least one digit."

    # Rule 3: The password must contain at least one uppercase letter.
    if not re.search(r'[A-Z]', password):
        return "Non-compliant.", "The given password did not pass the following criteria:\n- Your password must contain at least one uppercase letter."

    # Rule 4: The password must contain at least one special character.
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Non-compliant.", "The given password did not pass the following criteria:\n- Your password must contain at least one special character."

    # If all rules are satisfied, the password is very strong.
    return "Compliant.", "Your password is very strong and meets all security requirements."

# Example usage:
password = input("Enter the password string you want to evaluate: ")
category, description = evaluate_password_strength(password)
print(f"Your password is  {category} ")
print(description)