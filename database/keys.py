from pydantic import BaseModel
from typing import List

class create_key(BaseModel):
    name :str
    scope : List[str] = ['read']
    limit :int = 60