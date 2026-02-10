from airflow import DAG
from airflow.providers.microsoft.mssql.operators.mssql import MsSqlOperator
from datetime import datetime



with DAG("test_mssql_conn", start_date=datetime(2025,1,1), schedule=None, catchup=False) as dag:
    t1 = MsSqlOperator(
        task_id="ping",
        mssql_conn_id="192.168.5.41",
        sql="SELECT 1;",
    )