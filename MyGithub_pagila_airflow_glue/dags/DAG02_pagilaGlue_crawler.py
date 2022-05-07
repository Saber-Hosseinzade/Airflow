import pathlib
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.amazon.aws.operators.glue_crawler import GlueCrawlerOperator
from airflow.utils.dates import days_ago

DagID = pathlib.Path(__file__).stem

Crawler = "learnit2022_saber_pagila_postgres_crawler"

DEFAULT_ARGS = {
    "owner": "Saber_Hosseinzade",
    "depends_on_past": False,
    "retries": 0,
    "email_on_failure": False,
    "email_on_retry": False,
}

with DAG(
    dag_id= DagID,
    description="Run Crawlers to catalog data from Postgres",
    default_args=DEFAULT_ARGS,
    dagrun_timeout=timedelta(minutes=15),
    start_date=days_ago(7),
    schedule_interval=None,
    tags=["pagila_glue"],
) as dag:
    
    Start = DummyOperator(task_id = "Start")

    Complete = DummyOperator(task_id="Complete")

    list_glue_tables = BashOperator(
        task_id="list_glue_tables",
        bash_command="""aws glue get-tables --database-name learnit2022_saber_pagila_postgres \
                        --query 'TableList[].Name' --output table""",
    )

    Crawler_run = GlueCrawlerOperator(
        task_id=f"run_crawler", config={"Name": Crawler}
    )

    Start >> Crawler_run >> list_glue_tables >> Complete

