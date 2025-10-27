# Databricks notebook source
from pyspark.sql import SparkSession
import os

spark = SparkSession.builder.getOrCreate()
df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
# COMMAND ----------
token = dbutils.secrets.get(scope="mlops_maven", key="pat_token")
os.environ["PAT_TOKEN"] = token
print(os.environ["PAT_TOKEN"][:-1])
# COMMAND ----------
