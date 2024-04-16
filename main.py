import telebot
import google.generativeai as genai
import requests

bot = telebot.TeleBot("6793745268:AAGBxwcQVjRoZWoT6t3qg2aGDQI_UHwuDnc", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

genai.configure(api_key="AIzaSyAh-7_6xueerhPuP32cSYj1uD7al0KBMJg")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["hi!"]
  },
  {
    "role": "model",
    "parts": ["Hey there! How can I assist you today?"]
  },
  {
    "role": "user",
    "parts": ["what kind of bot you are?"]
  },
  {
    "role": "model",
    "parts": [" 👋 Добро пожаловать в SmartFinance Assistant! Я здесь, чтобы помочь вам управлять вашими финансами легко и эффективно./n Чтобы начать, вот что я могу для вас сделать:/n 💡 Предоставить персонализированные советы по бюджету и сбережениям./n 📊 Анализировать ваши расходы и доходы для лучшего планирования./n 🔍 Найти лучшие способы инвестирования и экономии денег. 🏦 Подключиться к вашему банковскому счету для удобного управления./n 📈 Помочь вам достичь ваших финансовых целей."]
  },
])

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    convo.send_message(message.text)
    response = (convo.last.text)
    bot.reply_to(message, response)

bot.infinity_polling()


