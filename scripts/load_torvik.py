# Downloads one season of Bart Torvik player stats and saves it to DuckDB.
import io
import requests
import pandas as pd
import duckdb

YEAR = 2025  # 2025 = the 2024-25 season
URL = f"https://barttorvik.com/getadvstats.php?year={YEAR}&csv=1"

resp = requests.get(URL, timeout=60)
resp.raise_for_status()
df = pd.read_csv(io.StringIO(resp.text), header=None)

print(df.shape)
print(df.head())

con = duckdb.connect("data/cbb.duckdb")
con.execute(f"CREATE OR REPLACE TABLE raw_players_{YEAR} AS SELECT * FROM df")
print(con.execute(f"SELECT COUNT(*) FROM raw_players_{YEAR}").fetchone())
con.close()
