from fastapi import Depends, HTTPException, Header
from typing import Optional

def get_current_user(authorization: Optional[str] = Header(None)):
    if authorization == "Bearer dummy_admin_token":
        return {"username": "admin", "role": "admin"}
    elif authorization == "Bearer dummy_user_token":
        return {"username": "user1", "role": "user"}
    raise HTTPException(status_code=401, detail="Invalid token")
