# You are building a basic user verification tool for a learning website. Complete the following steps:

# Create a Boolean variable has_account and assign it True.
# Create another Boolean variable email_verified and assign it False.
# Use a logical operator to check if the user can log in. A user can log in only if they have an account and their email is verified. Store the result in can_login.
# To validate an email address, check if it contains the @ symbol, which is required for a valid email. For example, if the email is "g@example.com", confirm that @ is present. Store the result in a Boolean variable is_email_valid.
# The platform allows login only if the user’s age is greater than or equal to 18. Create a variable user_age and assign it 17. Use a comparison operator to check if the age is valid. Store the result in is_age_valid.
# Update the login logic to allow login only if has_account, email_verified, is_email_valid, and is_age_valid are all True. Store this final result in can_login_final.
# Print the results of can_login, is_email_valid, is_age_valid, and can_login_final.
# Use an identity operator to confirm that has_account is True and print the result.


has_account = True
email_verified = False


can_login = has_account and email_verified


email = "g@example.com"
is_email_valid = "@" in email


user_age = 17
is_age_valid = user_age >= 18


can_login_final = has_account and email_verified and is_email_valid and is_age_valid


print("Can login (initial check):", can_login)
print("Is email valid:", is_email_valid)
print("Is age valid:", is_age_valid)
print("Can login (final check):", can_login_final)


print("Does has_account refer to True?", has_account is True)
