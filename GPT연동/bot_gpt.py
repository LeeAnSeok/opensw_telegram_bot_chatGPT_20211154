import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler
from openai import OpenAI


TOKEN = "6881294482:AAEwliP1LDBTVEyYYs4sGuNxeRi7S0i9qis"


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=chatGPT(update.effective_message.text))

def chatGPT(request_message):
  # client = OpenAI(
  #     api_key="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"
  # )

  # completion = client.chat.completions.create(
  #   model="gpt-3.5-turbo",
  #   messages=[
  #     {"role": "system",
  #      "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
  #     {"role": "user", "content": request_message}
  #   ],
  #   response_format={"type": "json_object"}
  # )

  # return completion.choices[0].message['content']
  return "GPT Echo 결과값: " + request_message


if __name__ == '__main__':
    application = ApplicationBuilder().token("6881294482:AAEwliP1LDBTVEyYYs4sGuNxeRi7S0i9qis").build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()