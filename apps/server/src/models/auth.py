from pydantic import BaseModel, EmailStr

class EmailSchema(BaseModel):
    email: EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    code: str

class Token(BaseModel):
    access_token: str
    token_type: str
