import psycopg2

from src.conf.conf_load import load_config
from src.conf.typing_schema import DatabaseConf 

database_conf = DatabaseConf(** load_config().data["database_config"])


conn = psycopg2.connect(
    host=database_conf.host,
    port=database_conf.port,
    dbname=database_conf.dbname,
    user=database_conf.user,
    password=database_conf.password
)


