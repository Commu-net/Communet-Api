from fastapi import APIRouter , Form  , UploadFile
from fastapi.responses import JSONResponse
from utils.extractor import extract_excel
from utils import generate_patterns 
from typing import Optional
from models.models import VerifyEmailModel
from db.operations import insertValidatedMails

router = APIRouter()

@router.post("/api/v1/parser")
async def parse_emails(user_email : str = Form(), file : UploadFile = Form()) -> JSONResponse:
    try:

        supported_extensions = {'xls', 'xlsx', 'xlsm', 'xlsb', 'odf', 'ods', 'odt' , 'csv'}

        if file is None:
            return JSONResponse({"message": "No File found"}, status_code=404)

        extension = file.filename.split('.')[-1]

        if extension not in supported_extensions:
            return JSONResponse(content={"message": "Format not supported"}, status_code=401)

        await extract_excel(file,user_email)

        return JSONResponse({"message": "Received"})

    except Exception as e:
        print(e)
        return JSONResponse({"message": "Server error"}, status_code=500)
    
@router.post("/api/v1/verify")
async def verify_email(payload : VerifyEmailModel) -> JSONResponse :
    
    print(payload)
    email_patterns = generate_patterns.generate_email_patterns(payload.first_name,payload.last_name,payload.company_domain)
    print(email_patterns)
    valid_emails = generate_patterns.check_mails(email_patterns)
    # print(3)
    
    if len(valid_emails) == 0 :
        return JSONResponse({"message" : "Cant generate valid emails from given information"} , status_code=401)
    
    name = f"{payload.first_name} {payload.last_name}"
    
    # print(4)
    
    await insertValidatedMails(valid_emails , name , payload.company_domain , payload.user_email)
    
    # print(5)
    
    return JSONResponse({"emails" : valid_emails , "message" : "emails were added to your account"})

@router.get("/")
async def read_root():
    return {"Hello": "World"}