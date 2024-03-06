from email_validator import validate_email
import socket 
import smtplib
import dns.resolver

def verify_email(email):
  
        # Check that the email address is valid. Turn on check_deliverability
        # for first-time validations like on account creation pages (but not
        # login pages).
        emailinfo = validate_email(email, check_deliverability=True)    
        # After this point, use only the normalized form of the email address,
        # especially before going to a database query.

        email = emailinfo.normalized

        # Extract domain from email address
        domain = email.split('@')[-1]

        # Resolve MX records for the domain
        default_resolver = dns.resolver.get_default_resolver()
        response = default_resolver.resolve(domain, "MX")

        # Sort and filter out null MX records
        mtas = sorted([(r.preference, str(r.exchange).rstrip('.')) for r in response])
        mtas = [(preference, exchange) for preference, exchange in mtas if exchange != ""]

        deliverability_info = {"mx": mtas, "mx_fallback_type": None}

        if len(mtas) == 0:  # No MX records found, try A records
            print("a")
            response = default_resolver.resolve(domain, "A")
            deliverability_info["mx"] = [(0, str(r)) for r in response]
            deliverability_info["mx_fallback_type"] = "A"
        
        if len(deliverability_info) == 0:  # No A records found, try AAAA records
            print("aaa")
            response = default_resolver.resolve(domain, "AAAA")
            deliverability_info["mx"] = [(0, str(r)) for r in response]
            deliverability_info["mx_fallback_type"] = "AAAA"
        
        mxRecord = deliverability_info.get("mx", None)
        
        if mxRecord is None or len(mtas) == 0:
            raise dns.resolver.NoAnswer("No MX record found")

        print(mxRecord)

        host = socket.gethostname()

        for preference, exchange in mxRecord:
            try:
                print(exchange)
                server = smtplib.SMTP()
                server.set_debuglevel(0)
                server.connect(exchange)
                server.helo(host)
                server.mail(email)
                code, message = server.rcpt(email)
                server.quit()

                # Assume 250 as Success
                if code > 200 and code < 300:
                    print(f"{email} is valid")
                    return True
                else:
            # This block will run if no mail server from the MX records was able to verify the email address
                    print(f"Invalid mail")
                    return False
              
            except Exception as e:
                # Handle exceptions here, e.g., connection errors
                print(f"Verification failed for {exchange}: {str(e)}")
        

        # The exception message is human-readable explanation of why it's
        # not a valid (or deliverable) email address.
        return False

