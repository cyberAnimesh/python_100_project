"""
This program checks whether your email is valid or not.
"""

def Email_Address_Validator(Email):

    # Space not allowed
    if " " in Email:
        return "Invalid Email Address (Space Not Allowed)"

    # '@' must be exactly one
    if Email.count("@") != 1:
        return "Invalid Email Address (@ Issue)"

    # Dot must be present
    if "." not in Email:
        return "Invalid Email Address (Dot Missing)"

    at_index = Email.index("@")
    dot_index = Email.rindex(".")

    # '@' should come before dot
    if at_index > dot_index:
        return "Invalid Email Address (@ after dot)"

    # '@' should not be at start and dot not at end
    if at_index == 0 or dot_index == len(Email) - 1:
        return "Invalid Email Address (Wrong Position)"

    return "Valid Email"


user_email = input("Enter Your Email Address: ")
print(Email_Address_Validator(user_email))
