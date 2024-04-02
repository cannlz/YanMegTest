import sqlite3 as sq

from aiogram import types, executor, Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
import asyncio
from asgiref.sync import sync_to_async
import urlextract
from get_id import get_id_link
import random
from megaparser import parser_mega
from time import sleep

bot = Bot("7199689299:AAFOqQLAVhExufJdm2ScspXHRDlkdjdZYIg")
dp = Dispatcher(bot, storage=MemoryStorage())
baseMain = sq.connect('megmark.db', check_same_thread = False)

class AwaitMessages(StatesGroup):
    message_min_price = State()
    message_max_price = State()
    message_type_delivery = State()
    message_bonus = State()
    message_add_link = State()
    message_add_proxy = State()



async def scheduled(wait_for):
  while True:
    settings_user = baseMain.execute(f'SELECT user_id, min_price, max_price, delivery_type, min_precent_bonus, proxy FROM users').fetchall()
    
    list_delivery = ['UNKNOWN_OFFER_DUE_DATE', 'COLLECT_TODAY_OFFER_DUE_DATE', 'DEFAULT_DELIVERY_OFFER_DUE_DATE']

    for one_user in settings_user:
        if one_user[5] != 'Отсутствуют':
            userinfo = baseMain.execute(f'SELECT link_id, search_query FROM list_data WHERE user_id = {one_user[0]}').fetchall()
            for i in range(0,2):
                for one_line in userinfo:
                    page = 0
                    if one_line[i] is not None:
                        await asyncio.sleep((random.randint(10,20)))
                        if i == 0:

                            if one_user[3] == 'all_types_delivery':
                                for one_delivery in list_delivery:
                                    while page <= 112:
                                        good_links = await sync_to_async (parser_mega)(one_delivery, one_user[1], one_user[2],  None, one_user[4], one_line[i], one_user[5], page)
                                        for one_message in good_links:
                                            check_sended_links = baseMain.execute(f'SELECT link, price, precent_bonus FROM used_links WHERE link = "{one_message[4]}"').fetchone()
                                            if check_sended_links is not None:
                                                if check_sended_links[1] > int(one_message[0]) or check_sended_links[1] < int(one_message[0]):
                                                    baseMain.execute(f'UPDATE used_links SET price = {one_message[0]} WHERE link = "{one_message[4]}"')
                                                    baseMain.commit()
                                                
                                                if check_sended_links[2] > int(one_message[1]) or check_sended_links[2] < int(one_message[1]):
                                                    baseMain.execute(f'UPDATE used_links SET precent_bonus = {one_message[1]} WHERE link = "{one_message[4]}"')
                                                    baseMain.commit() 
                                            else:
                                                baseMain.execute(f'INSERT INTO used_links (link, price, precent_bonus) VALUES ("{one_message[4]}", {one_message[0]}, {one_message[1]});')
                                                baseMain.commit()
                                                await bot.send_photo(chat_id=one_user[0], photo=one_message[5], caption=f'Название: {one_message[6]}\n\nЦена: {one_message[0]} руб.\nПроцент бонусов: {one_message[1]}%\nКоличество бонусов: {one_message[2]}\nПродавец: {one_message[3]}\n\nСсылка на товар: {one_message[4]}', parse_mode='HTML')
                                        page += 28
                                        await asyncio.sleep((random.randint(5,10)))
                            else:
                                while page <= 112:
                                    good_links = await sync_to_async (parser_mega)(one_user[3], one_user[1], one_user[2],  None, one_user[4], one_line[i], one_user[5], page)
                                    for one_message in good_links:
                                        check_sended_links = baseMain.execute(f'SELECT link, price, precent_bonus FROM used_links WHERE link = "{one_message[4]}"').fetchone()
                                        if check_sended_links is not None:
                                            if check_sended_links[1] > int(one_message[0]) or check_sended_links[1] < int(one_message[0]):
                                                baseMain.execute(f'UPDATE used_links SET price = {one_message[0]} WHERE link = "{one_message[4]}"')
                                                baseMain.commit()
                                            
                                            if check_sended_links[2] > int(one_message[1]) or check_sended_links[2] < int(one_message[1]):
                                                baseMain.execute(f'UPDATE used_links SET precent_bonus = {one_message[1]} WHERE link = "{one_message[4]}"')
                                                baseMain.commit() 
                                        else:
                                            baseMain.execute(f'INSERT INTO used_links (link, price, precent_bonus) VALUES ("{one_message[4]}", {one_message[0]}, {one_message[1]});')
                                            baseMain.commit()
                                            await bot.send_photo(chat_id=one_user[0], photo=one_message[5], caption=f'Название: {one_message[6]}\n\nЦена: {one_message[0]} руб.\nПроцент бонусов: {one_message[1]}%\nКоличество бонусов: {one_message[2]}\nПродавец: {one_message[3]}\n\nСсылка на товар: {one_message[4]}', parse_mode='HTML')
                                    page += 28
                                    await asyncio.sleep((random.randint(5,10)))
                        elif i == 1:

                            if one_user[3] == 'all_types_delivery':
                                for one_delivery in list_delivery:
                                    while page <= 112:
                                        good_links = await sync_to_async (parser_mega)(one_delivery, one_user[1], one_user[2], one_line[i], one_user[4], None, one_user[5], page)
                                        for one_message in good_links:
                                            check_sended_links = baseMain.execute(f'SELECT link, price, precent_bonus FROM used_links WHERE link = "{one_message[4]}"').fetchone()
                                            if check_sended_links is not None:
                                                if check_sended_links[1] > int(one_message[0]) or check_sended_links[1] < int(one_message[0]):
                                                    baseMain.execute(f'UPDATE used_links SET price = {one_message[0]} WHERE link = "{one_message[4]}"')
                                                    baseMain.commit()
                                                
                                                if check_sended_links[2] > int(one_message[1]) or check_sended_links[2] < int(one_message[1]):
                                                    baseMain.execute(f'UPDATE used_links SET precent_bonus = {one_message[1]} WHERE link = "{one_message[4]}"')
                                                    baseMain.commit() 
                                            else:
                                                baseMain.execute(f'INSERT INTO used_links (link, price, precent_bonus) VALUES ("{one_message[4]}", {one_message[0]}, {one_message[1]});')
                                                baseMain.commit()
                                                await bot.send_photo(chat_id=one_user[0], photo=one_message[5], caption=f'Название: {one_message[6]}\n\nЦена: {one_message[0]} руб.\nПроцент бонусов: {one_message[1]}%\nКоличество бонусов: {one_message[2]}\nПродавец: {one_message[3]}\n\nСсылка на товар: {one_message[4]}', parse_mode='HTML')
                                        page += 28
                                        await asyncio.sleep((random.randint(5,10)))
                            else:
                                while page <= 112:
                                    good_links = await sync_to_async (parser_mega)(one_user[3], one_user[1], one_user[2], one_line[i], one_user[4], None, one_user[5], page)
                                    for one_message in good_links:
                                        check_sended_links = baseMain.execute(f'SELECT link, price, precent_bonus FROM used_links WHERE link = "{one_message[4]}"').fetchone()
                                        if check_sended_links is not None:
                                            if check_sended_links[1] > int(one_message[0]) or check_sended_links[1] < int(one_message[0]):
                                                baseMain.execute(f'UPDATE used_links SET price = {one_message[0]} WHERE link = "{one_message[4]}"')
                                                baseMain.commit()
                                            
                                            if check_sended_links[2] > int(one_message[1]) or check_sended_links[2] < int(one_message[1]):
                                                baseMain.execute(f'UPDATE used_links SET precent_bonus = {one_message[1]} WHERE link = "{one_message[4]}"')
                                                baseMain.commit() 
                                        else:
                                            baseMain.execute(f'INSERT INTO used_links (link, price, precent_bonus) VALUES ("{one_message[4]}", {one_message[0]}, {one_message[1]});')
                                            baseMain.commit()
                                            await bot.send_photo(chat_id=one_user[0], photo=one_message[5], caption=f'Название: {one_message[6]}\n\nЦена: {one_message[0]} руб.\nПроцент бонусов: {one_message[1]}%\nКоличество бонусов: {one_message[2]}\nПродавец: {one_message[3]}\n\nСсылка на товар: {one_message[4]}', parse_mode='HTML')
                                    page += 28
                                    await asyncio.sleep((random.randint(5,10)))
    await asyncio.sleep(wait_for)



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 2  # кол-во кнопок в строке
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_min_price = types.KeyboardButton("📉Мин. цена")
    btn_max_price = types.KeyboardButton("📈Макс. цена")
    btn_delivery = types.KeyboardButton("🚚Доставка")
    btn_bonus = types.KeyboardButton("💸% бонусов")
    btn_add_link = types.KeyboardButton("🔗Добавить ссылку")
    btn_status = types.KeyboardButton("⚙️Мои настройки")
    btn_proxy = types.KeyboardButton("🌐Добавить прокси")
    keyboard_markup.add(btn_add_link, btn_min_price, btn_max_price, btn_delivery, btn_bonus, btn_status, btn_proxy)
    try:
        check_user_base = baseMain.execute(f'SELECT user_id FROM users WHERE user_id = "{message.from_user.id}"').fetchone()
        check_user_links_base = baseMain.execute(f'SELECT user_id FROM list_data WHERE user_id = "{message.from_user.id}"').fetchone()

        if check_user_base is None:
            baseMain.execute(f'INSERT INTO users (user_id) VALUES ("{message.from_user.id}");')
            baseMain.commit()
        elif check_user_links_base is None:
            baseMain.execute(f'INSERT INTO list_data (user_id) VALUES ("{message.from_user.id}");')
            baseMain.commit()
    except Exception as e:
        print(e)
        pass
    await message.delete()
    await message.answer("Мегамаркет парсер", reply_markup=keyboard_markup)
    

#ГЛАВНОЕ МЕНЮ CALLBACK
@dp.callback_query_handler(text_startswith="start", state="*")
async def start_callback(call: types.CallbackQuery):
    await call.message.delete()
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_min_price = types.KeyboardButton("📉Мин. цена")
    btn_max_price = types.KeyboardButton("📈Макс. цена")
    btn_delivery = types.KeyboardButton("🚚Доставка")
    btn_bonus = types.KeyboardButton("💸% бонусов")
    btn_add_link = types.KeyboardButton("🔗Добавить ссылку")
    btn_status = types.KeyboardButton("⚙️Мои настройки")
    btn_proxy = types.KeyboardButton("🌐Добавить прокси")
    keyboard_markup.add(btn_add_link, btn_min_price, btn_max_price, btn_delivery, btn_bonus, btn_status, btn_proxy)
    await bot.send_message(text="Мегамаркет парсер", chat_id=call.from_user.id, reply_markup=keyboard_markup)


#МЕНЮ НАСТРОЕК
@dp.message_handler(lambda message: message.text == "⚙️Мои настройки")
async def parser(message: types.Message):
    await message.delete()

    list_data_links = []
    userinfo = baseMain.execute(f'SELECT link, search_query FROM list_data WHERE user_id = {message.from_user.id}').fetchall()

    for i in range(0,2):
        for one_line in userinfo:
            if one_line[i] is not None:
                list_data_links.append(one_line[i])

    markup = InlineKeyboardMarkup() # создаём клавиатуру
    markup.row_width = 1 # кол-во кнопок в строке
    for i in list_data_links: # цикл для создания кнопок
        markup.add(InlineKeyboardButton(i, callback_data=i)) #Создаём кнопки, i[1] - название, i[2] - каллбек дата
    markup.add(InlineKeyboardButton(text="❌Закрыть", callback_data="start"))
    userinfo = baseMain.execute(f'SELECT * FROM users WHERE user_id = "{message.from_user.id}"').fetchone()
    await message.answer(f"⚙️Настройки пользователя: {userinfo[1]} \n\n📉Минимальная цена: {userinfo[2]} руб.\n📈Максимальная цена: {userinfo[3]} руб.\n🚚Тип доставки: {userinfo[4]} \n💸От какого % бонусов искать: {userinfo[5]}%\nПрокси: {userinfo[6]}\n\nДля удаления ссылки/ключевого запроса, нажмите на кнопку, которую хотите удалить", reply_markup=markup)

#ОБРАБОТЧИК ГЕНЕРАЦИИ КНОПОК С ССЫЛКАМИ
@dp.callback_query_handler(lambda call: True)
async def stoptopupcall(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.delete()
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    markup.add(InlineKeyboardButton(text="❌Закрыть", callback_data="start"))

    list_data_links = []
    userinfo = baseMain.execute(f'SELECT link, search_query FROM list_data WHERE user_id = {callback_query.from_user.id}').fetchall()
    for i in range(0,2):
        for one_line in userinfo:
            if one_line[i] is not None:
                list_data_links.append(one_line[i])

    if callback_query.data in list_data_links: # делаем проверку есть ли наш идентификатор в тех кнопках
        extractor = urlextract.URLExtract()
        try:
            urls = extractor.find_urls(callback_query.data)
        except:
            urls = ''
            pass
        if len(urls) > 0:
            baseMain.execute(f'DELETE from list_data WHERE link = "{callback_query.data}"')
            baseMain.commit()
            await bot.send_message(callback_query.from_user.id, f'Ссылка "{callback_query.data}" успешно удалена!', reply_markup=markup) # делаем вывод инфы
        else:
            baseMain.execute(f'DELETE from list_data WHERE search_query = "{callback_query.data}"')
            baseMain.commit()
            await bot.send_message(callback_query.from_user.id, f'Поисковый запрос "{callback_query.data}" успешно удален!', reply_markup=markup) # делаем вывод инфы

#МИНИМАЛЬНАЯ ЦЕНА
@dp.message_handler(lambda message: message.text == "📉Мин. цена")
async def parser(message: types.Message):
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    markup.add(InlineKeyboardButton(text="❌Закрыть", callback_data="start"))
    await message.delete()
    await message.answer("Введите минимальную цену товара:", reply_markup=markup)
    await AwaitMessages.message_min_price.set()

#МИНИМАЛЬНАЯ ЦЕНА FSM МАШИНА
@dp.message_handler(state=AwaitMessages.message_min_price)  # Принимаем состояние
async def started(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:  # Устанавливаем состояние ожидания
        proxy['message_min_price'] = message.text
    
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    markup.add(InlineKeyboardButton(text="❌Закрыть", callback_data="start"))

    if proxy["message_min_price"] != "стоп" and proxy["message_min_price"].isdigit():
        baseMain.execute(f'UPDATE users SET min_price = {message.text} WHERE user_id = "{message.from_user.id}"')
        baseMain.commit()
        userinfo = baseMain.execute(f'SELECT * FROM users WHERE user_id = "{message.from_user.id}"').fetchone()
        await message.answer(f"⚙️Настройки пользователя: {userinfo[1]} \n\n📉Минимальная цена: {userinfo[2]} руб.\n📈Максимальная цена: {userinfo[3]} руб.\n🚚Тип доставки: {userinfo[4]} \n💸От какого % бонусов искать: {userinfo[5]}%\nПрокси: {userinfo[6]}", reply_markup=markup)
        await state.finish()  # Выключаем состояние
    else:
        await message.answer(f'❌Действие отменено или введён неверный тип данных\nЭто "{message.text}" точно число?', reply_markup=markup)
        await state.finish()

    await state.finish()


#МАКСИМАЛЬНАЯ ЦЕНА
@dp.message_handler(lambda message: message.text == "📈Макс. цена")
async def parser(message: types.Message):
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    markup.add(InlineKeyboardButton(text="❌Закрыть", callback_data="start"))
    await message.delete()
    await message.answer("Введите максимальную цену товара:", reply_markup=markup)
    await AwaitMessages.message_max_price.set()

#МАКСИМАЛЬНАЯ ЦЕНА FSM МАШИНА
@dp.message_handler(state=AwaitMessages.message_max_price)  # Принимаем состояние
async def started(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:  # Устанавливаем состояние ожидания
        proxy['message_max_price'] = message.text
    
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    markup.add(InlineKeyboardButton(text="❌Закрыть", callback_data="start"))

    if proxy["message_max_price"] != "стоп" and proxy["message_max_price"].isdigit():
        baseMain.execute(f'UPDATE users SET max_price = {message.text} WHERE user_id = "{message.from_user.id}"')
        baseMain.commit()
        userinfo = baseMain.execute(f'SELECT * FROM users WHERE user_id = "{message.from_user.id}"').fetchone()
        await message.answer(f"⚙️Настройки пользователя: {userinfo[1]} \n\n📉Минимальная цена: {userinfo[2]} руб.\n📈Максимальная цена: {userinfo[3]} руб.\n🚚Тип доставки: {userinfo[4]} \n💸От какого % бонусов искать: {userinfo[5]}%\nПрокси: {userinfo[6]}", reply_markup=markup)
        await state.finish()  # Выключаем состояние
    else:
        await message.answer(f'❌Действие отменено или введён неверный тип данных\nЭто "{message.text}" точно число?', reply_markup=markup)
        await state.finish()

    await state.finish()


#ВЫБОР ТИПА ДОСТАВКИ
@dp.message_handler(lambda message: message.text == "🚚Доставка")
async def parser(message: types.Message):
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    markup.add(InlineKeyboardButton(text="Любая доставка", callback_data="UNKNOWN_OFFER_DUE_DATE"))
    markup.add(InlineKeyboardButton(text="Забрать сегодня в магазине", callback_data="COLLECT_TODAY_OFFER_DUE_DATE"))
    markup.add(InlineKeyboardButton(text="Завтра или позже", callback_data="DEFAULT_DELIVERY_OFFER_DUE_DATE"))
    markup.add(InlineKeyboardButton(text="Использовать всё", callback_data="all_types_delivery"))
    markup.add(InlineKeyboardButton(text="❌Закрыть", callback_data="start"))
    await bot.send_message(chat_id=message.from_user.id, text='Укажите желаемый тип доставки:', reply_markup=markup)
    await message.delete()
    await AwaitMessages.message_type_delivery.set()

#ВЫБОР ТИПА ДОСТАВКИ FSM МАШИНА
@dp.callback_query_handler(state=AwaitMessages.message_type_delivery)  # Принимаем состояние
async def echos(callback_query: types.CallbackQuery, state: FSMContext):
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    markup.add(InlineKeyboardButton(text="❌Закрыть", callback_data="start"))

    async with state.proxy() as data:
        data["message_type_delivery"] = callback_query.data
    
    if data["message_type_delivery"] == "UNKNOWN_OFFER_DUE_DATE" or data["message_type_delivery"] == "COLLECT_TODAY_OFFER_DUE_DATE" or data["message_type_delivery"] == "DEFAULT_DELIVERY_OFFER_DUE_DATE" or data["message_type_delivery"] == "all_types_delivery":
        await callback_query.message.delete()
        baseMain.execute(f'UPDATE users SET delivery_type = "{callback_query.data}" WHERE user_id = "{callback_query.from_user.id}"')
        baseMain.commit()
        userinfo = baseMain.execute(f'SELECT * FROM users WHERE user_id = "{callback_query.from_user.id}"').fetchone()
        await bot.send_message(chat_id=callback_query.from_user.id, text=f"⚙️Настройки пользователя: {userinfo[1]} \n\n📉Минимальная цена: {userinfo[2]} руб.\n📈Максимальная цена: {userinfo[3]} руб.\n🚚Тип доставки: {userinfo[4]} \n💸От какого % бонусов искать: {userinfo[5]}%\nПрокси: {userinfo[6]}", reply_markup=markup)
        await state.finish()  # Выключаем состояние
    else:
        await callback_query.message.delete()
        await bot.send_message(chat_id=callback_query.from_user.id, text=f'❌Действие отменено', reply_markup=markup)
        await state.finish()

    await state.finish()


#ВЫБОР % ОТ БОНУСОВ
@dp.message_handler(lambda message: message.text == "💸% бонусов")
async def parser(message: types.Message):
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    markup.add(InlineKeyboardButton(text="❌Закрыть", callback_data="start"))
    await message.delete()
    await message.answer('Укажите, от какого % бонусов искать товары(писать только число, без знака "%"):', reply_markup=markup)
    await AwaitMessages.message_bonus.set()

#ВЫБОР % ОТ БОНУСОВ FSM МАШИНА
@dp.message_handler(state=AwaitMessages.message_bonus)  # Принимаем состояние
async def started(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:  # Устанавливаем состояние ожидания
        proxy['message_bonus'] = message.text
    
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    markup.add(InlineKeyboardButton(text="❌Закрыть", callback_data="start"))

    if proxy["message_bonus"] != "стоп" and proxy["message_bonus"].isdigit():
        baseMain.execute(f'UPDATE users SET min_precent_bonus = {message.text} WHERE user_id = "{message.from_user.id}"')
        baseMain.commit()
        userinfo = baseMain.execute(f'SELECT * FROM users WHERE user_id = "{message.from_user.id}"').fetchone()
        await message.answer(f"⚙️Настройки пользователя: {userinfo[1]} \n\n📉Минимальная цена: {userinfo[2]} руб.\n📈Максимальная цена: {userinfo[3]} руб.\n🚚Тип доставки: {userinfo[4]} \n💸От какого % бонусов искать: {userinfo[5]}%\nПрокси: {userinfo[6]}", reply_markup=markup)
        await state.finish()  # Выключаем состояние
    else:
        await message.answer(f'❌Действие отменено или введён неверный тип данных\nЭто "{message.text}" точно число?', reply_markup=markup)
        await state.finish()

    await state.finish()


#ДОБАВЛЕНИЕ ССЫЛКИ
@dp.message_handler(lambda message: message.text == "🔗Добавить ссылку")
async def parser(message: types.Message):
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    markup.add(InlineKeyboardButton(text="❌Закрыть", callback_data="start"))
    await message.delete()
    check_limit = baseMain.execute(f'SELECT * FROM list_data WHERE user_id = {message.from_user.id}').fetchall()
    if len(check_limit) < 10:
        await message.answer('Пришлите ссылку на категорию/подкатегорию или поисковый запрос:\nПример ссылки: https://megamarket.ru/catalog/smartfony-apple/\nПример поискового запроса: iphone 15 pro', reply_markup=markup)
        await AwaitMessages.message_add_link.set()
    else:
        await message.answer('❌Превышен лимит ссылок для парсера (10 ссылок) . Пожалуйста, удалите не используемые ссылки, после чего попробуйте снова', reply_markup=markup)


#ДОБАВЛЕНИЕ ССЫЛКИ FSM МАШИНА
@dp.message_handler(state=AwaitMessages.message_add_link)  # Принимаем состояние
async def started(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:  # Устанавливаем состояние ожидания
        proxy['message_add_link'] = message.text
    
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    markup.add(InlineKeyboardButton(text="❌Закрыть", callback_data="start"))

    if proxy["message_add_link"] != "стоп":
        extractor = urlextract.URLExtract()
        check_url = False
        url_id = ''
        try:
            urls = extractor.find_urls(message.text)
            if len(urls) > 0:
                proxy = baseMain.execute(f'SELECT proxy FROM users WHERE user_id = {message.from_user.id}').fetchone()
                url_id = get_id_link(urls[0], proxy[0])
            else:
                check_url = True
                urls = False
        except:
            urls = False
            pass
        
        if url_id is not None:
            if urls != False and len(url_id) > 0:
                baseMain.execute(f'INSERT INTO list_data (link, user_id, link_id) VALUES ("{urls[0]}", {message.from_user.id}, {url_id});')
                baseMain.commit()
                await message.answer(f"✅Ссылка успешно добавлена: {message.from_user.id}", reply_markup=markup)
                await state.finish()
            elif check_url:
                baseMain.execute(f'INSERT INTO list_data (search_query, user_id) VALUES ("{message.text}", {message.from_user.id});')
                baseMain.commit()
                await message.answer(f"✅Поисковый запрос успешно добавлен: {message.from_user.id}", reply_markup=markup)
                await state.finish()

        else:
            await message.answer(f'❌Действие отменено или возникла ошибка\nПроверьте правильность ссылки:"{message.text}"', reply_markup=markup)
            await state.finish()

        await state.finish()  # Выключаем состояние
    else:
        await message.answer(f'❌Действие отменено или возникла ошибка', reply_markup=markup)
        await state.finish()

    await state.finish()


#ДОБАВЛЕНИЕ ПРОКСИ
@dp.message_handler(lambda message: message.text == "🌐Добавить прокси")
async def parser(message: types.Message):
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    markup.add(InlineKeyboardButton(text="❌Закрыть", callback_data="start"))
    await message.delete()
    await message.answer("Введите строку с прокси РОССИЯ http/https(1 шт):\n\nФормат прокси: username:password@ip:port\n\nКупить можно тут: proxywhite.com", reply_markup=markup)
    await AwaitMessages.message_add_proxy.set()

#ДОБАВЛЕНИЕ ПРОКСИ FSM МАШИНА
@dp.message_handler(state=AwaitMessages.message_add_proxy)  # Принимаем состояние
async def started(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:  # Устанавливаем состояние ожидания
        proxy['message_add_proxy'] = message.text
    
    markup = InlineKeyboardMarkup()  # создаём клавиатуру
    markup.row_width = 1  # кол-во кнопок в строке
    markup.add(InlineKeyboardButton(text="❌Закрыть", callback_data="start"))

    if proxy["message_add_proxy"] != "стоп" and '@' in message.text and ':' in message.text:
        baseMain.execute(f'UPDATE users SET proxy = "{message.text}" WHERE user_id = {message.from_user.id}')
        baseMain.commit()
        userinfo = baseMain.execute(f'SELECT * FROM users WHERE user_id = "{message.from_user.id}"').fetchone()
        await message.answer(f"⚙️Настройки пользователя: {userinfo[1]} \n\n📉Минимальная цена: {userinfo[2]} руб.\n📈Максимальная цена: {userinfo[3]} руб.\n🚚Тип доставки: {userinfo[4]} \n💸От какого % бонусов искать: {userinfo[5]}%\nПрокси: {userinfo[6]}", reply_markup=markup)
        await state.finish()  # Выключаем состояние
    else:
        await message.answer(f'❌Действие отменено или введён неверный тип данных\nФормат прокси: username:password@ip:port', reply_markup=markup)
        await state.finish()

    await state.finish()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(random.randint(120, 360))) # поставим 10 секунд, в качестве теста
    executor.start_polling(dp, skip_updates=True)