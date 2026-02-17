inputs = input("Enter weights: ")

weights = inputs.split(" ")
invlaid_entries=[]
overload=[]
heavy_load=[]
normal_load=[]
very_light=[]
for p in weights:
    p = int(p)
    if p<0:
        invlaid_entries.append(p)
    elif p>=0 and p<=5:
        very_light.append(p)
    elif  p>=6 and p<=25:
        normal_load.append(p)
    elif p>=26 and p<=60:
        heavy_load.append(p)
    else :
        overload.append(p)

name = input("enter your name:")
l = len(name)
pli = l%3
totalvalid=len(weights)-len(invlaid_entries)
totalaffect=0
if pli==0:
    invlaid_entries= invlaid_entries + overload
    totalaffect=len(overload)
elif pli == 1:
    totalaffect=len(very_light)
    very_light = []
else :
    totalaffect=len(invlaid_entries)+len(overload)+len(very_light)
    invlaid_entries=[] 
    overload = []
    very_light=[]      

print("totalvalid =",totalvalid)
print("total affected =",totalaffect)
print("l and pli are:",l ,pli)
print("invlaid_entries=",invlaid_entries)
print("overload=",overload)
print("heavy_load=",heavy_load)
print("normal_load=",normal_load)
print("very_light=",very_light)

