import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(
    "data/processed/cleaned_air_quality.csv",
    parse_dates=["timestamp"]
) # reload cleaned csv

engine = create_engine(
    "postgresql+psycopg2://postgres:201204@localhost:5432/urban_env_analytics"
) # connected to postgres

df.to_sql(
    "air_quality",
    engine,
    if_exists="replace",
    index=False
) # load data into the table

print("Data loaded successfully!")

from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM air_quality"))
    print(result.fetchone())