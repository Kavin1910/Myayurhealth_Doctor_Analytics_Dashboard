import pandas as pd
import random
import numpy as np

# Parameters for synthetic data
NUM_DOCTORS = 5
NUM_RECORDS = 500
DOCTORS = [f"Dr. {chr(65 + i)}" for i in range(NUM_DOCTORS)]  # ["Dr. A", "Dr. B", ..., "Dr. E"]
OUTCOMES = ["Successful", "Ongoing", "Unsuccessful"]

# Generate synthetic data
data = {
    "Consultation ID": [f"C{str(i).zfill(4)}" for i in range(1, NUM_RECORDS + 1)],
    "Doctor": [random.choice(DOCTORS) for _ in range(NUM_RECORDS)],
    "Consultation Date": pd.date_range(start="2023-01-01", end="2023-11-30").to_pydatetime().tolist()
                          + random.choices(pd.date_range(start="2023-01-01", end="2023-11-30"), k=NUM_RECORDS - 334),
    "Feedback": [random.randint(1, 5) for _ in range(NUM_RECORDS)],
    "Outcome": [random.choice(OUTCOMES) for _ in range(NUM_RECORDS)],
    "Response Time": [random.uniform(5, 60) for _ in range(NUM_RECORDS)],  # Response time in minutes
    "Revenue": [random.uniform(50, 500) for _ in range(NUM_RECORDS)],  # Revenue in USD
    "Retention": [random.choice([0, 1]) for _ in range(NUM_RECORDS)],
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Response Time and Revenue to 2 decimal places
df["Response Time"] = df["Response Time"].round(2)
df["Revenue"] = df["Revenue"].round(2)

# Save to CSV
df.to_csv("doctor_performance.csv", index=False)

print("Synthetic dataset generated and saved as doctor_performance.csv.")
