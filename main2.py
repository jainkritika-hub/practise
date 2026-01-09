import pandas as pd
import os
import csv

RAW = "rawData"
CLEAN = "cleanData"
DIRTY = "dirtyData"

os.makedirs(CLEAN, exist_ok=True)
os.makedirs(DIRTY, exist_ok=True)

for file in os.listdir(RAW):
    if file.endswith("2.csv"):
        filePath = os.path.join(RAW,file)

        df = pd.read_csv(filePath)

        df.columns = df.columns.str.strip().str.lower()

        df.drop_duplicates(df, inplace=True)

        df["price"] = pd.to_numeric(df["price"], errors="coerce")
        df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")


        invalid = df[(df["price"].isna()) | (df["quantity"].isna()) | (df["price"]<0) | (df["quantity"]<0)]

        valid = df.drop(invalid.index)

        valid.to_csv(os.path.join(CLEAN,file),index=False)
        invalid.to_csv(os.path.join(DIRTY,f"ganda data {file}"),index=False)
        print(os.path.join(DIRTY,f"ganda data {file}"))


