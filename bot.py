import telebot 
import os 
from dotenv import load_dotenv
load_dotenv()

bot=telebot.TeleBot(os.getenv("API_TOKEN"))


USD_TO_KGS_RATE=87.7

KGS_TO_USD_RATE= 1 / USD_TO_KGS_RATE

EUR_TO_KGS_RATE=95.13
KGS_TO_EUR_RATE= 1 / EUR_TO_KGS_RATE

USD_TO_EUR_RATE=0.92
EUR_TO_USD_RATE = 1 /USD_TO_KGS_RATE

# КОМАНДА СТАРТА 
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Привет я бот для обмен валют , напиши сумму и валюту которую хочушь обменять . \n пример  \n100 KGS\n50 USD\n 20 EUR ")

@bot.message_handler(func=lambda message : True)
def exchange_currency(message):
    try:
        text=message.text.strip().upper()
        amount , currency = text.split()
        amount= float(amount)

        if currency =="KGS":
            usd_amount= amount * KGS_TO_USD_RATE
            eur_amount=amount * KGS_TO_EUR_RATE
            bot.reply_to(message, f"{amount} KGS - {usd_amount} USD\n {eur_amount} EUR" )
        elif currency == "USD":
            kgs_amount=amount * USD_TO_KGS_RATE
            eur_amount=amount* USD_TO_EUR_RATE
            bot.reply_to(message, f"{amount} USD = {kgs_amount} KGS\n {eur_amount} EUR")
        elif  currency == "EUR":
            kgs_amount=amount * EUR_TO_KGS_RATE
            bot.reply_to(message, f" {amount} EUR - {kgs_amount } KGS\n   ")
        else:
            bot.reply_to(message, "Извините я могу обменивать  только KGS , USD , EUR")
    except ValueError:
        bot.reply_to(message, "Пожалуйста видите правильный формат . Пример : \n100 KGS\n 50 USD\n 20 EUR")

bot.polling()

        
  
