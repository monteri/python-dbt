import os
import duckdb
import sys

# Minio creds
os.environ['AWS_REGION'] = 'us-east-1'
os.environ['AWS_ACCESS_KEY_ID'] = 'Wqa37YZthLqDN9PMvJE1'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'yQDN1IKaza894lr0r6UUUaTOmt93Ca1u8MME2HPe'

def configure_s3(con):
    con.execute(f"""
      SET s3_endpoint        = 'localhost:9000';
      SET s3_region          = '{os.environ['AWS_REGION']}';
      SET s3_access_key_id   = '{os.environ['AWS_ACCESS_KEY_ID']}';
      SET s3_secret_access_key = '{os.environ['AWS_SECRET_ACCESS_KEY']}';
      SET s3_use_ssl         = false;
      SET s3_url_style       = 'path';
    """)

def main():
    # ensure creds are present
    for var in ('AWS_REGION','AWS_ACCESS_KEY_ID','AWS_SECRET_ACCESS_KEY'):
        if var not in os.environ:
            print(f"ERROR: please set {var}", file=sys.stderr)
            sys.exit(1)

    # 1) in-memory DuckDB
    con = duckdb.connect()

    # 2) configure MinIO/S3
    configure_s3(con)

    # 3) read every parquet under */*.parquet
    parquet_glob = "s3://python-dbt/parquet/sales_summary.parquet/*/*.parquet"
    df = con.execute(f"""
      SELECT *
      FROM read_parquet('{parquet_glob}')
      WHERE sale_date = '2022-04-04'
    """).df()

    # 4) inspect or process
    print("Total rows:", len(df))
    print(df.head())

if __name__ == "__main__":
    main()