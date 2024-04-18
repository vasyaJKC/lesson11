from telebot import TeleBot
from keyboard import generate_main_menu, laptop_manu, buy_laptop
from parser_laptops import product_data

token = '7161393431:AAEbBFmJ32Z7vOPyxpqBTRZpWsn-PzI0_zY'
bot = TeleBot(token)

data_name = product_data[0]['Noutbok nomi']
data_price = product_data[0]['Noutbok narxi']
data_kridit = product_data[0]["Muddatli to'lov"]
data_image = product_data[0]["Noutbok rasmi"]
@bot.message_handler(['start'])
def start(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_id = message.from_user.id
    send_mess = f'Salom!\nIsmingiz: {first_name}\nFamiliyangiz{last_name}\nSizning user ID: {user_id}'
    contact = bot.send_message(chat_id, send_mess, reply_markup=generate_main_menu())
    bot.register_next_step_handler(contact, registeration)

def registeration(message):
    chat_id = message.chat.id
    phone_number = message.contact.phone_number
    bot.send_message(chat_id, f"Siz {phone_number} nomer orqali ro'yxatdan o'tdingiz!", reply_markup=laptop_manu())
    bot.register_next_step_handler(message, laptop)


def laptop(message):
    chat_id = message.chat.id
    if message.text == 'Laptop':
        for product in product_data:
            product_image = product["Noutbok rasmi"]
            product_name = product['Noutbok nomi']
            product_price = product['Noutbok narxi']
            product_kredit = product["Muddatli to'lov"]
            laptop_data = f"Noutbok nomi: {product_name}\n\nNoutbok narxi: {product_price}\n\nMudatli to'lov: {product_kredit}"
            bot.send_photo(chat_id, product_image, caption=laptop_data, reply_markup=buy_laptop())




while True:
    try:
        print("Bot run!")
        bot.polling()

    except:
        print("error")
        bot.stop_polling()
        



