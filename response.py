from datetime import datetime
import helper_function as hf

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

    ## TODO: To copy from Super User
    
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

    if user_message[:5] == 'stock':
        raw_text = user_message.split(' ')
        try:
            stock_name = raw_text[1]
        except IndexError:
            return "Please specify Stock Name"
        try:
            stock_action = raw_text[2]
        except IndexError:
            return "Please specify the action"
        if stock_action in ['hist','history','h']:
            return hf.stock_history(stock_name)
        elif stock_action in ['info','information','i']:
            return hf.stock_info(stock_name)
    #CANDO : Add a return command to reply to unknown messages
