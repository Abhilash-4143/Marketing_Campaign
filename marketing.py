import pandas as pd
import numpy as np

df = pd.read_csv("marketing_campaign.csv", sep="\t")
log = [f"Original shape: {df.shape}"]

df.columns = df.columns.str.strip().str.lower().str.replace(r"[^\w]+", "_", regex=True)

before = len(df)
df = df.drop_duplicates().drop_duplicates(subset="id", keep="first").reset_index(drop=True)
log.append(f"Removed {before - len(df)} duplicate rows")

df["dt_customer"] = pd.to_datetime(df["dt_customer"], format="%d-%m-%Y", errors="coerce")

df.loc[df["year_birth"] < 1940, "year_birth"] = np.nan
df["age"] = (df["dt_customer"].dt.year - df["year_birth"])

marital_map = {
    "Together": "Partner", "Married": "Partner",
    "Single": "Single", "Divorced": "Single", "Widow": "Single",
    "Alone": "Single", "Absurd": "Single", "YOLO": "Single",
}
df["marital_status"] = df["marital_status"].str.strip().map(marital_map)

df["education"] = df["education"].replace({"2n Cycle": "Master", "Graduation": "Graduate"})

df.loc[df["income"] > 200000, "income"] = np.nan
df["income"] = df["income"].fillna(df["income"].median())
log.append(f"Income nulls/outliers filled with median: {df['income'].median():.0f}")

df = df.drop(columns=["z_costcontact", "z_revenue"])

df["total_spend"] = df[[
    "mntwines","mntfruits","mntmeatproducts",
    "mntfishproducts","mntsweetproducts","mntgoldprods"
]].sum(axis=1)
df["children"] = df["kidhome"] + df["teenhome"]

df["age"] = df["age"].astype("Int64")
df["income"] = df["income"].astype(float)

df["dt_customer"] = df["dt_customer"].dt.strftime("%d-%m-%Y")  # consistent display format
df.to_csv("cleaned_marketing_campaign.csv", index=False)

log.append(f"Final shape: {df.shape}")
log.append(f"Columns: {list(df.columns)}")
with open("cleaning_summary.txt", "w") as f:
    f.write("\n".join(log))
print("Done.")
