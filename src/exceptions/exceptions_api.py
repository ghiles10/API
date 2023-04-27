from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.exceptions.exceptions import UserNotExists, UserAlreadyExists


def exception_handlers_api(app: FastAPI) -> None:
    
    @app.exception_handler(UserNotExists)
    def handle_user_not_exists_exception(request: Request, exc: UserNotExists):
        return JSONResponse(status_code=404, content="User doesn't exist")

    @app.exception_handler(UserAlreadyExists)
    
    def handle_user_not_found_exception(request: Request, exc: UserAlreadyExists):
        return JSONResponse(status_code=400, content="User already exist")


    return None