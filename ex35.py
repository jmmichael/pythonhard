from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("type a number")

	if how_much < 50:
		print "Not greedy, you win"
		exit(0)
	else:
		dead("Greedy")

def bear_room():
	print "There is a bear here"
	print "The bear has honey"
	print "The dear is in front of another door"
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		choice = raw_input("> ")

		if choice == "take honey":
			dead("Bear slaps you face")
		elif choice == "taunt bear" and not bear_moved:
			print "Bear has moved from the door. Go through"
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("Bear chews you leg off")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			 print "No idea what that means"

def croom():
	print "Here you see the evil C"
	print "It stares at you and you go insane"
	print "Flee or eat your head?"

	choice =raw_input("> ")
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty")
	else:
		croom()
def dead(why):
	print why, "Good job"
	exit (0)

def start():
	print"You are in a dark room"
	print "There is a door to your right and left"
	print "Which one do you take?"

	choice = raw_input("left or right> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		croom()
	else:
		dead("Stumble about until dead")

start()
