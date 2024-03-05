from fastapi import UploadFile
import pandas as pd 
import uuid 
from typing import Optional
from math import ceil
import re
from db import connect , operations
import os 

chunk_size = 1024 * 1024

async def extract_excel(file : UploadFile ,  user_email : str) -> int | None:
    
    file_extension = file.filename.split('.')[-1]
    fileid = f'{uuid.uuid1()}.{file_extension}'
    
    global chunk_size
    
    if user_email is None :
        
        raise ValueError("user email not found")
    
    company_names : list[str] = []
    names : list[str] = []
    emails : list[str] = []
    
    with open(f'./upload/{fileid}','wb+') as f:
        num_chunks = ceil(file.size / chunk_size)
        num_chunks_remaining = num_chunks

        while num_chunks_remaining > 0:
            chunk = await file.read(chunk_size)
            if not chunk:
                break
            f.write(chunk)
            num_chunks_remaining -= 1
        
    with open(f'./upload/{fileid}','rb+') as f:
        
        df = pd.read_excel(f'./upload/{fileid}')
        
        df.fillna(value=str(''),inplace=True)
        
        if df is None or df.columns is None :
            raise Exception('DataFrame is empty')    
        
        name_col : str | None = findNames(df.columns)

        if name_col is not None :
            name_row = df[f'{name_col}']
            for row in name_row:
                names.append(str(row))
        
        company_col : str | None = findCompanyName(df.columns)
        
        if company_col is not None :
            company_row = df[f'{company_col}']
            for row in company_row:
                company_names.append(str(row))
                
        email_col : str | None = findEmailName(df.columns)
        
        if email_col is None : 
            raise Exception('No column containing emails found')
        
        else :
            email_row = df[f'{email_col}']

            for row in email_row :
                emails.append(verifyEmails(str(row)))
    
    if len(company_names) == 0 : 
        company_names = ['' for _ in range(0,len(emails))]
    
    if len(names) == 0 :
        names = ['' for _ in range(0 , len(emails)) ] 
    
    os.remove(f'./upload/{fileid}')
  
    await operations.insertEmails(emails,names,company_names,user_email)
    

              
def findNames(columns : list[str]) -> str | None:
    name_pattern = r'\b(?:name|names|username|usernames)\b'

    for col in columns :
        if re.match(name_pattern , col.lower().strip()) is not None :
            return col 
    
    return None

def findCompanyName(columns : list[str]) -> str | None :
    
    company_pattern = r'\b(?:company|companies|company name|company_name|business|enterprise|firm|corporation|inc)\b'
    
    for col in columns :
        if re.match(company_pattern,col.lower().strip()) is not None:
            return col
        
    return None

def findEmailName(columns : list[str]) -> str | None : 
    
    email_pattern = r'.*email.*'
    
    for col in columns :
        if re.match(email_pattern , col.lower().strip()) is not None :
            return col 
        
    return None 

def verifyEmails(email: str) -> str:
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(email_pattern, email) is not None:
        return email
    
    return ''

