import telebot 
import config 
from telebot import types
from string import Template



bot = telebot.TeleBot(config.TOKEN)


user_dict = {}


class User:
    def __init__(self, city):
        self.city = city

        keys = ['fullname', 'phone', 'driverSeria', 'repairs']
        
        for key in keys:
            self.key = None



# если /help, /start
@bot.message_handler(commands=['help', 'start'])
def welcome(message):

    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("iPhone 7")
    item2 = types.KeyboardButton("iPhone 7+")
    item3 = types.KeyboardButton("iPhone 8")
    item4 = types.KeyboardButton("iPhone X")
    item5 = types.KeyboardButton("iPhone Xr")
    item6 = types.KeyboardButton("Airpods")
    item7 = types.KeyboardButton("Lightning")
    item8 = types.KeyboardButton("Защитное стекло")
    item9 = types.KeyboardButton("Оформление заказа 📃")
    item10 = types.KeyboardButton("Заказать ремонт 🔧")
    

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы заинтересовать вас в нашей продукции.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)


 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'iPhone 7':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("iPhone 7 32gb", callback_data='Iphone7 32')
            item2 = types.InlineKeyboardButton("iPhone 7 128gb", callback_data='Iphone7 128')
            
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Какой объем памяти вас интересует?', reply_markup=markup)



        elif message.text == 'iPhone 7+':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("iPhone 7+ 32gb", callback_data='Iphone7plus 32')
            item2 = types.InlineKeyboardButton("iPhone 7+ 128gb", callback_data='Iphone7plus 128')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Какой объем памяти вас интересует?', reply_markup=markup)




        elif message.text == 'iPhone 8':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("iPhone 8 64gb", callback_data='Iphone8 64')
            item2 = types.InlineKeyboardButton("iPhone 8 64gb (переклейка экрана)", callback_data='Iphone8 2 64')
            item3 = types.InlineKeyboardButton("iPhone 8+ 64gb", callback_data='Iphone8plus 64')
            
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'Какой модель телефона вас интресует?', reply_markup=markup)




        elif message.text == 'iPhone X':

            bot.send_message(message.chat.id, 'iPhone X 64gb')
            bot.send_message(message.chat.id, '555$ 💸')



            
        elif message.text == 'iPhone Xr':

            bot.send_message(message.chat.id, 'iPhone Xr 64gb')
            bot.send_message(message.chat.id, '575$ 💸')
            

   
        elif message.text == 'Airpods':
            
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("AirPods 1", callback_data='1st')
            item2 = types.InlineKeyboardButton("AirPods 2", callback_data='2gen')
            item3 = types.InlineKeyboardButton("AirPods Pro", callback_data='pro')
 
            markup.add(item1, item2, item3)
 
            bot.send_message(message.chat.id, 'Какая версия ваc интересует?', reply_markup=markup)




        elif message.text == 'Lightning':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Поштучно", callback_data='1it')
            item2 = types.InlineKeyboardButton("Оптом", callback_data='opt')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Что ваc интересует?', reply_markup=markup)

        elif message.text == 'Защитное стекло':

            bot.send_message(message.chat.id, 'Защитное стекло на любую модель iPhone 📲')
            bot.send_message(message.chat.id, '250 грн')

        elif message.text == 'Заказать ремонт 🔧':
            chat_id = message.chat.id
            user_dict[chat_id] = User(message.text)
            # удалить старую клавиатуру
            markup = types.ReplyKeyboardRemove(selective=False)


            msg = bot.send_message(chat_id, 'Фамилия Имя Отчество', reply_markup=markup)
            bot.register_next_step_handler(msg, process_fullname_repairs)
            




        #Выбрать город 
        elif message.text == 'Оформление заказа 📃':

                
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                itembtn1 = types.KeyboardButton('Киев')
                itembtn2 = types.KeyboardButton('Одесса')
                itembtn3 = types.KeyboardButton('Харьков')
                itembtn4 = types.KeyboardButton('Днепр')
                itembtn5 = types.KeyboardButton('Запорожье')
                itembtn6 = types.KeyboardButton('Львов')
                markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)


                msg = bot.send_message(message.chat.id, 'Ваш город?', reply_markup=markup)
                bot.register_next_step_handler(msg, process_city_step)


        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')




#Ремонт 
#Номер телефона 
def process_fullname_repairs(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text


        msg = bot.send_message(chat_id, 'Ваш номер телефона:')
        bot.register_next_step_handler(msg, process_phone_repairs)


    except Exception as e:
        bot.reply_to(message, 'ooops!!')


#Что вы хотите заказать 
def process_phone_repairs(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text
        msg = bot.send_message(message.chat.id, 'Опишите вашу проблему:')
        bot.register_next_step_handler(msg, process_repairs_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


#Отправка заявки
def process_repairs_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.repairs = message.text

    
    # ваша заявка "Имя пользователя"
    bot.send_message(chat_id, getOrderData(user, 'Ваша заявка', message.from_user.first_name), parse_mode="Markdown")

    #sticker
    sti = open('static/phone.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("iPhone 7")
    item2 = types.KeyboardButton("iPhone 7+")
    item3 = types.KeyboardButton("iPhone 8")
    item4 = types.KeyboardButton("iPhone X")
    item5 = types.KeyboardButton("iPhone Xr")
    item6 = types.KeyboardButton("Airpods")
    item7 = types.KeyboardButton("Lightning")
    item8 = types.KeyboardButton("Защитное стекло")
    item9 = types.KeyboardButton("Оформление заказа 📃")
    item10 = types.KeyboardButton("Заказать ремонт 🔧")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
    bot.send_message(message.chat.id, 'Что вас ещё интресует?', reply_markup=markup)

    # отправить в группу
    bot.send_message(config.chat_id, getOrderData(user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")



# формирует вид заявки регистрации
# нельзя делать перенос строки Template
# в send_message должно стоять parse_mode="Markdown"
def getOrderData(user, title, name):
    t = Template('$title *$name* \n Заявка: *$userCity* \n ФИО: *$fullname* \n Телефон: *$phone* \n Описание проблемы: *$repairs* \n *Мы с вами свяжимся, ждите звонка!*')


    return t.substitute({
        'title': title,
        'name': name,
        'userCity': user.city,
        'fullname': user.fullname,
        'phone': user.phone,
        'repairs': user.repairs
        
    })





#Регистрация
#ФИО
def process_city_step(message):
    try:

        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)
        # удалить старую клавиатуру
        markup = types.ReplyKeyboardRemove(selective=False)


        msg = bot.send_message(chat_id, 'Фамилия Имя Отчество', reply_markup=markup)
        bot.register_next_step_handler(msg, process_fullname_step)


    except Exception as e:
        bot.reply_to(message, 'ooops!!')




#Номер телефона 
def process_fullname_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text


        msg = bot.send_message(chat_id, 'Ваш номер телефона:')
        bot.register_next_step_handler(msg, process_phone_step)


    except Exception as e:
        bot.reply_to(message, 'ooops!!')



#Что вы хотите заказать 
def process_phone_step(message):
    try:

        int(message.text)
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text


        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('iPhone 7 32gb')
        itembtn2 = types.KeyboardButton('iPhone 7 128gb')
        itembtn3 = types.KeyboardButton('iPhone 7+ 32gb')
        itembtn4 = types.KeyboardButton('iPhone 7+ 128gb')
        itembtn5 = types.KeyboardButton('iPhone 8 64gb')
        itembtn6 = types.KeyboardButton('iPhone 8 64gb(переклейка экрана)')
        itembtn7 = types.KeyboardButton('iPhone 8+ 64gb')
        itembtn8 = types.KeyboardButton('iPhone X 64gb')
        itembtn9 = types.KeyboardButton('iPhone Xr 64gb')
        itembtn10 = types.KeyboardButton('AirPods 1')
        itembtn11 = types.KeyboardButton('AirPods 2')
        itembtn12 = types.KeyboardButton('AirPods Pro')
        itembtn13 = types.KeyboardButton('Lightning')
        itembtn14 = types.KeyboardButton('Защитное стекло')
       
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10, itembtn11, itembtn12,itembtn13,itembtn14)

        msg = bot.send_message(message.chat.id, 'Что вы будете заказывать?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_driverSeria_step)
        
    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что то другое. Пожалуйста введите номер телефона.')
        bot.register_next_step_handler(msg, process_phone_step)



def process_driverSeria_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.driverSeria = message.text

    
    # ваша заявка "Имя пользователя"
    bot.send_message(chat_id, getRegData(user, 'Ваш заказ', message.from_user.first_name), parse_mode="Markdown")


    #sticker
    sti = open('static/phone.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)


    # удалить старую клавиатуру
    markup = types.ReplyKeyboardRemove(selective=False)


    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("iPhone 7")
    item2 = types.KeyboardButton("iPhone 7+")
    item3 = types.KeyboardButton("iPhone 8")
    item4 = types.KeyboardButton("iPhone X")
    item5 = types.KeyboardButton("iPhone Xr")
    item6 = types.KeyboardButton("Airpods")
    item7 = types.KeyboardButton("Lightning")
    item8 = types.KeyboardButton("Защитное стекло")
    item9 = types.KeyboardButton("Оформление заказа 📃")
    item10 = types.KeyboardButton("Заказать ремонт 🔧") 

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
    bot.send_message(message.chat.id, 'Что вас ещё интресует?', reply_markup=markup)
    

    # отправить в группу
    bot.send_message(config.chat_id, getRegData(user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")



# формирует вид заявки регистрации
# нельзя делать перенос строки Template
# в send_message должно стоять parse_mode="Markdown"
def getRegData(user, title, name):
    t = Template('$title *$name* \n Город: *$userCity* \n ФИО: *$fullname* \n Телефон: *$phone* \n Товар: *$driverSeria* \n *Мы с вами свяжимся, ждите звонка!*')


    return t.substitute({
        'title': title,
        'name': name,
        'userCity': user.city,
        'fullname': user.fullname,
        'phone': user.phone,
        'driverSeria': user.driverSeria
        
    })



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:


            if call.data == '1st':
                bot.send_message(call.message.chat.id, '130$ 💸')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="AirPods 1",
                reply_markup=None)


            elif call.data == '2gen':
                bot.send_message(call.message.chat.id, '170$ 💸')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="AirPods 2",
                reply_markup=None)


            elif call.data == 'pro':
                bot.send_message(call.message.chat.id, '300$ 💸')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="AirPods Pro",
                reply_markup=None)


            elif call.data == 'Iphone7 32':
                bot.send_message(call.message.chat.id, '225$ 💸')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Iphone7 32gb",
                reply_markup=None)
                

            elif call.data == 'Iphone7 128':
                bot.send_message(call.message.chat.id, '270$ 💸')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Iphone7 128gb",
                reply_markup=None)


            elif call.data == 'Iphone7plus 32':
                bot.send_message(call.message.chat.id, '340$ 💸')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Iphone7+ 32gb",
                reply_markup=None)


            elif call.data == 'Iphone7plus 128':
                bot.send_message(call.message.chat.id, '360$ 💸')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Iphone7+ 128gb",
                reply_markup=None)


            elif call.data == 'Iphone8 64':
                bot.send_message(call.message.chat.id, '345$ 💸')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Iphone8 64gb",
                reply_markup=None)


            elif call.data == 'Iphone8plus 64':
                bot.send_message(call.message.chat.id, '450$ 💸')
                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Iphone8+ 64gb",
                reply_markup=None)


            elif call.data == 'Iphone8 2 64':
                bot.send_message(call.message.chat.id, '335$ 💸')
                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Iphone8 64gb (переклейка экрана!)",
                reply_markup=None)

            elif call.data == '1it':
                bot.send_message(call.message.chat.id, '200 грн')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Iphone8 64gb (переклейка экрана!)",
                reply_markup=None)

            elif call.data == 'opt':
                bot.send_message(call.message.chat.id, '10шт. 1000 грн')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Iphone8 64gb (переклейка экрана!)",
                reply_markup=None)
         
            # show alert
            #bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                #text="Я ебал тебя в рот!!!")
    except Exception as e:
        print(repr(e))
# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.

bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()        

#Run
if __name__ == '__main__':
    bot.polling(none_stop=True)
