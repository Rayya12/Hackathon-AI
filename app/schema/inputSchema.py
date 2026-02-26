from pydantic import BaseModel
from typing import List

class InputData(BaseModel):
    nitrogen : List[float]
    temperature : List[float]
    humidity : List[float]
    ph : List[float]
    rainfall : List[float]
    
    
    
    