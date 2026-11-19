# Accept a username using input()
username = input("Enter username: ")

# Define validation checks
# 1. Must contain at least 5 characters
is_long_enough = len(username) >= 5

# 2. Must not contain only spaces (length > 0 and stripped string is not empty)
is_not_only_spaces = len(username.strip()) > 0

# 3. Must not be equal to "admin", ignoring uppercase/lowercase differences
is_not_admin = username.lower() != "admin"

# Evaluate all rules combined using Boolean logic
is_valid = is_long_enough and is_not_only_spaces and is_not_admin

# Print whether the username is valid or invalid and display a meaningful reason if rejected
if is_valid:
    print("Username is valid.")
else:
    print("Username is invalid. Reason:")
    if not is_long_enough:
        print("- The username must contain at least 5 characters.")
    if not is_not_only_spaces:
        print("- The username must not contain only spaces.")
    if not is_not_admin:
        print("- The username cannot be 'admin'.")
