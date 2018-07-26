class Room(object):
	def __init__(self, max_seats):
		self.max_seats = max_seats
		self.taken_seats = 0
		
	def get_remaining_seats(self):
		return self.max_seats - self.taken_seats
		
	def scheduling_seats(self, wanted_seats): 
		if (wanted_seats + self.taken_seats > self.max_seats):
			print ("You have too many people for this room, the maximum is {} people.".format(self.max_seats))
		else:
			self.taken_seats += wanted_seats
			print ("You have scheduled {} seats in this room.".format(wanted_seats))

def seats():
	gym = Room(1000) # need to update this line once room_types is done
	running = True
	while(running):
		msg = "How many seats would you like? There are {} seats remaining.\n"
		response = input(msg.format(gym.get_remaining_seats()))
		if (response == 'q'):
			print ("You have quit successfully.")
			break
		try: 
			response = int(response)		
			gym.scheduling_seats(response)
		except:
			print ("Enter a number of seats less than or equal to {} or press 'q' to quit.".format(gym.get_remaining_seats()))			
seats()

# need to import information from room_types once its done



	