from psycopg2.extensions import connection, cursor

from src.exceptions.exceptions import UserAlreadyExists, UserNotExists
from src.models_response.users import User, CreateUserResponse


class UserService:

    """ this class allows for the user to interact with the api"""

    def __init__(self, conn :connection ) -> None :

        self.conn = conn 


    @classmethod
    def check_query(cls, cur:cursor , user_id: str, exception_class: Exception):
        
        """ to check if the request works well and returns what is requested  """

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

        
    def create_user(self, data: User) -> CreateUserResponse : 

        """ allow to create user """
        
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

            return CreateUserResponse(** {"user_id":user_row } ) 
            

    def get_users_info(self, user_id : str) -> User : 

        """ retieve user informations """
        
        with self.conn.cursor() as cur: 
            
            cur.execute("SELECT * FROM users where id= %s", (user_id, ) )

            # checking 
            user_row = self.check_query(cur, user_id, UserNotExists)

            # Get column names
            column_names = [desc[0] for desc in cur.description]

            # combining column names with row values
            user_dict = dict(zip(column_names, user_row))

            self.conn.commit()

            return User( **user_dict ) 
        
    
    def update_user(self, user_id: str, data_update: User) -> CreateUserResponse : 
        
        """update user infos"""
        
        if self.get_users_info( user_id) != None : 
            
            with self.conn.cursor() as cur:
                
                data_update = data_update.dict()
                cur.execute( """
                                UPDATE users
                                SET nom = %s, prenom = %s, age = %s
                                WHERE id = %s
                            """,
                            ( data_update['nom'], data_update['prenom'], data_update['age'], data_update['id'] ) 
                            )
                
                user_row = self.check_query(cur, user_id, UserNotExists)

                self.conn.commit()

                return CreateUserResponse(**{"user_id":user_row } ) 
                     
            
    def delete_user(self, user_id: str) -> CreateUserResponse : 
        
            with self.conn.cursor() as cur:

                cur.execute( """
                            DELETE FROM users where id= %s
                            """,
                            (user_id, )
                            )

                
                user_row = self.check_query(cur, user_id, UserNotExists)

                self.conn.commit()

                return CreateUserResponse(** {"user_id":user_row } ) 
        