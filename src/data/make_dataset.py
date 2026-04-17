import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from config.paths import (
    RAW_DATA_FILE,
    CLEAN_DATA_FILE,
    X_TRAIN_FILE,
    X_TEST_FILE,
    Y_TRAIN_FILE,
    Y_TEST_FILE,
)

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("/", "_", regex=False)
        .str.replace("?", "", regex=False)
    )
    return df

def clean_categorical_strings(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    cat_cols = df.select_dtypes(include="object").columns
    for col in cat_cols:
        df[col] = df[col].astype(str).str.strip().str.replace("'", "", regex=False)
    return df

def fix_financial_stress(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["financial_stress"] = df["financial_stress"].replace("?", np.nan)
    moda = df["financial_stress"].mode()[0]
    df["financial_stress"] = df["financial_stress"].fillna(moda)
    df["financial_stress"] = pd.to_numeric(df["financial_stress"], errors="coerce")
    return df

def prepare_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    df = pd.read_csv(RAW_DATA_FILE)

    df = clean_column_names(df)
    df = clean_categorical_strings(df)
    df = fix_financial_stress(df)

    cols_baja_variabilidad = ["work_pressure", "job_satisfaction", "profession"]
    df = df.drop(columns=cols_baja_variabilidad)

    frecuencia_degree = df["degree"].value_counts()
    categorias_frecuentes = frecuencia_degree[frecuencia_degree >= 500].index
    df["degree_grouped"] = np.where(df["degree"].isin(categorias_frecuentes), df["degree"], "Other")
    df = df.drop(columns=["degree"])

    frecuencia_city = df["city"].value_counts()
    ciudades_frecuentes = frecuencia_city[frecuencia_city >= 500].index
    df["city_grouped"] = np.where(df["city"].isin(ciudades_frecuentes), df["city"], "Other")
    df = df.drop(columns=["city"])

    df.to_csv(CLEAN_DATA_FILE, index=False)

    X = df.drop(columns=["depression", "id"], errors="ignore")
    y = df["depression"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    X_train.to_csv(X_TRAIN_FILE, index=False)
    X_test.to_csv(X_TEST_FILE, index=False)
    y_train.to_csv(Y_TRAIN_FILE, index=False)
    y_test.to_csv(Y_TEST_FILE, index=False)

    return X_train, X_test, y_train, y_test