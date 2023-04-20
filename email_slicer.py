def email_slicer():
    print("Welcome to EmailSlicer")
    email_address = input("enter your email address : ").lower()
    username, domain = email_address.split('@')
    extention = email_address.split('.')[1]
    print("Username : " + username)
    print("Domain : " + domain)
    print("Extention : " + extention)

while True:
    email_slicer()