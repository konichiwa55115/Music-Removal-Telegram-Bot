import os
from pyrogram import Client, filters
import shutil
from os import system as cmd
import audioread
from yt_dlp import YoutubeDL

bot = Client(
    "msrmv",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6199159516:AAG2zfGoYPkEU5xQ7ypxerhbhgWgj5V8IbM"
)
audioexs = [".mp3",".ogg",".m4a"]
videoexs = [".mp4",".mkv",".wmv"]



def musicrmv(x,y):
  
  file_path = x
  user_id = y
  filename = os.path.basename(file_path)
  nom,ex = os.path.splitext(filename)
  mp4file = f"{nom}.mp4"
  mp3file = f"{nom}.mp3"
  finalsound = f"{nom}.wav"
  cmd(f'mkdir workdir')
  cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "{mp3file}" -y''')
  def duration_detector(length):
        seconds = length
        return seconds
  with audioread.audio_open(mp3file) as f:
            totalsec = f.duration
  if totalsec<= 100 :
         cmd(f'''spleeter separate -p spleeter:2stems -o workdir "{mp3file}"''')
         if ex in audioexs :
            cmd(f'''ffmpeg -i "./workdir/{nom}/vocals.wav" -q:a 0 -map a "{mp3file}" -y''')
            bot.send_audio(user_id,mp3file,caption=nom)
         elif ex in videoexs :
          cmd(f'''ffmpeg -i "{file_path}" -i "./workdir/{nom}/vocals.wav" -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 "{mp4file}" -y''')
          bot.send_video(user_id, mp4file,caption=nom)
          os.remove(mp4file)
  else :
        cmd(f'mkdir parts')
        cmd(f'''ffmpeg -i "{mp3file}" -f segment -segment_time 100 -c copy "./parts/rmvd%09d.wav" -y''')
        dir_path = "./parts/"
        numbofitems = len(os.listdir(dir_path))
        for x in range(0,numbofitems):
             myzfillvar = str(x).zfill(9)
             pathy=f"./parts/rmvd{myzfillvar}.wav"
             cmd(f'''spleeter separate -p spleeter:2stems -o workdir "{pathy}"''')
             rmvdvoice = f"./workdir/rmvd{myzfillvar}/vocals.wav"
             with open('list.txt', 'a') as f:
                f.write(f'''file {rmvdvoice} \n''')   
        cmd(f'''ffmpeg -f concat -safe 0 -i list.txt "{finalsound}" -y''')
        if ex in audioexs : 
           cmd(f'''ffmpeg -i "{finalsound}" -q:a 0 -map a "{mp3file}" -y''')
           bot.send_audio(user_id, mp3file,caption=nom)
        elif ex in videoexs : 
             cmd(f'''ffmpeg -i "{file_path}" -i "{finalsound}" -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 "{mp4file}" -y''')
             bot.send_video(y, mp4file,caption=nom)
             os.remove(mp4file)
        shutil.rmtree('./parts/') 
        os.remove("list.txt")
  shutil.rmtree('./workdir/')
  if os.path.isfile(file_path):
   os.remove(file_path)
  else :
     print("pass anyway !")
  os.remove(mp3file)


@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا فصل الموسيقا , فقط أرسل الفيديو/ الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/sunnay6626/2 ",disable_web_page_preview=True)

@bot.on_message(filters.private & filters.incoming & filters.video | filters.document | filters.audio )
def _telegram_file(client, message):
     sent_message = message.reply_text('جار الفصل', quote=True)
     file_path = message.download(file_name="./downloads/")
     user_id = message.from_user.id
     musicrmv(file_path,user_id)
     sent_message.delete()
     



bot.run()
