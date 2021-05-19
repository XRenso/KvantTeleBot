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
button_robo_info = KeyboardButton('🤖Промробоквантум🤖')
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


#кнопки КвантУМов
########
    #IT
it_info_btn = KeyboardButton('🔎 Про IT-квантум 🔎')
it_tutor_btn = KeyboardButton('👩‍💻 Наставники 👨‍💻')

    #Robo
robo_info_btn = KeyboardButton('🔎 Про Промробоквантум 🔎')
robo_tutor_btn = KeyboardButton('👩‍💼 Наставники 👨‍💼')
    #Prom
design_info_btn = KeyboardButton('🔎 Про Промдизайнквантум 🔎')
design_tutor_btn = KeyboardButton('🧑‍🎨 Наставники 👨‍🎨')
    #Aero
aero_info_btn = KeyboardButton('🔎 Про Аэроквантум 🔎')
aero_tutor_btn = KeyboardButton('👷‍♀️ Наставники 👷‍♂️')
    #Energy
energy_info_btn = KeyboardButton('🔎 Про Энерджиквантум 🔎')
energy_tutor_btn = KeyboardButton('👩‍🎓 Наставники 👨‍🎓')
    #HiTech
hitech_info_btn = KeyboardButton('🔎 Про Хайтек 🔎')
hitech_tutor_btn = KeyboardButton('👩‍🔧 Наставники 👨‍🔧')
    #Geo
geo_info_btn = KeyboardButton('🔎 Про Хайтек 🔎')
geo_tutor_btn = KeyboardButton('👩‍🏫 Наставники 👨‍🏫')


#########
    #общие кнопки КвантУМов
back_to_kavnt_list_btn = KeyboardButton('⬅️ Назад к квантУМам ➡️')


######################################################################
#клавиатуры
kvantum_choose_kb = ReplyKeyboardMarkup(resize_keyboard = True).add(button_it_info).add(button_robo_info,button_aero_info).add(button_design_info,button_energy_info).add(button_hitech_info,button_geo_info).add(button_back_on_more_info)



admin_kb = ReplyKeyboardMarkup(resize_keyboard = True).row(admin_button_add_event, admin_button_delete_event)
admin_kb.add(button_on_main_menu)

moreInfo_kb = ReplyKeyboardMarkup(resize_keyboard = True).row(moreInfo_button_aboutKvant).row(moreInfo_button_kvants,moreInfo_button_events).row(button_rss_control).row(button_on_main_menu)

main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(button_num_techHelp,button_soccial)
main_menu_kb.add(button_more_info).add(button_creator)

####################################################################################
#клавиатура квантУМов
    #IT
it_info_kb = ReplyKeyboardMarkup(resize_keyboard = True).row(it_info_btn)
it_info_kb.add(it_tutor_btn).row(back_to_kavnt_list_btn, button_on_main_menu)

    #Robo
robo_info_kb = ReplyKeyboardMarkup(resize_keyboard = True).add(robo_info_btn).add(robo_tutor_btn).row(back_to_kavnt_list_btn, button_on_main_menu)
    #Prom
design_info_kb = ReplyKeyboardMarkup(resize_keyboard = True).add(design_info_btn).add(design_tutor_btn).row(back_to_kavnt_list_btn, button_on_main_menu)
    #Aero
aero_info_kb = ReplyKeyboardMarkup(resize_keyboard = True).add(aero_info_btn).add(aero_tutor_btn).row(back_to_kavnt_list_btn, button_on_main_menu)
    #Energy
energy_info_kb = ReplyKeyboardMarkup(resize_keyboard = True).add(energy_info_btn).add(energy_tutor_btn).row(back_to_kavnt_list_btn, button_on_main_menu)
    #HiTech
hitech_info_kb = ReplyKeyboardMarkup(resize_keyboard = True).add(hitech_info_btn).add(hitech_tutor_btn).row(back_to_kavnt_list_btn, button_on_main_menu)
    #Geo
geo_info_kb = ReplyKeyboardMarkup(resize_keyboard = True).add(geo_info_btn).add(geo_tutor_btn).add(back_to_kavnt_list_btn,button_on_main_menu)

##########################################################################
#инлайн клавиатура

#start
inline_continueMenu = InlineKeyboardButton('Да', callback_data = 'yesStart')
inline_notContinueMenu = InlineKeyboardButton('Нет', callback_data = 'noStart')

#menuControl
inline_backMainMenu = InlineKeyboardButton('Да', callback_data = 'backMainMenu')
inline_stayHereMenu = InlineKeyboardButton('Нет', callback_data = 'stayHere')


#social
inline_CreatorTelegram = InlineKeyboardButton('Telegram Разработчика', url = 'https://t.me/XRenso')
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
