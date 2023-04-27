import sys
sys.path.append(".")

from database.query import USERS_QUERY 
from database.utils import get_postgres_connection

from src.conf.conf_load import load_config
from src.conf.typing_schema import DatabaseConf 

database_conf = DatabaseConf(** load_config().data["database_config"])

conn = get_postgres_connection(database_conf.host,database_conf.port, database_conf.dbname, 
                               database_conf.user, database_conf.password )


# Création d'une table dans la base de données
with conn.cursor() as cur:
    cur.execute( USERS_QUERY )
    conn.commit()

