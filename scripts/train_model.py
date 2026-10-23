# Predict a transfer's new minutes share (min_pct) with linear regression.
import duckdb
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

con = duckdb.connect("data/cbb.duckdb")
for f in ["sql/02_transfers.sql", "sql/03_features.sql"]:
    con.execute(open(f).read())
df = con.execute("SELECT * FROM transfer_features").fetchdf()

FEATURES = ["prev_min_pct", "prev_ortg", "prev_usage", "level_jump"]
TARGET = "min_pct"

train = df[df.season < 2025]
test = df[df.season == 2025]

model = LinearRegression().fit(train[FEATURES], train[TARGET])
pred = model.predict(test[FEATURES])

baseline_mae = mean_absolute_error(test[TARGET], test["prev_min_pct"])
model_mae = mean_absolute_error(test[TARGET], pred)

print(f"Train rows: {len(train)}, Test rows: {len(test)}")
print(f"Baseline error (guess last year's minutes): {baseline_mae:.1f}")
print(f"Model error:                                {model_mae:.1f}")
print("\nWhat each feature does (coefficient):")
for name, coef in zip(FEATURES, model.coef_):
    print(f"  {name:14s} {coef:+.2f}")
