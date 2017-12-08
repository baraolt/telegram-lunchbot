#! /usr/bin/python3
import telepot, time, datetime
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
import subprocess

menuFM = ''
menuGG = ''
menuKL = ''
menuSU = ''
menuHO = ''
menuCC = ''
menuALL = ''
timestamp = ''

'''
BOT logic
'''

def update_menus():

    CalcProc = subprocess.Popen('/home/pi/LunchBot/LM_fetchMenus.py')
    CalcProc.wait()

def load_menus():
    
    global menuFM, menuGG, menuKL, menuSU, menuHO, menuCC, menuALL, timestamp
    
    menuFM = ''
    menuGG = ''
    menuKL = ''
    menuSU = ''
    menuHO = ''
    menuCC = ''
    menuALL = ''
    timestamp = ''

    FMfile = open('/home/pi/LunchBot/MenuFiles/FMfile.txt')
    menuFM = FMfile.read()
    FMfile.close()
    GGfile = open('/home/pi/LunchBot/MenuFiles/GGfile.txt')
    menuGG = GGfile.read()
    GGfile.close()
    KLfile = open('/home/pi/LunchBot/MenuFiles/KLfile.txt')
    menuKL = KLfile.read()
    KLfile.close()
    SUfile = open('/home/pi/LunchBot/MenuFiles/SUfile.txt')
    menuSU = SUfile.read()
    SUfile.close()
    HOfile = open('/home/pi/LunchBot/MenuFiles/HOfile.txt')
    menuHO = HOfile.read()
    HOfile.close()
    CCfile = open('/home/pi/LunchBot/MenuFiles/CCfile.txt')
    menuCC = CCfile.read()
    CCfile.close()
    menuALL = menuFM + '\n' + menuGG + '\n' + menuKL + '\n' + menuSU + '\n' + menuHO

    TSfile = open('/home/pi/LunchBot/MenuFiles/TSfile.txt')
    timestamp = TSfile.read()
    TSfile.close()
    
    print('Updated variables from files')
    
def on_inline_query(msg):
    def compute():
        query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
        print('Inline Query:', query_id, from_id, query_string)

        articles = [InlineQueryResultArticle(
                        id='aaa',
                        title='FATMAMA (text)',
                        input_message_content=InputTextMessageContent(message_text=menuFM)),
                    InlineQueryResultArticle(
                        id='aab',
                        title='GettoGulyás (text)',
                        input_message_content=InputTextMessageContent(message_text=menuGG)),
                    InlineQueryResultArticle(
                        id='aac',
                        title='Kőleves (text)',
                        input_message_content=InputTextMessageContent(message_text=menuKL)),
                    InlineQueryResultArticle(
                        id='aad',
                        title='Suelto Bistro (text)',
                        input_message_content=InputTextMessageContent(message_text=menuSU)),
                    InlineQueryResultArticle(
                        id='aae',
                        title='Hokedli (text)',
                        input_message_content=InputTextMessageContent(message_text=menuHO)),
                    InlineQueryResultArticle(
                        id='aaf',
                        title='Central Canteen (photo)',
                        input_message_content=InputTextMessageContent(message_text=menuCC)),
                    InlineQueryResultArticle(
                        id='aag',
                        title='All text menus',
                        input_message_content=InputTextMessageContent(message_text=menuALL)),
                    ]

        return articles

    answerer.answer(msg, compute)


def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print ('Chosen Inline Result:', result_id, from_id, query_string)

'''SETUP related functions'''
menuValue = ''
GLmsg = ''
mID = ''


def on_chat_message(msg):
    content_type, chat_type, chat_id, date, message_id = telepot.glance(msg, long=True)
    global menuValue, GLmsg, mID
    GLmsg = msg
    if msg["text"] == '/setup':
        if menuValue == '':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Update menus', callback_data='update_menu'),
                 InlineKeyboardButton(text='Last fetch', callback_data='last_fetch')],
                [InlineKeyboardButton(text='Cancel', callback_data='exit')],
            ])
            sent = bot.sendMessage(chat_id, 'Choose an option', reply_markup=keyboard)
            mID = telepot.message_identifier(sent)
        elif menuValue == 'update_menu':
            menuValue = ''
            bot.editMessageText(mID, "Updating menus...", reply_markup=None)
            mID = ''
            update_menus()
            load_menus()
            time.sleep(1)
            bot.sendMessage(chat_id, "Updating done!")
        elif menuValue == 'last_fetch':
            menuValue = ''
            bot.editMessageText(mID, "Last fetch: " + timestamp, reply_markup=None)
            mID = ''
        elif menuValue == 'exit':
            menuValue = ''
            bot.editMessageText(mID, "Cancelled. Use /setup command to bring up preferences again.", reply_markup=None)
            mID = ''
    elif msg["text"] == '/cancel':
        if mID != '':
            bot.editMessageText(mID, "OK, cancelled operation", reply_markup=None)
        else: bot.sendMessage(chat_id, "There's nothing to cancel")
    else: bot.sendMessage(chat_id, "Use /setup command to open preferences!")

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    global menuValue
    menuValue = query_data
    if menuValue == 'update_menu':
        bot.answerCallbackQuery(query_id, text='Updating menus')
        time.sleep(1)
    on_chat_message(GLmsg)

TOKEN = '<YOUR BOTs TOKEN>'

bot = telepot.Bot(TOKEN)
answerer = telepot.helper.Answerer(bot)

MessageLoop(bot, {'inline_query': on_inline_query,
                  'chosen_inline_result': on_chosen_inline_result,
                  'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
load_menus()
print("Listening... (Press CTRL+C to stop)")
while 1:
    time.sleep(10)
