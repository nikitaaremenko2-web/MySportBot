import telebot
from telebot import types 

# --- ВАШ ТОКЕН ---
TOKEN = '8349342282:AAEOTrRSlPdQiIEwCf9j4sgKfCHkscL8fAU'

# Ініціалізуємо бота
bot = telebot.TeleBot(TOKEN)

# --- ОБРОБНИК КОМАНДИ /start ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    rates_button = types.InlineKeyboardButton(text="⚽️ Поточні Ставки", callback_data="/rates")
    balance_button = types.InlineKeyboardButton(text="💰 Мій Баланс", callback_data="/balance")
    help_button = types.InlineKeyboardButton(text="❓ Допомога", callback_data="/help")
    keyboard.add(rates_button)
    keyboard.add(balance_button, help_button) 

    welcome_text = (
        "👋 **Вітаю! Я — бот 'Ставки на спорт'.**\n\n"
        "Я допоможу вам швидко переглянути актуальні коефіцієнти та зробити ставки.\n"
        "Оберіть дію, щоб розпочати:"
    )

    bot.send_message(
        message.chat.id, 
        welcome_text, 
        reply_markup=keyboard, 
        parse_mode="Markdown" 
    )

# --- ОБРОБНИК НАТИСКАННЯ КНОПОК ---
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "/rates":
        bot.send_message(call.message.chat.id, "Ви натиснули 'Поточні Ставки'. Тут буде список ігор та коефіцієнтів.")
    elif call.data == "/balance":
        bot.send_message(call.message.chat.id, "Ваш баланс: 0.00 UAH. Поповніть рахунок!")
    elif call.data == "/help":
        bot.send_message(call.message.chat.id, "З усіх питань звертайтесь до Адміна.")

    bot.answer_callback_query(call.id)
  
