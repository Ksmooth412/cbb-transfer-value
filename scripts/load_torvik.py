# Downloads several seasons of Torvik player stats into one DuckDB table.
import io, time
import requests
import pandas as pd
import duckdb

YEARS = [2022, 2023, 2024, 2025]
frames = []
for year in YEARS:
    url = f"https://barttorvik.com/getadvstats.php?year={year}&csv=1"
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    df = pd.read_csv(io.StringIO(resp.text), header=None)
    df.columns = [str(c) for c in df.columns]
    print(year, df.shape)
    frames.append(df)
    time.sleep(2)  # be polite to the site

all_df = pd.concat(frames, ignore_index=True)
con = duckdb.connect("data/cbb.duckdb")
con.execute("CREATE OR REPLACE TABLE raw_players AS SELECT * FROM all_df")
print(con.execute('SELECT "31" AS season, COUNT(*) FROM raw_players GROUP BY 1 ORDER BY 1').fetchall())
con.close()
