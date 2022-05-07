import pathlib
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.utils.dates import days_ago

DagID = pathlib.Path(__file__).stem

TABLES = ["actor", "address", "category", "city", "country", "customer", "film", "film-actor", "film-category", 
              "inventory", "language", "payment", "rental", "staff", "store"]

DEFAULT_ARGS = {
    "owner": "Saber_Hosseinzade",
    "depends_on_past": False,
    "retries": 0,
    "email_on_failure": False,
    "email_on_retry": False,
}

with DAG(
    dag_id=DagID,
    description="Run Glue Jobs - source data to staging zone",
    default_args=DEFAULT_ARGS,
    dagrun_timeout=timedelta(minutes=30),
    start_date=days_ago(7),
    schedule_interval=None,
    tags=["pagila_glue"],
) as dag:
    
    Start = DummyOperator(task_id="Start")
    Finish = DummyOperator(task_id="Finish")

    list_glue_tables = BashOperator(
        task_id="list_glue_tables",
        bash_command="""aws glue get-tables --database-name learnit2022_saber_pagila_staging \
                          --query 'TableList[].Name'  --output table""",
    )

    for table in TABLES:
        run_jobs_staging = GlueJobOperator(
            task_id=f"run_job_{table}_sz", job_name=f"learnit2022_saber_pagila_{table}_glue_sz"
        )

        Start >> run_jobs_staging >> list_glue_tables >> Finish 
        
