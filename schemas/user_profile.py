from pydantic import BaseModel
from typing import Optional

class UserProfileResponse(BaseModel):
    username: str
    module_assigned: Optional[str]

class UserProfileUpdate(BaseModel):
    module_assigned: Optional[str]
