# -*- coding: utf-8 -*-
from pyrogram import Client, filters
from time import sleep
from pyrogram.errors import FloodWait
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)
from pyrogram.raw import functions
import random
import requests
import json
import os
import sys
import shutil
from pyrogram.raw import types


# Code by Jaster # 
# TG - @ImperatorReich #


app = Client('my_account')
spam_stop = True
spnick_stop = True
flex_stop = True
fp_stop = True

def progress(current, total):
	if total != 0:
		print(f"{current * 100 / total:.1f}%")
		sleep(0.2)
		print(f"{current * 100 / total:.1f}%")
		sleep(0.2)
		print(f"{current * 100 / total:.1f}%")
		sleep(0.2)
		print(f"{current * 100 / total:.1f}%")
		sleep(0.2)
		print(f"{current * 100 / total:.1f}%")

def randomer():
	ass = str(int(1000 * (random.random())))
	return str(ass)
# msgcid = msg.chat.id
# vot tut

@app.on_message(filters.command(['up','update'],prefixes='.')& filters.me)
def update(_,msg):
	rep = 'https://raw.githubusercontent.com/ImperatorReich/ImperorUserBot/main/main.py'
	req = requests.get(rep, allow_redirects=True)
	open('main.py', 'wb').write(req.content)
	restarter()

@app.on_message(filters.command(['h','help'],prefixes='.')& filters.me)
def help(_,msg):
	app.edit_message_text(msg.chat.id,msg.message_id,"Заглянь в избранное")
	app.send_message('me',"- Команды - \nКоманды которые пишуться в ответ на сообщение =>\n1.s - Сохранение самоуничтожаюшихся сообщений\n2.echo - для полной инфы(разработки) о сообщении\n3.dead - zxc spam\n4.Команды для сохранения инфы с групп(каналов которые запретили пересылку,сохранение)\n4.1 ct(copytext) - Копировать текст \n4.2 dm(downloadmedia) - Скачать медиа(Видео,фото,голосовые,видеосообщения,документы,войсы,гифки)\nКоманды osint =>\n1.echo - Вполне подходит под ету роль так как телеграм не показывает всей инфы \n2.check (id Пользователя) - Пробив по базе мурикс\n3.info (@username или id) - Информация о пользователе \n4.infoch (@chat_username или chat_id) - Инфа о чате\nРазвлекательные и полезные команды =>\n1.spam (Ваше сообщение) - по названию можно понять что это спам\n2.spamstop - Остановить дрочку\n3.mention [@username] (Ваше сообщение) - Удобный упоменатель\n4.sendloc (1 координата) (2 координата) - Отправить в чат любую локацию\n5.sendcon (номер к прмеру +1337) (название контакта) - Можете отправить любой контакт с любым номеромv")

@app.on_message(filters.command('deletecash',prefixes='.')& filters.me)
def delcash(_, msg):
	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
	shutil.rmtree('downloads')

@app.on_message(filters.command(['s','savemedia'],prefixes='.')& filters.me)
def s(_, msg):
	# app.send_photo(msg.photo.file_id)
	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
	mention = '**От пользователя**-'+"["+msg.reply_to_message.from_user.first_name+"](tg://user?id="+str(msg.reply_to_message.from_user.id)+")"
	try:
		capl = mention+'\n Текст-\n'+msg.reply_to_message.caption
	except Exception as e:
		capl = mention
	app.send_document('me',app.download_media(msg.reply_to_message),caption=capl)

@app.on_message(filters.command('waifu',prefixes='.')& filters.me)
def waifu(_, msg):
	# app.send_photo(msg.photo.file_id)
	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
	#
	try:
		pmsgg = msg.text.split('.waifu ', maxsplit=1)[1]
		text = pmsgg.split(" ", 1)
		firstdata = text[0]
		twodata = text[1]
		type = firstdata
		category = twodata
		a = requests.get('https://api.waifu.pics/'+type+'/'+category)
		img = a.json()
		app.send_photo(msg.chat.id,img['url'])
	except Exception as e:
		app.send_message(msg.chat.id,'**писать команду так .waifu тип**(__sfw,nsfw__) **категория**([Для sfw = __waifu ,neko ,shinobu ,megumin ,bully ,cuddle ,cry ,hug ,awoo ,kiss ,lick ,pat ,smug ,bonk ,yeet ,blush ,smile ,wave ,highfive ,handhold ,nom ,bite ,glomp ,slap ,kill ,kick ,happy ,wink ,poke ,dance ,cringe__]\n[Для nsfw=__waifu,neko,trap,blowjob__])')

	# print(img['url'])


@app.on_message(filters.command(['cс','cсс'],prefixes='.')& filters.me)
def cсс(_,msg):
	app.delete_messages(msg.chat.id, msg.message_id, revoke=True)
	idd = msg.reply_to_message.from_user.id
	result = app.send(functions.users.GetFullUser(id=app.resolve_peer(idd)))
	print(result)

@app.on_message(filters.command(['cu','copyuser'],prefixes='.')& filters.me)
def cu(_,msg):
	app.delete_messages(msg.chat.id, msg.message_id, revoke=True)
	try:
		pmsgg = msg.text.split('.cu', maxsplit=1)[1]
	except:
		pmsgg = msg.text.split('.copyuser', maxsplit=1)[1]
	id = msg.reply_to_message.from_user.id
	inf = app.get_users(id)
	try:
		result = app.send(functions.users.GetFullUser(id=app.resolve_peer(id)))
		bio = result.about
	except Exception as e:
		bio = ''
	# print(str(result.user.id)+','+result.user.first_name+','+result.user.last_name+','+result.about)
	firstname = inf.first_name
	lastname = inf.last_name
	username = inf.username
	photo = app.get_profile_photos(id, limit=1)
	photo = photo[0].file_id
	if lastname == None:
		lastname = ''
	if username == None:
		username = ''
	if bio == None:
		bio = ''
	app.update_profile(firstname,lastname,bio)
	app.set_profile_photo(photo=app.download_media(photo))
	if pmsgg != ' n':
		try:
			app.update_username(username)
		except:
			try:
				sleep(3)
				legitusername = str(username)
				legitusername = legitusername + legitusername[-1]
				app.update_username(legitusername)
			except FloodWait as e:
				app.send_message(msg.chat.id,'Подожди задержку '+str(e.x))

	print('Firstname:'+firstname)
	print('Lastname:'+lastname)
	print('BIO:'+bio)
	print('file_id:'+photo)
	print('Username:@'+username)

# @app.on_raw_update()
# def raw(client, update, users, chats):
#     print(update)

@app.on_message(filters.command(['mode','modeficate'],prefixes='.')& filters.me)
def modificate(_, msg):
	app.delete_messages(msg.chat.id, msg.message_id, revoke=True)
	s = os.getcwd()
	app.download_media(msg.reply_to_message,s+'/main.py')
	print(os.getcwd())
	app.send_message(msg.chat.id,'Перезапуститесь .restart')

@app.on_message(filters.command('version',prefixes='.')& filters.me)
def version(_, msg):
	app.edit_message_text(msg.chat.id,msg.message_id,'1.2')

def restarter():
	os.execv(sys.executable, [sys.executable] + sys.argv)

@app.on_message(filters.command(['restart','res'],prefixes='.')& filters.me)
def restart(_, msg):
	app.delete_messages(msg.chat.id, msg.message_id, revoke=True)
	restarter()
	print('sss')

@app.on_message(filters.command(['fp','flexprint'],prefixes='.')& filters.me)
def fp(_, msg):
	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
	global fp_stop
	fp_stop = False
	while(fp_stop != True):
		app.send_chat_action(msg.chat.id, "typing")
		sleep(0.05)
		app.send_chat_action(msg.chat.id, "upload_video")
		sleep(0.05)
		app.send_chat_action(msg.chat.id, "playing")
		sleep(0.05)
		app.send_chat_action(msg.chat.id, "upload_photo")
		sleep(0.05)
		app.send_chat_action(msg.chat.id, "record_video")
		sleep(0.05)
		app.send_chat_action(msg.chat.id, "record_audio")
		sleep(0.05)
		app.send_chat_action(msg.chat.id, "upload_audio")
		sleep(0.05)
		app.send_chat_action(msg.chat.id, "upload_document")
		sleep(0.05)
		app.send_chat_action(msg.chat.id, "find_location")
		sleep(0.05)
		app.send_chat_action(msg.chat.id, "record_video_note")
		sleep(0.05)
		app.send_chat_action(msg.chat.id, "upload_video_note")
		sleep(0.05)
		app.send_chat_action(msg.chat.id, "choose_contact")
		sleep(0.05)
		app.send_chat_action(msg.chat.id, "speaking")

@app.on_message(filters.command(['stopfp','stopflexprint'],prefixes='.')& filters.me)
def fpstop(_, msg):
	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
	app.send_chat_action(msg.chat.id, "cancel")
	global fp_stop
	fp_stop = True

# @app.on_message(filters.command('s',prefixes='.')& filters.me)
# def s(_, msg):
# 	# app.send_photo(msg.photo.file_id)
# 	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
# 	name = str(msg.reply_to_message.photo.file_id)+'.jpg'
# 	app.download_media(msg.reply_to_message.photo.file_id,name)
# 	# with open("downloads\\sss.jpg","rb") as misc:
# 	# 	f=misc.read()
# 	app.send_photo("me", "downloads\\"+name)
# 	sleep(1)
# 	path = os.path.join(os.path.abspath(os.path.dirname(__file__))+'\\downloads', name)
# 	os.remove(path)

@app.on_message(filters.command('echo',prefixes='.')& filters.me)
def echo(_, msg):
	print(msg)
	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)


@app.on_message(filters.command('spam',prefixes='.')& filters.me)
def spam(_, msg):
	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
	pmsg = msg.text.split('.spam',maxsplit = 1)[1]
	global spam_stop
	spam_stop = False
	while(spam_stop != True):
		app.send_message(msg.chat.id,pmsg+" "+randomer())
		sleep(0.05)

@app.on_message(filters.command('spamstop',prefixes='.')& filters.me)
def spamstop(_, msg):
	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
	global spam_stop
	spam_stop = True

# @app.on_message(filters.command('nick',prefixes='.')& filters.me)
# def nick(_,msg):
# 	# app.update_username('AAAAAAA')
# 	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
# 	global spnick_stop
# 	spnick_stop = False
# 	pmsg = msg.text.split('.nick',maxsplit = 1)[1]
# 	while(spnick_stop != True):
# 		abiba = randomer()
# 		app.update_profile(first_name=abiba+" " + pmsg +" " +abiba)
# 		sleep(0.2)

# @app.on_message(filters.command('nickstop',prefixes='.')& filters.me)
# def nickstop(_,msg):
# 	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
# 	global spnick_stop
# 	spnick_stop = True

# @app.on_message(filters.command('flex',prefixes='.')& filters.me)
# def flex(_,msg):
# 	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
# 	global flex_stop
# 	flex_stop = False
# 	pmsg = msg.text.split('.flex',maxsplit = 1)[1]
# 	text = pmsg
# 	standart = "_"
# 	tbp = ''
# 	while(flex_stop != True):
# 		try:
# 			if tbp != pmsg:
# 				print(tbp)
# 				app.update_profile(first_name=standart+tbp+' '+standart)
# 				sleep(1)
# 				tbp = tbp + text[0]
# 				text = text[1:]
# 			else:
# 				tbp = ''
# 				text = pmsg
# 		except FloodWait as e:
# 			print(e)
# 			sleep(e.x)

# @app.on_message(filters.command('flexstop',prefixes='.')& filters.me)
# def nickstop(_,msg):
# 	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
# 	global flex_stop
# 	flex_stop = True

@app.on_message(filters.command('dead',prefixes='.')& filters.me)
def dead(_,msg):
	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
	pmsg = msg.text.split('.dead',maxsplit = 1)[1]
	original = 1000
	mention = "["+msg.reply_to_message.from_user.first_name+"](tg://user?id="+str(msg.reply_to_message.from_user.id)+")"
	while original > 0:
		try:
			print(original)
			app.send_message(msg.chat.id,str(original)+"-7 **zxc** "+mention+" покойник")
			original = original - 7
			sleep(0.05)
		except FloodWait as e:
			print(e)
			sleep(e.x)
	app.send_message(msg.chat.id,"zxc "+pmsg)

@app.on_message(filters.command('mention',prefixes='.')& filters.me)
def mention(_,msg):
	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
	pmsg = msg.text.split('.mention ',maxsplit = 1)[1]
	pmsgg = msg.text.split('.mention ',maxsplit = 1)[1]
	text = pmsgg.split(" ",1)
	usernam = text[0]
	text = text[1]
	print(usernam+" --- "+text)
	try:
		app.send_message(msg.chat.id,"["+pmsg+"](tg://user?id="+str(msg.reply_to_message.from_user.id)+")")
	except Exception as e:
		try:
			app.send_message(msg.chat.id,"["+text+"](tg://user?id="+str(app.get_users(usernam).id)+")")
		except Exception as e:
			user = msg.entities
			# user = user.json()
			user[0].user.id
			app.send_message(msg.chat.id, "[" + text + "](tg://user?id=" + str(user[0].user.id) + ")")

@app.on_message(filters.command('check',prefixes='.')& filters.me)
def check(_,msg):
	pmsg = msg.text.split('.check',maxsplit = 1)[1]
	pmsg = pmsg.replace(' ', '')
	a = requests.get('http://api.murix.ru/eye?v=1.2&uid='+ str(pmsg)).json()
	app.edit_message_text(msg.chat.id,msg.message_id,a['data'])
	print(a.text)
	print(pmsg)

@app.on_message(filters.command('info',prefixes='.')& filters.me)
def info(_,msg):
	pmsg = msg.text.split('.info ',maxsplit = 1)[1]
	print(app.get_users(pmsg))
	info = app.get_users(pmsg)
	app.edit_message_text(msg.chat.id,msg.message_id,info)

@app.on_message(filters.command(['ct','copytext'],prefixes='.')& filters.me)
def ct(_,msg):
	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
	try:
		capt = msg.reply_to_message.caption
		capt = capt +" - copied text"
		print(capt)
		app.send_message("me",capt)
	except Exception as e:
		app.send_message("me",msg.reply_to_message.text)



@app.on_message(filters.command('sendloc',prefixes='.')& filters.me)
def sendloc(_,msg):
	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
	pmsgg = msg.text.split('.sendloc ',maxsplit = 1)[1]
	text = pmsgg.split(" ",1)
	firstdata = text[0]
	twodata = text[1].replace(' ', '')
	print('first_data-'+str(firstdata)+" : twodata-"+twodata)
	app.send_location(msg.chat.id, float(firstdata), float(twodata))

@app.on_message(filters.command('sendcon',prefixes='.')& filters.me)
def sendcon(_,msg):
	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
	pmsgg = msg.text.split('.sendcon ',maxsplit = 1)[1]
	text = pmsgg.split(" ",1)
	firstdata = text[0]
	twodata = text[1]
	# .replace(' ', '')
	app.send_contact(msg.chat.id,firstdata, twodata)

@app.on_message(filters.command('infoch',prefixes='.')& filters.me)
def infoch(_,msg):
	app.delete_messages(msg.chat.id,msg.message_id,revoke=True)
	inf = msg.text.split('.infoch ',maxsplit = 1)[1]
	chat = app.get_chat(inf)
	print(chat)
	print('+++++++++++++++++++++++++ \n +++++++++++++++++++++++')
	try:
		linkchat = chat.linked_chat.id
		lci = app.get_chat(linkchat)
		print(lci)
	except Exception as e:
		pass

aa = 0

@app.on_message(filters.command(['am','allmention'],prefixes='.')& filters.me)
def menter(_,msg):
	app.delete_messages(msg.chat.id, msg.message_id, revoke=True)
#
	try:
		pmsgg = msg.text.split('.am ', maxsplit=1)[1]
	except:
		try:
			pmsgg = msg.text.split('.allmention ', maxsplit=1)[1]
		except:
			pass
	try:
		text = pmsgg.split(" ", 2)
		firstdata = text[0]
		twodata = text[1]
		threedata = text[2]
	except:
		app.send_message(msg.chat.id,'Правильно писать так - .am (Текст зазыва) (Задержка) (Количество)')
#
	# app.send_message(msg.chat.id,firstdata+','+twodata+','+threedata)
	# print(app.iter_chat_members(msg.chat.id).user.first_name)
	for member in app.iter_chat_members(msg.chat.id,limit=int(threedata)):
		global aa
		aa += 1
		print(str(member.user.id)+':'+str(aa))
		app.send_message(msg.chat.id, "[" + firstdata + "](tg://user?id=" + str(member.user.id) + ")")
		sleep(float(twodata))


app.run()