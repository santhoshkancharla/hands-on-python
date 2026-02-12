#personilisation option A
registration_number = input("Enter registration number")
#taking input from user
total_inputs = int(input("Enter no of inputs:"))
data = []

for index in range(total_inputs):
    user_input = input("Enter input :")
    if user_input.isdigit():
        data.append(int(user_input))
    else:
        data.append(user_input)

#applying filter to separate
numbers = []
strings = []

for element in data:
    if type(element) == int:
        numbers.append(element)
    else:
        strings.append(element)

# Option A logic applied
last_digit = int(registration_number[-1])

if last_digit % 2 == 0:
    numbers.reverse()
else:
    strings.reverse()

#Output
print("Numbers list :", numbers)
print("Strings list :", strings)
print("Total numbers : ", len(numbers))
print("Total strings : ", len(strings))
