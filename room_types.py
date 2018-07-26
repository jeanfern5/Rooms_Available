rooms = {
			'gym': 100, 'gym 2': 50, 'library': 40, 'study room': 20, 'study room 2':10,			
			'study room 3': 5, 'computer room':10, 'game room': 30, 'event room': 200, 
			'cafe':15
			}
		
def room_type():
	running = True
	while(running):
		answer = input("What room are you looking to schedule?\n")
		if (answer == 'q'):
			print ("You have quit successfully.")
			break
		for key in rooms:
			if (key == answer):
				try: 
					print ("You have successfully scheduled {} room.".format(answer))
				except:
					print ("Enter a valid room or press 'q' to quit.")
		
	

room_type()		