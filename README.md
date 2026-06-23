# Flight Delay ML Pipeline

## Machine Learning Pipeline for Flight Departure Delay Prediction

A reproducible machine learning pipeline developed to predict flight departure delays using U.S. transportation data. The project demonstrates data engineering, machine learning workflow automation, experiment tracking, and version-controlled data management using industry-standard tools.

---

## Project Overview

The objective of this project was to build an end-to-end machine learning pipeline capable of:

- Ingesting raw flight data
- Validating and formatting datasets
- Cleaning and filtering records
- Training a predictive machine learning model
- Tracking experiments and model artifacts
- Maintaining reproducibility through version control

The workflow was designed to support repeatable model training and deployment while following machine learning operations (MLOps) principles.

---

## Technologies Used

### Programming Languages
- Python
- R

### Data Science & Machine Learning
- Pandas
- NumPy
- Scikit-learn
- Ridge Regression

### MLOps & Version Control
- Git
- GitHub
- DVC (Data Version Control)
- MLflow

### Development Environment
- Jupyter Notebook
- VS Code
- Conda

---

## Project Architecture

### Data Formatting
Raw transportation data is transformed into a standardized schema compatible with the predictive model.

### Data Validation & Cleaning
Business rules are applied to:

- Filter departures from JFK Airport
- Remove missing delay values
- Convert delay fields to numeric values
- Remove extreme outliers
- Produce model-ready datasets

### Model Training
A Ridge Regression model is trained and evaluated using multiple parameter configurations.

### Experiment Tracking
MLflow records:

- Model parameters
- Training metrics
- Model artifacts
- Experiment history

### Data Versioning
DVC tracks dataset changes and supports reproducible machine learning workflows.

---

## Repository Structure

```text
.
├── data/
├── format_data.py
├── clean_data.py
├── poly_regressor_Python_1.0.0.py
├── finalized_model.pkl
├── MLproject
├── pipeline_env.yaml
├── README.md
└── model_performance_test.jpg
```

---

## Key Features

- Automated data preprocessing pipeline
- Reproducible machine learning workflow
- MLflow experiment tracking
- DVC data versioning
- Ridge Regression model development
- Model artifact generation
- End-to-end pipeline execution

---

## Machine Learning Workflow

1. Acquire raw flight data
2. Format dataset structure
3. Validate and clean records
4. Generate model-ready dataset
5. Train Ridge Regression model
6. Track experiments using MLflow
7. Export model artifacts
8. Maintain reproducibility with DVC and Git

---

## Learning Outcomes

This project demonstrates practical experience with:

- Data preprocessing
- Machine learning pipeline development
- Experiment tracking
- Model lifecycle management
- Reproducible analytics workflows
- Version-controlled data science projects

---

## Author

**Joanna Ronchi**

Master of Science, Data Analytics (Data Science Specialization)

GitHub: https://github.com/joannar77

LinkedIn: https://www.linkedin.com/in/joanna-ronchi/

---

## License

This repository is provided for portfolio and educational purposes.
