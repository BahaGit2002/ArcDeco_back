import telepot

token = '5486021009:AAEhdGYan8pdYkosXenSs8CDDVyDcK2Fbp4'
my_id = 2007559970
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(my_id, text, parse_mode="Markdown")

