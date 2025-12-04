# Step 1: Create Boolean variables
has_account = True
email_verified = False

# Step 2: Check if the user can log in (needs account AND verified email)
can_login = has_account and email_verified

# Step 3: Validate email by checking '@'
email = "g@example.com"
is_email_valid = "@" in email

# Step 4: Age validation
user_age = 17
is_age_valid = user_age >= 18

# Step 5: Final login check
can_login_final = has_account and email_verified and is_email_valid and is_age_valid

# Step 6: Print results
print("can_login:", can_login)
print("is_email_valid:", is_email_valid)
print("is_age_valid:", is_age_valid)
print("can_login_final:", can_login_final)

# Step 7: Identity operator check
print("has_account is True:", has_account is True)