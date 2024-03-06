from pydantic import BaseModel , Field 
# from fastapi import UploadFile
from typing import Optional

# class UploadFileRequest(BaseModel):
#     file : UploadFile
#     user_id : Optional[str] = None
#     user_email : str = Field(...)

class VerifyEmailModel(BaseModel):
    user_email : str 
    first_name : str
    last_name : str 
    company_domain :  str