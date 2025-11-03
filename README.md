# Maven MLOps Course - Databricks

A comprehensive MLOps course project demonstrating best practices for machine learning on Databricks, focusing on house price prediction using the Ames Housing dataset.

## Overview

This project serves as course material for learning MLOps on Databricks. It demonstrates how to structure, package, and deploy machine learning projects with proper configuration management, modular code design, and integration with Databricks services.

**Current Status:** Week 1 - Data Preprocessing and Project Setup

## Project Structure

```
maven_mlops_course/
├── src/
│   └── house_price/           # Main Python package
│       ├── __init__.py        # Package initialization and version management
│       ├── config.py          # Configuration management with Pydantic
│       └── data_processor.py  # Data preprocessing and splitting
├── notebooks/                 # Databricks notebooks
│   ├── week1_demo.py         # Demonstration notebook
│   └── week1.pretty_notebook.py  # Main preprocessing pipeline
├── scripts/                   # Standalone Python scripts
│   └── data_processor.py     # Script version of data processing
├── data/
│   └── data.csv              # Housing dataset (1,461 rows × 81 columns)
├── .databricks/              # Databricks Asset Bundle configuration
├── pyproject.toml            # Modern Python project configuration
├── project_config.yml        # MLOps configuration (environments, features, hyperparameters)
├── databricks.yml            # Databricks Bundle configuration
└── Taskfile.yaml             # Task automation
```

## Features (Week 1)

### Data Processing Pipeline
- **Data Preprocessing**: Handles missing values, type conversions, and feature engineering
- **Train/Test Split**: 80/20 split with configurable parameters
- **Databricks Integration**: Saves processed datasets as Delta tables in Unity Catalog
- **Change Data Feed**: Enables CDC for audit trails and data lineage

### Configuration Management
- **Environment-specific configs**: Separate settings for `prd`, `acc`, and `dev` environments
- **Feature definitions**: 10 numeric and 18 categorical features defined in YAML
- **Hyperparameters**: Centralized configuration for model training parameters
  - `learning_rate`: 0.01
  - `n_estimators`: 1000
  - `max_depth`: 6

### Modular Design
- Pydantic models for configuration validation
- Reusable `DataProcessor` class with clear separation of concerns
- Type hints throughout the codebase
- Comprehensive docstrings

## Key Technologies

- **Python**: 3.11 - 3.12
- **ML/Data Science**: pandas, numpy, scikit-learn, lightgbm
- **Databricks**: databricks-sdk, databricks-feature-engineering
- **MLflow**: Experiment tracking (v2.17.0)
- **Configuration**: Pydantic for validation, YAML for storage
- **Package Management**: UV for fast dependency resolution

## Setup

### Prerequisites
- Python 3.11 or 3.12
- Access to a Databricks workspace
- UV package manager installed

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd maven_mlops_course
```

2. Create virtual environment and install dependencies:
```bash
task create-venv
task sync-dev
```

Or manually:
```bash
uv venv --python 3.11
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip sync --extra dev
```

3. Set up Databricks authentication:
   - Create a Databricks PAT token
   - Store it in Databricks secrets (scope: `mlops_maven`)

## Usage

### Running the Preprocessing Pipeline

The main preprocessing notebook is located at `notebooks/week1.pretty_notebook.py`:

1. Open the notebook in Databricks
2. The pipeline will:
   - Load configuration from `project_config.yml` (dev environment)
   - Read the housing dataset from `data/data.csv`
   - Preprocess data (handle missing values, create features)
   - Split into train/test sets (80/20)
   - Save to Delta tables in Unity Catalog:
     - `{catalog}.{schema}.train_set`
     - `{catalog}.{schema}.test_set`
   - Enable Change Data Feed for both tables

### Configuration

Edit `project_config.yml` to customize:
- Feature lists (numeric and categorical)
- Target variable
- Hyperparameters
- Environment-specific catalog and schema names
- MLflow experiment names

Example:
```yaml
num_features:
  - LotFrontage
  - LotArea
  - OverallQual
  # ... more features

cat_features:
  - MSZoning
  - Neighborhood
  # ... more features

target: SalePrice

environments:
  dev:
    catalog_name: dev_catalog
    schema_name: house_price
```

## Dataset

The project uses the Ames Housing dataset with 1,461 properties and 81 features including:

**Numeric Features (10 selected)**:
- LotFrontage, LotArea, OverallQual, OverallCond
- YearBuilt, YearRemodAdd, MasVnrArea
- TotalBsmtSF, GrLivArea, GarageCars

**Categorical Features (18 selected)**:
- MSZoning, Street, Alley, LotShape, LandContour
- Neighborhood, Condition1, BldgType, HouseStyle
- RoofStyle, Exterior1st, Exterior2nd, MasVnrType
- Foundation, Heating, CentralAir, SaleType, SaleCondition

**Target**: SalePrice

**Note**: Datasets are saved as Delta tables in Unity Catalog, which differs from typical MLOps projects but is beneficial for this Databricks-focused course.

## Future Roadmap

The following features are planned for upcoming weeks:

- **Week 2+**: Training data preparation and feature engineering
- **Model Training**: Train and tune machine learning models
- **Model Registry**: Register models with MLflow
- **Model Deployment**: Deploy models using Databricks Asset Bundles
- **Monitoring**: Implement model monitoring and drift detection
- **CI/CD**: Automated testing and deployment pipelines

## Development

### Code Quality
- Uses pre-commit hooks for code formatting and linting
- Full type annotations with mypy
- Comprehensive docstrings following Google style

### Testing
Testing framework (pytest) is configured but test suite is pending implementation.

### Databricks Connect
Development dependencies include `databricks-connect` for local development and debugging.

## Version

Current version: `0.0.1`

## License

This is course material for educational purposes.

## Contributing

This is a training project. For questions or issues related to the course, please contact the course instructor.
