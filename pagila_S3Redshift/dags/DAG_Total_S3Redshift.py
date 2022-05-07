import pathlib
from datetime import timedelta

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from airflow.utils.dates import days_ago

DagID = pathlib.Path(__file__).stem

DEFAULT_ARGS = {
    "owner": "Saber_Hosseinzade",
    "depends_on_past": False,
    "retries": 0,
    "email_on_failure": False,
    "email_on_retry": False,
}

def _slack_failure_notification(context):
    slack_msg = f"""
            :red_circle: DAG Failed.
            *Task*: {context.get('task_instance').task_id}
            *Dag*: {context.get('task_instance').dag_id}
            *Execution Time*: {context.get('execution_date')}
            *Log Url*: {context.get('task_instance').log_url}
            """
    failed_alert = SlackWebhookOperator(
        task_id="slack_notification", http_conn_id="slack_webhook", message=slack_msg
    )

    return failed_alert.execute(context=context)


def _slack_success_notification(context):
    slack_msg = f"""
            :large_green_circle: DAG Succeeded.
            *Task*: {context.get('task_instance').task_id}
            *Dag*: {context.get('task_instance').dag_id}
            *Execution Time*: {context.get('execution_date')}
            *Log Url*: {context.get('task_instance').log_url}
            """
    success_alert = SlackWebhookOperator(
        task_id="slack_notification", http_conn_id="slack_webhook", message=slack_msg
    )

    return success_alert.execute(context=context)


with DAG(
    dag_id=DagID,
    description="Run all DAGs",
    default_args=DEFAULT_ARGS,
    dagrun_timeout=timedelta(minutes=60),
    start_date=days_ago(7),
    schedule_interval=None,
    on_failure_callback=_slack_failure_notification,
    on_success_callback=_slack_success_notification,
    tags=["s3_redshift"],
) as dag:
    
    
    Start = DummyOperator(task_id="Start")
    Finish = DummyOperator(task_id="Finish")

    run_dag01 = TriggerDagRunOperator(
        task_id="run_dag01",
        trigger_dag_id="DAG01_pagilaS3Redshift_createTables",
        wait_for_completion=True,
    )

    run_dag02 = TriggerDagRunOperator(
        task_id="run_dag02",
        trigger_dag_id="DAG02_pagilaS3Redshift_loadTables",
        wait_for_completion=True,
    )

    run_dag03 = TriggerDagRunOperator(
        task_id="run_dag03",
        trigger_dag_id="DAG03_pagilaS3Redshift_loadNewData",
        wait_for_completion=True,
    )



    Start >> run_dag01 >> run_dag02 >> run_dag03 >> Finish
