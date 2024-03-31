from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.db import create_user, get_user

app = FastAPI()

class User(BaseModel):
    username: str
    password: str
    email: str
    full_name: str

@app.post("/signup/")
def signup(user: User):
    created_user = create_user(user)
    return created_user

@app.post("/login/")
def login(user: User):
    stored_user = get_user(user.username)
    if not stored_user:
        raise HTTPException(status_code=404, detail="User not found")
    if stored_user['password'] != user.password:
        raise HTTPException(status_code=401, detail="Incorrect password")
    return {"message": "Login successful"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)