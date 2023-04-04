import os
import telegram
import openai
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MODEL_ENGINE = os.getenv('MODEL_ENGINE', 'text-davinci-002')
MAX_TOKENS = int(os.getenv('MAX_TOKENS', 60))
STOP = os.getenv('STOP', '')
TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
N = int(os.getenv('N', 1))

bot = telegram.Bot(token=TELEGRAM_TOKEN)

openai.api_key = OPENAI_API_KEY

def generate_message(message_text):
    prompt = f"{message_text.strip()} [CHAT GPT]"
    response = openai.Completion.create(
        engine=MODEL_ENGINE,
        prompt=prompt,
        max_tokens=MAX_TOKENS,
        n=N,
        stop=STOP,
        temperature=TEMPERATURE,
    )
    message = response.choices[0].text.strip()
    return message

def handle_message(update, context):
    message_text = update.message.text
    reply_text = generate_message(message_text)
    update.message.reply_text(reply_text)

def main():
    updater = telegram.Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(telegram.MessageHandler(telegram.Filters.text & ~telegram.Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
