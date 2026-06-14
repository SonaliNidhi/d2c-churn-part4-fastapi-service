
import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv(
    "rfm_modeling_snapshot.csv"
)

features = [

    "recency_days",
    "frequency_180d",
    "monetary_180d",
    "ticket_count_90d",
    "sessions_30d"

]

X = df[features]

y = df["churn_next_60d"]

model = Pipeline([

    (
        "imputer",
        SimpleImputer(
            strategy="median"
        )
    ),

    (
        "classifier",
        RandomForestClassifier(
            n_estimators=500,
            random_state=42
        )
    )

])

model.fit(X, y)

joblib.dump(
    model,
    "model.pkl"
)

print("Model saved successfully")
