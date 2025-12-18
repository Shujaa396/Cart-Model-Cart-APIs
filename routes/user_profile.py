from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from database import get_session
from auth.jwt_auth import get_current_user
from models.user import User
from schemas.user_profile import UserProfileResponse, UserProfileUpdate

router = APIRouter()
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != "dummy_user_token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": "admin", "module_assigned": "inventory"}

@router.get("/user/profile", response_model=UserProfileResponse)
def get_user_profile(user=Depends(get_current_user), session: Session = Depends(get_session)):
    db_user = session.query(User).filter(User.username == user["username"]).first()
    return {
        "username": db_user.username,
        "module_assigned": db_user.module_assigned
    }

@router.patch("/user/profile")
def update_user_profile(
    data: UserProfileUpdate,
    user=Depends(get_current_user),
    session: Session = Depends(get_session)
):
    db_user = session.query(User).filter(User.username == user["username"]).first()
    db_user.module_assigned = data.module_assigned
    session.commit()
    return {"message": "Module updated"}
