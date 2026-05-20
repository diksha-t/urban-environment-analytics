from fastapi import FastAPI
from sqlalchemy import create_engine, text
import pandas as pd

app = FastAPI()

# connecting with the datbase
engine = create_engine(
    "postgresql+psycopg2://postgres:201204@localhost:5432/urban_env_analytics"
)

@app.get("/")
def root():
    return {"message": "Urban Environmental Analytics API"}

@app.get("/average-pm25")
def average_pm25():
    query = "SELECT AVG(pm25) AS average_pm25 FROM air_quality;"
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")[0]

@app.get("/monthly-trends")
def monthly_trends():
    query = '''
    SELECT
        DATE_TRUNC('month', timestamp) AS month,
        AVG(pm25) AS avg_pm25
    FROM air_quality
    GROUP BY month
    ORDER BY month;
    '''
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")