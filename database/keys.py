from pydantic import BaseModel , Field
from typing import List
from datetime import datetime 

class create_key(BaseModel):
    api_key: str
    name :str
    scope : List[str] = Field(default_factory=List)
    rate_limit : int = 10
    usage_count :int = 0
    created_at : datetime = Field(default_factory=datetime.utcnow)
    is_active : bool 