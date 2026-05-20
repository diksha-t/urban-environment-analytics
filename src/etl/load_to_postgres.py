from sqlalchemy import text
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:201204@localhost:5432/urban_env_analytics"
) # connected to postgres

with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM air_quality"))
    print(result.fetchone())