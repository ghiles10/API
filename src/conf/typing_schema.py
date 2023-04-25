from typing import Dict, List, Optional, Sequence
from pydantic import BaseModel


class DatabaseConf(BaseModel): 
    """Database configuration"""
    
    host : str
    port : int
    dbname : str
    user : str
    password : str
    

