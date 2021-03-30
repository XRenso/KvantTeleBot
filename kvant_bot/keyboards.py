from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

import webParse as WP
import asyncio

#обычная клавиатура
button_creator = KeyboardButton('™️Создатель©️')
button_num_techHelp = KeyboardButton('Номер тех.поддержки 📞')
button_soccial = KeyboardButton('Мы в соц.сетях 📱')
button_Admin = KeyboardButton('Админ Панель')
button_more_info = KeyboardButton('Информация о Кванториум - Сахалин ℹ️')
button_on_main_menu = KeyboardButton('↩️На главное меню ↪️')
button_rss_control = KeyboardButton('📰Управление подпиской на новости📰')



#клавиатура выбора квантума
button_it_info = KeyboardButton('💻IT-квантум💻')
button_aero_info = KeyboardButton('✈️Аэроквантум✈️')
button_design_info = KeyboardButton('🎨Промдизайнквантум🎨')
button_energy_info = KeyboardButton('⚡Энерджиквантум⚡')	
button_hitech_info = KeyboardButton('⚙️Хайтек⚙️') 
button_geo_info = KeyboardButton('🗺️Геоквантум🗺️')
button_back_on_more_info = KeyboardButton('↩️Назад')

#второй уровень клавиатуры с информацией
moreInfo_button_aboutKvant = KeyboardButton('📜Общая информация про КванториУМ65.📜')
moreInfo_button_kvants = KeyboardButton('🖥КвантУМы🖥')
moreInfo_button_events = KeyboardButton('🎟️ МЕРОПРИЯТИЕ 🎟️')
moreInfo_button_music = KeyboardButton('🎵Подборка музыки от КванториУМа🎵')

admin_button_add_event = KeyboardButton('⚒️ Добавить событие ⚒️')
admin_button_delete_event = KeyboardButton('🚫 Удалить события 🚫')
admin_button_delete_music = KeyboardButton('❌ Удалить музыку ❌')


#клавиатуры
kvantum_choose_kb = ReplyKeyboardMarkup(resize_keyboard = True).add(button_it_info,button_aero_info).add(button_design_info,button_energy_info).add(button_hitech_info,button_geo_info).add(button_back_on_more_info)



admin_kb = ReplyKeyboardMarkup(resize_keyboard = True).row(admin_button_add_event, admin_button_delete_event)
admin_kb.add(button_on_main_menu)

moreInfo_kb = ReplyKeyboardMarkup(resize_keyboard = True).row(moreInfo_button_aboutKvant).row(moreInfo_button_kvants,moreInfo_button_events).row(button_rss_control).row(button_on_main_menu)

main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(button_num_techHelp,button_soccial)
main_menu_kb.add(button_more_info).add(button_creator)





#инлайн клавиатура

#start
inline_continueMenu = InlineKeyboardButton('Да', callback_data = 'yesStart')
inline_notContinueMenu = InlineKeyboardButton('Нет', callback_data = 'noStart')

#menuControl
inline_backMainMenu = InlineKeyboardButton('Да', callback_data = 'backMainMenu')
inline_stayHereMenu = InlineKeyboardButton('Нет', callback_data = 'stayHere')


#social
inline_CreatorTelegram = InlineKeyboardButton('Telegram', url = 'https://t.me/XRenso')
inline_social_inst = InlineKeyboardButton('Инстаграмм🤳', url = 'https://www.instagram.com/kvantorium_65/')
inline_social_site = InlineKeyboardButton('Сайт🌎', url = 'http://kvantorium.iroso.ru')
inline_rss_on = InlineKeyboardButton('Подписаться', callback_data= 'RSSon')
inline_rss_off = InlineKeyboardButton('Отписаться', callback_data = 'RSSoff')

#admin
inline_admin_deleteEvent = InlineKeyboardButton('Да', callback_data = 'deleteEvent')
inline_admin_StayAdmin = InlineKeyboardButton('Нет', callback_data = 'stayMessage')
inline_admin_deleteMusic = InlineKeyboardButton('Да', callback_data = 'delMusic')
inline_admin_addEvent = InlineKeyboardButton('Да', callback_data = 'write_event')



#admin
inline_kb_addEvent = InlineKeyboardMarkup().row(inline_admin_addEvent, inline_admin_StayAdmin)
inline_kb_deleteEvent = InlineKeyboardMarkup().row(inline_admin_deleteEvent, inline_admin_StayAdmin)
inline_kb_deleteMusic = InlineKeyboardMarkup().row(inline_admin_deleteMusic, inline_admin_StayAdmin)


#user
inline_kb_social = InlineKeyboardMarkup().row(inline_social_inst, inline_social_site)
inline_kb_RSS = InlineKeyboardMarkup().row(inline_rss_on,inline_rss_off)
def inline_kb_news(urlik):
	inline_url_news = InlineKeyboardButton('⏮️Подробнее⏭️', url = urlik)
	inline_kb_news = InlineKeyboardMarkup().row(inline_url_news)
	return inline_kb_news


inline_kb_Creator = InlineKeyboardMarkup().add(inline_CreatorTelegram)

inline_kb_mainMenu_back = InlineKeyboardMarkup().row(inline_backMainMenu, inline_stayHereMenu)

inline_kb_start = InlineKeyboardMarkup().row(inline_continueMenu, inline_notContinueMenu)