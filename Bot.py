from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from Config import TOKEN
import sqlite3
import datetime
from datetime import datetime
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import time

API_TOKEN = TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

async def ABI169S(exfp, RU, M, F, I, G, H, O, IN, B, message):
	if M != None: 
		if F != None:
			bal = RU + M + F
			lst = obj.get_dir("M", "Ф", bal, exfp)
			if lst != []:
				if RU <= 55 or M <= 48 or F <= 46:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С математикой и физикой:\n\n"+'\n\n'.join(lst))
		if I != None:
			bal = RU + M + I
			lst = obj.get_dir("M", "И", bal, exfp)
			if lst != []:
				if RU <= 55 or M <= 48 or I <= 55:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С математикой и информатикой:\n\n"+'\n\n'.join(lst))
		if G != None:
			bal = RU + M + G
			lst = obj.get_dir("M", "Г", bal, exfp)
			if lst != []:
				if RU <= 55 or M <= 48:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С математикой и географией:\n\n"+'\n\n'.join(lst))
		if H != None:
			bal = RU + M + H
			lst = obj.get_dir("M", "Ис", bal, exfp)
			if lst != []:
				if RU <= 55 or M <= 48: 
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С математикой и историей:\n\n"+'\n\n'.join(lst))
		if O != None:
			bal = RU + M + O
			lst = obj.get_dir("M", "О", bal, exfp)
			if lst != []:
				if RU <= 55 or M <= 48 or O <= 50:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С математикой и обществознанием:\n\n"+'\n\n'.join(lst))
		if IN != None:
			bal = RU + M + IN
			lst = obj.get_dir("M", "Ин", bal, exfp)
			if lst != []:
				if RU <= 55 or M <= 48: 
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С математикой и иностранным языком:\n\n"+'\n\n'.join(lst))
		if B != None:
			bal = RU + M + B
			lst = obj.get_dir("M", "Б", bal, exfp)
			if lst != []:
				if RU <= 55 or M <= 48:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С математикой и биологией:\n\n"+'\n\n'.join(lst))

	if F != None: 
		if I != None:
			bal = RU + F + I
			lst = obj.get_dir("Ф", "И", bal, exfp)
			if lst != []:
				if RU <= 55 or F <= 46 or I <= 55:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С физикой и информатикой:\n\n"+'\n\n'.join(lst))
		if G != None:
			bal = RU + F + G
			lst = obj.get_dir("Ф", "Г", bal, exfp)
			if lst != []:
				if RU <= 55 or F <= 46: 
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С физикой и географией:\n\n"+'\n\n'.join(lst))
		if H != None:
			bal = RU + F + H
			lst = obj.get_dir("Ф", "Ис", bal, exfp)
			if lst != []:
				if RU <= 55 or F <= 46: 
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С физикой и историей:\n\n"+'\n\n'.join(lst))
		if O != None:
			bal = RU + F + O
			lst = obj.get_dir("Ф", "О", bal, exfp)
			if lst != []:
				if RU <= 55 or F <= 46 or O <= 50:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С физикой и обществознанием:\n\n"+'\n\n'.join(lst))
		if IN != None:
			bal = RU + F + IN
			lst = obj.get_dir("Ф", "Ин", bal, exfp)
			if lst != []:
				if RU <= 55 or F <= 46: 
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С физикой и иностранным языком:\n\n"+'\n\n'.join(lst))
		if B != None:
			bal = RU + F + B
			lst = obj.get_dir("Ф", "Б", bal, exfp)
			if lst != []:
				if RU <= 55 or F <= 46:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С физикой и биологией:\n\n"+'\n\n'.join(lst))

	if I != None: 
		if G != None:
			bal = RU + I + G
			lst = obj.get_dir("И", "Г", bal, exfp)
			if lst != []:
				if RU <= 55 or I <= 55:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С информатикой и географией:\n\n"+'\n\n'.join(lst))
		if H != None:
			bal = RU + I + H
			lst = obj.get_dir("И", "Ис", bal, exfp)
			if lst != []:
				if RU <= 55 or I <= 55:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С информатикой и историей:\n\n"+'\n\n'.join(lst))
		if O != None:
			bal = RU + I + O
			lst = obj.get_dir("И", "О", bal, exfp)
			if lst != []:
				if RU <= 55 or I <= 55 or O <= 50:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С информатикой и обществознанием:\n\n"+'\n\n'.join(lst))
		if IN != None:
			bal = RU + I + IN
			lst = obj.get_dir("И", "Ин", bal, exfp)
			if lst != []:
				if RU <= 55 or I <= 55:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С информатикой и иностранным языком:\n\n"+'\n\n'.join(lst))
		if B != None:
			bal = RU + I + B
			lst = obj.get_dir("И", "Б", bal, exfp)
			if lst != []:
				if RU <= 55 or I <= 55:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С информатикой и биологией:\n\n"+'\n\n'.join(lst))

	if G != None: 
		if H != None:
			bal = RU + G + H
			lst = obj.get_dir("Г", "Ис", bal, exfp)
			if lst != []:
				if RU <= 55:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С географией и историей:\n\n"+'\n\n'.join(lst))
		if O != None:
			bal = RU + G + O
			lst = obj.get_dir("Г", "О", bal, exfp)
			if lst != []:
				if RU <= 55 or O <= 50:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С географией и обществознанием:\n\n"+'\n\n'.join(lst))
		if IN != None:
			bal = RU + G + IN
			lst = obj.get_dir("Г", "Ин", bal, exfp)
			if lst != []:
				if RU <= 55 :
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С географией и иностранным языком:\n\n"+'\n\n'.join(lst))
		if B != None:
			bal = RU + G + B
			lst = obj.get_dir("Г", "Б", bal, exfp)
			if lst != []:
				if RU <= 55 :
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С географией и биологией:\n\n"+'\n\n'.join(lst))

	if H != None: 
		if O != None:
			bal = RU + H + O
			lst = obj.get_dir("Ис", "О", bal, exfp)
			if lst != []:
				if RU <= 55 or O <= 50:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С историей и обществознанием:\n\n"+'\n\n'.join(lst))
		if IN != None:
			bal = RU + H + IN
			lst = obj.get_dir("Ис", "Ин", bal, exfp)
			if lst != []:
				if RU <= 55 :
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С историей и иностранным языком:\n\n"+'\n\n'.join(lst))
		if B != None:
			bal = RU + H + B
			lst = obj.get_dir("Ис", "Б", bal, exfp)
			if lst != []:
				if RU <= 55:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С историей и биологией:\n\n"+'\n\n'.join(lst))

	if IN != None: 
		if O != None:
			bal = RU + IN + O
			lst = obj.get_dir("Ин", "О", bal, exfp)
			if lst != []:
				if RU <= 55 or O <= 50:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С иностранным языком и обществознанием:\n\n"+'\n\n'.join(lst))
		if B != None:
			bal = RU + IN + B
			lst = obj.get_dir("Ин", "Б", bal, exfp)
			if lst != []:
				if RU <= 55:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("С иностранным языком и биологией:\n\n"+'\n\n'.join(lst))

	if O != None: 
		if B != None:
			bal = RU + B + O
			lst = obj.get_dir("Б", "О", bal, exfp)
			if lst != []:
				if RU <= 55 or O <= 50:
					await message.answer("Быллы по одному или нескольким предметам прошли порог только для поступления в филиалы МАИ.")
				await message.answer("с биологией и обществознанием:\n\n"+'\n\n'.join(lst))

class Mydialog(StatesGroup):
    otvet1 = State()
    otvet2 = State()
    otvet3 = State()
    otvet4 = State()
    otvet5 = State()
    otvet6 = State()
    otvet7 = State()
    otvet8 = State()
    otvet9 = State()
    otvet10 = State()

class User:
	# Функция для соединения с БД
	def connect_to_db(self):
		self.connect = sqlite3.connect('BDdiplom.db')
		self.cursor = self.connect.cursor()

	# Закрываем соединение с БД
	def close(self):
		self.connect.close()

    # Получаем id всех пользователей, позже будем проверять наличие пользователя в этом списке
	def get_all_id(self):
		self.connect_to_db()
		request = "SELECT id FROM Bot"
		result = self.cursor.execute(request).fetchall()
		self.close()

		return [i[0] for i in result]

    # Добавляем нового пользователя
	def add_id_to_db(self, user_id, name_user):
		self.connect_to_db()
		now = datetime.now()
		request = "INSERT or REPLACE into  Bot(idu, nameu, datime) VALUES(?, ?, ?)"
		self.cursor.execute(request, (user_id, name_user, now.strftime('%Y-%m-%d %H:%M:%S')))
		self.connect.commit()
		self.close()

    # Получаем поле back по пользователю
	def get_field(self, user_id):
		self.connect_to_db()
		request = f"SELECT back FROM Bot WHERE idu=?"
		result = self.cursor.execute(request, (user_id,)).fetchone()
		self.close()
		return result[0]

	# Меняем значение поля back
	def set_field(self, user_id, value):
		now = datetime.now()
		self.connect_to_db()
		request = f"UPDATE Bot SET back=?, datime=? WHERE idu=?"
		self.cursor.execute(request, (value, now.strftime('%Y-%m-%d %H:%M:%S'), user_id))
		self.connect.commit()
		self.close()

	def set_bal(self, user_id, exam, value):
		self.connect_to_db()
		request = f"UPDATE Bot SET "+exam+"=? WHERE idu=?"
		self.cursor.execute(request, (value, user_id))
		self.connect.commit()
		self.close()

	def get_bal(self, user_id, exam):
		self.connect_to_db()
		request = f"SELECT "+exam+" FROM Bot WHERE idu=?"
		result = self.cursor.execute(request, (user_id,)).fetchone()
		self.close()
		return result[0]

	def get_dir(self, lg, llg, bal, exfp):
		i = []
		self.connect_to_db()
		request = f"SELECT name, "+exfp+", loc FROM UGE WHERE exam LIKE '%"+lg+"%' AND exam LIKE '%"+llg+"%' AND "+exfp+" <="+str(bal)+" AND NOT (exam LIKE '%"+lg+"/"+llg+"%' OR exam LIKE '%"+llg+"/"+lg+"%')"
		result = self.cursor.execute(request).fetchall()
		self.close()
		for row in result:
			i.append(row[0]+". Проходной балл: "+str(row[1])+". Местоположение: "+row[2]+".")
		return i

	def del_bal(self, user_id):
		self.connect_to_db()
		request = f"UPDATE Bot SET bru=?, bm=?, bf=?, bi=?, bh=?, bo=?, bin=?, bg=? WHERE idu=?"
		self.cursor.execute(request, (None, None, None, None, None, None, None, None, user_id))
		self.connect.commit()
		self.close()

	def get_calall(self, idc):
		i = []
		self.connect_to_db()
		request = f"SELECT dname, dtext, dtime FROM Cal WHERE id=?"
		result = self.cursor.execute(request, (idc,)).fetchall()
		self.close()
		for row in result:
			i.append(row[0]+".\nПодробнее: "+row[1]+"\nВремя проведения: "+row[2]+".")
		return i

	def get_calname(self, idc):
		i = []
		self.connect_to_db()
		request = f"SELECT dname, d, M FROM Cal WHERE id=?"
		result = self.cursor.execute(request, (idc,)).fetchall()
		self.close()
		for row in result:
			i.append(row[0]+"-"+row[1]+"."+row[2])
		return i

	def get_calnum(self):
		self.connect_to_db()
		request = f"SELECT dname FROM Cal"
		result = len(self.cursor.execute(request).fetchall())
		self.close()
		return result

	def get_info(self, tar):
		i = []
		self.connect_to_db()
		request = f"SELECT name, loc, exam, balf, balp, sf, sp, k1, k2, k3 FROM UGE WHERE name=? OR k1=? OR k2=? OR k3=?"
		result = self.cursor.execute(request, (tar, tar, tar, tar)).fetchall()
		self.close()
		for row in result:
			l0 = row[0]
			l1 = row[1]
			l2 = row[2]
			l3 = row[3]
			l4 = row[4]
			l5 = row[5]
			l6 = row[6]
			l7 = row[7]
			l8 = row[8]
			l9 = row[9]
			if l3 == None:
				l3 = "-"
			if l4 == None:
				l4 = "-"
			if l5 == None:
				l5 = "-"
			if l6 == None:
				l6 = "-"
			if l7 == None:
				l7 = "-"
			if l8 == None:
				l8 = "-"
			if l9 == None:
				l9 = "-"
			i.append("Название:"+l0+".\nМестоположение: "+l1+"\nЭкзамены, которые нужны для поступления: "+l2+".\nПроходной бал на бюджет: "+str(l3)+".\nПроходной бал на коммерцию: "+str(l4)+".\nМест на бюджете: "+str(l5)+".\nПлатных мест: "+str(l6)+".\nКоды оброзовательных программ: "+l7+"; "+l8+"; "+l9+".")
		return i
			
obj = User()

@dp.message_handler(commands=['start']) #Явно указываем в декораторе, на какую команду реагируем. 
async def start(message: types.Message):

	obj.add_id_to_db(message.from_user.id, message.from_user.first_name)

	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_1 = types.KeyboardButton(text="Что такое МАИ?")
	keyboard.add(button_1)
	button_2 = types.KeyboardButton(text="Узнай себя: профориентационный тест")
	keyboard.add(button_2)
	button_3 = types.KeyboardButton(text="О поступлении 2023")
	keyboard.add(button_3)
	button_4 = types.KeyboardButton(text="Подготовка к поступлению")
	keyboard.add(button_4)
	button_5 = types.KeyboardButton(text="Дни открытых дверей")
	keyboard.add(button_5)
	button_6 = types.KeyboardButton(text="Календарь абитуриента!")
	keyboard.add(button_6)
	photo = open('МАИ.jpg', 'rb')
	await bot.send_photo(chat_id=message.chat.id, photo=photo)
	photo.close()
	await message.answer("Привет, {0.first_name}! Я чат-бот приёмной комиссии МАИ. Я расскажу тебе о нашем университете и отвечу на твои вопросы. Переходи в меню ⬇️.".format(message.from_user), reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Что такое МАИ?")
async def MAI(message: types.Message):
	k1 = types.InlineKeyboardMarkup()
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	b11 = types.InlineKeyboardButton("Лучший вуз", url='https://youtu.be/AgK85v1TJSE')
	k1.add(b11)
	button_1 = types.KeyboardButton(text="Узнать больше о МАИ")
	keyboard.add(button_1)
	button_2 = types.KeyboardButton(text="Наши социальные сети")
	keyboard.add(button_2)
	bb = types.KeyboardButton(text="Назад")
	keyboard.add(bb)
	obj.set_field(message.from_user.id, '0')
	await message.answer("Давай посмотрим 📹.", reply_markup=k1)
	await message.answer("Продолжаем удивлять.", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Узнать больше о МАИ")
async def MAI1(message: types.Message):
	k2 = types.InlineKeyboardMarkup()
	b21 = types.InlineKeyboardButton("МАИ", url='priem.mai.ru')
	k2.add(b21)
	obj.set_field(message.from_user.id, '0')
	await message.answer("МАИ сегодня — это целая экосистема, которая формирует успешных специалистов. Здесь каждый может овладеть современными технологиями и профессиями будущего, найти друзей и единомышленников, расти и развиваться во всех сферах жизни.\nСобрали для тебя цифры, факты и не только!", reply_markup=k2)

@dp.message_handler(lambda message: message.text == "Наши социальные сети")
async def MAI2(message: types.Message):
	k1 = types.InlineKeyboardMarkup()
	b1 = types.InlineKeyboardButton("ВК", url='https://vk.com/maiuniversity')
	b2 = types.InlineKeyboardButton("Телеграм", url='https://t.me/MAIuniversity')
	b3 = types.InlineKeyboardButton("Ютуб", url='https://www.youtube.com/channel/UCrmLlRAoO8j4w4yF8fpqLMQ')
	k1.add(b1, b2, b3)
	await message.answer("Делимся ссылками на социальные сети для абитуриентов МАИ. Не забудь подписаться!", reply_markup=k1)

@dp.message_handler(lambda message: message.text == "Узнай себя: профориентационный тест")
async def TEST(message: types.Message):
	k2 = types.InlineKeyboardMarkup()
	b21 = types.InlineKeyboardButton("Тест", url='https://pre.mai.ru/admission/preparation/test/')
	k2.add(b21)
	await message.answer("Мы составили для вас профориентационный тест, который, может помочь вам лучше разобраться в своих увлечениях и найти верный образовательный путь. Тест подскажет направление, а конечный выбор за вами!", reply_markup=k2)

@dp.message_handler(lambda message: message.text == "О поступлении 2023")
async def ABI(message: types.Message):
	kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_1 = types.KeyboardButton(text="Поступаю на бакалавриат/специалитет")
	kb1.add(button_1)
	button_2 = types.KeyboardButton(text="Поступаю в магистратуру")
	kb1.add(button_2)
	button_3 = types.KeyboardButton(text="Иностранный гражданин")
	kb1.add(button_3)
	bb = types.KeyboardButton(text="Назад")
	kb1.add(bb)
	obj.set_field(message.from_user.id, '0')
	await message.answer("Что правильно ответить на твои вопросы, давай познакомимся поближе 🙂", reply_markup=kb1)

@dp.message_handler(lambda message: message.text == "Поступаю на бакалавриат/специалитет")
async def ABI1(message: types.Message):
	kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_1 = types.KeyboardButton(text="Проходные быллы прошлых лет")
	kb1.add(button_1)
	button_2 = types.KeyboardButton(text="Выбрать направление")
	kb1.add(button_2)
	button_3 = types.KeyboardButton(text="Количество мест")
	kb1.add(button_3)
	button_4 = types.KeyboardButton(text="Обучение по контракту")
	kb1.add(button_4)
	button_5 = types.KeyboardButton(text="Про общежития")
	kb1.add(button_5)
	button_6 = types.KeyboardButton(text="Калькулятор ЕГЭ")
	kb1.add(button_6)
	button_7 = types.KeyboardButton(text="Информация о направлениях")
	kb1.add(button_7)
	bb = types.KeyboardButton(text="Назад")
	kb1.add(bb)
	obj.set_field(message.from_user.id, '1')
	await message.answer("Чем интересуешься?", reply_markup=kb1)

@dp.message_handler(lambda message: message.text == "Проходные быллы прошлых лет")
async def ABI11(message: types.Message):
	kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_1 = types.KeyboardButton(text="2022")
	button_2 = types.KeyboardButton(text="2020")
	button_3 = types.KeyboardButton(text="2019")
	kb2.add(button_1, button_2, button_3)
	bb = types.KeyboardButton(text="Назад")
	kb2.add(bb)
	obj.set_field(message.from_user.id, '2')
	await message.answer("Сейчас посмотрим...", reply_markup=kb2)

@dp.message_handler(lambda message: message.text == "2022")
async def ABI111(message: types.Message):
	kb3 = types.InlineKeyboardMarkup()
	b101 = types.InlineKeyboardButton("2022", url='https://priem.mai.ru/bachelor/tests/?layout=table&index=4')
	kb3.add(b101)
	await message.answer("Я бы не поступил.", reply_markup=kb3)

@dp.message_handler(lambda message: message.text == "2020")
async def ABI112(message: types.Message):
	kb3 = types.InlineKeyboardMarkup()
	b101 = types.InlineKeyboardButton("2020", url='https://files.mai.ru/site/education/points2020.pdf')
	kb3.add(b101)
	await message.answer("Я бы не поступил.", reply_markup=kb3)

@dp.message_handler(lambda message: message.text == "2019")
async def ABI113(message: types.Message):
	kb3 = types.InlineKeyboardMarkup()
	b101 = types.InlineKeyboardButton("2019", url='https://files.mai.ru/site/education/points2019.pdf')
	kb3.add(b101)
	await message.answer("Я бы не поступил.", reply_markup=kb3)

@dp.message_handler(lambda message: message.text == "Выбрать направление")
async def ABI12(message: types.Message):
	kb3 = types.InlineKeyboardMarkup()
	b101 = types.InlineKeyboardButton("Направления", url='https://priem.mai.ru/bachelor/programs/')
	kb3.add(b101)
	await message.answer("У нас много чего есть.", reply_markup=kb3)

@dp.message_handler(lambda message: message.text == "Количество мест")
async def ABI13(message: types.Message):
	kb3 = types.InlineKeyboardMarkup()
	b101 = types.InlineKeyboardButton("Количество мест", url='https://mai.ru/abitur/priemKolMest/')
	kb3.add(b101)
	await message.answer("Смотрим...", reply_markup=kb3)

@dp.message_handler(lambda message: message.text == "Обучение по контракту")
async def ABI14(message: types.Message):
	kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_1 = types.KeyboardButton(text="Стоимость")
	kb2.add(button_1)
	bb = types.KeyboardButton(text="Назад")
	kb2.add(bb)
	obj.set_field(message.from_user.id, '2')
	await message.answer("Сейчас посмотрим...", reply_markup=kb2)

@dp.message_handler(lambda message: message.text == "Стоимость")
async def ABI141(message: types.Message):
	kb3 = types.InlineKeyboardMarkup()
	b101 = types.InlineKeyboardButton("Стоимость обучения", url='https://mai.ru/education/studies/price/firstcourse/?layout=table&index=0')
	kb3.add(b101)
	await message.answer("Информация о стоимости обучния представлена на странице.", reply_markup=kb3)

@dp.message_handler(lambda message: message.text == "Про общежития")
async def ABI15(message: types.Message):
	kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_1 = types.KeyboardButton(text="Порядок предоставления мест в общежитиях")
	kb2.add(button_1)
	button_2 = types.KeyboardButton(text="Порядок заселения в общежития")
	kb2.add(button_2)
	button_3 = types.KeyboardButton(text="Распределение мест в общежитиях")
	kb2.add(button_3)
	button_4 = types.KeyboardButton(text="Заселение в общежитие студентов 1 курса")
	kb2.add(button_4)
	bb = types.KeyboardButton(text="Назад")
	kb2.add(bb)
	obj.set_field(message.from_user.id, '2')
	await message.answer("Сейчас расскажем.", reply_markup=kb2)

@dp.message_handler(lambda message: message.text == "Порядок предоставления мест в общежитиях")
async def ABI151(message: types.Message):
	kb3 = types.InlineKeyboardMarkup()
	b101 = types.InlineKeyboardButton("Предоставления мест в общежитиях", url='https://priem.mai.ru/orders/hostel/terms/')
	kb3.add(b101)
	await message.answer("Информация представлена на странице.", reply_markup=kb3)

@dp.message_handler(lambda message: message.text == "Порядок заселения в общежития")
async def ABI152(message: types.Message):
	kb3 = types.InlineKeyboardMarkup()
	b101 = types.InlineKeyboardButton("Заселения в общежития", url='https://priem.mai.ru/orders/hostel/check-in/')
	kb3.add(b101)
	await message.answer("Информация представлена на странице.", reply_markup=kb3)

@dp.message_handler(lambda message: message.text == "Распределение мест в общежитиях")
async def ABI153(message: types.Message):
	await message.answer("В общежитиях МАИ для приёма на 1-й курс на программы бакалавриата, программы специалитета и программы магистратуры в 2023 году будет выделено не менее 800 мест."
"Места в общежитии, оставшиеся невостребованными после зачисления по особой и целевой квотам переходят на общий конкурс.")

@dp.message_handler(lambda message: message.text == "Заселение в общежитие студентов 1 курса")
async def ABI154(message: types.Message):
	kb3 = types.InlineKeyboardMarkup()
	b101 = types.InlineKeyboardButton("Заселение студентов 1 курса", url='https://priem.mai.ru/orders/hostel/check-in2020/')
	kb3.add(b101)
	await message.answer("Информация представлена на странице.", reply_markup=kb3)

@dp.message_handler(lambda message: message.text == "Калькулятор ЕГЭ")
async def ABI16(message: types.Message):
	kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_1 = types.KeyboardButton(text="Русский язык")
	kb1.add(button_1)
	button_2 = types.KeyboardButton(text="Математика")
	kb1.add(button_2)
	button_3 = types.KeyboardButton(text="Физика")
	kb1.add(button_3)
	button_4 = types.KeyboardButton(text="Информатика и ИКТ")
	kb1.add(button_4)
	button_5 = types.KeyboardButton(text="Обществознание")
	kb1.add(button_5)
	button_6 = types.KeyboardButton(text="История")
	kb1.add(button_6)
	button_7 = types.KeyboardButton(text="География")
	kb1.add(button_7)
	button_8 = types.KeyboardButton(text="Иностранный язык")
	kb1.add(button_8)
	button_9 = types.KeyboardButton(text="Биология")
	kb1.add(button_9)
	button_10 = types.KeyboardButton(text="Найти направления (Ввел все быллы)")
	kb1.add(button_10)
	button_11 = types.KeyboardButton(text="Обнулить введенные баллы")
	kb1.add(button_11)
	bb = types.KeyboardButton(text="Назад")
	kb1.add(bb)
	obj.set_field(message.from_user.id, '2')
	await message.answer("Для выбора направления введите ваши баллы ЕГЭ.", reply_markup=kb1)

@dp.message_handler(lambda message: message.text == "Русский язык")
async def ABI161(message: types.Message):
	await Mydialog.otvet1.set()
	await message.answer("Введите баллы ЕГЭ по русскому языку.")

@dp.message_handler(state=Mydialog.otvet1)
async def process_message1(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		if message.text.isdigit() == True and int(message.text) <= 100 and  int(message.text) >= 40:
			obj.set_bal(message.from_user.id, "bru", message.text)
			await message.answer("Записано, введите следующие быллы или перейдите к результату.")
		elif message.text.isdigit() == False:
			await message.answer("Я вас не понимаю, ввод некорректный.")
		else:
			await message.answer("Ваши баллы не проходят порог(")
		await state.finish()

@dp.message_handler(lambda message: message.text == "Математика")
async def ABI162(message: types.Message):
	await Mydialog.otvet2.set()
	await message.answer("Введите баллы ЕГЭ по математике.")

@dp.message_handler(state=Mydialog.otvet2)
async def process_message2(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		if message.text.isdigit() == True and int(message.text) <= 100 and  int(message.text) >= 39:
			obj.set_bal(message.from_user.id, "bm", message.text)
			await message.answer("Записано, введите следующие быллы или перейдите к результату.")
		else:
			await message.answer("Я вас не понимаю, ввод некорректный.")
		await state.finish()

@dp.message_handler(lambda message: message.text == "Физика")
async def ABI163(message: types.Message):
	await Mydialog.otvet3.set()
	await message.answer("Введите баллы ЕГЭ по физике.")

@dp.message_handler(state=Mydialog.otvet3)
async def process_message3(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		if message.text.isdigit() == True and int(message.text) <= 100 and  int(message.text) >= 39:
			obj.set_bal(message.from_user.id, "bf", message.text)
			await message.answer("Записано, введите следующие быллы или перейдите к результату.")
		else:
			await message.answer("Я вас не понимаю, ввод некорректный.")
		await state.finish()

@dp.message_handler(lambda message: message.text == "Информатика и ИКТ")
async def ABI164(message: types.Message):
	await Mydialog.otvet4.set()
	await message.answer("Введите баллы ЕГЭ по информатике и ИКТ.")

@dp.message_handler(state=Mydialog.otvet4)
async def process_message4(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		if message.text.isdigit() == True and int(message.text) <= 100 and  int(message.text) >= 44:
			obj.set_bal(message.from_user.id, "bi", message.text)
			await message.answer("Записано, введите следующие быллы или перейдите к результату.")
		else:
			await message.answer("Я вас не понимаю, ввод некорректный.")
		await state.finish()

@dp.message_handler(lambda message: message.text == "Обществознание")
async def ABI165(message: types.Message):
	await Mydialog.otvet5.set()
	await message.answer("Введите баллы ЕГЭ по обществознанию.")

@dp.message_handler(state=Mydialog.otvet5)
async def process_message5(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		if message.text.isdigit() == True and int(message.text) <= 100 and  int(message.text) >= 45:
			obj.set_bal(message.from_user.id, "bo", message.text)
			await message.answer("Записано, введите следующие быллы или перейдите к результату.")
		else:
			await message.answer("Я вас не понимаю, ввод некорректный.")
		await state.finish()

@dp.message_handler(lambda message: message.text == "История")
async def ABI166(message: types.Message):
	await Mydialog.otvet6.set()
	await message.answer("Введите баллы ЕГЭ по истории.")

@dp.message_handler(state=Mydialog.otvet6)
async def process_message6(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		if message.text.isdigit() == True and int(message.text) <= 100 and  int(message.text) >= 50:
			obj.set_bal(message.from_user.id, "bh", message.text)
			await message.answer("Записано, введите следующие быллы или перейдите к результату.")
		else:
			await message.answer("Я вас не понимаю, ввод некорректный.")
		await state.finish()

@dp.message_handler(lambda message: message.text == "География")
async def ABI167(message: types.Message):
	await Mydialog.otvet7.set()
	await message.answer("Введите баллы ЕГЭ по географии.")

@dp.message_handler(state=Mydialog.otvet7)
async def process_message7(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		if message.text.isdigit() == True and int(message.text) <= 100 and  int(message.text) >= 50:
			obj.set_bal(message.from_user.id, "bg", message.text)
			await message.answer("Записано, введите следующие быллы или перейдите к результату.")
		else:
			await message.answer("Я вас не понимаю, ввод некорректный.")
		await state.finish()

@dp.message_handler(lambda message: message.text == "Иностранный язык")
async def ABI168(message: types.Message):
	await Mydialog.otvet8.set()
	await message.answer("Введите баллы ЕГЭ по иностранному языку.")

@dp.message_handler(state=Mydialog.otvet8)
async def process_message8(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		if message.text.isdigit() == True and int(message.text) <= 100 and  int(message.text) >= 50:
			obj.set_bal(message.from_user.id, "bin", message.text)
			await message.answer("Записано, введите следующие быллы или перейдите к результату.")
		else:
			await message.answer("Я вас не понимаю, ввод некорректный.")
		await state.finish()

@dp.message_handler(lambda message: message.text == "Биология")
async def ABI169(message: types.Message):
	await Mydialog.otvet9.set()
	await message.answer("Введите баллы ЕГЭ по биологии.")

@dp.message_handler(state=Mydialog.otvet9)
async def process_message9(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		if message.text.isdigit() == True and int(message.text) <= 100 and  int(message.text) >= 36:
			obj.set_bal(message.from_user.id, "bb", message.text)
			await message.answer("Записано, введите следующие быллы или перейдите к результату.")
		else:
			await message.answer("Я вас не понимаю, ввод некорректный.")
		await state.finish()

@dp.message_handler(lambda message: message.text == "Найти направления (Ввел все быллы)")
async def ABI169(message: types.Message):
	RU = obj.get_bal(message.from_user.id, "bru")
	M = obj.get_bal(message.from_user.id, "bm")
	F = obj.get_bal(message.from_user.id, "bf")
	I = obj.get_bal(message.from_user.id, "bi")
	G = obj.get_bal(message.from_user.id, "bg")
	H = obj.get_bal(message.from_user.id, "bh")
	O = obj.get_bal(message.from_user.id, "bo")
	IN = obj.get_bal(message.from_user.id, "bin")
	B = obj.get_bal(message.from_user.id, "bb")
	with open("buge.txt", "r") as f:
		text = f.read()
	if text == '0':
		await message.answer("Направления, куда вы проходите на бюджет:")
		await message.answer("Просим вас обратить особое внимание на то, что результаты работы чат-бота основываются на проходных баллах прошлых лет. В текущем году конкурсная ситуация может измениться.")
		await ABI169S("balf", RU, M, F, I, G, H, O, IN, B, message)
		await message.answer("Направления, куда вы проходите платно:")
		await ABI169S("balp", RU, M, F, I, G, H, O, IN, B, message)
	if text == '1':
		await message.answer("Идет обновление базы данных, пожалуйста, повторите попытку позже.")
	f.close()

@dp.message_handler(lambda message: message.text == "Обнулить введенные баллы")
async def ABI1610(message: types.Message):
	obj.del_bal(message.from_user.id)
	await message.answer("Баллы обнулены.")

@dp.message_handler(lambda message: message.text == "Информация о направлениях")
async def ABI17(message: types.Message):
	with open("buge.txt", "r") as f:
		text = f.read()
	if text == '0':
		await Mydialog.otvet10.set()
		await message.answer("Чтобы получить информацию по конкретному направлению введите его название или код образовательной программы.")
	elif text == '1':
		await message.answer("Идет обновление базы данных, пожалуйста, повторите попытку позже.")

@dp.message_handler(state=Mydialog.otvet10)
async def process_message_info(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		lst = obj.get_info(message.text)
		if lst != []:
			await message.answer(''.join(lst))
			await message.answer("Если вы хотите получить информацию по другим направлениям, нажмите кнопку \"Информация о направлениях\" еще раз.")
		else:
			await message.answer("Не смог ничего найти. Нажмите кнопку еще раз, чтобы попробовать снова.")
		await state.finish()

@dp.message_handler(lambda message: message.text == "Поступаю в магистратуру")
async def ABI2(message: types.Message):
	kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_1 = types.KeyboardButton(text="Количество мест")
	kb1.add(button_1)
	button_2 = types.KeyboardButton(text="Вступительные испытания")
	kb1.add(button_2)
	button_3 = types.KeyboardButton(text="Общая информация")
	kb1.add(button_3)
	bb = types.KeyboardButton(text="Назад")
	kb1.add(bb)
	obj.set_field(message.from_user.id, '1')
	await message.answer("Чем интересуешься?", reply_markup=kb1)

@dp.message_handler(lambda message: message.text == "Вступительные испытания")
async def ABI21(message: types.Message):
	kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_1 = types.KeyboardButton(text="Программы вступительных испытаний")
	kb1.add(button_1)
	button_2 = types.KeyboardButton(text="Расписание экзаменов и консультаций")
	kb1.add(button_2)
	bb = types.KeyboardButton(text="Назад")
	kb1.add(bb)
	obj.set_field(message.from_user.id, 'mag1')
	await message.answer("Не каждый сможет.", reply_markup=kb1)	

@dp.message_handler(lambda message: message.text == "Программы вступительных испытаний")
async def ABI211(message: types.Message):
	kb3 = types.InlineKeyboardMarkup()
	b101 = types.InlineKeyboardButton("Программы вступительных испытаний", url='https://priem.mai.ru/orders/testing/magistracy-guidelines/?referer=https%3A%2F%2Fyandex.ru%2F')
	kb3.add(b101)
	await message.answer("Смотрим...", reply_markup=kb3)

@dp.message_handler(lambda message: message.text == "Расписание экзаменов и консультаций")
async def ABI211(message: types.Message):
	kb3 = types.InlineKeyboardMarkup()
	b101 = types.InlineKeyboardButton("Расписание экзаменов и консультаций", url='https://priem.mai.ru/master/tests/#schedule')
	kb3.add(b101)
	await message.answer("Смотрим...", reply_markup=kb3)

@dp.message_handler(lambda message: message.text == "Общая информация")
async def ABI22(message: types.Message):
	await message.answer("При подаче заявления в приёмную комиссию вы можете выбрать одно направление, на которое хотите поступать.\n· Все экзамены проводятся в письменной форме;\n· Иностранные граждане имеют право сдавать экзамены на английском языке и/или с использованием дистанционных технологий;\n· Абитуриентам создаются условия для сдачи экзаменов с учётом ограничений по здоровью.")

@dp.message_handler(lambda message: message.text == "Иностранный гражданин")
async def ABI3(message: types.Message):
	kb3 = types.InlineKeyboardMarkup()
	b101 = types.InlineKeyboardButton("Для иностранных граждан", url='https://priem.mai.ru/orders/foreign-applicants/?referer=https%3A%2F%2Fyandex.ru%2F')
	kb3.add(b101)
	await message.answer("Особенности проведения приёма иностранных граждан и лиц без гражданства:", reply_markup=kb3)

@dp.message_handler(lambda message: message.text == "Подготовка к поступлению")
async def PRE(message: types.Message):
	kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_1 = types.KeyboardButton(text="Центр подготовительных курсов")
	kb1.add(button_1)
	button_2 = types.KeyboardButton(text="Физико-математическая школа")
	kb1.add(button_2)
	bb = types.KeyboardButton(text="Назад")
	kb1.add(bb)
	obj.set_field(message.from_user.id, '0')
	await message.answer("МАИ поможет подготовиться к поступлению, а также к участию в олимпиадах и конкурсах, победители которых получают дополнительные баллы или поступают вне конкурса ", reply_markup=kb1)	

@dp.message_handler(lambda message: message.text == "Центр подготовительных курсов")
async def PRE1(message: types.Message):
	kb1 = types.InlineKeyboardMarkup()
	b1 = types.InlineKeyboardButton("Информация о курсах МАИ", url='https://pre.mai.ru/admission/courses/')
	kb1.add(b1)
	await message.answer("В Центре подготовительных курсов пройти обучение могут ученики 8-11 классов, студенты колледжей, а также иностранные граждане. Подробнее:", reply_markup=kb1)

@dp.message_handler(lambda message: message.text == "Физико-математическая школа")
async def PRE2(message: types.Message):
	kb1 = types.InlineKeyboardMarkup()
	b1 = types.InlineKeyboardButton("Школа", url='https://pre.mai.ru/admission/fmshmai/')
	kb1.add(b1)
	await message.answer("Физико-математическая школа — это курсы дополнительного обучения для учеников 9-11 классов, где углубленно изучаются физика и математика. Подробнее:", reply_markup=kb1)

@dp.message_handler(lambda message: message.text == "Дни открытых дверей")
async def FREEday(message: types.Message):
	k2 = types.InlineKeyboardMarkup()
	b21 = types.InlineKeyboardButton("Дни открытых дверей 2023", url='https://pre.mai.ru/events/public/?from=mairu&referer=https%3A%2F%2Fyandex.ru%2F')
	k2.add(b21)
	await message.answer("Расписание Дней открытых дверей, а также онлайн записи прошедших мероприятий ты найдёшь на нашем сайте для школьников. Жми на кнопку!", reply_markup=k2)

@dp.message_handler(lambda message: message.text == "Календарь абитуриента!") #Явно указываем в декораторе, на какую команду реагируем. 
async def Calendar(message: types.Message):
	with open("bcal.txt", "r") as f:
		text = f.read()
	if text == '0':
		for i in range(1, obj.get_calnum()+1):
			lst = obj.get_calall(i)
			await message.answer(''.join(lst))
			name = obj.get_calname(i)
			cal = open('ICS\\'+''.join(name)+'.ics', 'rb')
			await bot.send_document(message.chat.id, cal)
			cal.close()
			time.sleep(0.5)
		await message.answer('Весь календарь загружен.')
	elif text == '1':
		await message.answer('Идет обновление базы данных, пожалуйста, повторите попытку позже.')
	f.close()

@dp.message_handler(lambda message: message.text == "Назад")
async def Back(message: types.Message):

	if obj.get_field(message.from_user.id) == '0':
		await start(message)
	elif obj.get_field(message.from_user.id) == '1':
		await ABI(message)
	elif obj.get_field(message.from_user.id) == '2':
		await ABI1(message)
	elif obj.get_field(message.from_user.id) == "mag1":
		await ABI2(message)
	elif obj.get_field(message.from_user.id) == "Sch1":
		await PRE(message)

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)