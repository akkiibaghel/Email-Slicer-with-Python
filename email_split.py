email = input("enter the email_id")
user_name = email[:email.index("@")]
domain_name = email[email.index("@") +1:]
print(f"Your name is '{user_name}' and your company name is '{domain_name}' " )
