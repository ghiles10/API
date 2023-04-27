from fastapi import APIRouter 
from fastapi import FastAPI

from database.utils import get_postgres_connection 
from src.services.users_services import UserService
from src.models_response.users import User, CreateUserResponse
from src.conf.conf_load import load_config
from src.conf.typing_schema import DatabaseConf 


# load configuration file 
database_conf = DatabaseConf(** load_config().data["database_config"])

# get postgres connection object cursor 
conn = get_postgres_connection(database_conf.host,database_conf.port, database_conf.dbname, 
                               database_conf.user, database_conf.password )

user_service = UserService(conn)

def create_router():

    router = APIRouter(
        prefix="/api", 
        tags=["users"]
    )


    @router.get("/{id}", response_model=User )
    def get_id(id : str):

        return user_service.get_users_info(id)  
    
    
    
    @router.post("/add_users",  status_code=201, response_model= CreateUserResponse )
    def add_user(data: User):
        
        return user_service.create_user(data)
    
    @router.put("/update_user", response_model= CreateUserResponse  )
    def update_user(user_id : str, data_update : User) : 
        
        return user_service.update_user(user_id,data_update )
 

    @router.delete("/delete_user", response_model = CreateUserResponse )
    def delete_user(user_id: str) : 
        
        return user_service.delete_user(user_id)
        
        
    return router

def create_application() -> FastAPI:

    user_router = create_router()

    app = FastAPI()
    app.include_router(user_router)
    
    return app


app = create_application() 