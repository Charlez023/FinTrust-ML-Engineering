# FinTrust ML Engineering — Repository Structure

The repository is organised into separate folders for the data, code, tests, and documentation. This makes the project easier to manage as development continues.

```text
FinTrust ML Engineering/

├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── preprocessing/
│   └── inference/
│
├── tests/
│
├── docs/
│   └── week1/
│
├── README.md
├── requirements.txt
└── .gitignore
```

The `data/raw/` folder contains the original project data and resources, while `data/processed/` is for data that has been cleaned or transformed.

The `notebooks/` folder is for exploration and experiments. The `src/` folder contains the main Python code, with separate folders for data, features, models, preprocessing, and inference.

The `tests/` folder is for testing the ML workflow, while `docs/week1/` contains the Week 1 documentation.

`README.md` provides basic project information, `requirements.txt` lists the Python packages used, and `.gitignore` prevents unnecessary files such as virtual environments and cache files from being tracked by Git.