from pydantic import BaseModel


class OutputData(BaseModel):
    prediction_class : str
    probability : float
    top3 : dict[str,float]