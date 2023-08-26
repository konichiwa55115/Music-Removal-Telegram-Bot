import os
from pyrogram import Client, filters
import shutil
from os import system as cmd
import audioread

bot = Client(
    "msrmv",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6199159516:AAG2zfGoYPkEU5xQ7ypxerhbhgWgj5V8IbM"
)
#put your id,hash and token instead of stars ***
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا فصل الموسيقا , فقط أرسل الفيديو/ الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/sunnay6626/2 ",disable_web_page_preview=True)
    
@bot.on_message(filters.private & filters.incoming & filters.video | filters.document )
def _telegram_file(client, message):
  try: 
    with open('mp4file.mp4', 'r') as fh:
        if os.stat('mp4file.mp4').st_size == 0: 
            pass
        else:
            sent_message = message.reply_text('هناك عملية منتجة تتم الآن . أرسل بعد مدة من فضلك ', quote=True)
            return
  except FileNotFoundError: 
    pass  
  
  user_id = message.from_user.id 
  file = message.video
  file_path = message.download(file_name="./downloads/")
  filename = os.path.basename(file_path)
  realname, ext = os.path.splitext(filename)
  global mp3file
  mp3file = realname+".mp3"
  global mp4file
  mp4file= realname+".mp4"
  finalsound = realname+".wav"
  cmd(f'mkdir workdir')
  sent_message = message.reply_text('جار الفصل \n\n قال رسول الله ﷺ  لَيَكونَنَّ مِن أُمَّتي أقْوامٌ يَسْتَحِلُّونَ الحِرَ والحَرِيرَ، والخَمْرَ والمَعازِفَ، ولَيَنْزِلَنَّ أقْوامٌ إلى جَنْبِ عَلَمٍ، يَرُوحُ عليهم بسارِحَةٍ لهمْ، يَأْتِيهِمْ -يَعْنِي الفقِيرَ- لِحاجَةٍ، فيَقولونَ: ارْجِعْ إلَيْنا غَدًا، فيُبَيِّتُهُمُ اللَّهُ، ويَضَعُ العَلَمَ، ويَمْسَخُ آخَرِينَ قِرَدَةً وخَنازِيرَ إلى يَومِ القِيامَةِ. ( صحيح البخاري)', quote=True)
  cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "./workdir/{mp3file}" -y''')

  def duration_detector(length):
        seconds = length
        return seconds
  with audioread.audio_open(f"./workdir/{mp3file}") as f:
            totalsec = f.duration
  if totalsec<= 300 :
         cmd(f'''spleeter separate -p spleeter:2stems -o workdir "./workdir/{mp3file}"''')
         cmd(f'''ffmpeg -i "{file_path}" -i "./workdir/{realname}/vocals.wav" -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 "./workdir/mp4file.mp4" -y''')
         cmd(f'''mv "./workdir/mp4file.mp4" "{mp4file}"''')
         
         with open(f"{mp4file}", 'rb') as f:
          bot.send_video(message.chat.id, f)
         shutil.rmtree('./workdir/')
         shutil.rmtree('./downloads/')
         cmd(f''' rm "{mp4file}"''')


  else :
        cmd(f'mkdir parts')
        cmd(f'''ffmpeg -i "./workdir/{mp3file}" -f segment -segment_time 300 -c copy "./parts/{realname}%09d.wav" -y''')
        dir_path = "./parts/"
        count = 0
        for path in os.listdir(dir_path):
                if os.path.isfile(os.path.join(dir_path, path)):
                            count += 1
                            numbofitems=count
        coca=0
        while (coca < numbofitems): 
             pathy=f"./parts/{realname}00000000{coca}.wav"
             cmd(f'''spleeter separate -p spleeter:2stems -o workdir "{pathy}"''')
             coca += 1                    
        with open('./workdir/list.txt', 'x') as f:
             kaka=0
             while (kaka < numbofitems):
                f.write(f'file {realname}00000000{kaka}/vocals.wav\n')
                kaka += 1
        cmd(f'''ffmpeg -f concat -safe 0 -i ./workdir/list.txt "./workdir/{finalsound}" -y''')
        cmd(f'''ffmpeg -i {file_path} -i "./workdir/{finalsound}" -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 "./workdir/mp4file.mp4" -y''')
        cmd(f'''mv "./workdir/mp4file.mp4" "{mp4file}"''')
        with open(f"{mp4file}", 'rb') as f:
          bot.send_video(message.chat.id, f)
          shutil.rmtree('./workdir/')
          shutil.rmtree('./parts/') 
          shutil.rmtree('./downloads/')
          cmd(f''' rm "{mp4file}"''')


@bot.on_message(filters.private & filters.incoming & filters.audio | filters.voice )
def _telegram_file(client, message):
  try: 
    with open('mp3file.mp3', 'r') as fh:
        if os.stat('mp3file.mp3').st_size == 0: 
            pass
        else:
            sent_message = message.reply_text('هناك عملية منتجة تتم الآن . أرسل بعد مدة من فضلك ', quote=True)
            return
  except FileNotFoundError: 
    pass  
    
  user_id = message.from_user.id 
  file = message.voice
  file_path = message.download(file_name="./downloads/")
  filename = os.path.basename(file_path)
  realname, ext = os.path.splitext(filename)
  global mp3file
  mp3file = realname+".mp3"
  finalsound = realname+".wav"
  cmd(f'mkdir workdir')
  vocals=f"./workdir/{realname}/vocals.wav"
  sent_message = message.reply_text('جار الفصل \n\n قال رسول الله ﷺ  لَيَكونَنَّ مِن أُمَّتي أقْوامٌ يَسْتَحِلُّونَ الحِرَ والحَرِيرَ، والخَمْرَ والمَعازِفَ، ولَيَنْزِلَنَّ أقْوامٌ إلى جَنْبِ عَلَمٍ، يَرُوحُ عليهم بسارِحَةٍ لهمْ، يَأْتِيهِمْ -يَعْنِي الفقِيرَ- لِحاجَةٍ، فيَقولونَ: ارْجِعْ إلَيْنا غَدًا، فيُبَيِّتُهُمُ اللَّهُ، ويَضَعُ العَلَمَ، ويَمْسَخُ آخَرِينَ قِرَدَةً وخَنازِيرَ إلى يَومِ القِيامَةِ. ( صحيح البخاري)', quote=True)
  cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "./workdir/{mp3file}" -y''')

  def duration_detector(length):
        seconds = length
        return seconds
  with audioread.audio_open(f"workdir/{mp3file}") as f:
            totalsec = f.duration
  if totalsec<= 300 :
         cmd(f'''spleeter separate -p spleeter:2stems -o workdir "./workdir/{mp3file}"''')
         cmd(f'''ffmpeg -i "{vocals}" -q:a 0 -map a "./workdir/mp3file.mp3" -y''')
         cmd(f'''mv "./workdir/mp3file.mp3" "{mp3file}"''')


         with open(f"{mp3file}", 'rb') as f:
          bot.send_audio(message.chat.id, f)
          shutil.rmtree('./workdir/')
          shutil.rmtree('./downloads/')
          cmd(f'''rm "{mp3file}"''')


  else :
        cmd(f'mkdir parts')
        cmd(f'''ffmpeg -i "./workdir/{mp3file}" -f segment -segment_time 300 -c copy "./parts/{realname}%09d.wav" -y''')

        dir_path = "./parts/"
        count = 0
        for path in os.listdir(dir_path):
                if os.path.isfile(os.path.join(dir_path, path)):
                            count += 1
                            numbofitems=count
        coca=0
        while (coca < numbofitems): 
             pathy=f"./parts/{realname}00000000{coca}.wav"
             cmd(f'''spleeter separate -p spleeter:2stems -o workdir "{pathy}"''')
             coca += 1                    
        with open('./workdir/list.txt', 'x') as f:
             kaka=0
             while (kaka < numbofitems):
                f.write(f'file {realname}00000000{kaka}/vocals.wav\n')
                kaka += 1
        cmd(f'''ffmpeg -f concat -safe 0 -i ./workdir/list.txt "./workdir/{finalsound}" -y''')
        cmd(f'''ffmpeg -i "{finalsound}" -q:a 0 -map a "./workdir/mp3file.mp3" -y''')
        cmd(f'''mv "./workdir/mp3file.mp3" "{mp3file}"''')



        with open(f"./workdir/{mp3file}", 'rb') as f:
          bot.send_audio(message.chat.id, f)
        shutil.rmtree('./workdir/')
        shutil.rmtree('./parts/')   
        shutil.rmtree('./downloads/')

          
        

        
 
bot.run()
