import psycopg2
from psycopg2.extensions import connection

# from src.conf.conf_load import load_config
# from src.conf.typing_schema import DatabaseConf 

# database_conf = DatabaseConf(** load_config().data["database_config"])

def get_postgres_connection( host:str, port: int, dbname :str, user:str, password: str ) -> connection : 
    
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )

    return conn



