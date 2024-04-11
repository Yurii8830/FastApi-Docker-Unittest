from pydantic import BaseModel
from datetime import date

class Record(BaseModel):
    title: str
    content: str
    user_id: int
    date: date
