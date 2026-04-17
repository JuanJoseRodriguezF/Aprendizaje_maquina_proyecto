from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

MODELS_DIR = ROOT_DIR / "models"
NOTEBOOKS_DIR = ROOT_DIR / "notebooks"
REPORTS_DIR = ROOT_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
DASHBOARD_DIR = REPORTS_DIR / "dashboard"
PRESENTATION_DIR = REPORTS_DIR / "presentation"

SRC_DIR = ROOT_DIR / "src"

RAW_DATA_FILE = RAW_DIR / "raw.csv"
CLEAN_DATA_FILE = INTERIM_DIR / "students_depression_clean.csv"

X_TRAIN_FILE = PROCESSED_DIR / "X_train.csv"
X_TEST_FILE = PROCESSED_DIR / "X_test.csv"
Y_TRAIN_FILE = PROCESSED_DIR / "y_train.csv"
Y_TEST_FILE = PROCESSED_DIR / "y_test.csv"


def ensure_project_dirs() -> None:
    dirs = [
        RAW_DIR,
        INTERIM_DIR,
        PROCESSED_DIR,
        MODELS_DIR,
        FIGURES_DIR,
        DASHBOARD_DIR,
        PRESENTATION_DIR,
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)