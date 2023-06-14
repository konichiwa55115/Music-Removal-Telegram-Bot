import os
from pyrogram import Client, filters
import subprocess
bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6199159516:AAF62NQbzVB3bWm79sgzOHO8BG4ND5dBMLU"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا فصل الموسيقا , فقط أرسل الفيديو هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)
    
@bot.on_message(filters.private & filters.incoming & filters.video )
def _telegram_file(client, message):
  try: 
    with open("./downloads/entry", 'r') as fh:
      
            sent_message = message.reply_text('هناك عملية يتم الآن . أرسل الصوتية بعد مدة من فضلك', quote=True)
            return
  except FileNotFoundError: 
    pass  
  user_id = message.from_user.id 
  sent_message = message.reply_text('جار الفصل \n\n قال رسول الله ﷺ  لَيَكونَنَّ مِن أُمَّتي أقْوامٌ يَسْتَحِلُّونَ الحِرَ والحَرِيرَ، والخَمْرَ والمَعازِفَ، ولَيَنْزِلَنَّ أقْوامٌ إلى جَنْبِ عَلَمٍ، يَرُوحُ عليهم بسارِحَةٍ لهمْ، يَأْتِيهِمْ -يَعْنِي الفقِيرَ- لِحاجَةٍ، فيَقولونَ: ارْجِعْ إلَيْنا غَدًا، فيُبَيِّتُهُمُ اللَّهُ، ويَضَعُ العَلَمَ، ويَمْسَخُ آخَرِينَ قِرَدَةً وخَنازِيرَ إلى يَومِ القِيامَةِ. ( صحيح البخاري)', quote=True)
  file = message.video
  file_path = message.download(file_name="entry")

    # Execute speech.py script with entry file
  subprocess.call(['ffmpeg', '-i',"./downloads/entry",'-q:a','0','-map','a',"entry.mp3",'-y' ])
  subprocess.call(['ffmpeg','-i',"./downloads/entry",'-c','copy','-an',"entry.mp4",'-y'])
  subprocess.call(['spleeter', 'separate', '-p', 'spleeter:2stems', '-o', 'output' , "entry.mp3" ])
  subprocess.call(['mv',"./output/entry/vocals.wav" , "./output/entry/vocals.mp3" ])
  subprocess.call(['ffmpeg', '-i',"entry.mp4",'-i',"./output/entry/vocals.mp3",'-c:v','copy','-c:a','aac','output.mp4','-y' ])
    # Upload transcription file to user
  with open("./output.mp4", 'rb') as f:
        bot.send_video(message.chat.id, f)
  subprocess.call(['sudo','rm','-r',"./downloads/entry"]) 
  subprocess.call(['sudo','rm','-r',"entry.mp4"]) 
  subprocess.call(['sudo','rm','-r',"entry.mp3"]) 
  subprocess.call(['sudo','rm','-r',"output.mp4"]) 
 
 

bot.run()
