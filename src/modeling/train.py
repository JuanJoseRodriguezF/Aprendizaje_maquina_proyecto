import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

def build_models(X_train: pd.DataFrame) -> dict:
    num_cols = X_train.select_dtypes(include=["int64", "float64"]).columns.tolist()
    cat_cols = X_train.select_dtypes(include=["object"]).columns.tolist()

    preprocessor_scaled = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
        ]
    )

    preprocessor_tree = ColumnTransformer(
        transformers=[
            ("num", "passthrough", num_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
        ]
    )

    models = {
        "Regresión Logística": Pipeline([
            ("preprocessor", preprocessor_scaled),
            ("model", LogisticRegression(max_iter=1000, random_state=42))
        ]),
        "Árbol de Decisión": Pipeline([
            ("preprocessor", preprocessor_tree),
            ("model", DecisionTreeClassifier(max_depth=5, random_state=42))
        ]),
        "Random Forest": Pipeline([
            ("preprocessor", preprocessor_tree),
            ("model", RandomForestClassifier(n_estimators=200, max_depth=8, random_state=42))
        ]),
        "KNN": Pipeline([
            ("preprocessor", preprocessor_scaled),
            ("model", KNeighborsClassifier(n_neighbors=7))
        ])
    }
    return models