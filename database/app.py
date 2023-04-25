
import sys
sys.path.append(".")

from database.query import USERS_QUERY 
from database.utils import conn


# Création d'une table dans la base de données
with conn.cursor() as cur:
    cur.execute( USERS_QUERY )
    conn.commit()

