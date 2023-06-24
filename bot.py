import os
from pyrogram import Client, filters
import subprocess
import audioread
bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6199159516:AAFyFAF4vw5m34wmFIr0hSc1J4WFQIV4UuY"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا فصل الموسيقا , فقط أرسل الفيديو هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)
    
@bot.on_message(filters.private & filters.incoming & filters.video | filters.document )
def _telegram_file(client, message):
  try: 
    with open("myfile.txt", 'r') as fh:
      
            sent_message = message.reply_text('هناك عملية يتم الآن . أرسل الفيديو بعد مدة من فضلك', quote=True)
            return
  except FileNotFoundError: 
    pass  
    f = open("myfile.txt", "x")
    user_id = message.from_user.id 
    file = message.video
    file_path = message.download(file_name="entry.mp4")
    subprocess.call(['ffmpeg', '-i',"./downloads/entry.mp4",'-q:a','0','-map','a',"entry.mp3",'-y' ])

    def duration_detector(length):
        seconds = length
        return seconds
    with audioread.audio_open('entry.mp3') as f:
            totalsec = f.duration
    if totalsec<= 600 :
         
         sent_message = message.reply_text('جار الفصل \n\n قال رسول الله ﷺ  لَيَكونَنَّ مِن أُمَّتي أقْوامٌ يَسْتَحِلُّونَ الحِرَ والحَرِيرَ، والخَمْرَ والمَعازِفَ، ولَيَنْزِلَنَّ أقْوامٌ إلى جَنْبِ عَلَمٍ، يَرُوحُ عليهم بسارِحَةٍ لهمْ، يَأْتِيهِمْ -يَعْنِي الفقِيرَ- لِحاجَةٍ، فيَقولونَ: ارْجِعْ إلَيْنا غَدًا، فيُبَيِّتُهُمُ اللَّهُ، ويَضَعُ العَلَمَ، ويَمْسَخُ آخَرِينَ قِرَدَةً وخَنازِيرَ إلى يَومِ القِيامَةِ. ( صحيح البخاري)', quote=True)
         subprocess.call(['spleeter', 'separate', '-p', 'spleeter:2stems', '-o', 'output' , "entry.mp3" ])  
         subprocess.call(['ffmpeg', '-i',"./downloads/entry.mp4",'-i',"./output/entry/vocals.wav",'-c:v','copy','-c:a','aac','-map','0:v:0','-map','1:a:0','output.mp4','-y' ])
         with open("./output.mp4", 'rb') as f:
          bot.send_video(message.chat.id, f)
          subprocess.call(['unlink',"myfile.txt"]) 
    else :
        subprocess.call(['rm','-r',"./parts/"])
        subprocess.call(['mkdir',"parts"])
        subprocess.call(['ffmpeg', '-i', "entry.mp3", '-f', 'segment', '-segment_time', '600' ,'-c', 'copy', 'parts/output%09d.wav','-y']) 
        dir_path = "./parts/"
        count = 0
        for path in os.listdir(dir_path):
                if os.path.isfile(os.path.join(dir_path, path)):
                            count += 1
                            numbofitems=count
        coca=0
        while (coca < numbofitems): 
             pathy=f'./parts/output00000000{coca}.wav'
             subprocess.call(['spleeter', 'separate', '-p', 'spleeter:2stems', '-o', 'output' , pathy ]) 
             coca += 1                    
        with open('list.txt', 'x') as f:
             kaka=0
             while (kaka < numbofitems):
                f.write(f'file output/output00000000{kaka}/vocals.wav\n')
                kaka += 1
        subprocess.call(['ffmpeg','-f','concat','-safe','0','-i',"list.txt", "finalsound.wav",'-y']) 
        subprocess.call(['ffmpeg', '-i',"./downloads/entry.mp4",'-i',"finalsound.wav",'-c:v','copy','-c:a','aac','-map','0:v:0','-map','1:a:0','output.mp4','-y' ])
        with open("./output.mp4", 'rb') as f:
          bot.send_video(message.chat.id, f)
          subprocess.call(['unlink',"myfile.txt"]) 
          subprocess.call(['unlink',"list.txt"]) 



        
 
bot.run()
