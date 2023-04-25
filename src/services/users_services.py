from database.utils import conn
from src.exceptions import UserAlreadyExists, UserNotExists

class UserService : 

    def __init__(self, conn) -> None:
        self.conn = conn 

    @classmethod
    def check_query(cls, cur, user_id, exception_class):

        affected_rows = cur.rowcount
        if affected_rows < 1:
            raise exception_class(user_id)

        try : 
            user_row = cur.fetchone()
            return user_row
        
        except Exception as e :
            return user_id

        
    def create_user(self, data) : 
        
        with self.conn.cursor() as cur:

            cur.execute( """
                            INSERT INTO users (id, nom, prenom, age)
                            VALUES (%s, %s, %s, %s)
                            ON CONFLICT (id) DO NOTHING
                        """,
                        tuple(data.split(","))   
                        )

            user_id = data.split(',')[0]

            user_row = self.check_query(cur, user_id, UserAlreadyExists)

            self.conn.commit()

            return user_row
            

    def get_users_info(self, user_id) : 
        
        with self.conn.cursor() as cur: 
            
            cur.execute("SELECT * FROM users where id= %s", (user_id, ) )

            user_row = self.check_query(cur, user_id, UserNotExists)

            return user_row 
        
