import os
from pyrogram import Client, filters
import subprocess
bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5714654934:AAEVIR8baWhJcgUOtWeNmrSjvdRfYRiY7tI"
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
  user_id = message.from_user.id 
  sent_message = message.reply_text('جار الفصل \n\n قال رسول الله ﷺ  لَيَكونَنَّ مِن أُمَّتي أقْوامٌ يَسْتَحِلُّونَ الحِرَ والحَرِيرَ، والخَمْرَ والمَعازِفَ، ولَيَنْزِلَنَّ أقْوامٌ إلى جَنْبِ عَلَمٍ، يَرُوحُ عليهم بسارِحَةٍ لهمْ، يَأْتِيهِمْ -يَعْنِي الفقِيرَ- لِحاجَةٍ، فيَقولونَ: ارْجِعْ إلَيْنا غَدًا، فيُبَيِّتُهُمُ اللَّهُ، ويَضَعُ العَلَمَ، ويَمْسَخُ آخَرِينَ قِرَدَةً وخَنازِيرَ إلى يَومِ القِيامَةِ. ( صحيح البخاري)', quote=True)
  file = message.video
  file_path = message.download(file_name="entry.mp4")
  f = open("myfile.txt", "x")


  subprocess.call(['spleeter', 'separate', '-p', 'spleeter:5stems', '-o', 'output' , "./downloads/entry.mp4" ])  
  subprocess.call(['ffmpeg', '-i',"./downloads/entry.mp4",'-i',"./output/entry/vocals.wav",'-c:v','copy','-c:a','aac','-map','0:v:0','-map','1:a:0','output.mp4','-y' ])
  with open("./output.mp4", 'rb') as f:
        bot.send_video(message.chat.id, f)
  subprocess.call(['unlink',"myfile.txt"]) 
 
 
 

bot.run()
