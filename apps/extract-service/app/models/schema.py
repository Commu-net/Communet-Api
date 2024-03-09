from typing import List , Optional
from pydantic import BaseModel, Field
from datetime import datetime

class UserModel(BaseModel):
    name: str
    email: str
    sub: str
    picture: str
    googleId: str
    accessToken: str
    emailSelected: List[str]
    rToken: str

    class Config:
        populate_by_name = True
        
class EmailModel(BaseModel):
    email: str
    name: str
    currentDesignation: Optional[str] = Field(default="")
    addedOn: datetime = Field(default=datetime.now())
    company: Optional[str] = Field(default="")


    class Config:
        populate_by_name = True