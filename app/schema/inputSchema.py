from pydantic import BaseModel
from typing import List,Any, Optional

class InputData(BaseModel):
    weather: Optional[Any] = None
    soil: Optional[Any] = None
    
    
    
    