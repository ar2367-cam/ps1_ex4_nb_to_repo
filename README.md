# Titanic Data Journey

This project explores the Titanic passenger data and builds a baseline random forest model to predict survival. The reusable code (loading data, feature engineering, plots, summaries and the model) is in the `titanic` package, and `Titanic Data Journey.ipynb` calls it step by step.

- `titanic/`: the Python package (settings are in `titanic/config.py`)
- `data/`: `train.csv`, `test.csv` and `gender_submission.csv`
- `Titanic Data Journey.ipynb`: the analysis notebook

## How to run the code

You need [pixi](https://pixi.sh) installed.

1. Clone the repository and move into it:
   ```
   git clone https://github.com/ar2367-cam/ps1_ex4_nb_to_repo.git
   cd ps1_ex4_nb_to_repo
   ```
2. Create the environment from `pixi.toml` / `pixi.lock`:
   ```
   pixi install
   ```
3. Open `Titanic Data Journey.ipynb` in VS Code, click "Select Kernel" (top right), choose "Python Environments" and pick the interpreter in `.pixi/envs/default`, then run all cells.

`pixi install` also installs the `titanic` package from this repository (an editable install, set up in `pyproject.toml`), so it can be imported from any folder and edits to the code take effect straight away.

Note: `pixi.toml` currently lists only the `win-64` platform. On macOS or Linux, run `pixi workspace platform add osx-arm64` (or `linux-64`) before `pixi install`.
