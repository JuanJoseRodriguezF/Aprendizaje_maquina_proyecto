import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

from config.paths import MODELS_DIR

def train_and_evaluate(models: dict, X_train, X_test, y_train, y_test):
    results = []
    predictions = {}
    probabilities = {}

    file_names = {
        "Regresión Logística": "pipeline_logreg.joblib",
        "Árbol de Decisión": "pipeline_tree.joblib",
        "Random Forest": "pipeline_rf.joblib",
        "KNN": "pipeline_knn.joblib",
    }

    for name, pipeline in models.items():
        pipeline.fit(X_train, y_train)

        y_pred = pipeline.predict(X_test)
        y_prob = pipeline.predict_proba(X_test)[:, 1]

        predictions[name] = y_pred
        probabilities[name] = y_prob

        results.append({
            "Modelo": name,
            "Accuracy": accuracy_score(y_test, y_pred),
            "Precision": precision_score(y_test, y_pred),
            "Recall": recall_score(y_test, y_pred),
            "F1-score": f1_score(y_test, y_pred),
            "ROC-AUC": roc_auc_score(y_test, y_prob)
        })

        joblib.dump(pipeline, MODELS_DIR / file_names[name])

    results_df = pd.DataFrame(results).sort_values(by="F1-score", ascending=False).reset_index(drop=True)

    best_model_name = results_df.iloc[0]["Modelo"]
    best_pred = predictions[best_model_name]
    best_prob = probabilities[best_model_name]

    return results_df, best_model_name, best_pred, best_prob