import copy

def generate_data():
    users = [
        {"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}},
        {"id": 2, "data": {"files": ["c.txt"], "usage": 300}}
    ]
    return users

def replicate_data(original):
    assigned = original            
    shallow = list(original)        
    deep = copy.deepcopy(original)  
    return assigned, shallow, deep

def modify_data(data, roll_number):
    for user in data:
        if roll_number % 2 == 0:
            user["data"]["files"].append("new_file.txt")
        else:
            if len(user["data"]["files"]) > 0:
                user["data"]["files"].pop()

        user["data"]["usage"] += 100

def check_integrity(original, shallow, deep):
    leakage_count = 0
    safe_count = 0
    overlap_count = 0

    print("\n--- Integrity Analysis ---")

    for i in range(len(original)):
        orig_files = set(original[i]["data"]["files"])
        shallow_files = set(shallow[i]["data"]["files"])
        deep_files = set(deep[i]["data"]["files"])

        if orig_files == shallow_files:
            print(f"User {original[i]['id']} → Data Leakage Detected")
            leakage_count += 1
        else:
            print(f"User {original[i]['id']} → No Leakage")

        if orig_files != deep_files:
            print(f"User {original[i]['id']} → Deep Copy Safe")
            safe_count += 1

        overlap = orig_files.intersection(shallow_files)
        overlap_count += len(overlap)

        print(f"Common Files: {overlap}")

    return (leakage_count, safe_count, overlap_count)

users = generate_data()

print("Original Data (BEFORE):")
print(users)

assigned, shallow, deep = replicate_data(users)

roll_number = 6  
modify_data(shallow, roll_number)

print("\nOriginal Data (AFTER modification on shallow):")
print(users)

print("\nShallow Copy:")
print(shallow)

print("\nDeep Copy (unchanged):")
print(deep)

result = check_integrity(users, shallow, deep)

print("\nFinal Report (leakage_count, safe_count, overlap_count):")
print(result)
