import telebot
from telebot import types
token=
client=telebot.TeleBot(token)
chatid=
@client.message_handler(commands=['start'])
def start(message):
	client.send_message(message.chat.id,'Здравствуйте,Для записи прошу ответить на несколько вопросов. Без этого я не смогу Вас сориентировать по времени, ведь не буду знать, сколько нам его потребуется.')
	# 

	
	msg1=client.send_message(message.chat.id,'1. что Вас беспокоит?\n2. Как давно?\n3. что делали сами?\n4. если посещали врача, то какого, что было рекомендовано и какой был результат?')
	

	client.register_next_step_handler(msg1,one_q)

@client.message_handler(content_types=['text,photo'])
def one_q(message):

	messageagsd=message.text
	client.send_message(chatid, "Запрос от\n*{name} {last} @{user_name}*".format(name=message.chat.first_name, last=message.chat.last_name,user_name=message.chat.username), parse_mode="Markdown")
	client.send_message(chatid,messageagsd)


	a=message.text

	murkup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=types.KeyboardButton('Локальная обработка')
	item2=types.KeyboardButton('Обработка стопы')
	item3=types.KeyboardButton('Обработка пальцев')
	item4=types.KeyboardButton('Полный педикюр')
	murkup.add(item1,item2,item3,item4)
	msg2=client.send_message(message.chat.id,'Что вы хотите от меня?',reply_markup=murkup)
	client.register_next_step_handler(msg2,two_q)
def two_q(message):
	if message.text=='Локальная обработка':
		b=message.text
		
		client.send_message(chatid,b)
		
	elif message.text=='Обработка стопы':
		b=message.text
		client.send_message(chatid,b)

	elif message.text=='Обработка пальцев':
		
		b=message.text
		client.send_message(chatid,b)
		
	elif message.text=='Полный педикюр':
	
		b=message.text
		client.send_message(chatid,b)
	murkup2=types.ReplyKeyboardRemove()
	msg3=client.send_message(message.chat.id,'Отправьте фото ',reply_markup=murkup2)
	
	
	client.register_next_step_handler(msg3,free_q)
	
	


def free_q(message):

	if message.content_type == 'photo':
		raw = message.photo[2].file_id
		name='Photo.jpg'
		file_info = client.get_file(raw)
		downloaded_file = client.download_file(file_info.file_path)
		with open(name,'wb') as new_file:
			new_file.write(downloaded_file)
		img = open(name, 'rb')
		
		client.send_photo(chatid, img)

	
	msg4=client.send_message(message.chat.id,'Когда вам было бы удобно записаться (напишите примерно дату)?')
	
	
	client.register_next_step_handler(msg4,four_q)
	
def four_q(message):
	d=message.text
	msg5=client.send_message(message.chat.id,'Оставьте ваш номер телефона☎️. С вами свяжусь в ближайшее время и предложат варианты!')
	client.register_next_step_handler(msg5,five_q)
	client.send_message(chatid,f'Когда удобно записаться: {d}')
def five_q(message):
	number=message.text
	client.send_message(chatid,f'Номер телефона:{number}')

	
	client.send_message(message.chat.id,'Спасибо что выбрали нас❤️ С вами свяжусь в ближайшее время и предложат варианты')
	client.send_message(message.chat.id,'Если хотите начать бронированние заного, нажмите сюда: /start')
	
	client.send_message(chatid,'✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅')

client.enable_save_next_step_handlers(delay=2)
client.load_next_step_handlers()
client.polling(none_stop=True, interval=0)
