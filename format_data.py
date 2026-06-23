import pandas as pd

print("format_data.py is running")

# Read raw dataset
df = pd.read_csv("data/raw_ny_july_2025.csv")

print("Original shape:", df.shape)

rename_map = {
    "DAY_OF_MONTH": "DAY",
    "DAY_OF_WEEK": "DAY_OF_WEEK",
    "ORIGIN": "ORG_AIRPORT",
    "DEST": "DEST_AIRPORT",
    "CRS_DEP_TIME": "SCHEDULED_DEPARTURE",
    "DEP_TIME": "DEPARTURE_TIME",
    "DEP_DELAY": "DEPARTURE_DELAY",
    "CRS_ARR_TIME": "SCHEDULED_ARRIVAL",
    "ARR_TIME": "ARRIVAL_TIME",
    "ARR_DELAY": "ARRIVAL_DELAY",
}

df = df.rename(columns=rename_map)

required_columns = [
    "YEAR",
    "MONTH",
    "DAY",
    "DAY_OF_WEEK",
    "ORG_AIRPORT",
    "DEST_AIRPORT",
    "SCHEDULED_DEPARTURE",
    "DEPARTURE_TIME",
    "DEPARTURE_DELAY",
    "SCHEDULED_ARRIVAL",
    "ARRIVAL_TIME",
    "ARRIVAL_DELAY",
]

df = df[required_columns].dropna()
print("Filtered shape:", df.shape)

df.to_csv("data/formatted.csv", index=False)
print("File written to data/formatted.csv")