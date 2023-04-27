from fastapi import FastAPI
from src.exceptions.exceptions_api import exception_handlers_api

from src.routes.router import create_router

def create_application() -> FastAPI:

    user_router = create_router()

    app = FastAPI()
    app.include_router(user_router)
    exception_handlers_api(app)
    
    return app


app = create_application() 
