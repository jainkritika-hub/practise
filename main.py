import pandas as pd
import os
import csv

RAW_DATA = "rawData"
CLEAN = "cleanData"
DIRTY = "dirtyData"


os.makedirs(CLEAN,exist_ok=True)
os.makedirs(DIRTY,exist_ok=True)



for file in os.listdir(RAW_DATA):
    if file.endswith(".csv"):
        file_path = os.path.join(RAW_DATA,file)

        df = pd.read_csv(file_path)

        #1 Column clenaup
        df.columns = df.columns.str.strip().str.lower()

        #2 Remove dupliactes
        df.drop_duplicates(inplace=True)

        #3 Numeric conversion
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
        df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

        #4 Invalid rows
        invalid = df[(df["price"].isna()) | (df["quantity"].isna()) | (df["price"]<0) | (df["quantity"]<0)]

        valid = df.drop(invalid.index)


        valid.to_csv(os.path.join(CLEAN,file),index=False)
        invalid.to_csv(os.path.join(DIRTY,f"invalid-{file}"),index=False)

