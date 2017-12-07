from bs4 import BeautifulSoup
import requests, re

## Gather information
print('Paste full URL of menu (including http://):')
menuURL = input()

'''Load page'''
print('OK, fetching menu...')
getPage = requests.get(menuURL)
getPage.raise_for_status() # checks for error
menuPage = BeautifulSoup(getPage.content, 'html.parser')

print('OK, now please paste or write here one of the foods from the menu, exactly how it appears on the menu:')
firstInput = input().lower()
firstFood = menuPage.find(text = re.compile(firstInput, re.I)) 
tag = firstFood.parent.name

print('Allright, the last step is to write or paste another food from the menu. Try to add from different section (for example dessert):')
secondInput = input().lower()
secondFood = menuPage.find(text = re.compile(secondInput, re.I))

## Find level of all foods in HTML
checkLvl = False
length = len(secondInput)
level = firstFood.parent
while checkLvl == False:
    for i in range(len(level.text)):
        chunk = level.text[i:i+length].lower()
        if chunk == secondInput:
            checkLvl = True
            break
    if checkLvl == False:
        level = level.parent
        print('Level up!')

foodList = level.select(tag)
print('\nOK, this is what I got:\n')
for item in range(len(foodList)):
    print(foodList[item].text)

print('\nThese are the attributes you need to look for:\n')
print(str(level.attrs))
