import random

#list = []
#for list in list:
#	print "%s" % list

#add = input("Enter an activity: ")
#if add not in list: list.append(add)
#else: print("Already added!")

#print(random.choice(list))

chore = ['tidy kitchen', 'do dishes', 'tidy lounge', 'tidy bedroom', 'clean bathroom', 'hoover', 'tidy random crap', 'do course work']
fun = ['paint models', 'play card game', 'play Borderlands', 'play Warframe', 'play Army of Two', 'play Resistance', 'play Warhammer']
passive = ['listen to music', 'watch a film: Comedy', 'watch a film: Animated', 'watch a tv series', 'watch youtube videos']

#print("You should do " (random.choice(chore)) "then " (random.choice(fun)) "while listening or watching " (random.choice(passive)))
print (random.choice(chore), random.choice(fun), random.choice(passive))
