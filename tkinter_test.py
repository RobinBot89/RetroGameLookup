#Import Shit
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#Create a list for shit
item_list=[]
name_list=[]

#make a dictionary to match titles to price
NEW_dic={}
COMPLETE_dic={}
LOOSE_dic={}

#GLOBAL VARS
choice1=0
quality=0

def get_name(item_string, game_list, console):
	if choice is 1:
		first_index = item_string.find('nintendo-nes/')
		second_index = item_string.find('?')
		game_name=item_string[first_index + 13:second_index]
		if game_name not in game_list:
			game_list.append(game_name)
	if choice is 2:
		first_index = item_string.find('super-nintendo/')
		second_index = item_string.find('?')
		game_name = item_string[first_index + 15:second_index]
		if game_name not in game_list:
			game_list.append(game_name)
	if choice is 3:
		first_index=item_string.find('64/')
		second_index = item_string.find('?')
		game_name = item_string[first_index + 3:second_index]
		if game_name not in name_list:
			game_list.append(game_name)
	return game_name

def make_dic(item_string,value,my_dic):
	if choice is 1:
		first_index = item_string.find('nintendo-nes/')
		second_index = item_string.find('?')
		key=item_string[first_index + 13:second_index]
		my_dic.update({key: value})

	if choice is 2:
		first_index = item_string.find('super-nintendo/')
		second_index = item_string.find('?')
		key = item_string[first_index + 15:second_index]
		my_dic.update({key:value})

	if choice is 3:
		first_index=item_string.find('64/')
		second_index = item_string.find('?')
		game_name = item_string[first_index + 3:second_index]
		my_dic.update({key:value})
		# Return an incremental quality counter

def get_prices_for_cat(my_dic,my_str):
	count=0
	running_total=0.0
	for key in my_dic:
		count = count + 1
	#return a list of dictionary values
	val_list=my_dic.values()

	averaged_price=sum(val_list,0)/count
	print('The averaged price for the following category, {}, is: ${}'.format(my_str,averaged_price))

#assign html var to be open the webpage with urlopen module

choice=int(input('What game system do you want? 1=nes 2=snes 3=n64: '))

if choice is 1:
	link='https://gamevaluenow.com/nintendo-nes'
if choice is 2:
	link='https://gamevaluenow.com/super-nintendo'
if choice is 3:
	link='https://gamevaluenow.com/nintendo-64'

html= urlopen(link)

#Assign bs to be BeautifulSoup object and open selected link
bs=BeautifulSoup(html, 'html.parser')
#create regex object for pattern matching
x=re.compile('([$].*.\...)')

#find all 'a' class markers and put in a list
bs_list=bs.find_all('a', attrs={'class':'game-link'})

for game in bs_list:
	#find each price in raw data and return one at a time in list format
	result=re.findall(x, str(game))

	#grab all names and throw in a list
	name=get_name(str(game), name_list, choice)

	if result:
		# format prices into float values
		result = float(result[0].replace('$', ''))

		# Reset quality counter
		if quality > 3:
			quality = 0

		#Update Quality
		if name in name_list:
			quality=quality+1
			if quality == 1:
				make_dic(str(game), result, LOOSE_dic)
			if quality == 2:
				make_dic(str(game), result, COMPLETE_dic)
			if quality == 3:
				make_dic(str(game), result, NEW_dic)



print('Raw Data:')
print(bs_list)

print('List of Names:')
print(name_list)

print('New Key Value Pairs:')
print(NEW_dic)
get_prices_for_cat(NEW_dic,'NEW')

print('Complete in Box Key Value Pairs:')
print(COMPLETE_dic)
get_prices_for_cat(COMPLETE_dic,'CIB')

print('Loose Key Value Pairs:')
print(LOOSE_dic)
get_prices_for_cat(LOOSE_dic,'LOOSE')




