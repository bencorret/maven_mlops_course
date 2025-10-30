from loguru import logger
import yaml
import sys
from pyspark.sql import SparkSession
import pandas as pd
from pathlib import Path

from house_price.config import ProjectConfig
from house_price.data_processor import DataProcessor

git_token = dbutils.secrets.get(scope="mlops_maven", key="pat_token")
install_cmd = f"git+https://{git_token}@github.com/bencorret/trainings@master#subdirectory=mlops_external_library"
sys.path.append(str(Path.cwd().parent / 'src'))

from mlops_external_library.timer import Timer


config = ProjectConfig.from_yaml(config_path="../project_config.yml", env="dev")

logger.info("Configuration loaded:")
logger.info(yaml.dump(config, default_flow_style=False))

# Load the house prices dataset
spark = SparkSession.builder.getOrCreate()
filepath = "../data/data.csv"
df = pd.read_csv(filepath)

# Load the house prices dataset
with Timer() as preprocess_timer:
    # Initialize DataProcessor
    data_processor = DataProcessor(df, config, spark)

    # Preprocess the data
    data_processor.preprocess()

logger.info(f"Data preprocessing: {preprocess_timer}")

# Split the data
X_train, X_test = data_processor.split_data()
logger.info("Training set shape: %s", X_train.shape)
logger.info("Test set shape: %s", X_test.shape)

# Save to catalog
logger.info("Saving data to catalog")
data_processor.save_to_catalog(X_train, X_test)

# Enable change data feed (only once!)
logger.info("Enable change data feed")
data_processor.enable_change_data_feed()
