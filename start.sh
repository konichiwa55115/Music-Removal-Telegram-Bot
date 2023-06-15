echo "Cloning Repo...."
git clone https://github.com/konichiwa55115/transtest /LazyDeveloper
cd /LazyDeveloper
pip3 install -r requirements.txt
pip3 install spleeter
echo "Starting Bot...."
python3 bot.py
