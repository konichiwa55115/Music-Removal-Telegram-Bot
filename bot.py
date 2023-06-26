import os
from pyrogram import Client, filters
import subprocess
import audioread
bot = Client(
    "msrmv",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5714654934:AAEVIR8baWhJcgUOtWeNmrSjvdRfYRiY7tI"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا فصل الموسيقا , فقط أرسل الفيديو/ الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)
    
@bot.on_message(filters.private & filters.incoming & filters.video | filters.document )
def _telegram_file(client, message):
  try: 
    with open("myfile.txt", 'r') as fh:
      
            sent_message = message.reply_text('هناك عملية تتم الآن . أرسل الفيديو/الصوتية بعد مدة من فضلك', quote=True)
            return
  except FileNotFoundError: 
    pass  
    f = open("myfile.txt", "x")
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
  vocals=f"./output/{realname}/vocals.wav"
  accompliant = f"./output/{realname}/accompaniment.wav"
  subprocess.call(['ffmpeg', '-i',file_path,'-q:a','0','-map','a',mp3file,'-y' ])

  def duration_detector(length):
        seconds = length
        return seconds
  with audioread.audio_open(mp3file) as f:
            totalsec = f.duration
  if totalsec<= 600 :
         
         sent_message = message.reply_text('جار الفصل \n\n قال رسول الله ﷺ  لَيَكونَنَّ مِن أُمَّتي أقْوامٌ يَسْتَحِلُّونَ الحِرَ والحَرِيرَ، والخَمْرَ والمَعازِفَ، ولَيَنْزِلَنَّ أقْوامٌ إلى جَنْبِ عَلَمٍ، يَرُوحُ عليهم بسارِحَةٍ لهمْ، يَأْتِيهِمْ -يَعْنِي الفقِيرَ- لِحاجَةٍ، فيَقولونَ: ارْجِعْ إلَيْنا غَدًا، فيُبَيِّتُهُمُ اللَّهُ، ويَضَعُ العَلَمَ، ويَمْسَخُ آخَرِينَ قِرَدَةً وخَنازِيرَ إلى يَومِ القِيامَةِ. ( صحيح البخاري)', quote=True)
         subprocess.call(['spleeter', 'separate', '-p', 'spleeter:2stems', '-o', 'output' , mp3file ])  
         subprocess.call(['ffmpeg', '-i',file_path,'-i',f"./output/{realname}/vocals.wav",'-c:v','copy','-c:a','aac','-map','0:v:0','-map','1:a:0',mp4file,'-y' ])
         with open(mp4file, 'rb') as f:
          bot.send_video(message.chat.id, f)
          subprocess.call(['unlink',"myfile.txt"]) 
          subprocess.call(['unlink',vocals]) 
          subprocess.call(['unlink',accompliant]) 
          subprocess.call(['unlink',mp3file]) 
          subprocess.call(['unlink',mp4file]) 
          subprocess.call(['unlink',file_path]) 





  else :
        sent_message = message.reply_text('جار الفصل \n\n قال رسول الله ﷺ  لَيَكونَنَّ مِن أُمَّتي أقْوامٌ يَسْتَحِلُّونَ الحِرَ والحَرِيرَ، والخَمْرَ والمَعازِفَ، ولَيَنْزِلَنَّ أقْوامٌ إلى جَنْبِ عَلَمٍ، يَرُوحُ عليهم بسارِحَةٍ لهمْ، يَأْتِيهِمْ -يَعْنِي الفقِيرَ- لِحاجَةٍ، فيَقولونَ: ارْجِعْ إلَيْنا غَدًا، فيُبَيِّتُهُمُ اللَّهُ، ويَضَعُ العَلَمَ، ويَمْسَخُ آخَرِينَ قِرَدَةً وخَنازِيرَ إلى يَومِ القِيامَةِ. ( صحيح البخاري)', quote=True)
        subprocess.call(['ffmpeg', '-i', mp3file, '-f', 'segment', '-segment_time', '600' ,'-c', 'copy', f'parts/{realname}%09d.wav','-y']) 
        dir_path = "./parts/"
        count = 0
        for path in os.listdir(dir_path):
                if os.path.isfile(os.path.join(dir_path, path)):
                            count += 1
                            numbofitems=count
        coca=0
        while (coca < numbofitems): 
             pathy=f"./parts/{realname}00000000{coca}.wav"
             subprocess.call(['spleeter', 'separate', '-p', 'spleeter:2stems', '-o', 'output' , pathy ]) 
             coca += 1                    
        with open('list.txt', 'x') as f:
             kaka=0
             while (kaka < numbofitems):
                f.write(f'file output/{realname}00000000{kaka}/vocals.wav\n')
                kaka += 1
        subprocess.call(['ffmpeg','-f','concat','-safe','0','-i',"list.txt", finalsound,'-y']) 
        subprocess.call(['ffmpeg', '-i',file_path,'-i',finalsound,'-c:v','copy','-c:a','aac','-map','0:v:0','-map','1:a:0',mp4file,'-y' ])
        with open(mp4file, 'rb') as f:
          bot.send_video(message.chat.id, f)
          subprocess.call(['unlink',"myfile.txt"]) 
          subprocess.call(['unlink',"list.txt"]) 
          subprocess.call(['unlink',mp4file]) 
          subprocess.call(['unlink',mp3file]) 
          subprocess.call(['unlink',finalsound]) 
          subprocess.call(['unlink',file_path]) 

        zaza=0
        while (zaza < numbofitems): 
             pathy=f'./parts/{realname}00000000{zaza}.wav'
             nagy=f"./output/{realname}00000000{zaza}/vocals.wav"
             hady=f"./output/{realname}00000000{zaza}/accompaniment.wav"
             subprocess.call(['unlink', pathy ]) 
             subprocess.call(['unlink', nagy ]) 
             subprocess.call(['unlink', hady ]) 
             zaza += 1           
        

@bot.on_message(filters.private & filters.incoming & filters.audio | filters.voice )
def _telegram_file(client, message):
  try: 
    with open("myfile.txt", 'r') as fh:
      
            sent_message = message.reply_text('هناك عملية تتم الآن . أرسل الفيديو/الصوتية بعد مدة من فضلك', quote=True)
            return
  except FileNotFoundError: 
    pass  
    f = open("myfile.txt", "x")
  user_id = message.from_user.id 
  file = message.voice
  file_path = message.download(file_name="./downloads/")
  filename = os.path.basename(file_path)
  realname, ext = os.path.splitext(filename)
  global mp3file
  mp3file = realname+".mp3"
  finalsound = realname+".wav"
  vocals=f"./output/{realname}/vocals.wav"
  result=f"./output/{realname}/{mp3file}"
  accompliant = f"./output/{realname}/accompaniment.wav"
  subprocess.call(['ffmpeg', '-i',file_path,'-q:a','0','-map','a',mp3file,'-y' ])

  def duration_detector(length):
        seconds = length
        return seconds
  with audioread.audio_open(mp3file) as f:
            totalsec = f.duration
  if totalsec<= 600 :
         
         sent_message = message.reply_text('جار الفصل \n\n قال رسول الله ﷺ  لَيَكونَنَّ مِن أُمَّتي أقْوامٌ يَسْتَحِلُّونَ الحِرَ والحَرِيرَ، والخَمْرَ والمَعازِفَ، ولَيَنْزِلَنَّ أقْوامٌ إلى جَنْبِ عَلَمٍ، يَرُوحُ عليهم بسارِحَةٍ لهمْ، يَأْتِيهِمْ -يَعْنِي الفقِيرَ- لِحاجَةٍ، فيَقولونَ: ارْجِعْ إلَيْنا غَدًا، فيُبَيِّتُهُمُ اللَّهُ، ويَضَعُ العَلَمَ، ويَمْسَخُ آخَرِينَ قِرَدَةً وخَنازِيرَ إلى يَومِ القِيامَةِ. ( صحيح البخاري)', quote=True)
         subprocess.call(['spleeter', 'separate', '-p', 'spleeter:2stems', '-o', 'output' , mp3file ])  
         subprocess.call(['ffmpeg', '-i',vocals,'-q:a','0','-map','a',mp3file,'-y' ])

         with open(mp3file, 'rb') as f:
          bot.send_audio(message.chat.id, f)
          subprocess.call(['unlink',"myfile.txt"]) 
          subprocess.call(['unlink',vocals]) 
          subprocess.call(['unlink',accompliant]) 
          subprocess.call(['unlink',mp3file]) 
          subprocess.call(['unlink',file_path]) 





  else :
        sent_message = message.reply_text('جار الفصل \n\n قال رسول الله ﷺ  لَيَكونَنَّ مِن أُمَّتي أقْوامٌ يَسْتَحِلُّونَ الحِرَ والحَرِيرَ، والخَمْرَ والمَعازِفَ، ولَيَنْزِلَنَّ أقْوامٌ إلى جَنْبِ عَلَمٍ، يَرُوحُ عليهم بسارِحَةٍ لهمْ، يَأْتِيهِمْ -يَعْنِي الفقِيرَ- لِحاجَةٍ، فيَقولونَ: ارْجِعْ إلَيْنا غَدًا، فيُبَيِّتُهُمُ اللَّهُ، ويَضَعُ العَلَمَ، ويَمْسَخُ آخَرِينَ قِرَدَةً وخَنازِيرَ إلى يَومِ القِيامَةِ. ( صحيح البخاري)', quote=True)
        subprocess.call(['ffmpeg', '-i', mp3file, '-f', 'segment', '-segment_time', '600' ,'-c', 'copy', f'parts/{realname}%09d.wav','-y']) 
        dir_path = "./parts/"
        count = 0
        for path in os.listdir(dir_path):
                if os.path.isfile(os.path.join(dir_path, path)):
                            count += 1
                            numbofitems=count
        coca=0
        while (coca < numbofitems): 
             pathy=f"./parts/{realname}00000000{coca}.wav"
             subprocess.call(['spleeter', 'separate', '-p', 'spleeter:2stems', '-o', 'output' , pathy ]) 
             coca += 1                    
        with open('list.txt', 'x') as f:
             kaka=0
             while (kaka < numbofitems):
                f.write(f'file output/{realname}00000000{kaka}/vocals.wav\n')
                kaka += 1
        subprocess.call(['ffmpeg','-f','concat','-safe','0','-i',"list.txt", finalsound,'-y']) 
        subprocess.call(['ffmpeg', '-i',finalsound,'-q:a','0','-map','a',mp3file,'-y' ])

        with open(mp3file, 'rb') as f:
          bot.send_audio(message.chat.id, f)
          subprocess.call(['unlink',"myfile.txt"]) 
          subprocess.call(['unlink',"list.txt"]) 
          subprocess.call(['unlink',mp3file]) 
          subprocess.call(['unlink',finalsound]) 
          subprocess.call(['unlink',file_path]) 

        zaza=0
        while (zaza < numbofitems): 
             pathy=f'./parts/{realname}00000000{zaza}.wav'
             nagy=f"./output/{realname}00000000{zaza}/vocals.wav"
             hady=f"./output/{realname}00000000{zaza}/accompaniment.wav"
             subprocess.call(['unlink', pathy ]) 
             subprocess.call(['unlink', nagy ]) 
             subprocess.call(['unlink', hady ]) 
             zaza += 1           
        

        
 
bot.run()
