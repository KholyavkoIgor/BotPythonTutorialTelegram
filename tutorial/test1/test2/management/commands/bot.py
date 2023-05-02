from django.core.management.base import BaseCommand
from django.conf import settings
#from telegram import Bot
#from telegram import Update
#from telegram.ext import CallbackContext
#from telegram.ext.filters import Filters
#from telegram.ext import MessageHandler
#from telegram.ext import Updater
#from telegram.utils.request import Request

from test2.models import Message
from test2.models import Profile
q=Profile.objects.get_or_create()
import telebot
bot1 = telebot.TeleBot('yourkeyhere')
from telebot import types
'''
@bot1.message_handler(commands=['start'])
def start_message(message):
    bot1.send_message(message.chat.id,'Привет')

@bot1.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot1.send_message(message.chat.id,'Выберите что вам нужно',reply_markup=markup)
@bot1.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кнопка":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Кнопка 2")
        markup.add(item1)
        bot1.send_message(message.chat.id,'Выберите что вам нужно',reply_markup=markup)
    elif message.text=="Кнопка 2":
        bot1.send_message(message.chat.id,'Спасибо!')

bot1.infinity_polling()
'''
class Command(BaseCommand):
    help = 'Телеграмм-бот'
    def handle(self, *args, **options):
        @bot1.message_handler(commands=['start'])
        def start_message(message):
            bot1.send_message(message.chat.id,f'Привет, {message.from_user.username},\n готов к работе')
            p, _ = Profile.objects.get_or_create(
                external_id=message.chat.id,
                defaults={
                    'name':message.from_user.username,
                    }
                                                )
            q=p
            #print(f'q - {dir(q)}')
            #print(f'p - {dir(p)}')          Message.__doc__.__dict__
            #print(f'q - {q.__dict__}')
            #print(type(q))

        @bot1.message_handler(commands=['button'])
        def button_message(message):
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("хочу учиться")
            markup.add(item1)
            bot1.send_message(message.chat.id,'Выберите команду хочу учиться',reply_markup=markup)

        @bot1.message_handler(content_types='text')
        def message_reply(message):
            '''
            if message.text=="хочу учиться":
                #print(f'm - {Message.profile.__dict__}')
                #print(f'm - {dir(Message)}')
                #print(f'm - {Message._meta.get_field(texteng)}')
                m = Message(
                        profile = q[0],
                        text=message.text,
                )
                m.save()
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                item2=types.KeyboardButton("записать слово")
                item3=types.KeyboardButton("записать лекцию")
                item4=types.KeyboardButton("узнать слово")
                item5=types.KeyboardButton("узнать лекцию")
                markup.add(item2)
                markup.add(item3)
                markup.add(item4)
                markup.add(item5)
                bot1.send_message(message.chat.id,'Выберите что Вам нужно',reply_markup=markup)
            '''
            if "записать слово " in message.text:
                soobsheniye = message.text.split()
                if len(soobsheniye) == 4:
                    m = Message(
                        profile=q[0],
                        text=message.text,
                        textrus=soobsheniye[2],
                        texteng=soobsheniye[3],
                        lecturename='0'
                    )
                    m.save()
                    bot1.send_message(message.chat.id, 'слово записано')
                elif len(soobsheniye) == 5:
                    m = Message(
                        profile=q[0],
                        text=message.text,
                        textrus=soobsheniye[2],
                        texteng=soobsheniye[3],
                        lecturename=soobsheniye[4]
                    )
                    m.save()
                    bot1.send_message(message.chat.id,'слово записано')
                else:
                    bot1.send_message(message.chat.id, 'некорректный ввод, повторите запрос')
            elif "записать лекцию " in message.text:
                lst = message.text.split('\n')
                lecname = lst[0].split()[-1]
                for i in range(1,len(lst)):
                    m = Message(
                        profile = q[0],
                        text = message.text,
                        textrus = lst[i].split()[0],
                        texteng = lst[i].split()[1],
                        lecturename = lecname
                    )
                    m.save()
                bot1.send_message(message.chat.id,'лекция записана')
            elif "узнать слово " in message.text:
                #bot1.send_message(message.chat.id,'слово изучено')
                #print(Message.objects.get(text1="Текст").text2)
                #print(Message.objects.filter(textrus__contains='кошка')[0])
                slovo = message.text.split()[2]
                if (len(Message.objects.filter(textrus__contains=slovo)) > 0):
                    for i in Message.objects.filter(textrus__contains=slovo):
                        bot1.send_message(message.chat.id, Message.objects.filter(textrus__contains=slovo)[0].texteng)
                elif (len(Message.objects.filter(texteng__contains=slovo)) > 0):
                    for i in Message.objects.filter(texteng__contains=slovo):
                        bot1.send_message(message.chat.id, Message.objects.filter(texteng__contains=slovo)[0].textrus)
                else:
                    bot1.send_message(message.chat.id, 'слово неизвестно')
            elif "узнать лекцию " in message.text:
                #bot1.send_message(message.chat.id,'лекция изучена')
                lec = message.text.split()[2]
                leccont = Message.objects.filter(lecturename__contains=lec)
                lec = 'лекция \"' + lec + '\":'
                spisokspiskov = []
                if len(leccont) > 0:
                    for i in leccont:
                        if [i.textrus,i.texteng] not in spisokspiskov:
                            spisokspiskov.append([i.textrus,i.texteng])
                            lec = lec + '\n' + i.textrus + ' ' + i.texteng
                    bot1.send_message(message.chat.id, lec)
                else:
                    bot1.send_message(message.chat.id, 'лекция неизвестна')
                spisokspiskov.clear()
            elif True: 
                bot1.send_message(message.chat.id,'некорректный ввод, повторите запрос')
              


            
        bot1.infinity_polling()
















"""
p, _ = Profile.objects.get_or_create(
external_id=chat_id,
defaults={

}
)
"""









'''
def log_errors(f):

    def inner(wargs, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:

            error_message =f'Произошла ошибка: {e}'
            print(error_message)
            raise e
    return inner
@log_errors
def do_echo(update: Update, context: CallbackContext):
    chat_id=update.message.chat_id
    text = update.message.text

    

    reply_text = "Ваш ID = {}\n\n{}".format(chat_id, text)
    update.message.reply_text(
        text = reply_text,
        )

class Command(BaseCommand):
    help = 'Телеграмм-бот'
    def handle(self, *args, **options):
        #1 - правильное подключение
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
            )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
            #base_url=settings.PROXY_URL,
            )
        print(bot.get_me())

        #2 - обработчики
        updater = Updater(
            bot=bot,
            use_context=True,
            )
        message_handler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(message_handler)

        #3 - запустить бесконечную обработку входящих сообщений
        updater.start_polling()
        updater.idle()
'''        








        
