from pydantic import BaseModel


class User(BaseModel) : 

    id: str
    nom: str 
    prenom: str
    age: int 


class CreateUserResponse(BaseModel) : 

    user_id: str

