import pandas as pd

from config.paths import REPORTS_DIR, DASHBOARD_DIR

def export_outputs(X_test, y_test, best_pred, best_prob, results_df):
    df_dashboard = X_test.copy()
    df_dashboard["depression_real"] = y_test.values
    df_dashboard["depression_pred"] = best_pred
    df_dashboard["probabilidad_depresion"] = best_prob

    df_dashboard.to_csv(REPORTS_DIR / "dashboard_base.csv", index=False)
    results_df.to_csv(REPORTS_DIR / "resultados_modelos.csv", index=False)

    df_dashboard.to_csv(DASHBOARD_DIR / "dataset_dashboard.csv", index=False)
    results_df.to_csv(DASHBOARD_DIR / "metricas_modelos.csv", index=False)

    return df_dashboard