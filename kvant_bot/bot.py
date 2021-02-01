import config
import telebot
from telebot import types
import random
import constants
import os
import shutil
import codecs
import sys
import aiogram
import requests
#тех.работы
text_tech_work_settings = 'Настройки тех.работ'
text_tech_work_on = 'Объявить тех.работы'
text_tech_work_off = 'Закончить тех.работы'
text_would_setting_tech_work = 'Что сделать?'
text_tech_work_succes_on = 'Сервер успешно переведён в режим тех.работ'
text_tech_work_unsucces_on = 'Сервер уже находится на тех.работах'
text_tech_work_succes_off = 'Сервер успешно переведён в обычный режим'
text_tech_work_unsucces_off = 'Сервер уже находится в обычном режиме'


tech_work = False
text_tech_work_for_users = 'Бот сейчас на тех.работах'



#симуляция браузера
headers = requests.utils.default_headers()
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

#информация про кванториум сахалин
text_full_info_about_kvantorium_65 = '📜Общая информация про КванториУМ65.📜'
text_full_info_about_kvantorium_65_text = 'Привет👋, наш КванториУМ самый первый🥇 на острове Сахалин, вы представляете?! Это же круто быть одними из первых, мы с открытия (2017 год) обучаем детей и помогаем им узнавать новое в жизни. У нас имеется 7 КвантУМов, много разных педагогов с которыми вы сможете приятно провести время за обучением.'
token = config.token
client = telebot.TeleBot(config.token)
bot = aiogram.Bot(token = config.token)
dp = aiogram.Dispatcher(bot)

#RSS
FEED_URL = 'https://www.feedforall.com/sample.xml'

events = None#Текст мероприятий
text_ejtiejteite = 'https://t.me/XRenso'		

admin_list = [483058216]
admin = False
#MR- свод основных комманд и пунктов
#MR2 - строго обрабатывать действия пользователя связанных с админ доступом
  

@client.message_handler(commands = ['get_id'])
def get_id(message):
	client.send_message(message.chat.id, message.chat.id)

@client.message_handler(commands = ['start'])
def get_start(message):
	global admin


	
		

	if message.chat.id in admin_list:
		client.send_message(message.chat.id, 'У вас есть права администратора')
		admin = True
	markup_inline = types.InlineKeyboardMarkup()
	item_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'YES') #начальные кнопки которые спрашивают хочет ли пользователь продолжить
	item_no = types.InlineKeyboardButton(text = 'Нет', callback_data = 'NO')


	markup_inline.add(item_yes, item_no)
	client.send_message(message.chat.id,  'Здравствуйте, добро пожаловать🖐.Это оффициальный бот тех.поддержки КванториУМа65🤖. Желаете продолжить?🤔', 
		reply_markup = markup_inline

		)

def hello(message):
	 with open('events.txt', 'w', encoding= 'utf-8') as f:
	 	f.write(str(message.text))
	 events = message.text
	 client.send_message(message.chat.id, 'Событие добавлено')
	

def save_music(message):
	pass
	

@client.message_handler(content_types = ['text'])
def get_text (message):
	global events
	global admin
	global tech_work
	admin = False
	if message.chat.id in admin_list:
			admin = True
	

	markup_inline = types.InlineKeyboardMarkup()

	text_inst = 'https://www.instagram.com/kvantorium_65/' #ссылка на инстаграмм
	text_site = 'http://kvantorium.iroso.ru'    #ссылка на сайт
	number_reception = '+74242300277' #номер рецепшн
	#гипер-ссылки
	item_inst = types.InlineKeyboardButton(text="Инстаграмм🤳", url= text_inst )
	item_net = types.InlineKeyboardButton(text = 'Сайт🌎',url= text_site)

	#MR1 - логика кнопок(любое местко где кнопки отправляют текст нужно чтобы они соотвествовали данным)
	if tech_work == False:
		if message.text == 	'Номер тех.поддержки 📞':
			client.send_message(message.chat.id, number_reception)
		elif message.text == text_full_info_about_kvantorium_65:
			client.send_message(message.chat.id, text_full_info_about_kvantorium_65_text)
		elif message.text == 'Мы в соц.сетях 📱':
			markup_inline.add(item_inst, item_net)
			client.send_message(message.chat.id, 'Выберите тип соц.сети', reply_markup = markup_inline)

		elif message.text == '🎟️ МЕРОПРИЯТИЕ 🎟️':
			success = True # успех изначально равен Правде чтобы не было проблем
			ready = False # готовность чтобы код не выполнялся паралелльно
			try:
				f = open('events.txt')
				f.close()
				ready = False #готовность равна лже т.к комманда только выполняется и ошибка не перехвачена

			except  IOError:
				print('unsucces')
				success = False #перехват ошибки 
			finally:

				ready = True #и если всё таки удалось найти файл, то его открываем

			if success == True and ready == True: #если успех равен првде и готовность, то мы открываем и берём событие
				
				f = codecs.open('events.txt','r', 'utf_8_sig' )

				fd = f.read()
				
				client.send_message(message.chat.id, fd.encode().decode('utf-8'))


			elif success == False and ready == True: # если успех равен лжи, а код готов, то бот пишет что нет событий
				client.send_message(message.chat.id, 'Сейчас нет каких либо мероприятий😥')

		elif message.text == '↩️На главное меню ↪️':
			markup_inline = types.InlineKeyboardMarkup()
			item_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'main_menu') #начальные кнопки которые спрашивают хочет ли пользователь продолжить
			item_no = types.InlineKeyboardButton(text = 'Нет', callback_data = 'stay_here')


			markup_inline.add(item_yes, item_no)
			client.send_message(message.chat.id,  'Вы точно хотите вернутся на главное меню?',
			reply_markup = markup_inline

			)
		elif message.text == '⚒️Написать событие ⚒️' and admin == True:
			markup_inline = types.InlineKeyboardMarkup()

			item_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'write_event')
			item_no = types.InlineKeyboardButton(text = 'Нет', callback_data = 'stay_message')

			markup_inline.add(item_yes, item_no)
			client.send_message(message.chat.id, 'Вы уверены?🤔', reply_markup = markup_inline)

			
		elif message.text == '🚫Удалить события🚫' and admin == True:
			markup_inline = types.InlineKeyboardMarkup()

			item_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'delete') #начальные кнопки которые спрашивают хочет ли пользователь продолжить
			item_no = types.InlineKeyboardButton(text = 'Нет', callback_data = 'stay_message')


			markup_inline.add(item_yes, item_no)
			client.send_message(message.chat.id,  'Вы уверены?🤔', 
			reply_markup = markup_inline

			)
		elif message.text == '🎵Подборка музыки от КванториУМа🎵':
			check_file = os.path.exists('music')
			path = './music'
			music_count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
			if check_file == True:
				if music_count > 0:
					client.send_message(message.chat.id, 'Вот наша подборка)')
					for file in os.listdir('music/'):
						if file.split('.')[-1] == 'mp3' or file.split('.')[-1] == 'ogg':
							

							audio = open('music/' + file, 'rb')
							client.send_audio(message.chat.id, audio)	
				elif music_count < 0:
					client.send_message(message.chat.id, 'К сожелению сейчас подборка отсутвует😥')
			elif check_file == False:
				path = './music/'
				client.send_message(call.message.chat.id, 'Музыка отсутвует😥')
				os.mkdir(path)



			


		elif message.text == 'Информация о Кванториум - Сахалин ℹ️':

			keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item_own_info = types.KeyboardButton(text_full_info_about_kvantorium_65)
			item_kvants = types.KeyboardButton('КвантУМы')
			item_event = types.KeyboardButton('🎟️ МЕРОПРИЯТИЕ 🎟️')
			item_music = types.KeyboardButton('🎵Подборка музыки от КванториУМа🎵')
			item_main_menu = types.KeyboardButton('↩️На главное меню ↪️')

			
			keyboard.row(item_own_info)
			keyboard.row(item_kvants, item_event)
			keyboard.row(item_music)
			keyboard.row(item_main_menu)
			client.send_message(message.chat.id, 'Выберите интересующую вас информацию.', reply_markup = keyboard) #переход в меню с информацией

		elif message.text == '™️Создатель©️':
			markup_inline = types.InlineKeyboardMarkup()
			item_telegram = types.InlineKeyboardButton(text = 'Телеграм', url = text_ejtiejteite) #НИ ВКОЕМ СЛУЧАЕМ НЕ ТРОГАТЬ) ОТ ОРИГИНАЛЬНОГО СОЗДАТЕЛЯ

			markup_inline.add(item_telegram)
			client.send_message(message.chat.id, 'Одерий Ярослав Александрович', reply_markup = markup_inline)


		elif message.text == '❌ Удалить музыку ❌' and admin == True:
			markup_inline = types.InlineKeyboardMarkup()

			item_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'delete_music') #начальные кнопки которые спрашивают хочет ли пользователь продолжить
			item_no = types.InlineKeyboardButton(text = 'Нет', callback_data = 'stay_message')


			markup_inline.add(item_yes, item_no)
			client.send_message(message.chat.id,  'Вы уверены?🤔', 
			reply_markup = markup_inline

			)
			

		elif message.text == '➕Управление подборкой музыки➕' and admin == True:
			
			keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)

			item_add_music = types.KeyboardButton('🎶 Добавить музыку 🎶')
			item_delete_music = types.KeyboardButton('❌ Удалить музыку ❌')
			item_back_adminPan = types.KeyboardButton('⚙ Вернутся в Админ Панель ⚙')
			keyboard.row( item_delete_music)
			keyboard.row(item_back_adminPan)
			client.send_message(message.chat.id, 'Теперь вам подвластна музыка КванториУМа🎵', reply_markup = keyboard)

		elif message.text == '🎶 Добавить музыку 🎶' and admin == True:
			write_event = client.send_message(message.chat.id, 'Отправляйте музыку для подборки' )
			client.register_next_step_handler(write_event, save_music)


		elif message.text == text_tech_work_settings and admin == True:
			markup_inline = types.InlineKeyboardMarkup()
			item_yes = types.InlineKeyboardButton(text = text_tech_work_on, callback_data = 'tech_work_on') 
			item_no = types.InlineKeyboardButton(text = text_tech_work_off, callback_data = 'tech_work_off')
			markup_inline.add(item_yes,item_no)
			client.send_message(message.chat.id, text_would_setting_tech_work , reply_markup = markup_inline)

		
		

		elif message.text == '⚙ Вернутся в Админ Панель ⚙' and admin == True:
			markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)

			item_send_message =types.KeyboardButton('⚒️Написать событие ⚒️')
			item_main_menu = types.KeyboardButton('↩️На главное меню ↪️')
			item_go_on_tech_work = types.KeyboardButton(text_tech_work_settings)
			item_delete_events = types.KeyboardButton('🚫Удалить события🚫')
			item_music_control = types.KeyboardButton('➕Управление подборкой музыки➕')
			markup_reply.row(item_send_message, item_delete_events)
			markup_reply.row(item_music_control)
			markup_reply.row(item_go_on_tech_work)
			markup_reply.row (item_main_menu)

			client.send_message(message.chat.id, 'С возвращением', reply_markup = markup_reply)
		elif message.text == 'Админ Панель' and admin == True:

			markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)

			item_send_message =types.KeyboardButton('⚒️Написать событие ⚒️')
			item_go_on_tech_work = types.KeyboardButton(text_tech_work_settings)
			item_main_menu = types.KeyboardButton('↩️На главное меню ↪️')
			item_delete_events = types.KeyboardButton('🚫Удалить события🚫')
			item_music_control = types.KeyboardButton('➕Управление подборкой музыки➕')
			markup_reply.row(item_send_message, item_delete_events)
			markup_reply.row(item_music_control)
			markup_reply.row(item_go_on_tech_work)
			markup_reply.row (item_main_menu)

			client.send_message(message.chat.id, 'Добро пожаловать в админ панель.', reply_markup = markup_reply)
	elif tech_work == True:
		if admin == False:
			client.send_message(message.chat.id, text_tech_work_for_users)
		if message.text == '↩️На главное меню ↪️':
				markup_inline = types.InlineKeyboardMarkup()
				item_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'main_menu') #начальные кнопки которые спрашивают хочет ли пользователь продолжить
				item_no = types.InlineKeyboardButton(text = 'Нет', callback_data = 'stay_here')
				markup_inline.add(item_yes, item_no)
				client.send_message(message.chat.id,  'Вы точно хотите вернутся на главное меню?',
				reply_markup = markup_inline

				)
		elif message.text == text_tech_work_settings and admin == True:
			markup_inline = types.InlineKeyboardMarkup()

			item_yes = types.InlineKeyboardButton(text = text_tech_work_on, callback_data = 'tech_work_on') 
			item_no = types.InlineKeyboardButton(text = text_tech_work_off, callback_data = 'tech_work_off')
			markup_inline.add(item_yes,item_no)
			client.send_message(message.chat.id, text_would_setting_tech_work , reply_markup = markup_inline)


		elif admin == True:
			if message.text == '↩️На главное меню ↪️':
				markup_inline = types.InlineKeyboardMarkup()
				item_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'main_menu') #начальные кнопки которые спрашивают хочет ли пользователь продолжить
				item_no = types.InlineKeyboardButton(text = 'Нет', callback_data = 'stay_here')
				markup_inline.add(item_yes, item_no)
				client.send_message(message.chat.id,  'Вы точно хотите вернутся на главное меню?',
				reply_markup = markup_inline

				)
			

			elif message.text == '⚒️Написать событие ⚒️' and admin == True:
				markup_inline = types.InlineKeyboardMarkup()

				item_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'write_event')
				item_no = types.InlineKeyboardButton(text = 'Нет', callback_data = 'stay_message')

				markup_inline.add(item_yes, item_no)
				client.send_message(message.chat.id, 'Вы уверены?🤔', reply_markup = markup_inline)
			elif message.text == '🚫Удалить события🚫' and admin == True:
				markup_inline = types.InlineKeyboardMarkup()

				item_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'delete') #начальные кнопки которые спрашивают хочет ли пользователь продолжить
				item_no = types.InlineKeyboardButton(text = 'Нет', callback_data = 'stay_message')


				markup_inline.add(item_yes, item_no)
				client.send_message(message.chat.id,  'Вы уверены?🤔', 
				reply_markup = markup_inline

				)

			elif message.text == 'Админ Панель' and admin == True:

				markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)

				item_send_message =types.KeyboardButton('⚒️Написать событие ⚒️')
				item_go_on_tech_work = types.KeyboardButton(text_tech_work_settings)
				item_main_menu = types.KeyboardButton('↩️На главное меню ↪️')
				item_delete_events = types.KeyboardButton('🚫Удалить события🚫')
				item_music_control = types.KeyboardButton('➕Управление подборкой музыки➕')
				markup_reply.row(item_send_message, item_delete_events)
				markup_reply.row(item_music_control)
				markup_reply.row(item_go_on_tech_work)
				markup_reply.row (item_main_menu)
				client.send_message(message.chat.id, 'Добро пожаловать в админ панель.', reply_markup = markup_reply)

			elif message.text == '❌ Удалить музыку ❌' :
				markup_inline = types.InlineKeyboardMarkup()

				item_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'delete_music') #начальные кнопки которые спрашивают хочет ли пользователь продолжить
				item_no = types.InlineKeyboardButton(text = 'Нет', callback_data = 'stay_message')


				markup_inline.add(item_yes, item_no)
				client.send_message(message.chat.id,  'Вы уверены?🤔', 
				reply_markup = markup_inline

				)
				

			elif message.text == '➕Управление подборкой музыки➕' :
				
				keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)

				item_add_music = types.KeyboardButton('🎶 Добавить музыку 🎶')
				item_delete_music = types.KeyboardButton('❌ Удалить музыку ❌')
				item_back_adminPan = types.KeyboardButton('⚙ Вернутся в Админ Панель ⚙')
				keyboard.row( item_delete_music)
				keyboard.row(item_back_adminPan)
				client.send_message(message.chat.id, 'Теперь вам подвластна музыка КванториУМа🎵', reply_markup = keyboard)

			elif message.text == '🎶 Добавить музыку 🎶' :
				write_event = client.send_message(message.chat.id, 'Отправляйте музыку для подборки' )
				client.register_next_step_handler(write_event, save_music)
			
			elif message.text == '⚙ Вернутся в Админ Панель ⚙' and admin == True:
				markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)

				item_send_message =types.KeyboardButton('⚒️Написать событие ⚒️')
				item_main_menu = types.KeyboardButton('↩️На главное меню ↪️')
				item_go_on_tech_work = types.KeyboardButton(text_tech_work_settings)
				item_delete_events = types.KeyboardButton('🚫Удалить события🚫')
				item_music_control = types.KeyboardButton('➕Управление подборкой музыки➕')
				markup_reply.row(item_send_message, item_delete_events)
				markup_reply.row(item_music_control)
				markup_reply.row(item_go_on_tech_work)
				markup_reply.row (item_main_menu)

				client.send_message(message.chat.id, 'С возвращением', reply_markup = markup_reply)
			
			

@client.callback_query_handler(func = lambda call: True)
def answer(call):
	global admin
	admin = False
	global tech_work

	text_start_comm = '/start' #текст комманды для вызова первого сообщения

	if call.data == 'YES':
		if call.message.chat.id in admin_list:
			admin = True
		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)

		#опознание кнопок берётся с MR1

		item_number = types.KeyboardButton('Номер тех.поддержки 📞')  
		item_social = types.KeyboardButton('Мы в соц.сетях 📱')
		item_info = types.KeyboardButton('Информация о Кванториум - Сахалин ℹ️')
		item_creator = types.KeyboardButton('™️Создатель©️')
		item_adminka = types.KeyboardButton('Админ Панель')

		#главное меню
		markup_reply.row(item_number,item_social) 
		markup_reply.row(item_info)
		markup_reply.row(item_creator)
		if admin == True:
			markup_reply.add(item_adminka)
			print('Admin was added')

		client.send_message(call.message.chat.id, 'Добро пожаловать, приятного пользования ботом 🤝.',    #строка при приветствовании пользователя
			reply_markup = markup_reply
			)

	elif call.data == 'NO':
		client.send_message(call.message.chat.id, 'Очень жаль 😥. Если хотите вернутся используйте следущую комманду: ' + text_start_comm)

	elif call.data == 'tech_work_on':
		if tech_work == False:
			tech_work = True
			client.send_message(call.message.chat.id, text_tech_work_succes_on)
		elif tech_work == True:
			client.send_message(call.message.chat.id, text_tech_work_unsucces_on)
	elif call.data == 'tech_work_off':
		if tech_work == True:
			tech_work = False
			client.send_message(call.message.chat.id, text_tech_work_succes_off)
		elif tech_work == False:
			client.send_message(call.message.chat.id, text_tech_work_unsucces_off)

	elif call.data == 'stay_message':

		fartik = ['Фуххх, повезло', 'Щелчок таноса удалось избежать', 'Вас не уволят)', 'Какой генний чел который придумал отмену', 'Интересный факт - Вы Администратор)', 'Как дела?', 'КванториУМ хорошая вещь', 'Хорошего дня, Администратор', 'Как работа?', 'Удачи в жизни', 'Хорошая работа, Администратор', 'Вы были спасены, мои поздравления', 'Отличная погода, наверное.... Я всё таки бот не знаю как погода']
		client.send_message(call.message.chat.id, random.choice(fartik))
	elif call.data == 'write_event':
		write_event = client.send_message(call.message.chat.id, 'Введите ваше мероприятие/событие:' )
		client.register_next_step_handler(write_event, hello)

	elif call.data == 'main_menu':
		if call.message.chat.id in admin_list:
			admin = True

		main_menu_meet = ['Гном нашёл вас и привез обратно', 'Вы нашли магический портал, и он переместил вас сюда', 'Да, здравствуйет магия прогроммирования' , 'Kahoooooooooot', 'Голуби нашли вас и пренисли вас обратно', 'Вжух Вжух, вы дома)', 'What\'s up', 'Какое чудное время. Технологии могут переместить вас на главное меню.']
		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)

		item_number = types.KeyboardButton('Номер тех.поддержки 📞')  
		item_social = types.KeyboardButton('Мы в соц.сетях 📱')
		item_info = types.KeyboardButton('Информация о Кванториум - Сахалин ℹ️')
		item_adminka = types.KeyboardButton('Админ Панель')
		item_creator = types.KeyboardButton('™️Создатель©️')

		#главное меню
		markup_reply.row(item_number,item_social) 
		markup_reply.row(item_info)
		markup_reply.row(item_creator)
		if admin == True:
			markup_reply.row(item_adminka)
			print('Admin was added')
		client.send_message(call.message.chat.id, random.choice(main_menu_meet),    #строка при приветствовании пользователя
			reply_markup = markup_reply
			)
	elif call.data == 'delete':
		success = True
		client.delete_message(call.message.chat.id, call.message.message_id)
		fact = ['✔️Молодец удалил событие, я тебя поздравляю✔️', '⚙️Тебе нравится работать?⚙️', '😎Это крутой бот😎', '🎵Какая ваша любимая музыка?🎵','Интересный факт - от вас завсит судьба кнопки 🎟️ МЕРОПРИЯТИЕ 🎟️', 'Вам нравится КванториУМ?']
		try:
			f = open('events.txt')
			f.close()
			ready = False #готовность равна лже т.к комманда только выполняется и ошибка не перехвачена

		except  IOError:
			print('unsucces')
			success = False #перехват ошибки 
		finally:

			ready = True #и если всё таки удалось найти файл, то его открываем

		if success == True and ready == True: #если успех равен првде и готовность, то мы открываем и берём событие
			path_event = 'events.txt'
			os.remove(path_event)
			client.send_message(call.message.chat.id, '✔️Событие успешно удаленно✔️')
			client.send_message(call.message.chat.id, random.choice(fact))
		elif success == False and ready == True: # если успех равен лжи, а код готов, то бот пишет что нет событий
			client.send_message(call.message.chat.id, 'К сожелению события отсутвуют чтобы их удалить')
	elif call.data == 'stay_here':
		neudacha = ['К счастью вы успели выпрыгнуть из портала', 'Вы спрятались от гномов', 'Прогроммист спас вас от неминуемого краха']
		client.send_message(call.message.chat.id, random.choice(neudacha))
	elif call.data == 'delete_music':
		check_file = os.path.exists('music')
		if check_file == True:
			path = './music/'
			music_count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
			if music_count > 1:
				shutil.rmtree(path)
				os.mkdir(path)
				client.send_message(call.message.chat.id, 'Музыка успешно удаленна')
			elif music_count < 1:
				client.send_message(call.message.chat.id, 'Музыка отсутвует😥')
		elif check_file == False:
			path = './music/'
			client.send_message(call.message.chat.id, 'Музыка отсутвует😥')
			os.mkdir(path)
	client.delete_message(call.message.chat.id, call.message.message_id)

client.polling(none_stop=True)
