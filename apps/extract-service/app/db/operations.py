from db import connect
from models.schema import EmailModel , UserModel
from pymongo.errors import DuplicateKeyError

Users = connect.User_collection
Emails = connect.Email_collection

async def insertEmails(emails : list[str], names : list[str] , company_names : list[str] ,user_email : str) -> None:
    global Users
    global Emails 
    
    
    for i in range(0 , len(emails)):
        # data : EmailModel = {
        #     'emails' : emails[i],
        #     'name' : names[i],
        #     'currentDesignation' : company_names[i]
        # }
        
        data = EmailModel(
            email=emails[i],
            name=names[i],
            currentDesignation=company_names[i]
        )
        
        inserted_email = ''
        # If this email already exists, we won't add it twice 
        dumped_data = data.model_dump(mode='to_python')
        
        try:
            # if await Emails.find_one({"email" : dumped_data.get('email')}) is None or await Emails.find_one({"name" : dumped_data.get('name')}) is None:
            try:
                    inserted_email = await Emails.insert_one(dumped_data)
            except DuplicateKeyError:
                        print("Email already exists in the database. Skipping insertion.")
                        inserted_email = await Emails.find_one({"email": dumped_data.get('email')})

            user = await Users.find_one({"email" : user_email})
            if user is None :
                raise Exception("User not found")
            update_user = await Users.update_one(
                filter={"email" : user_email},
                update={"$addToSet" : {"emailSelected" : inserted_email['_id']}})
            
        except Exception as e:
            print(e)

async def insertValidatedMails(emails : list[str] , name : str , company_name : str,user_email : str):
    
    for i in range(0 , len(emails)):
        # data : EmailModel = {
        #     'emails' : emails[i],
        #     'name' : names[i],
        #     'currentDesignation' : company_names[i]
        # }
        
        data = EmailModel(
            email=emails[i],
            name=name,
            currentDesignation=company_name
        )
        
        inserted_email = ''
        # If this email already exists, we won't add it twice 
        dumped_data = data.model_dump(mode='to_python')
        
        try:
            # if await Emails.find_one({"email" : dumped_data.get('email')}) is None or await Emails.find_one({"name" : dumped_data.get('name')}) is None:
            try:
                    inserted_email = await Emails.insert_one(dumped_data)
            except DuplicateKeyError:
                        print("Email already exists in the database. Skipping insertion.")
                        inserted_email = await Emails.find_one({"email": dumped_data.get('email')})

            user = await Users.find_one({"email" : user_email})
            if user is None :
                raise Exception("User not found")

            await Users.update_one(
                filter={"email" : user_email},
                update={"$addToSet" : {"emailSelected" : inserted_email['_id']}})
            
        except Exception as e:
            print(e)
            
            
        