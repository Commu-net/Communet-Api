from utils.validator import verify_email
import dns.resolver
import asyncio

def generate_email_patterns(first_name : str , last_name : str , company_domain : str):
    # Define the email patterns without duplicates
    email_patterns = ['{first}', '{f}{last}', '{first}.{last}',  '{f}.{last}', '{last}{f}', '{first}_{last}']

    # Generate email patterns with the company name as the domain for both '.com' and '.net'
    email_patterns_with_domain = [f'{pattern}@{company_domain}.com' for pattern in email_patterns]
    # email_patterns_with_domain += [f'{pattern}@{company_domain}.net' for pattern in email_patterns]
    emails = [pattern.format(first=first_name.lower(),
                                                  last=last_name.lower(),
                                                  f=first_name[0])
                                   for pattern in email_patterns_with_domain]
    
    return emails


def check_mails(emails : list):
    valid_emails = []
    try:
        for email in emails :
            print(f"Validating {email}")
            # result = await asyncio.wait_for(verify_email(email),timeout=10.0)
            result = verify_email(email)
            if result == True :
                valid_emails.append(email)
    except dns.resolver.NoAnswer as e :
            print(e)
            return valid_emails 
    except dns.resolver.NXDOMAIN as e :
            print(e)
            return valid_emails
    except Exception as e:
            print(e)
    
    return valid_emails

