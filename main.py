import constants as keys
from telegram.ext import *
import response as R
import users

print("Bot Started...")

def start_command(update, context):
    update.message.reply_text('Type something random to get started!')


def help_command(update, context):
    update.message.reply_text('If you need any help! You asked Del for it.')

def handle_message(update,context):
    text = str(update.message.text).lower()
    print(">>>> User Id : ",update.message.from_user.id,"<<<<")
    print(">>> Message : ",update.message.text,"<<<")
    if int(update.message.from_user.id) in users.super_user_list:
        response = R.super_user_response(text)
    else:
        response = R.normal_user_response(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("Start",start_command))
    dp.add_handler(CommandHandler("Start", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
