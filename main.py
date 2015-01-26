import random

house = ['lounge', 'bedroom', 'kitchen', 'bathroom']

lounge_chore = ['clear couch', 'clear desks', 'organise warhammer', 'hoover/mop floor']
bedroom_chore = ['change bedsheets', 'do washing', 'organise toys', 'organise cupboards']
kitchen_chore = ['clean dishes', 'wipe counters', 'organise cupboards', 'hoover/mop floor']
bathroom_chore = ['clean toilet', 'clean sink', 'clean bathtub/tiles']

#you should [PREP VERB] while [ACTIVITY]
fun = ['do hobby', 'play a card game', 'play Borderlands', 'play Warframe', 'play Army of Two', 'play Resistance', 'play Warhammer']
passive = ['listening to music', 'watching a film: Comedy', 'watching a film: Animated', 'watching a tv series', 'watching youtube videos']

room = random.choice(house)
fun = random.choice(fun)
passive = random.choice(passive)

def chore(room):
	for h in house:
		if room == 'lounge':
			lounge = random.choice(lounge_chore)
			print (lounge)
			break
		if room == 'bedroom':
			bedroom = random.choice(bedroom_chore)
			print (bedroom)
			break
		if room == 'kitchen':
			kitchen = random.choice(kitchen_chore)
			print (kitchen)
			break
		if room == 'bathroom':
			bathroom = random.choice(bathroom_chore)
			print (bathroom)
			break
		else: 
			print('ERROR')

def roomdec(room):
	print("The room picked was " + room + ".")

roomdec(room) 
chore(room)

print ("As a reward, you should " + fun + ", while " + passive + ".")
