fullname = input("Enter your full name: ")
email = input("Enter your email: ")
mobile = input("Enter your mobile number: ")
age = input("Enter your age: ")

valid = True

if fullname[0] == " " or fullname[-1] == " ":
    valid = False

if len(fullname.split(" ")) != 2:
    valid = False

if email[0] == "@" or email[-1] == "@" or "@" not in email or "." not in email:
    valid = False

if len(mobile) != 10 or not mobile.isdigit() or mobile[0] == "0":
    valid = False

if not age.isdigit():
    valid = False
else:
    age = int(age)
    if age < 18 or age > 60:
        valid = False

if valid:
    print("User profile valid")
    print("Login successful...")
else:
    print("User profile invalid")