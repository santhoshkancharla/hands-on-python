username = input("Enter username: ")
password = int(input("Enter password: "))
if username == "sunny" and password == 995910:
    print("\nLogin Successful.\n")
    n = int(input("Enter number of buildings to analyze: "))
    readings = []
    for i in range(n):
        value = int(input(f"Enter reading for building {i+1}: "))
        readings.append(value)
    valid = [e for e in readings if e >= 0]
    total = sum(valid)
    e_dictionary = {
        "efficient": [e for e in readings if 0 <= e <= 50],
        "moderate": [e for e in readings if 51 <= e <= 150],
        "high": [e for e in readings if e > 150],
        "invalid": [e for e in readings if e < 0]
    }
    Num_buildings = len(readings)
    analysis = (total, Num_buildings)
    high_count = len(e_dictionary["high"])
    eff_count = len(e_dictionary["efficient"])
    mod_count = len(e_dictionary["moderate"])
    if total > 600:
        result = "Energy Waste Detected. The electricity board is not happy."
    elif high_count > 3:
        result = "Overconsumption detected. Too much power usage."
    elif (eff_count - mod_count <= 1) and (mod_count - eff_count <= 1):
        result = "Balanced usage. Everything looks under control."
    elif eff_count > max(mod_count, high_count):
        result = "Efficient campus. Good job managing energy."
    else:
        result = "Moderate usage. Nothing unusual."
    print("Energy usage classification:")
    for key, value in e_dictionary.items():
        print(f"{key} buildings: {value}")
    print("\nTotal energy consumed:", analysis[0])
    print("Number of buildings analyzed:", analysis[1])
    print("System Conclusion:", result)
else:
    print("\nInvalid login. Access denied.")    
