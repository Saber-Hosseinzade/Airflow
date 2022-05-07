import pathlib
from datetime import timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.operators.dummy import DummyOperator
from airflow.operators.sql import SQLThresholdCheckOperator
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

DagID = pathlib.Path(__file__).stem

S3_BUCKET = Variable.get("landing_zone_bucket")

Schema = "myschema"
table = "payment"
BEGIN_DATE = "2007-02-01"
END_DATE = "2007-03-01"

DEFAULT_ARGS = {
    "owner": "saber_Hosseinzade",
    "depends_on_past": False,
    "retries": 0,
    "email_on_failure": False,
    "email_on_retry": False,
    "redshift_conn_id": "postgres_redshift",
    "postgres_conn_id": "postgres_redshift",
}

with DAG(
    dag_id=DagID,
    description="Load new data into Redshift",
    default_args=DEFAULT_ARGS,
    dagrun_timeout=timedelta(minutes=15),
    start_date=days_ago(1),
    schedule_interval=None,
    tags=["s3-redshift"],
) as dag:
    
    Start = DummyOperator(task_id="Start")

    Finish = DummyOperator(task_id="Finish")

    drop_staging_tables1 = PostgresOperator(
            task_id=f"drop_table_{table}_staging", 
            sql=f"DROP TABLE IF EXISTS {Schema}.{table}_staging;"
        )

    
    create_staging_tables = PostgresOperator(
        task_id=f"create_table_{table}_staging",
        sql=f"sql_files/pagilaS3Redshift/stagingTablesSqlFiles/pagilaS3Redshift_create_{table}_staging.sql",
    )


    s3_to_staging_tables = S3ToRedshiftOperator(
        task_id=f"{table}_to_staging",
        s3_bucket=S3_BUCKET,
        s3_key=f"landingZone/pagilaS3Redshift/csv/{table}.csv",
        schema=Schema,
        table=f"{table}_staging",
        copy_options=["csv"],
    )

    merge_staging_data = PostgresOperator(
        task_id=f"merge_{table}",
        sql=f"sql_files/pagilaS3Redshift/mergingTablesSqlFiles/merge_{table}.sql",
        params={"begin_date": BEGIN_DATE, "end_date": END_DATE},
    )

    drop_staging_tables2 = PostgresOperator(
        task_id=f"drop_{table}_staging",
        sql=f"DROP TABLE IF EXISTS {Schema}.{table}_staging;",
    )
    
    check_table = PostgresOperator(
        task_id="check_count_table",
        sql=f"select * from {Schema}.{table};",
    )
    
    
    check_task = SQLThresholdCheckOperator(
        task_id=f"check_table_{table}",
        conn_id=DEFAULT_ARGS["redshift_conn_id"],
        sql=f"SELECT COUNT(*) FROM {Schema}.{table} WHERE payment_date >= {BEGIN_DATE}",
        min_threshold=100,
        max_threshold=20000,
    )
    
    
    Start >> drop_staging_tables1 >> create_staging_tables >> s3_to_staging_tables >> merge_staging_data
    merge_staging_data >> drop_staging_tables2 >> check_table >> check_task >> Finish
