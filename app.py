# req: pip install pytelegrambotapi
import telebot

bot = telebot.TeleBot('Telegram_token')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text, end=" ")
    #print(message, end=" ")
    if message.text.lower() == "hello":
        bot.send_message(message.from_user.id, "Hello")
    elif message.text.lower() == "bye":
        bot.send_message(message.from_user.id, "Bye!")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Type  Hello or Bye")
    else:
        bot.send_message(message.from_user.id, "I don't understand you. Type /help.")

@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    #user_name = message.new_chat_member.first_name
    bot.send_message(message.chat.id, f"Welcome, user_name!")

bot.polling(none_stop=True, interval=0)
