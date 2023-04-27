from src.exceptions import UserAlreadyExists, UserNotExists
from psycopg2.extensions import connection
from src.models_response.users import User

class UserService : 


    def __init__(self, conn :connection ) -> None:
        self.conn = conn 

    @classmethod
    def check_query(cls, cur, user_id, exception_class):


        # checking behavioral query
        affected_rows = cur.rowcount
        if affected_rows < 1: 
            raise exception_class(user_id)

        try : 
            user_row = cur.fetchone()
            return user_row
        
        # if insert, user_row == none
        except Exception as e :
            return user_id

        
    def create_user(self, data: User) -> str : 
        
        with self.conn.cursor() as cur:

            cur.execute( """
                            INSERT INTO users (id, nom, prenom, age)
                            VALUES (%s, %s, %s, %s)
                            ON CONFLICT (id) DO NOTHING
                        """,
                        tuple( data.dict().values() ) 
                        )

            user_id = data.dict()['id']
            
            user_row = self.check_query(cur, user_id, UserAlreadyExists)

            self.conn.commit()

            return {"user_id":user_row}
            

    def get_users_info(self, user_id : str) -> User : 
        
        with self.conn.cursor() as cur: 
            
            cur.execute("SELECT * FROM users where id= %s", (user_id, ) )

            user_row = self.check_query(cur, user_id, UserNotExists)

            # Get column names
            column_names = [desc[0] for desc in cur.description]

            # combining column names with row values
            user_dict = dict(zip(column_names, user_row))

            self.conn.commit()

            return user_dict
        
