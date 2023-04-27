import psycopg2
from psycopg2.extensions import connection


def get_postgres_connection( host:str, port: int, dbname :str, user:str, password: str ) -> connection : 
    
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )

    return conn



