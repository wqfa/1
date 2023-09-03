import requests
import telebot
import time, base64, marshal, zlib, py_compile
import os	
token = "6298990568:AAHEtRvdqOnWh4GfyaC9HTVFx9hU0yODsOc"#توكن
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start'])
def start(message):
 
 bot.send_message(message.chat.id,f"""<strong>- ارسل ملفك البايثون ليتم تشفيره 
يتم تشفيره بأكثر من طبقة
⌁ انواع التشفير : 
ـ marshal,base46,zlib ـ</strong>""",parse_mode="html")
 @bot.message_handler(content_types=['document'])
 def send(message):
 	 bot.get_file(message.document.file_id)
 	 #bot.download_file(file_info.file_path)
 	# bot.send_photo(message.chat.id,open("file","rb"))
 	 file_info = bot.get_file(message.document.file_id)
 	 use = bot.download_file(file_info.file_path)
 	 bot.send_message(message.chat.id, f"""<strong>انتظر…</strong>""",parse_mode="html")
 	 cv =str("#@TeAmOn404")
 	 sa = compile(use, 'dg', 'exec')
 	 sb = marshal.dumps(sa)
 	 sc = zlib.compress(sb)
 	 sd = base64.b85encode(sc)
 	 b = '#https://t.me/C15CS\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b85decode(' + repr(sd) + '))))'
 	 d = open('[@TeAmOn404].py', 'w')
 	 d.write(b+'\n'+cv)
 	 d.close()
 	 file = {'document':open('[@TeAmOn404].py','rb')}
 	 tex = ("Done Encryption File")
 	 requests.post(f'https://api.telegram.org/bot{token}/sendDocument?chat_id={message.chat.id}&caption={tex}', files=file)
 	 bot.send_message(message.chat.id, f"[TeAm - 404 .](t.me/C15CS)",parse_mode="markdown",disable_web_page_preview="true")
 	 os.system(f'rm -rf [@TeAmOn404].py')
  	
bot.polling(True)
