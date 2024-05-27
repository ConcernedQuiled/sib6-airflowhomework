from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from wordcount import word_count

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 24),
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG(
    'wordcount_dag',
    default_args=default_args,
    description='A DAG for word count job',
    schedule_interval='@daily',
)

t1 = PythonOperator(
    task_id='run_wordcount_job',
    python_callable=word_count,
    dag=dag,
)
