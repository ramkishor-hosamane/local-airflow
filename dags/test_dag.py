

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 26),
    'retries': 1
}

# Define the DAG
with DAG(
    'simple_four_task_dag_with_delay',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    task_1 = BashOperator(
        task_id='task_1',
        bash_command='echo "Task 1 executed"; sleep 3'
    )

    task_2 = BashOperator(
        task_id='task_2',
        bash_command='echo "Task 2 executed"; sleep 3'
    )

    task_3 = BashOperator(
        task_id='task_3',
        bash_command='echo "Task 3 executed"; sleep 3'
    )

    task_4 = BashOperator(
        task_id='task_4',
        bash_command='echo "Task 4 executed"'
    )

    # Define dependencies
    task_1 >> task_2 >> task_3 >> task_4
