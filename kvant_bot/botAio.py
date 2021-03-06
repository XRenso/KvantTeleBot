import aiogram.utils.markdown as md
from aiogram import Bot, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
import aiogram
import asyncio
import config
##################################3

#другие файлы Py из этого проекта
import keyboards as kb
import webParse as WP
import kvantums_info as kinf

##########################3
import logging
import random
import os
import codecs
from sqlighter import SQLighter
from datetime import datetime

news_url = 'http://kvantorium.iroso.ru/news'

db = SQLighter('db.db')

async def check_updates(wait_for):
	while True:
		await asyncio.sleep(wait_for)
		html_news = WP.get_html(news_url)
		subscriptions = db.get_subscriptions()
		current_news_url = WP.get_url(html_news)
		f = codecs.open('lastData.txt','r', 'utf_8_sig' )
		last_news_url = f.read()
		if last_news_url != current_news_url:
			current_news_date = WP.get_date(html_news)
			current_news_title = WP.get_title(html_news)
			for s in subscriptions:
				try:
					await bot.send_message(s[1], current_news_title + italic('\nДата новости: ') + current_news_date, parse_mode = ParseMode.MARKDOWN, reply_markup = kb.inline_kb_news(current_news_url))
				except aiogram.utils.exceptions.BotBlocked:
					continue
			with open('lastData.txt', 'w', encoding= 'utf-8') as f:
				f.write(str(current_news_url))
				f.close()



bot = Bot(token = config.token)
dp = Dispatcher(bot, storage=MemoryStorage())



admin_list = [483058216, 1495232168]
admin = False


logging.basicConfig(level=logging.INFO)

eventText = None
events = None #текст событий

main_menu_meet =['🤯','Гном нашёл вас и привез обратно', 'Вы нашли магический портал, и он переместил вас сюда', 'Да, здравствуйет магия прогроммирования' , 'Kahoooooooooot', 'Голуби нашли вас и пренисли вас обратно', 'Вжух Вжух, вы дома)', 'What\'s up', 'Какое чудное время. Технологии могут переместить вас на главное меню.', 'Колдунья не обманула вас это и вправду портал', 'Интересно если машины захватят мир, то будет ли этот бот во главе?', 'На сколько умён этот бот', 'IT квантУМ самый первый в "КванторУМ"']

class AnswerAdmin(StatesGroup):
    event = State()

@dp.message_handler(commands =['send_all_photo'])
async def get_id(message):
	await get_photo_to_send_admin(message)
	try:
		photo = open('./rss.jpg', 'rb')
	except OSError:
		await get_photo_to_send_admin(message)
	subscriptions = db.get_subscriptions()
	global admin
	admin = False
	if message.chat.id in admin_list:
		admin = True
	if admin == True:
		for user in subscriptions:
			try:
				await bot.send_photo(user[1], './rss.jpg' ,caption = message.text)
			except aiogram.utils.exceptions.BotBlocked:
				continue
			except aiogram.utils.exceptions.CantTalkWithBots:
				continue
@dp.message_handler(content_types=['photo'])
async def get_photo_to_send_admin(message):
	await message.photo[-1].download('rss.jpg')

#запись полученного ответа пользователя в txt документ
async def hello(message):

	with open('events.txt', 'w', encoding= 'utf-8') as f:
		f.write(str(message.text))
	events = message.text
	await bot.send_message(message.chat.id, 'Событие добавлено')


#Получение ответа от пользователя
@dp.message_handler(state=AnswerAdmin.event)
async def event_text(message: types.Message, state:FSMContext):
	eventText = message

	await state.update_data(eventik=eventText)
	await hello(eventText)
	await state.finish()

#получение последних новостей
@dp.message_handler(commands =['last_news'])
async def get_id(message: types.Message):
	html_news = WP.get_html(news_url)
	current_news_date = WP.get_date(html_news)
	current_news_title = WP.get_title(html_news)
	current_news_url = WP.get_url(html_news)
	await bot.send_message(message.chat.id, current_news_title + italic('\nДата новости: ') + current_news_date, parse_mode = ParseMode.MARKDOWN, reply_markup = kb.inline_kb_news(current_news_url))

#получение id чата
@dp.message_handler(commands =['get_id'])
async def get_id(message: types.Message):
	await message.answer(message.from_user.id)

#открытие админ панели при наличии прав администратора
@dp.message_handler(commands = ['admin_pan'])
async def admin_pan_open(message: types.Message):
	global admin
	admin = False
	if message.chat.id in admin_list:
		admin = True
	if admin == True:
		await bot.send_message(message.chat.id, 'Добро пожаловать в Админ панель', reply_markup = kb.admin_kb)


#сделать рассылку пользователям
@dp.message_handler(commands = ['send_all'])
async def send_all(message: types.Message):
	subscriptions = db.get_subscriptions()
	global admin
	admin = False
	if message.chat.id in admin_list:
		admin = True
	if admin == True:
		for user in subscriptions:
			try:
				await bot.send_message(user[1], message.text[message.text.find(' '):])
			except aiogram.utils.exceptions.BotBlocked:
				continue
			except aiogram.utils.exceptions.CantTalkWithBots:
				continue

#комманда начала работы с ботом
@dp.message_handler(commands = ['start'])
async def start(message: types.Message):

	global admin
	admin = False
	if message.chat.id in admin_list:

		admin = True

	await message.answer('Здравствуйте, добро пожаловать🖐.Это оффициальный бот тех.поддержки КванториУМа65🤖. Желаете продолжить?🤔', reply_markup = kb.inline_kb_start)

#получние текстовых комманд
@dp.message_handler(content_types = ['text'])
async def get_text(message: types.Message):
	global events
	global admin
	admin = False


	#комманды обыных пользователей
	if message.chat.id in admin_list:
		admin = True
	if message.text == '↩️На главное меню ↪️':
		await bot.send_message(message.chat.id, 'Вы хотите вернутся на главное меню?', reply_markup = kb.inline_kb_mainMenu_back)
	elif message.text == '™️Создатель©️':
		await message.reply('BORCH Entertainment \nПрограммист - Одерий Ярослав Александрович', reply_markup = kb.inline_kb_Creator)
	elif message.text == 'Номер тех.поддержки 📞':
		await message.reply('+74242300277')
	elif message.text == 'Мы в соц.сетях 📱':
		await bot.send_message(message.chat.id, 'Выберите тип соц.сети', reply_markup = kb.inline_kb_social)
	elif message.text == 'Информация о Кванториум - Сахалин ℹ️':
		await bot.send_message(message.chat.id, 'Выберите интересующую вас информацию.', reply_markup = kb.moreInfo_kb)

	elif message.text == '©️Партнёры™️':
		await bot.send_message(message.chat.id, bold('Наши партнёры:'), parse_mode = ParseMode.MARKDOWN, reply_markup = kb.inline_kb_sponsors)
	elif message.text == '🎟️ МЕРОПРИЯТИЕ 🎟️':
		success = True # успех изначально равен Правде чтобы не было проблем
		ready = False # готовность чтобы код не выполнялся паралелльно
		try:
			f = open('events.txt')
			f.close()
			ready = False #готовность равна лже т.к комманда только выполняется и ошибка не перехвачена

		except  IOError:

			success = False #перехват ошибки
		finally:

			ready = True #и если всё таки удалось найти файл, то его открываем

		if success == True and ready == True: #если успех равен првде и готовность, то мы открываем и берём событие

			f = codecs.open('events.txt','r', 'utf_8_sig' )

			fd = f.read()

			await bot.send_message(message.chat.id, fd.encode().decode('utf-8'))


		elif success == False and ready == True: # если успех равен лжи, а код готов, то бот пишет что нет событий
			await bot.send_message(message.chat.id, 'Сейчас нет каких либо мероприятий😥')

	elif message.text == '📜Общая информация про КванториУМ65.📜':
		await bot.send_message(message.chat.id,bold('Миссия') + ' - ' + kinf.kvant_mission + bold('\nЦель') + ' - ' + kinf.kvant_aim, parse_mode = ParseMode.MARKDOWN)
	elif message.text == '📰Управление подпиской на новости📰':
		await bot.send_message(message.chat.id, 'Выберите что вы хотите сделать?', reply_markup = kb.inline_kb_RSS)
	elif message.text == '🖥КвантУМы🖥':
		await bot.send_message(message.chat.id, 'Выберите квантУМ', reply_markup = kb.kvantum_choose_kb)
	elif message.text == '↩️Назад':
		await bot.send_message(message.chat.id, 'С возвращением', reply_markup = kb.moreInfo_kb)

	elif message.text == '💻IT-квантум💻':
		nice_to_meet_u = ['Вставай, самурай, время взломать этого бота!', 'Остановиста С++', 'Мир не сбыточных мечтаний', '"Понаберут айтишников по объявлениям" Ковач Александра Александровна']
		random.shuffle(nice_to_meet_u)
		for i in nice_to_meet_u:
			await bot.send_message(message.chat.id, i, reply_markup = kb.it_info_kb)
			break
	elif message.text == '👩‍💻 Наставники 👨‍💻':
		await message.reply(kinf.it_tutors)
	elif message.text == '🔎 Про IT-квантум 🔎':
		await message.reply(kinf.it_info)

	elif message.text == '🤖Промробоквантум🤖':
		robo_meet = ['Робот сочинит симфонию? Робот превратит кусок холста в шедевр искусства?', 'Робот не может причинить вреда человеку, если только он не докажет, что в конечном счёте это будет полезно для всего человечества.', 'Робот не может причинить вреда человеку или своим бездействием допустить, чтобы человеку был причинен вред.']
		random.shuffle(robo_meet)
		for i in robo_meet:
			await bot.send_message(message.chat.id, i, reply_markup = kb.robo_info_kb)
			break

	elif message.text == '🔎 Про Промробоквантум 🔎':
		await message.reply(kinf.robo_info)
	elif message.text == '👩‍💼 Наставники 👨‍💼':
		await message.reply(kinf.robo_tutors)

	elif message.text == '✈️Аэроквантум✈️':
		await bot.send_message(message.chat.id, 'Выберите интересующую вас информацию', reply_markup = kb.aero_info_kb)

	elif message.text == '🔎 Про Аэроквантум 🔎':
		await message.reply(kinf.aero_info)

	elif message.text == '👷‍♀️ Наставники 👷‍♂️':
		await message.reply(kinf.aero_tutors)

	elif message.text == '🎨Промдизайнквантум🎨':
		await bot.send_message(message.chat.id, 'Выберите интересующую вас информацию', reply_markup = kb.design_info_kb)

	elif message.text == '🔎 Про Промдизайнквантум 🔎':
		await message.reply(kinf.design_info)
	elif message.text == '🧑‍🎨 Наставники 👨‍🎨':
		await message.reply(kinf.design_tutors)

	elif message.text == '⚡Энерджиквантум⚡':
		await bot.send_message(message.chat.id, 'Выберите интересующую вас информацию', reply_markup = kb.energy_info_kb)

	elif message.text == '🔎 Про Энерджиквантум 🔎':
		await message.reply(kinf.energy_info)
	elif message.text == '👩‍🎓 Наставники 👨‍🎓':
		await message.reply(kinf.energy_tutors)

	elif message.text == '⚙️Хайтек⚙️':
		await bot.send_message(message.chat.id, 'Выберите интересующую вас информацию', reply_markup = kb.hitech_info_kb)

	elif message.text == '🔎 Про Хайтек 🔎':
		await message.reply(kinf.hitech_info)
	elif message.text == '👩‍🔧 Наставники 👨‍🔧':
		await message.reply(kinf.hitech_tutors)

	elif message.text == '🗺️Геоквантум🗺️':
		await bot.send_message(message.chat.id, 'Выберите интересующую вас информацию', reply_markup = kb.geo_info_kb)

	elif message.text == '🔎 Про Геоквантум 🔎':
		await message.reply(kinf.geo_info)
	elif message.text == '👩‍🏫 Наставники 👨‍🏫':
		await message.reply(kinf.geo_tutors)
	elif message.text == '⬅️ Назад к квантУМам ➡️':
		await bot.send_message(message.chat.id, 'Выберите квантУМ', reply_markup = kb.kvantum_choose_kb)


	elif message.text == '🧑‍💼 Руководство ДТ "Кванториум" ГБОУ ИРОСО 🧑‍💼':
		photo = open('./Artem_Sidorov-1.jpg', 'rb')
		await bot.send_photo(message.chat.id, photo , caption = 'Сидоров Артем Витальевич' + '\nДиректор детского технопарка' + '\nНаименование направления подготовки и (или) специальности:' + '\nФГБОУ ВО «Сахалинский государственный университет» Институт экономики и востоковедения, бакалавр востоковедения, африканистики (японский язык), \nг. Южно-Сахалинск, 2014 г. \nФГБОУ ВО «Сахалинский государственный университет», магистратура по направлению подготовки «Педагогическое образование», магистр, \nг. Южно-Сахалинск, 2016 г.')


#######################################################################################3
	#админ комманды
	if admin == True:
		if message.text == 'Админ Панель':
			await bot.send_message(message.chat.id, 'Вы в меню админа', reply_markup = kb.admin_kb)
		elif message.text == '🚫 Удалить события 🚫':
			await bot.send_message(message.chat.id, 'Вы уверены?🤔', reply_markup = kb.inline_kb_deleteEvent)

		elif message.text == '⚒️ Добавить событие ⚒️':
			await bot.send_message(message.chat.id, 'Вы уверены?🤔', reply_markup = kb.inline_kb_addEvent)





@dp.callback_query_handler(lambda c: c.data)
async def answer (call: types.CallbackQuery):
	global admin
	admin = False
	if call.message.chat.id in admin_list:
		admin = True

	callback_data = call.data
	#комманды обычных пользователей
	if callback_data == 'yesStart':
		await call.bot.send_message(call.message.chat.id,' Добро пожаловать, приятного пользования ботом 🤝',
		 	reply_markup = kb.main_menu_kb)
	elif callback_data == 'backMainMenu':
		random.shuffle(main_menu_meet)
		for i in main_menu_meet:
			await call.bot.send_message(call.message.chat.id, i, reply_markup = kb.main_menu_kb)
			break
	elif callback_data == 'noStart':
		await call.bot.send_message(call.message.chat.id, 'Очень жаль 😥. Если хотите вернутся используйте следущую комманду: /start')
	elif callback_data == 'stayHere':
		neudacha = ['К счастью вы успели выпрыгнуть из портала', 'Вы спрятались от гномов', 'Прогроммист спас вас от неминуемого краха', 'Вы проспали свой автобус', 'Вас никто не забрал', 'Чародеи обманули вас никаих порталов здесь нет', 'Вы просто никуда не пошли', 'Вы посчитали портал опасным']
		random.shuffle(neudacha)
		for i in neudacha:
			await call.bot.send_message(call.message.chat.id, i)
			break

	elif callback_data == 'RSSon':
		if(not db.subscriber_exists(call.message.chat.id)):
		# если юзера нет в базе, добавляем его
			db.add_subscriber(call.message.chat.id)
		else:
		# если он уже есть, то просто обновляем ему статус подписки
			db.update_subscription(call.message.chat.id, True)

		await call.message.answer("Вы успешно подписались на рассылку!")


	elif callback_data == 'RSSoff':
		if(not db.subscriber_exists(call.message.chat.id)):
		# если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
			db.add_subscriber(call.message.chat.id, False)
			await call.message.answer("Вы итак не подписаны.")
		else:
		# если он уже есть, то просто обновляем ему статус подписки
			db.update_subscription(call.message.chat.id, False)
			await call.message.answer("Вы успешно отписаны от рассылки.")


	#админ комманды
	if admin == True:
		if callback_data == 'delMusic':

			check_file = os.path.exists('music')
			if check_file == True:
				path = './music/'
				music_count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
				if music_count > 1:
					shutil.rmtree(path)
					os.mkdir(path)
					await call.bot.send_message(call.message.chat.id, 'Музыка успешно удаленна')
				elif music_count < 1:
					await call.bot.send_message(call.message.chat.id, 'Музыка отсутвует😥')
			elif check_file == False:
				path = './music/'
				await call.bot.send_message(call.message.chat.id, 'Музыка отсутвует😥')
				os.mkdir(path)


		elif callback_data == 'deleteEvent':
			success = True
			fact = ['✔️Молодец удалил событие, я тебя поздравляю✔️', '⚙️Тебе нравится работать?⚙️', '😎Это крутой бот😎', '🎵Какая ваша любимая музыка?🎵','Интересный факт - от вас завсит судьба кнопки 🎟️ МЕРОПРИЯТИЕ 🎟️', 'Вам нравится КванториУМ?', 'Linux или Windows', 'Бот написан за бесплатно', 'Изначально бот был экспериментом', 'Разработка ещё началась в 2020г']
			try:
				f = open('events.txt')
				f.close()
				ready = False #готовность равна лже т.к комманда только выполняется и ошибка не перехвачена

			except  IOError:

				success = False #перехват ошибки
			finally:

				ready = True #и если всё таки удалось найти файл, то его открываем

			if success == True and ready == True: #если успех равен првде и готовность, то мы открываем и берём событие
				path_event = 'events.txt'
				os.remove(path_event)
				await call.bot.send_message(call.message.chat.id, '✔️Событие успешно удаленно✔️')
				random.shuffle(fact)
				for i in fact:
					await call.bot.send_message(call.message.chat.id, i)
					break
			elif success == False and ready == True: # если успех равен лжи, а код готов, то бот пишет что нет событий
				await call.bot.send_message(call.message.chat.id, 'К сожелению события отсутвуют чтобы их удалить')


		elif callback_data == 'stayMessage':
			fartik = ['Фуххх, повезло', 'Щелчок таноса удалось избежать', 'Вас не уволят)', 'Какой генний чел который придумал отмену', 'Интересный факт - Вы Администратор)', 'Как дела?', 'КванториУМ хорошая вещь', 'Хорошего дня, Администратор', 'Как работа?', 'Удачи в жизни', 'Хорошая работа, Администратор', 'Вы были спасены, мои поздравления', 'Отличная погода, наверное.... Я всё таки бот не знаю как погода', 'Вам нравится хотдоги?', '#FREE_OPERATING_SYSTEM_FOR_EVERYONE', '101 телеграмм', 'Мне нравится развивать этого бота']
			random.shuffle(fartik)
			for  i in fartik:
				await call.bot.send_message(call.message.chat.id, i)
				break


		elif callback_data == 'write_event':
			await call.bot.send_message(call.message.chat.id, 'Введите ваше мероприятие/событие:' )
			await AnswerAdmin.event.set()

	if callback_data != 'None_site':
		await call.message.delete()
	if callback_data == 'None_site':
		await call.bot.send_message(call.message.chat.id, 'К сожелению здесь сайт отсутвует😥')

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.create_task(check_updates(120))
	executor.start_polling(dp, skip_updates = True)
