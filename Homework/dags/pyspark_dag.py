from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from

def run_spark_job():
    import subprocess
    subprocess.run(['spark-submit', '/opt/airflow/scripts/spark_job.py'])

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 24),
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    description='An example DAG',
    schedule_interval='@daily',
)

t1 = PythonOperator(
    task_id='run_spark_job',
    python_callable=run_spark_job,
    dag=dag,
)
