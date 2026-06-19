from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import datetime
import papermill as pm

# Note: We use Papermill to execute the Jupyter Notebook automatically.
# Make sure papermill is installed in the Airflow environment.

def run_model_training():
    print("Starting model training by executing Jupyter Notebook...")
    
    # Path to the Jupyter Notebook (adjust the path to match Airflow's worker environment)
    input_notebook = '/opt/airflow/project/ML_Modeling.ipynb'
    output_notebook = '/opt/airflow/project/ML_Modeling_executed.ipynb'
    
    # Execute notebook using Papermill
    try:
        pm.execute_notebook(
            input_notebook,
            output_notebook
        )
        print("Model training completed successfully.")
    except Exception as e:
        print(f"Error during model training: {e}")
        raise e

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
}

dag = DAG(
    'travel_model_training_pipeline',
    default_args=default_args,
    description='Automated workflow for Travel Data Regression Models',
    schedule_interval=datetime.timedelta(days=1),
)

train_models_task = PythonOperator(
    task_id='train_models',
    python_callable=run_model_training,
    dag=dag,
)

# If we had data extraction and transformation steps, they would go here:
# extract_data_task >> transform_data_task >> train_models_task

train_models_task
