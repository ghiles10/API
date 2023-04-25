from fastapi import APIRouter 
from fastapi import FastAPI

from database.utils import conn 
from src.services.users_services import UserService

user_service = UserService(conn)

def create_router():

    router = APIRouter(
        prefix="/api", 
        tags=["users"]
    )

    @router.get("/users/{id}" )
    def get_id(id):
        return {"message": f"Hello {id}"}   
    
    
    @router.post("/add_users",  status_code=201)
    def add_user(data):

        return user_service.create_user(data)

    return router 


def create_application() -> FastAPI:

    user_router = create_router()

    app = FastAPI()
    app.include_router(user_router)
    
    return app



app = create_application() 