from fastapi import APIRouter 
from fastapi import FastAPI

from database.utils import get_postgres_connection 
from src.services.users_services import UserService
from src.models_response.users import User, CreateUserResponse
from src.conf.conf_load import load_config
from src.conf.typing_schema import DatabaseConf 

database_conf = DatabaseConf(** load_config().data["database_config"])

conn = get_postgres_connection(database_conf.host,database_conf.port, database_conf.dbname, 
                               database_conf.user, database_conf.password )

user_service = UserService(conn)

def create_router():

    router = APIRouter(
        prefix="/api", 
        tags=["users"]
    )

    @router.get("/users/{id}" )
    def get_id(id):
        return user_service.get_users_info(id)  
    
    
    @router.post("/add_users",  status_code=201, response_model= CreateUserResponse )
    def add_user(data: User):
        

        return user_service.create_user(data)

    return router 


def create_application() -> FastAPI:

    user_router = create_router()

    app = FastAPI()
    app.include_router(user_router)
    
    return app


app = create_application() 