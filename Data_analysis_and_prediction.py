import random
import math
import copy
import numpy as np
import pandas as pd

def generate_data(n=15):
    data = []
    for i in range(n):
        zone_data = {
            "zone": i + 1,
            "metrics": {
                "traffic": random.randint(50, 200),
                "pollution": random.randint(30, 150),
                "energy": random.randint(40, 180)
            },
            "history": [random.randint(10, 100) for _ in range(5)]
        }
        data.append(zone_data)
    return data

def personalize_data(data, roll_number):
    if roll_number % 2 == 0:
        return data[::-1] 
    else:
        return data[3:] + data[:3]

def custom_risk_score(t, p, e):
    return math.log(t + p + e) + math.sqrt(t)

def mutate_data(data):
    for d in data:
        d["metrics"]["traffic"] += 20
        d["metrics"]["pollution"] += 10
        d["history"].append(random.randint(50, 120))
    return data

def to_dataframe(data):
    rows = []
    for d in data:
        t = d["metrics"]["traffic"]
        p = d["metrics"]["pollution"]
        e = d["metrics"]["energy"]

        risk = custom_risk_score(t, p, e)

        rows.append([d["zone"], t, p, e, risk])

    df = pd.DataFrame(rows, columns=["zone", "traffic", "pollution", "energy", "risk"])
    return df

def manual_corr(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    num = np.sum((x - x_mean) * (y - y_mean))
    den = math.sqrt(np.sum((x - x_mean) ** 2) * np.sum((y - y_mean) ** 2))

    return num / den

def analyze(df):
    mean = df["risk"].mean()
    var = df["risk"].var()
    std = df["risk"].std()

    anomalies = df[df["risk"] > mean + std]["zone"].tolist()

    corr = manual_corr(df["traffic"].values, df["pollution"].values)

    stability_index = 1 / var if var != 0 else 0

    return mean, var, std, anomalies, corr, stability_index

def detect_clusters(risky_zones):
    clusters = []
    current = []

    for i in range(len(risky_zones)):
        if i == 0 or risky_zones[i] == risky_zones[i - 1] + 1:
            current.append(risky_zones[i])
        else:
            clusters.append(current)
            current = [risky_zones[i]]

    if current:
        clusters.append(current)

    return clusters

roll_number = 6

original = generate_data()

original = personalize_data(original, roll_number)

assignment_copy = original
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

print("BEFORE MUTATION:")
print(original[0])

mutate_data(shallow_copy)

print("\nAFTER MUTATION (Original affected due to shallow copy):")
print(original[0])

print("\nDeep Copy (Safe):")
print(deep_copy[0])

df = to_dataframe(original)
print("\nDATAFRAME:")
print(df)

mean, var, std, anomalies, corr, stability_index = analyze(df)

risky_zones = df[df["risk"] > mean]["zone"].tolist()

clusters = detect_clusters(sorted(risky_zones))

max_risk = df["risk"].max()
min_risk = df["risk"].min()

if stability_index > 1:
    decision = "System Stable"
elif stability_index > 0.5:
    decision = "Moderate Risk"
elif stability_index > 0.2:
    decision = "High Corruption Risk"
else:
    decision = "Critical Failure"

print("\nAnomaly Zones:", anomalies)
print("\nClusters:", clusters)
print("\nTuple Output:", (max_risk, min_risk, stability_index))
print("\nDecision:", decision)
