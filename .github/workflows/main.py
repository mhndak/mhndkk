from telebot import (TeleBot,types)
from json import (loads,dumps)
from mailer import Mailer
from os import path
from time import sleep

alEx = TeleBot("5338927255:AAHpQhmkeVlVW9lq7A1i7YGCcvsi1dA_xUY")


@alEx.message_handler(commands=['start'])
def Start(message):
	K = types.InlineKeyboardMarkup()
	Login = types.InlineKeyboardButton(text="Login 📲",callback_data="Login")
	SEND = types.InlineKeyboardButton(text="Send Messages ❕",callback_data="Send")
	LINk = types.InlineKeyboardButton(text="Add Link ( G - Ch ) •",callback_data="Links")
	
	K.add(SEND,Login)
	K.add(LINk)
	Name = message.chat.first_name
	alEx.reply_to(message,f'''💻|Hi , ( {Name} ) •
	
- أستطيع مراسلة التلغرام والإبلاغ عن البوتات والمجموعات التي تنشر أشياء غير أخلاقية •
- أستطيع رفع الحظر عن المجموعات والقنوات •
''',reply_markup=K)
@alEx.callback_query_handler(func=lambda call:True)
def ALEX(call):
	if call.data == "Login":
		Back = types.InlineKeyboardMarkup()
		Bback = types.InlineKeyboardButton("رجوع 🔙",callback_data="Back")
		Back.add(Bback)
		alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''Give me your account as :
			
- alex@gmail.nazih:FuckYou
- Email : alex@gmail.nazih •
- Password : FuckYou •			
''',reply_markup=Back),Smtplib)

	elif call.data == "Links":
		Back = types.InlineKeyboardMarkup()
		Bback = types.InlineKeyboardButton("رجوع 🔙",callback_data="Back")
		Back.add(Bback)
		alEx.register_next_step_handler(alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''Give me Telegram link • (Channel , Group ) •''',reply_markup=Back),LiNk)
	
	elif call.data == "Send":
		a,S,s=0,0,0
		if path.exists(f'{call.message.chat.id}smtp.json') == False:
			Back = types.InlineKeyboardMarkup()
			Bback = types.InlineKeyboardButton("رجوع 🔙",callback_data="Back")
			Back.add(Bback)
			alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="You Must login First ❗",reply_markup=Back)
			
		elif path.exists(f'{call.message.chat.id}smtp.json') == True:
			Back = types.InlineKeyboardMarkup()
			Bback = types.InlineKeyboardButton("رجوع 🔙",callback_data="Back")
			Back.add(Bback)
			with open(f'{call.message.chat.id}smtp.json','r') as c:
						Read=loads(c.read())
			Email = Read['smtplib']['Email']
			Password = Read['smtplib']['Pass']
			with open(f'{call.message.chat.id}link.json','r') as c:
						Read=loads(c.read())
			Link = Read['smtplib']['link']
			while 1:
				EmailS = ['abuse@telegram.org','Support@telegram.org','dmca@telegram.org','stopca@telegram.org']
				try:
					for Emaill in EmailS:
						mail = Mailer(email=Email,password=Password)
						mail.settings(repeat=10)
						sleep(0.05)
						try:
							mail.send(str(Emaill),'illegal 18+ image',f'''Hello Telegram Company I would like to report a group that violates Telegram standards and laws by publishing pornographic content 18+ porn posters and I ask you to remove the group forever, please .

Group link : {Link}''')
							if mail.status[0] == True:
								a+=1
								Alex = types.InlineKeyboardMarkup()
								Ca = types.InlineKeyboardButton("Cancel •",callback_data="Cancel")
								Sended = types.InlineKeyboardButton(f'''[ 📤 Sended ] ~> {a}''',callback_data="S")
								UnSended = types.InlineKeyboardButton(f'''[ 📥 UnSended ] ~> {s}''',callback_data="S")
								Sleep = types.InlineKeyboardButton(f'''[ 📨 Sleep ] ~> {S}''',callback_data="S")
								Alex.add(Sended)
								Alex.add(UnSended)
								Alex.add(Sleep)
								Alex.add(Ca)
								alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''- Im Sending The Messages …						''',reply_markup=Alex)
							else:
								s+=1
								Alex = types.InlineKeyboardMarkup()
								Ca = types.InlineKeyboardButton("Cancel •",callback_data="Cancel")
								Sended = types.InlineKeyboardButton(f'''[ 📤 Sended ] ~> {a}''',callback_data="S")
								UnSended = types.InlineKeyboardButton(f'''[ 📥 UnSended ] ~> {s}''',callback_data="S")
								Sleep = types.InlineKeyboardButton(f'''[ 📨 Sleep ] ~> {S}''',callback_data="S")
								Alex.add(Sended)
								Alex.add(UnSended)
								Alex.add(Sleep)
								Alex.add(Ca)
								alEx.edit_message_text(chat_id=call.message.chat.id,
			message_id=call.message.message_id,text='''
- Im Sending The Messages …						
''',reply_markup=Alex)
						except:
							S+=1
							
							Alex = types.InlineKeyboardMarkup()
							Ca = types.InlineKeyboardButton("Cancel •",callback_data="Cancel")
							Sended = types.InlineKeyboardButton(f'''[ 📤 Sended ~> ] {a}''',callback_data="S")
							UnSended = types.InlineKeyboardButton(f'''[ 📥 UnSended ] ~> {s}''',callback_data="S")
							Sleep = types.InlineKeyboardButton(f'''[ 📨 Sleep ] ~> {S}''',callback_data="S")
							Alex.add(Sended)
							Alex.add(UnSended)
							Alex.add(Sleep)
							Alex.add(Ca)
							sleep(14)
							alEx.edit_message_text(chat_id=call.message.chat.id,
			message_id=call.message.message_id,text='''
- Im Sending The Messages …						
''',reply_markup=Alex)
				except:
							pass
	elif call.data == 'Cancel':
		alEx.delete_message(call.message.chat.id,call.message.message_id)
		K = types.InlineKeyboardMarkup()
		Login = types.InlineKeyboardButton(text="Login 📲",callback_data="Login")
		SEND = types.InlineKeyboardButton(text="Send Messages ❕",callback_data="Send")
		LINk = types.InlineKeyboardButton(text="Add Link ( G - Ch ) •",callback_data="Links")
		K.add(SEND,Login)
		K.add(LINk)
		Name = call.message.chat.first_name
		alEx.send_message(call.message.chat.id,f'''💻|Hi , ( {Name} ) •
		
- أستطيع مراسلة التلغرام والإبلاغ عن البوتات والمجموعات التي تنشر أشياء غير أخلاقية •
- أستطيع رفع الحظر عن المجموعات والقنوات •
''',reply_markup=K)

	elif call.data == 'Back':
		K = types.InlineKeyboardMarkup()
		Login = types.InlineKeyboardButton(text="Login 📲",callback_data="Login")
		SEND = types.InlineKeyboardButton(text="Send Messages ❕",callback_data="Send")
		LINk = types.InlineKeyboardButton(text="Add Link ( G - Ch ) •",callback_data="Links")
		K.add(SEND,Login)
		K.add(LINk)
		Name = call.message.chat.first_name
		alEx.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''💻|Hi , ( {Name} ) •
		
- أستطيع مراسلة التلغرام والإبلاغ عن البوتات والمجموعات التي تنشر أشياء غير أخلاقية •
- أستطيع رفع الحظر عن المجموعات والقنوات •
''',reply_markup=K)

def LiNk(message):
	msg = message.text
	if 't.me' in msg:
		link={};smtp='smtplib'
		link[smtp]= {"link":str(msg)}
		with open(f'{message.chat.id}link.json','w') as s:
			s.write(dumps(link))
		K = types.InlineKeyboardMarkup()
		Bback = types.InlineKeyboardButton("رجوع 🔙",callback_data="Back")	
		K.add(Bback)
		alEx.reply_to(message,"Your Link Has Been Saved ❕ ",reply_markup=K)		
def Smtplib(message):	
	msg = message.text
	Id = message.chat.id
	if 'start' in msg:
		pass
	elif ':' in msg and '@' in msg:
		Email = msg.split(':')[0]
		Pass = msg.split(':')[1]
		email={};smtp='smtplib'
		email[smtp]= {"Email":str(Email),"Pass":str(Pass)}
		
		with open(f'{Id}smtp.json','w') as s:
			s.write(dumps(email))
		Back = types.InlineKeyboardMarkup()
		Bback = types.InlineKeyboardButton("رجوع 🔙",callback_data="Back")
		Back.add(Bback)
		alEx.reply_to(message,"Your Account Has Been Saved ❕ ",reply_markup=Back)
		
	elif ':' not in msg and '@' in msg:
		K = types.InlineKeyboardMarkup()
		Login = types.InlineKeyboardButton(text="مرة أخرى 🔄",callback_data="Login")
		Bback = types.InlineKeyboardButton("رجوع 🔙",callback_data="Back")	
		K.add(Bback,Login)
		alEx.reply_to(message,"Plz , Send Your Account correctly ❗ ",reply_markup=K)			
alEx.infinity_polling()
