from fastapi import APIRouter , Form  , UploadFile
from fastapi.responses import JSONResponse
from utils.extractor import extract_excel
from typing import Optional

router = APIRouter()

@router.post("/api/v1/parser")
async def parse_emails(file : UploadFile = Form(...), user_id : Optional[str] = None , user_email : str = Form(...)) -> JSONResponse:
    try:

        supported_extensions = {'xls', 'xlsx', 'xlsm', 'xlsb', 'odf', 'ods', 'odt' , 'csv'}

        if file is None:
            return JSONResponse({"message": "No File found"}, status_code=404)

        extension = file.filename.split('.')[-1]

        if extension not in supported_extensions:
            return JSONResponse(content={"message": "Format not supported"}, status_code=401)

        if extension == 'csv':
            pass
        else:
            await extract_excel(file, user_email ,user_id )

        return JSONResponse({"message": "Received"})

    except Exception as e:
        print(e)
        return JSONResponse({"message": "Server error"}, status_code=500)

@router.get("/")
async def read_root():
    return {"Hello": "World"}