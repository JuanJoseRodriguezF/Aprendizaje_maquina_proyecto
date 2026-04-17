from config.paths import ensure_project_dirs
from src.data.make_dataset import prepare_data
from src.modeling.train import build_models
from src.modeling.evaluate import train_and_evaluate
from src.reports.export import export_outputs

def main():
    ensure_project_dirs()

    X_train, X_test, y_train, y_test = prepare_data()
    models = build_models(X_train)

    results_df, best_model_name, best_pred, best_prob = train_and_evaluate(
        models, X_train, X_test, y_train, y_test
    )

    export_outputs(X_test, y_test, best_pred, best_prob, results_df)

    print(f"Proceso finalizado. Mejor modelo: {best_model_name}")

if __name__ == "__main__":
    main()