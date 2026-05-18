import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

# LOAD CLEANED DATASETS

crop_rec = pd.read_csv(
    "cleaned_data/clean_crop_recommendation.csv"
)

crop_prod = pd.read_csv(
    "cleaned_data/clean_crop_production.csv"
)

rainfall_df = pd.read_csv(
    "cleaned_data/clean_rainfall.csv"
)

yield_df = pd.read_csv(
    "cleaned_data/clean_yield.csv"
)

# UPLOAD CROP RECOMMENDATION

for _, row in crop_rec.iterrows():

    sql = """
    INSERT INTO crop_recommendation
    (N, P, K, temperature,
    humidity, ph, rainfall, label)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        row['N'],
        row['P'],
        row['K'],
        row['temperature'],
        row['humidity'],
        row['ph'],
        row['rainfall'],
        row['label']
    )

    cursor.execute(sql, values)

conn.commit()

print("Crop Recommendation Uploaded")

# UPLOAD CROP PRODUCTION

for _, row in crop_prod.iterrows():

    sql = """
    INSERT INTO crop_production
    (state, district, crop, year,
    season, area, production, yield_value)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        row['State'],
        row['District'],
        row['Crop'],
        row['Year'],
        row['Season'],
        row['Area'],
        row['Production'],
        row['Yield']
    )

    cursor.execute(sql, values)

conn.commit()

print("Crop Production Uploaded")

# UPLOAD RAINFALL

for _, row in rainfall_df.iterrows():

    sql = """
    INSERT INTO rainfall
    (area, year, average_rain_fall_mm_per_year)
    VALUES (%s,%s,%s)
    """

    values = (
        row['Area'],
        row['Year'],
        row['average_rain_fall_mm_per_year']
    )

    cursor.execute(sql, values)

conn.commit()

print("Rainfall Uploaded")

# UPLOAD YIELD

for _, row in yield_df.iterrows():

    sql = """
    INSERT INTO yield_data
    (area, item, year, value)
    VALUES (%s,%s,%s,%s)
    """

    values = (
        row['Area'],
        row['Item'],
        row['Year'],
        row['Value']
    )

    cursor.execute(sql, values)

conn.commit()

print("Yield Uploaded")

# CLOSE CONNECTION

cursor.close()
conn.close()

print("All Data Uploaded Successfully")