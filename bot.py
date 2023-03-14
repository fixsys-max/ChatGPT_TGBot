import telebot
import openai


# API-keys
openai.api_key = "OpenAI-API-key"
telegram_token = "Telegram-API-key"

# Telegram-bot initialisation
bot = telebot.TeleBot(telegram_token)


# /start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 "Hello! I am a bot that uses the ChatGPT model to generate text.\n"
                 "Привет! Я бот, который использует модель ChatGPT для генерации текста.\n")


# Handler for messages
@bot.message_handler(content_types=["text"])
def generate_response(message):
    # Getting the text of the message
    text = message.text

    # Using gpt model for answer
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}])

    # Sending message
    bot.send_message(message.chat.id, response.choices[0].message['content'])


# Bot launch
bot.polling()
