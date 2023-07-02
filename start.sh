echo "Cloning Repo...."
git clone https://github.com/konichiwa55115/Music-Removal-Telegram-Bot /kony
cd /kony
pip3 install -r requirements.txt
echo "Starting Bot...."
gunicorn app:app & python3 bot.py
