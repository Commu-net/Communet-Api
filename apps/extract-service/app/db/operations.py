from db import connect
from models.schema import EmailModel

Users = connect.User_collection
Emails = connect.Email_collection

async def insertEmails(emails : list[str], names : list[str] , company_names : list[str]) -> None:
    global Users
    global Emails 
    
    
    for i in range(0 , len(emails)):
        # data : EmailModel = {
        #     'emails' : emails[i],
        #     'name' : names[i],
        #     'currentDesignation' : company_names[i]
        # }
        
        data : EmailModel = EmailModel(
            email=emails[i],
            name=names[i],
            currentDesignation=company_names[i]
        )
        
        inserted_email = ''
        #If this email already exists  we wont add it twice 
        dumped_data = data.model_dump(mode='to_python')
        
        try:
            if await Emails.find_one({"email" : dumped_data.get('email')}) is None or await Emails.find_one({"name" : dumped_data.get('name')}) is None:
                inserted_email = await Emails.insert_one(dumped_data)
                print(inserted_email)

        except Exception as e:
            print(e)
            
            
            
        