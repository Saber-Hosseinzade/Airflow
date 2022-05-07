import pathlib
from datetime import timedelta

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago


DagID = pathlib.Path(__file__).stem


Schema = "myschema"
TablesList = ["actor", "address", "category", "city", "country", "customer", "film", "film_actor", "film_category", 
              "inventory", "language", "payment", "rental", "staff", "store"]

DEFAULT_ARGS = {
    "owner": "saber_Hosseinzade",
    "depends_on_past": False,
    "retries": 0,
    "email_on_failure": False,
    "email_on_retry": False,
    "postgres_conn_id": "postgres_redshift",
}


with DAG(
    dag_id=DagID,
    description="Create pagila database tables in Redshift and load data from S3 to tables in Redshift",
    default_args = DEFAULT_ARGS,
    dagrun_timeout = timedelta(minutes=5),
    start_date=days_ago(7),
    schedule_interval = None,
    tags=["s3_redshift"],
) as dag:
    
    Start = DummyOperator(task_id="Start")

    Finish = DummyOperator(task_id="Finish")


    for table in TablesList:
        
        drop_table = PostgresOperator(
            task_id=f"drop_table_{table}", 
            sql=f"DROP TABLE IF EXISTS {Schema}.{table};"
        )
        
        create_table = PostgresOperator(
            task_id=f"create_table_{table}", 
            sql=f"sql_files/pagilaS3Redshift/pagilaS3Redshift_create_{table}.sql"
        )
        
        

        Start >> drop_table >> create_table >> Finish
