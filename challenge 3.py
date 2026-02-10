list = input("Enter the marks of a student").split()
count = 0
count_f = 0
for z in list:
    x = int(z)
    if x>=90 and x<=100:
        print(x,'-->Excellent')
        count += 1
    elif x>=75 and x<=89:
        print(x,'-->Very Good')
        count +=1
    elif x>=60 and x<=74:
        print(x,'-->Good')
        count +=1
    elif x>=40 and x<=59:
        print(x,'-->Average')
        count +=1
    elif x>=0 and x<=39:
        print(x,'-->Fail')
        count_f +=1
    elif x<0 or x>100:
        print(x,'-->Invalid')
print("Total valid students :", count)
print("Total failed students :", count_f)
