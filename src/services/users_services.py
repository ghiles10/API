from database.utils import conn
from src.exceptions import UserAlreadyExists 

class UserService : 

    def __init__(self, conn) -> None:
        self.conn = conn 


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

            affected_rows = cur.rowcount
            if affected_rows < 1:
                raise UserAlreadyExists(user_id)
            
            cur.execute("""
                    SELECT * FROM users WHERE id = %s
                """, (user_id,))
            user_row = cur.fetchone()
            conn.commit()
            
            return user_row
            

    def get_users_info(self, user_id) : 
        