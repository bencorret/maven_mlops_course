# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
df = spark.read.table("samples.nyc_taxi_trips")
df.show(5)
# COMMAND ----------
