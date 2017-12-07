# telegram-lunchbot
A telegram bot written in python. The purpose is to collect lunch menus and paste them in a channel for speeding up decision making.
In it's current state it is designed to be hosted on a Raspberry Pi. Detailed article will be published and linked that explains the code logic.

## Install on Raspberry Pi
1. Create a folder on your Pi. Prefferably /home/pi/LunchBot/
2. Download all the files and the MenuFiles folder into the path described above.
3. Install all python modules necessary using pip3. Open terminal and execute these commands:
  - `sudo pip3 install beautifulsoup4`
  - `sudo pip3 install requests`
4. Make the .py files executable: open terminal, go to your folder (cd LunchBot), and execute the following:
  - `sudo chmod +x LM_Bot.py`
  - `sudo chmod +x LM_fetchMenus.py`
5. Set up a period for fetchMenus to run using CRON. Here's a detailed explanation how to schedule scripts on LINUX: https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/
EXAMPLE: since most restaurants post their daily lunch menu on facebook up until 11am
  - I scheduled `LM_fetchMenus.py` to run every weekday at 11:10am by adding this line to the CRON file: `10 11 * * 1-5 /home/pi/LunchBot/LM_fetchMenus.py`
6. Set up a time when the Bot logic should start and stop using CRON:
  - The bot is usually used between 11:30am and 12:30pm, therefore it makes sense for the logic to run in this timeframe. To start the Bot, this line was added to CRON file in my case: `25 11 * * 1-5 /home/pi/LunchBot/LM_Bot.py`
  - To stop the Bot at 12:35, this line is added to CRON: `35 12 * * 1-5 kilall -9 LM_Bot.py`
7. That's it, you're all set!
