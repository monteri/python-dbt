import duckdb
import os

# Minio creds
os.environ['AWS_REGION'] = 'us-east-1'
os.environ['AWS_ACCESS_KEY_ID'] = 'Wqa37YZthLqDN9PMvJE1'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'yQDN1IKaza894lr0r6UUUaTOmt93Ca1u8MME2HPe'

# 2. (Optional) configure your AWS credentials inside DuckDB
#    Alternatively you can rely on environment variables, IAM roles, etc.
con.execute(f"""
  SET s3_endpoint      = 'localhost:9000';
  SET s3_region        = '{os.environ['AWS_REGION']}';
  SET s3_access_key_id = '{os.environ['AWS_ACCESS_KEY_ID']}';
  SET s3_secret_access_key = '{os.environ['AWS_SECRET_ACCESS_KEY']}';
  SET s3_use_ssl       = false;
  SET s3_url_style     = 'path';  
""")