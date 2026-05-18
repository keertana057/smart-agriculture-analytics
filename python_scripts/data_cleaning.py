import pandas as pd
import numpy as np

# LOAD DATASETS

crop_rec = pd.read_csv(
    "datasets/Crop_recommendation.csv"
)

crop_prod = pd.read_csv(
    "datasets/India Agriculture Crop Production.csv"
)

yield_df = pd.read_csv(
    "datasets/yield.csv"
)

rainfall_df = pd.read_csv(
    "datasets/rainfall.csv"
)

# STANDARDIZE COLUMN NAMES

crop_rec.columns = crop_rec.columns.str.strip()
crop_prod.columns = crop_prod.columns.str.strip()
yield_df.columns = yield_df.columns.str.strip()
rainfall_df.columns = rainfall_df.columns.str.strip()

# REMOVE DUPLICATES

crop_rec.drop_duplicates(inplace=True)
crop_prod.drop_duplicates(inplace=True)
yield_df.drop_duplicates(inplace=True)
rainfall_df.drop_duplicates(inplace=True)

# HANDLE MISSING VALUES

for col in crop_rec.select_dtypes(include=np.number):
    crop_rec[col] = crop_rec[col].fillna(
        crop_rec[col].median()
    )

for col in crop_prod.select_dtypes(include=np.number):
    crop_prod[col] = crop_prod[col].fillna(
        crop_prod[col].median()
    )

for col in yield_df.select_dtypes(include=np.number):
    yield_df[col] = yield_df[col].fillna(
        yield_df[col].median()
    )

for col in rainfall_df.select_dtypes(include=np.number):
    rainfall_df[col] = rainfall_df[col].fillna(
        rainfall_df[col].median()
    )

# REMOVE INVALID VALUES

crop_rec = crop_rec[
    (crop_rec['temperature'] > 0) &
    (crop_rec['humidity'] > 0) &
    (crop_rec['rainfall'] > 0)
]

# FIX DATATYPES

rainfall_df['average_rain_fall_mm_per_year'] = pd.to_numeric(
    rainfall_df['average_rain_fall_mm_per_year'],
    errors='coerce'
)

yield_df['Value'] = pd.to_numeric(
    yield_df['Value'],
    errors='coerce'
)

# REMOVE OUTLIERS

def remove_outliers(df, column):

    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)

    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return df[
        (df[column] >= lower) &
        (df[column] <= upper)
    ]

crop_rec = remove_outliers(
    crop_rec,
    'rainfall'
)

# NORMALIZE TEXT COLUMNS

crop_prod['State'] = (
    crop_prod['State']
    .str.strip()
    .str.title()
)

crop_prod['Crop'] = (
    crop_prod['Crop']
    .str.strip()
    .str.title()
)

# SAVE CLEANED DATA

crop_rec.to_csv(
    "cleaned_data/clean_crop_recommendation.csv",
    index=False
)

crop_prod.to_csv(
    "cleaned_data/clean_crop_production.csv",
    index=False
)

yield_df.to_csv(
    "cleaned_data/clean_yield.csv",
    index=False
)

rainfall_df.to_csv(
    "cleaned_data/clean_rainfall.csv",
    index=False
)

print("Data Cleaning Completed")