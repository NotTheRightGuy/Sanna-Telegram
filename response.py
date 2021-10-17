from datetime import datetime

def normal_user_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello','hi','sup','yo'):
        return "Hey! How's it going?"
    if user_message in ("who are you","who are you?"):
        return "I'm Sanna!"
    if user_message in ("time",'time?'):
        now = datetime.now()
        date_time = now.strftime("%A %d %b %Y, %I:%M")

        return str(date_time)
    if user_message in ('sanna'):
        return "Kya hai bsdk?"


def super_user_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ('sanna'):
        return "Yes Daddy?"
    
    if user_message in ('hello','hi','sup','yo'):
        return "Hey! How's it going?"
    if user_message in ("who are you","who are you?"):
        return "I'm Sanna!"
    if user_message in ("time",'time?'):
        now = datetime.now()
        date_time = now.strftime("%A %d %b %Y, %I:%M")

        return str(date_time)

    #CANDO : Add a return command to reply to unknown messages
