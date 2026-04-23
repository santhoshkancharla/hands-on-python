import random
import math
import numpy as np
import pandas as pd

def generate_city_data(n=18):
    data = []

    for i in range(1, n - 2):
        record = {
            "zone": i,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        }
        data.append(record)

    data.append({"zone": n-1, "traffic": 50, "air_quality": 290, "energy": 420})  # extreme pollution
    data.append({"zone": n, "traffic": 0, "air_quality": 70, "energy": 120})      # zero traffic
    data.append({"zone": n+1, "traffic": 98, "air_quality": 250, "energy": 480})  # random spike

    return data

def custom_sort_by_traffic(data):
    n = len(data)

    for i in range(n):
        for j in range(0, n-i-1):
            if data[j]["traffic"] > data[j+1]["traffic"]:
                data[j], data[j+1] = data[j+1], data[j]

    return data

def classify_zone(record):
    if record["air_quality"] > 200 or record["traffic"] > 80:
        return "High Risk"
    elif record["energy"] > 400:
        return "Energy Critical"
    elif record["traffic"] < 30 and record["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"

def calculate_risk_score(t, aqi, e):
    return round((t * 0.35) + (aqi * 0.45) + (e * 0.20), 2)

def final_decision(avg_risk, high_risk_count):
    if avg_risk < 100:
        return "City Stable"

    elif avg_risk < 160:
        return "Moderate Risk"

    elif avg_risk < 220:
        return "High Alert"

    else:
        return "Critical Emergency"

city_data = generate_city_data()

city_data = custom_sort_by_traffic(city_data)

for row in city_data:
    row["category"] = classify_zone(row)
    row["risk_score"] = calculate_risk_score(
        row["traffic"],
        row["air_quality"],
        row["energy"]
    )
    row["sqrt_energy"] = round(math.sqrt(row["energy"]), 2)

df = pd.DataFrame(city_data)

matrix = df[["traffic", "air_quality", "energy"]].to_numpy()

mean_values = np.mean(matrix, axis=0)
variance_traffic = np.var(df["traffic"])

risk_list = list(df["risk_score"])
top_scores = sorted(risk_list, reverse=True)[:3]

top_zones = df[df["risk_score"].isin(top_scores)][["zone", "risk_score"]]

aqi_rising = []

for i in range(1, len(df)):
    if df.loc[i, "air_quality"] > df.loc[i-1, "air_quality"]:
        aqi_rising.append(df.loc[i, "zone"])

multi_factor = df[
    (df["risk_score"] > 180) &
    (df["zone"].isin(aqi_rising))
][["zone", "risk_score"]]

stability = "Stable Traffic Flow" if variance_traffic < 400 else "Unstable Traffic Flow"

critical_clusters = []

for i in range(len(df)-1):
    if df.loc[i, "risk_score"] > 180 and df.loc[i+1, "risk_score"] > 180:
        critical_clusters.append((df.loc[i, "zone"], df.loc[i+1, "zone"]))

risk_tuple = (
    max(df["risk_score"]),
    round(np.mean(df["risk_score"]), 2),
    min(df["risk_score"])
)

decision = final_decision(risk_tuple[1], len(top_zones))

print("\n===== SMART CITY DATAFRAME =====\n")
print(df)

print("\n===== COLUMN MEAN VALUES =====")
print("Traffic Mean      :", round(mean_values[0], 2))
print("AQI Mean          :", round(mean_values[1], 2))
print("Energy Mean       :", round(mean_values[2], 2))

print("\n===== TOP 3 WORST ZONES =====")
print(top_zones)

print("\n===== MULTI-FACTOR RISK ZONES =====")
print(multi_factor)

print("\n===== TRAFFIC STABILITY =====")
print(stability)

print("\n===== CRITICAL CLUSTERS =====")
print(critical_clusters if critical_clusters else "No consecutive clusters")

print("\n===== RISK TUPLE =====")
print("(max_risk, avg_risk, min_risk) =", risk_tuple)

print("\n===== FINAL SYSTEM DECISION =====")
print(decision)
