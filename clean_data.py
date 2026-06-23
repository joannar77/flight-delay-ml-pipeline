import pandas as pd

print("clean_data.py is running")

AIRPORT = "JFK"  # change to the chosen airport code ( LGA or EWR)

df = pd.read_csv("data/formatted.csv")
print("Original shape:", df.shape)

# REQUIRED: filter to departures from chosen airport (ORIGIN)
df = df[df["ORG_AIRPORT"] == AIRPORT]
print("After ORG_AIRPORT filter:", df.shape)

# Cleaning step 1: convert DEPARTURE_DELAY to numeric (invalid --> NaN)
df["DEPARTURE_DELAY"] = pd.to_numeric(df["DEPARTURE_DELAY"], errors="coerce")

# Cleaning step 2: drop rows missing departure delay
df = df.dropna(subset=["DEPARTURE_DELAY"])
print("After dropna:", df.shape)

# Cleaning step 3: remove extreme/impossible delays
df = df[df["DEPARTURE_DELAY"].between(-60, 600)]
print("After delay bounds filter:", df.shape)

df.to_csv("cleaned_data.csv", index=False)
print("File written to cleaned_data.csv")