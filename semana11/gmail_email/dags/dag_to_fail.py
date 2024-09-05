import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="otro_dag",
    start_date=datetime.datetime(2024, 9, 4),
    schedule="@daily",
    default_args ={"email_on_success": True, "email_on_retry": True,'email': ['anderson.coder.space@gmail.com']},
) as dag:

    bash_task = BashOperator(
        task_id="bash_task",
        bash_command='echo "Here is the message: Hello,world!" && exit 1',
    )

    bash_task
