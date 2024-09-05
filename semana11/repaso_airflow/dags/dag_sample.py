import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="my_dag_name",
    start_date=datetime.datetime(2024, 9, 4),
    schedule="@daily",
) as dag:

    bash_task = BashOperator(
        task_id="bash_task",
        bash_command='echo "Here is the message: Hello,world!"',
    )

    bash_task