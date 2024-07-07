from pydantic import BaseModel

class Slot(BaseModel):
    display: str
    fill: bool = False
    value: float = 0
