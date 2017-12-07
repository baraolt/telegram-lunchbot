# telegram-lunchbot
A telegram bot written in python. The purpose is to collect lunch menus and paste them in a channel for speeding up decision making.
In it's current state it is designed to be hosted on a Raspberry Pi. Detailed article will be published and linked that explains the code logic.

## Install on Raspberry Pi
1. Create a folder on your Pi. Prefferably /home/pi/LunchBot/
2. Download all the files and the MenuFiles folder into the path described above.
3. Install all python modules necessary using pip3 (detailed explanation coming...)
4. Make the .py files executable: open terminal, go to your folder (cd LunchBot), and execute the following:
  `sudo chmod +x LM_Bot.py`
  `sudo chmod +x LM_fetchMenus.py`
5. Set up a period for fetchMenus to run using CRON (detailed explanation coming...)
6. Set up a time when the Bot logic should start and stop using CRON (detailed explanation coming...)
7. That's it, you're all set!
