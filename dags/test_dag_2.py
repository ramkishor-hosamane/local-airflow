from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta

# Default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 26),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'email': ['rahosamane@squaretrade.com'],  # Change to your email
    'email_on_failure': True,
    'email_on_retry': False
}

# Define the DAG
with DAG(
    'simple_four_task_dag_with_email',
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

    send_email = EmailOperator(
        task_id='send_email',
        to='recipient@example.com',  # Change to your actual email
        subject='[Airflow] DAG Execution Completed',
        html_content="""
        <h3>Airflow DAG Execution Successful</h3>
        <p>The DAG <b>simple_four_task_dag_with_email</b> has completed successfully.</p>
        """,
    )

    # Define dependencies
    task_1 >> [task_2, task_3] >> task_4 >> send_email
