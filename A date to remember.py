# A Date to remember
# A date simulator!

import random

print('Hello and welcome to your date night! May I have your name?')
daterecipent = input()
datenames = ['Monica', 'Erica', 'Rita', 'Tina', 'Sandra', 'Mary']
date2 = random.choice(datenames)
print('Okay then', daterecipent, 'your date will be' , date2)
Feelings = {'Great', 'Good', 'Okay', 'Bad', 'Terrible'}
print('How much money do you have on you?')
wallet = int(input())
Gastax = wallet - 30
print('Since travel costs a lot, you spent about 30 dollars on gas. Getting to the resturaunt you now only have $',Gastax )
if Gastax < 0:
  print('You could not afford to make it to the resturaunt so your date ended')
  exit()
print('Welcome to Little Vietnam in Nyack!')
Menu = {'Lemongrass Beef Roll': 10, 'Dac Biet': 15, 'Banh Mi': 9, 'Shaken Beef': 18}
print(Menu)
print('What would you like from the menu:')
menuchoice = input()
if menuchoice == 'Lemongrass Beef Roll':
  Resturauntfood = Gastax - 10
elif menuchoice == 'Dac Biet':
  Resturauntfood = Gastax - 15 
elif menuchoice == 'Banh Mi':
  Resturauntfood = Gastax - 9
elif menuchoice == 'Shaken Beef':
  Resturauntfood = Gastax - 18
else:
  print('Not on the menu, I assume you are not hungry')
  Resturauntfood = Gastax - 0
Drinks = {'Thai Iced Tea': 5, 'Lemonade': 4, 'Salted Lemonade': 4.50, 'Soda': 2.50}
print(Drinks)
print('Would you like something to drink?')
drinkchoice = input()
if drinkchoice == 'Thai Iced Tea':
  finalwallet = Resturauntfood - 5
elif drinkchoice == 'Lemonade':
  finalwallet = Resturauntfood - 4
elif drinkchoice == 'Salted Lemonade':
  finalwallet = Resturauntfood - 4.50
elif drinkchoice == 'Soda':
  finalwallet = Resturauntfood - 2.50
else:
  print('Not thirsty I guess?')
  finalwallet = Resturauntfood - 0
print('How would you say the date is going?')
print(Feelings)
userfeelings = input()
if userfeelings == 'Great':
  uservar = 4
elif userfeelings == 'Good':
  uservar = 3
elif userfeelings == 'Okay':
  uservar = 2
elif userfeelings == 'Bad':
  uservar = 1
elif userfeelings == 'Terrible':
  uservar = 0
else:
  print('At a loss for words? I guess the date is going okay then.')
  uservar = 2
datefeelings = [1,2,3,4]
datefeelings2 =random.choice(datefeelings)
print('Time for the bill! Lets see if you overspent...')
if finalwallet < 0:
  print('Uh oh! You ran out of money for your date!Time to wash dishes...The date ended in failure')
  exit()
else:
  print('Thankfully you had enough to cover for your meal. I wonder did you get another date though.')
totalfeelings = uservar + datefeelings2
if totalfeelings >= 7:
  print('You have earned another date!')
elif totalfeelings == 6:
  print('There...might be a chance they havent checked their phone yet?')
else:
  print('There will be no followup date...')