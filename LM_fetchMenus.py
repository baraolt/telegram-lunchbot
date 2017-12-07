#! /usr/bin/python3
import requests, re
from bs4 import BeautifulSoup
import datetime

'''
Fetch menus
'''
menuFM = ''
menuGG = ''
menuKL = ''
menuSU = ''
menuHO = ''
menuCC = ''
menuALL = ''
timestamp = ''

def time_log():
    global timestamp
    dt = datetime.datetime.now()
    year = str(dt.year)
    month = str(dt.month)
    day = str(dt.day)
    hour = str(dt.hour)
    if len(str(dt.minute)) < 2:
        minute = '0' + str(dt.minute)
    else:
        minute = str(dt.minute)
    timestamp = year + '. ' + month + '. ' + day + '. ' + hour + ':' + minute
    TSfile = open('/home/pi/LunchBot/MenuFiles/TSfile.txt', 'w')
    TSfile.write(timestamp)
    TSfile.close()

def fetch_menus():
    print('Fetching menus')

    global menuFM, menuGG, menuKL, menuSU, menuHO, menuCC, menuALL
    
    # FATMAMA
    print('Fetching Fatmama...')
    getePageFM = requests.get('http://fatmama.hu')
    getePageFM.raise_for_status() # Checks for error
    menuPageFM = BeautifulSoup(getePageFM.content, 'html.parser')

    levelFM = menuPageFM.find(attrs={'id': 'post-710', 'class': ['article--page', 'article--main', 'article--subpage', 'border-simple', 'post-710', 'page', 'type-page', 'status-publish', 'has-post-thumbnail', 'hentry']})
    menuFM = '---FATMAMA---'
    menuFM = menuFM + '\n' + (re.sub(r'(\n){2,10}', '\n', levelFM.text))
    FMfile = open('/home/pi/LunchBot/MenuFiles/FMfile.txt', 'w')
    FMfile.write(menuFM)
    FMfile.close()
    getePageFM = ''
    menuPageFM = ''
    levelFM = ''

    # GettoGulyas FB
    print('Fetching GettoGulyas...')
    getePageGG = requests.get('https://www.facebook.com/pg/gettogulyas/posts/')
    getePageGG.raise_for_status() # Checks for error
    menuPageGG = BeautifulSoup(getePageGG.content, 'html.parser')

    levelGG = menuPageGG.find(attrs={'class': ['_1dwg', '_1w_m']})
    menuGG = '---GETTOGULYAS---'
    menuGG = menuGG + '\n' + (re.sub(r'(\n){2,10}', '\n', levelGG.text)) + '\n'
    GGfile = open('/home/pi/LunchBot/MenuFiles/GGfile.txt', 'w')
    GGfile.write(menuGG)
    GGfile.close()
    getePageGG = ''
    menuPageGG = ''
    levelGG = ''
    
    # Koleves FB
    print('Fetching Koleves...')
    getePageKL = requests.get('https://www.facebook.com/pg/Koleves/posts/')
    getePageKL.raise_for_status() # Checks for error
    menuPageKL = BeautifulSoup(getePageKL.content, 'html.parser')

    levelKL = menuPageKL.find(attrs={'class': ['_1dwg', '_1w_m']})
    menuKL = '---KOLEVES---'
    menuKL = menuKL + '\n' + (re.sub(r'(\n){2,10}', '\n', levelKL.text)) + '\n'
    KLfile = open('/home/pi/LunchBot/MenuFiles/KLfile.txt', 'w')
    KLfile.write(menuKL)
    KLfile.close()
    getePageKL = ''
    menuPageKL = ''
    levelKL = ''
    
    # Suelto FB
    print('Fetching Suelto...')
    getePageSU = requests.get('https://www.facebook.com/pg/suelto.bistro/posts/')
    getePageSU.raise_for_status() # Checks for error
    menuPageSU = BeautifulSoup(getePageSU.content, 'html.parser')

    levelSU = menuPageSU.find(attrs={'class': ['_1dwg', '_1w_m']})
    menuSU = '---SUELTO---'
    menuSU = menuSU + '\n' + (re.sub(r'(\n){2,10}', '\n', levelSU.text)) + '\n'
    SUfile = open('/home/pi/LunchBot/MenuFiles/SUfile.txt', 'w')
    SUfile.write(menuSU)
    SUfile.close()
    getePageSU = ''
    menuPageSU = ''
    levelSU = ''
    
    # Hokedli FB
    print('Fetching Hokedli...')
    getePageHO = requests.get('https://www.facebook.com/pg/hokedli/posts/')
    getePageHO.raise_for_status() # Checks for error
    menuPageHO = BeautifulSoup(getePageHO.content, 'html.parser')

    levelHO = menuPageHO.find(attrs={'class': ['_1dwg', '_1w_m']})
    menuHO = '---HOKEDLI---'
    menuHO = menuHO + '\n' + (re.sub(r'(\n){2,10}', '\n', levelHO.text)) + '\n'
    HOfile = open('/home/pi/LunchBot/MenuFiles/HOfile.txt', 'w')
    HOfile.write(menuHO)
    HOfile.close()
    getePageHO = ''
    menuPageHO = ''
    levelHO = ''
    
    #All text menus
    menuALL = menuFM + '\n' + menuGG + '\n' + menuKL + '\n' + menuSU + '\n' + menuHO
    
    # Central Canteen FB Photo
    print('Fetching Central Canteen...')
    getePageCC = requests.get('https://www.facebook.com/pg/centralcanteenbudapest/posts/')
    getePageCC.raise_for_status() # Checks for error
    menuPageCC = BeautifulSoup(getePageCC.content, 'html.parser')

    levelCC = menuPageCC.find(attrs={'class': ['_1dwg', '_1w_m']})
    menuCC = '---CENTRAL CANTEEN---'
    levelCCtext = str(levelCC)
    photoRegexCC = re.compile(r'photos/(.*?)\?')
    # photoRegexCC = re.compile(r'photos/pcb.(.*?)\?')
    # photoRegexCC = re.compile(r'photos/a.(.*?)\?')
    mo = photoRegexCC.search(levelCCtext)
    CCPhotoSrc = mo.group()
    CCPhotoSrc = CCPhotoSrc[:-1]
    CCPhoto = 'https://www.facebook.com/centralcanteenbudapest/' + CCPhotoSrc
    menuCC = menuCC + '\n' + CCPhoto
    CCfile = open('/home/pi/LunchBot/MenuFiles/CCfile.txt', 'w')
    CCfile.write(menuCC)
    CCfile.close()
    getePageCC = ''
    menuPageCC = ''
    levelCC = ''
    CCPhotoSrc = ''
    CCPhoto = ''
    
    time_log()

fetch_menus()
