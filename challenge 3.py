n = int(input("enter no of students:"))
marks = []
failcount = 0
valid =n
for i in range(n):

    marks.append(int(input("enter marks of student ")))

for p in marks:
    if p>0 and p<=39:
        print(p,"->fail")
        failcount = failcount+1
    elif p>=40 and p<=59:
        print(p,"->Average")
    elif p >=60 and p <=74 :
        print(p,"->Good")
    elif p >=75 and p <= 89:
        print(p,"->Very Good")
    elif p >= 89 and p <= 100:
        print(p,"->excellent")
    else :
        print("Invalid")
        valid = valid-1

print("Final summary:")
print("Total valid students:",valid)
print("Total fail students:",failcount)
