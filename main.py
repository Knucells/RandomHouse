import random
import time

house = ['lounge', 'bedroom', 'kitchen', 'bathroom']

lounge_chore = ['clear couch', 'clear desks', 'organise warhammer', 'hoover/mop floor']
bedroom_chore = ['change bedsheets', 'do washing', 'organise toys', 'organise cupboards']
kitchen_chore = ['clean dishes', 'wipe counters', 'organise cupboards', 'hoover/mop floor']
bathroom_chore = ['clean toilet', 'clean sink', 'clean bathtub/tiles']

#you should [PREP VERB] while [ACTIVITY]
fun = ['do hobby', 'play a card game', 'play Borderlands', 'play Warframe', 'play Army of Two', 'play Resistance', 'play Warhammer']
passive = ['listening to music', 'watching a film: Comedy', 'watching a film: Animated', 'watching a tv series', 'watching youtube videos']

class House(object):
	def __init__(self):
		self._room = random.choice(house)
		self._fun = random.choice(fun)
		self._passive = random.choice(passive)

	def room(self, room):
		return self._room

	def fun(self, fun):
		return self._fun

	def passive(self, passive):
		return self._passive

	room = property(room)
	fun = property(fun)
	passive = property(passive)

print room, fun, passive

#print("The room picked was " + room + ".")
#print ("As a reward, you should " + fun + ", while " + passive + ".")

def chore(room):
	for h in house:
		if room == 'lounge':
			lounge = random.choice(lounge_chore)
			print ("You should " + lounge + ".")
			break
		if room == 'bedroom':
			bedroom = random.choice(bedroom_chore)
			print ("You should " + bedroom + ".")
			break
		if room == 'kitchen':
			kitchen = random.choice(kitchen_chore)
			print ("You should " + kitchen + ".")
			break
		if room == 'bathroom':
			bathroom = random.choice(bathroom_chore)
			print ("You should " + bathroom + ".")
			break
		else: 
			print("ERROR")


#def reroll()
#roll = raw_input("Would you like to re-roll? Y/N")
	#if roll = "Y":


time.sleep(360)
