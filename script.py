# ETL Script 
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)

# Get the job arguments
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Initialize Spark and Glue context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read CSV file with ISO-8859-1 encoding into a Spark DataFrame
s3_path = "s3://source-bucket-name/folder/"
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("delimiter", ",") \
    .option("encoding", "ISO-8859-1") \
    .load(s3_path)

# Convert the DataFrame to a Glue DynamicFrame
dynamic_frame = DynamicFrame.fromDF(df, glueContext, "dynamic_frame")

# Use the DynamicFrame in your SQL query
SqlQuery0 = '''
SELECT *
FROM myDataSource
WHERE Country IN ('Japan', 'Israel', 'Bahrain', 'Hong Kong', 'Singapore', 'Lebanon', 'United Arab Emirates', 'Saudi Arabia');
'''

SQLQuery_node2024 = sparkSqlQuery(glueContext, query=SqlQuery0, mapping={"myDataSource": dynamic_frame}, transformation_ctx="SQLQuery_node2024")

# Write the processed data to S3
AmazonS3_node2024 = glueContext.write_dynamic_frame.from_options(
    frame=SQLQuery_node2024,
    connection_type="s3",
    format="csv",
    connection_options={"path": "s3://output-bucket-name/folder/", "partitionKeys": []},
    transformation_ctx="AmazonS3_node2024"
)

# Commit the job
job.commit()