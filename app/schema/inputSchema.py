from pydantic import BaseModel
from typing import List,Any, Optional

class InputData(BaseModel):
    wather: Optional[Any] = None
    soil: Optional[Any] = None
    
    
    
    