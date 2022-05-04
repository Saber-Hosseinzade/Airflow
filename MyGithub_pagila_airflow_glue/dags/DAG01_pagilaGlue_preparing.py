import pathlib
from datetime import timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

DagID = pathlib.Path(__file__).stem

S3_BUCKET = Variable.get("data_lake_bucket")

DEFAULT_ARGS = {
    "owner": "Saber_Hosseinzade",
    "depends_on_past": False,
    "retries": 0,
    "email_on_failure": False,
    "email_on_retry": False,
}

with DAG(
    dag_id=DagID,
    description="cleaning and preparing workspace",
    default_args=DEFAULT_ARGS,
    dagrun_timeout=timedelta(minutes=15),
    start_date=days_ago(7),
    schedule_interval=None,
    tags=["pagila_glue"],
) as dag:
    
    Start = DummyOperator(task_id="Start")

    Finish = DummyOperator(task_id="Finish")

    delete_landingzone_folder = BashOperator(
        task_id="delete_landingzone_folder",
        bash_command=f'aws s3 rm "s3://{S3_BUCKET}/landing_zone/pagila_glue/" --recursive',
    )

    list_landingzone_objects = BashOperator(
        task_id="list_landingzone_objects",
        bash_command=f"aws s3api list-objects-v2 --bucket {S3_BUCKET} --prefix landing_zone/pagila_glue/",
    )

    delete_stagingzone_folder = BashOperator(
        task_id="delete_stagingzone_folder",
        bash_command=f'aws s3 rm "s3://{S3_BUCKET}/staging_zone/pagila_glue/" --recursive',
    )

    list_stagingzone_objects = BashOperator(
        task_id="list_stagingzone_objects",
        bash_command=f"aws s3api list-objects-v2 --bucket {S3_BUCKET} --prefix staging_zone/pagila_glue/",
    )

    delete_catalog_database = BashOperator(
        task_id="delete_catalog_database",
        bash_command="""aws glue delete-database --name learnit2022_saber_pagila_postgres \
                        || echo 'Database learnit2022_saber_pagila_postgres not found.'""",
    )

    create_catalog_database = BashOperator(
        task_id="create_catalog_database",
        bash_command="""aws glue create-database --database-input \
            '{"Name": "learnit2022_saber_pagila_postgres", "Description": "pagila Database extracted from postgres"}'""",
    )
        
    Start >> [delete_landingzone_folder, delete_stagingzone_folder, delete_catalog_database] 
    delete_landingzone_folder >> list_landingzone_objects
    delete_stagingzone_folder >> list_stagingzone_objects
    delete_catalog_database >> create_catalog_database
    [list_landingzone_objects, list_stagingzone_objects, create_catalog_database] >> Finish
