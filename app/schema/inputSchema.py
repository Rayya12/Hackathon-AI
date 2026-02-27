from pydantic import BaseModel
from typing import List,Any

class InputData(BaseModel):
    wather : dict[str,dict[str,List[float]]]
    soil : dict[str,Any]
    
    
    
    