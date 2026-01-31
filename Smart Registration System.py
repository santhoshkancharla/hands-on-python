studentid = input("Enter Studentid : ")
email = input("Enter Email : ")
password = input("Enter Password : ")
referral = input("Enter Referral code : ")

isValid = True

# -------- Student ID validation --------
if (
    len(studentid) != 7 or
    not studentid.startswith("CSE") or
    studentid[3] != "-" or
    not studentid[4:7].isdigit()
):
    isValid = False

# -------- Email validation --------
if (
    email.count("@") != 1 or
    email.count(".") == 0 or
    email[0] == "@" or
    email[-1] == "@" or
    not email.endswith(".edu")
):
    isValid = False

# -------- Password validation --------
if len(password) < 8 or not password[0].isupper():
    isValid = False

digit = False
for c in password:
    if c.isdigit():
        digit = True

if not digit:
    isValid = False

# -------- Referral code validation --------
if (
    len(referral) != 6 or
    not referral.startswith("REF") or
    not referral[3:5].isdigit() or
    referral[5] != "@"
):
    isValid = False

# -------- Final result --------
if isValid:
    print("APPROVED")
else:
    print("REJECTED")
