#-----------------------------------------------------------Initializing Statements-------------------------------------------------------------
import pygame
import classes

pygame.init()

#Creates display dimensions and name of display
screen_length = 900
screen_height = 900
screen = pygame.display.set_mode((screen_length, screen_height))

pygame.display.set_caption("Binding of Ian")

#Creates font for when text is needed
font = pygame.font.Font(None, size = 30)
winFont = pygame.font.Font(None, size= 100) #Specific Font for winning

#Game over Overlay rects
again = pygame.Rect(600,600, 80,80) 
done_playing = pygame.Rect(150, 600, 80,80)
game_over = pygame.Rect(0,0, 900, 900)

#UI creation (Seperate from screen so that there can be an added transparency value)
surface = pygame.Surface((screen_length,screen_height), pygame.SRCALPHA)
paused = font.render('Game is paused', True, (0, 0, 0))

#Game over display text
death_text = font.render(('You lost! Would you like to try again?'), True, (255, 255, 255))
attempt = font.render(('Again?'), True, (255, 255, 255))
done = font.render(('Later!'), True, (255, 255, 255))

def Bar():
	pygame.draw.rect(surface, (0, 0, 0, 120), [130, 800, 640, 80])
#Creates the highlights of the item select, fourth value represents Transparency. 255 is solid, 0 is fully transparent
def item_select(x):
	pygame.draw.rect(surface, (128, 128, 128, 240),[x, 800, 80 , 10] )
	pygame.draw.rect(surface, (128, 128, 128, 240),[x, 800, 10 , 80] )
	pygame.draw.rect(surface, (128, 128, 128, 240),[x, 870, 80 , 10] )
	pygame.draw.rect(surface, (128, 128, 128, 240),[x+70, 800, 10 , 80])
#Get number of x tiles and y tiles
def num_tiles(file_name):
	file = open(file_name, 'r')
	grid = 0
	for line in file:
		grid+=1
	file.close()
	return grid

#Function creates the layout of the map based off text file
def create_tile(file_name, len, wid):
		final_room = False
		y = 0
		file = open(file_name, 'r')
		tile_size_x = len / num_tiles(file_name)
		tile_size_y = wid / num_tiles(file_name)
		tile_step = len / num_tiles(file_name)
		for line in file:
			x = 0
			for i in line.strip():
				#Tiles are given x location, y location, width of tile, height of tile, rgb values, boolean for isWall, boolean for isDoor, sppecifc map, and where to place the user going through door
				# Room 1 - Dark grey walls, red floors
				if i == 'X':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 60, 60, 60, False, False)) 
				elif i == 'O':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 141, 51, 51, False, False))
				elif i == 'x':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 60, 60, 60, True, False))
				# Room 2 - Purple walls, blue floors
				elif i == 'Q':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 119, 35, 75, False, False))
				elif i == 'P':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 97, 163, 221, False, False))
				elif i == 'q':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 119, 35, 75, True, False))
				# Room 3 - Grey walls, black floors
				elif i == 'R':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 128, 128, 128, False, False))
				elif i == 'E':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 0, 0, 0, False, False))
				elif i == 'r':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 128, 128, 128, True, False))
				# Room 4 - Green walls, dark purple floors
				elif i == 'G':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 45, 139, 54, False, False))
				elif i == 'H':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 86, 28, 90, False, False))
				elif i == 'g':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 45, 139, 54, True, False))
				# Room 5 - Gold walls, purple floors
				elif i == 'Y':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 210, 182, 63, False, False))
				elif i == 'U':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 109, 54, 255, False, False))
				elif i == 'y':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 210, 182, 63, True, False))
				# Brown accent tile
				elif i == 'W':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 150, 75, 0, False, False))
				# Special tiles
				elif i == 'F':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 141, 51, 51, False, False))
					list_monster.append(classes.boss(x, y, 40, 40))
				elif i == 'o':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 141, 51, 51, False, False))
					list_monster.append(classes.base_monster(x, y, 30, 40))
				# Door tiles - Right spawn
				elif i == 'A':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 0, 0, 0, False, True, 'Game/Maps/map.txt', 'L'))
				elif i == 'B':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 0, 0, 0, False, True, 'Game/Maps/map2.txt', 'R'))
				elif i == 'C':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 0, 0, 0, False, True, 'Game/Maps/map3.txt', 'R'))
				elif i == 'D':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 0, 0, 0, False, True, 'Game/Maps/map1.txt', 'R'))
				# Door tiles - Left spawn
				elif i == 'a':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 0, 0, 0, False, True, 'Game/Maps/map1.txt', 'L'))
				elif i == 'b':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 0, 0, 0, False, True, 'Game/Maps/map2.txt', 'L'))
				elif i == 'c':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 0, 0, 0, False, True, 'Game/Maps/map3.txt', 'L'))
				elif i == 'd':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 0, 0, 0, False, True, 'Game/Maps/map1.txt', 'L'))
				elif i == '=':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 0, 0, 0, False, True, 'Game/Maps/TreasureRoom.txt', 'L'))
				elif i == '*':
					list_tile.append(classes.tile(x, y, tile_size_x, tile_size_y, 139, 0, 0, False, False))
					list_monster.append(classes.Final_Boss(x, y, 50, 45))
				x += tile_step
			y += tile_step
		file.close()
		return final_room, False
#Allows for the user to play again if they lose or the option to quit
try_again = True
while try_again == True:
	time = -2 #Keeps Track of invinvcibility cooldown (Starts here so user could be hit immediately)
	map_time = -2 #Keeps track of map switching cool down (^^^)
	cannon_cooldown = 0 #Cannon cooldown
	clock = pygame.time.Clock() #created a clock object
	pause = False #Becomes true if Player presses escape
	item_info = pygame.Rect(20, 800, 70, 70) #Allows for bottom left of screen to be interactable
	rude_buster = classes.item('Game/Images/rude_buster.webp', 450, 450, 40, 40) #This is and following instances create items with their images, location, and dimensions.
	rude_buster_collected = False #Boolean of if item has been collected
	Boomerang = classes.item('Game/Images/boomerang.png', 450, 450, 50, 50)
	Boomerang_collected = False
	Cannon = classes.item('Game/Images/CannonBall.webp', 750, 450, 60, 60)
	CannonCollected = False
	current_slot = 0 #Starts with current selected slot to be 0
	#Checks for different states have been achieved in game
	goneAgainstBoss = False
	bossKilled = False
	FinalRoom = False
	FinalBossKilled = False
	GoneAgainstFinalBoss = False
	#lists of different objects
	user_projectile_list = []
	enemy_projectile_list = []
	list_tile = []
	list_monster = []
	list_items = {}
	
	#Creates user

	ian = classes.player()
	#Initializes the starting room using the map text file, Returns if its a final room, and automatically returns false once called
	FinalRoom, Tutorial= create_tile('Game/Maps/map3.txt', screen_length, screen_height)
	running = True
	Tutorial = True #To counteract the original False initializing
	#Value that helps determine how long the user is invulnerable for after attacked
	invincibility_check = 0

	#--------------------------------------------------Continuously Updates while game is Running----------------------------------------------------
	while running:
		if not pause:
			#keeps track of time, increases by 60 every secong(60fps)
			time += 1
		#Tuple that holds x and y of the mouse position
		mpos = pygame.mouse.get_pos()

		#Goes through each of the events that happens while running
		for event in pygame.event.get():
			#If the event type is attempting to close the window, running stops and shuts down everything.
			if event.type == pygame.QUIT:
				try_again = False
				running = False
			#Checks if the event is any key being pressed down(using this prevents holding a key from cause a rapidly repeated action)
			if event.type == pygame.KEYDOWN:
				#If the key pressed is spacebar, creates and appends a pellet object to projectile_list. Second part prevents a projectile from being shot while a boomerang is on the field.
				#Any helps by returning try if any instance of an item in projectile list returns as a boomerang
				if event.key == pygame.K_SPACE and not any(isinstance(item, classes.boomerang) for item in user_projectile_list):
					try:
						#Slot changes based off of user pressing keys 1-9
						if list_items[slot][0] == classes.Cannon: #Only the cannon has a time based cooldown
							if cannon_cooldown + 1 <= time//60:
								cannon_cooldown = time//60
								#A pellet that's an instance of whatever slot is selected is created and added to projectile list. Class allows for each pellet to be independent with eachother
								pellet = list_items[slot][0](ian.rect.x , ian.rect.y, mpos[0], mpos[1])
								user_projectile_list.append(pellet)
						else:
							pellet = list_items[slot][0](ian.rect.x , ian.rect.y, mpos[0], mpos[1])
							user_projectile_list.append(pellet)
							#Allows for an attempt at using the slot without causing an error is the slot has no value yet 
					except KeyError:
							pass
					#Pauses if escape is pressed and the game hasnt been paused already
				if event.key == pygame.K_ESCAPE and not pause:
					pause = True
				else:
					pause = False
		#Fills screen background with white	
		screen.fill((255, 255, 255))
		#Draws the tiles for the given map, where the color of walls change colors when the mouse hovers over(as) with it. Pausing makes only white background be seen.
		if not pause:
			for i in list_tile:
				pygame.draw.rect(screen, (i.r, (i.g), i.b), i.rect)
		#text Display tests (might be movable out of loop)
		enemies = font.render(('Enemies Present: ' + str(len(list_monster))), True, (255, 255, 255))
		player_health =font.render(('Health: ' + str(ian.health)), True, (255, 0, 0))
		timer = font.render(('Clock:' + str(time//60)), True, (255, 255, 255))
		#Limits framerate to 60fps, it also converts clock.tick()'s milliscond value into seconds
		delta_time = clock.tick(60) / 1000
		#As the framerate changes based off of different background processes, this gives a set amount of fluctuations 
		delta_time = max(0.001, min(0.1, delta_time))
		
		if not pause:
			#sets keys to what key was pressed
			keys = pygame.key.get_pressed()
			#Moves any of the projectiles on the screen towards the mouse position
			for i in list_monster:
				#testing monster type differentiation, classes.hit(player, damage, the time player gets hit). Returns time in seconds and enables invincibility
				if i.type == 'base' and ian.hit(i) and not ian.invincibilty:
					invincibility_check = classes.hit(ian, i.damage, time)
				elif i.type == 'strong' and ian.hit(i) and not ian.invincibilty:
					invincibility_check = classes.hit(ian, i.damage, time)
			#Differentiates weapon movement based off of weapon type
			for i in user_projectile_list:
				if isinstance(i, classes.base_weapon):
					i.movement(delta_time)
					screen.blit(i.image, (i.rect.x, i.rect.y))
				if isinstance(i, classes.boomerang):
					#Boomerang goes forward until its range is reached. Forward function keeps track of how far the boomerang has gone and sets its reached range to true if its reached its range
					if not i.reached_range:
						i.forward(delta_time)
						i.rotated_image = pygame.transform.rotate(i.image, i.angle)
						new_rect = i.rotated_image.get_rect(center=i.rect.center)
						screen.blit(i.rotated_image, (new_rect))

					else:
						#Boomerange comes back to player, at a faster speed as well.(Possibly want to make speeds accelerate)
						i.back_to_player(ian.rect.x, ian.rect.y, delta_time, list_tile)
						i.rotated_image = pygame.transform.rotate(i.image, i.angle)
						new_rect = i.rotated_image.get_rect(center=i.rect.center)
						screen.blit(i.rotated_image, (new_rect))
						if ian.rect.colliderect(i.rect):
							user_projectile_list.remove(i)
				if isinstance(i, classes.Cannon):
					i.movement(delta_time)
					screen.blit(i.image, (i.rect.x, i.rect.y))
		#monster_index
		if not pause:
			monster_index = 0
			while monster_index < len(list_monster):
			#Moves any of the monsters on the screen towards the player objects
				#The different rates at which projectile attack is appended to the boss type based off of health
				if list_monster[monster_index].type == 'boss' and list_monster[monster_index].health <= 6:
					if list_monster[monster_index].cooldown + .1 < time//30:
						list_monster[monster_index].cooldown = time//30
						enemy_projectile_list.append(classes.boss_attack(list_monster[monster_index].rect.x, list_monster[monster_index].rect.y,ian.rect.x, ian.rect.y, list_monster[monster_index].health))
				elif list_monster[monster_index].type == 'boss' and list_monster[monster_index].health <= 12:
					if list_monster[monster_index].cooldown + .7 < time//60:
						list_monster[monster_index].cooldown = time//60
						enemy_projectile_list.append(classes.boss_attack(list_monster[monster_index].rect.x, list_monster[monster_index].rect.y,ian.rect.x, ian.rect.y, list_monster[monster_index].health))
				elif list_monster[monster_index].type == 'boss':
					if list_monster[monster_index].cooldown + 2 < time//60:
						list_monster[monster_index].cooldown = time//60
						enemy_projectile_list.append(classes.boss_attack(list_monster[monster_index].rect.x, list_monster[monster_index].rect.y,ian.rect.x, ian.rect.y, list_monster[monster_index].health))
				#Makes the image of the boss appear of its hitbox(rect)		
				screen.blit(list_monster[monster_index].image, (list_monster[monster_index].rect.x, list_monster[monster_index].rect.y))
				#This is the movement for any mosnter that isn't considered the final boss, where they move towards the player using their individual move functions
				if list_monster[monster_index].type != 'Final Boss':
					list_monster[monster_index].move(ian.rect.x, ian.rect.y, delta_time, list_tile)
				else:
					#Since the Final boss only appears only appears on the final room, final room can be set to true
					FinalRoom = True
					#The final boss moves in a set path, so it only needs the rate at which it moves
					list_monster[monster_index].move(delta_time)
					#Cooldowns are for the rate at the final boss spawns the base_monster
					if list_monster[monster_index].cooldown + 2 < time//60:
						list_monster[monster_index].cooldown = time//60
						list_monster.append(classes.base_monster(list_monster[monster_index].rect.x, list_monster[monster_index].rect.y, 30, 40))
					#Speed inscreases as the final boss loses health
					if list_monster[monster_index].health <= 5:
						list_monster[monster_index].speed = 120
					elif list_monster[monster_index].health <= 10:
						list_monster[monster_index].speed = 60
				#Cycles through the players projectiles, while loop so I can use .remove for the specific pellet
				user_projectile_index = 0
				while user_projectile_index < len(user_projectile_list):
					#Checks for if the mosnter is hit by the user projectile, removes the pellet if they do(unless boomerang), and deals damage according to the pellets damage.
					if list_monster[monster_index].hit(user_projectile_list[user_projectile_index]) and (list_monster[monster_index].status != user_projectile_list[user_projectile_index].status or user_projectile_list[user_projectile_index].type != 'Boomerang'):
						list_monster[monster_index].status = user_projectile_list[user_projectile_index].status
						list_monster[monster_index].health -= user_projectile_list[user_projectile_index].dmg
						if user_projectile_list[user_projectile_index].type != 'Boomerang':
							user_projectile_list.remove(user_projectile_list[user_projectile_index])
						else:
							user_projectile_index+=1
					else:
						user_projectile_index+=1
				#Cycles through the enemy's projectile list, same function as if the user projectile hits the enemy
				enemy_projectile_index = 0
				while enemy_projectile_index < len(enemy_projectile_list):
					if ian.hit(enemy_projectile_list[enemy_projectile_index])  and not ian.invincibilty:
						invincibility_check = classes.hit(ian, enemy_projectile_list[enemy_projectile_index].dmg ,time)
						enemy_projectile_list.remove(enemy_projectile_list[enemy_projectile_index])
					else:
						enemy_projectile_index += 1
				if list_monster[monster_index].health <= 0:
					if list_monster[monster_index].type == 'boss':
						bossKilled = True
					if list_monster[monster_index].type == 'Final Boss':
						FinalBossKilled = True
					list_monster.pop(monster_index)
				else: 
					monster_index+=1
			for i in enemy_projectile_list:
					if isinstance(i, classes.boss_attack):
						i.movement(delta_time)
						screen.blit(i.image, (i.rect.x, i.rect.y))
			i = 0
			while i < (len(enemy_projectile_list)):
				#allows for Enemy projectiles to go through walls/obstacles
				if FinalRoom:
					i+=1
				elif enemy_projectile_list[i].collision(list_tile):
						enemy_projectile_list.pop(i)
				else:
					i+=1
			i = 0
			while i < (len(user_projectile_list)):
				if user_projectile_list[i].collision(list_tile) and user_projectile_list[i].type != 'Cannon':
					user_projectile_list.pop(i)
				else:
					i+=1
			screen.blit(ian.image, (ian.rect.x, ian.rect.y))
			screen.blit(enemies, (30,30))
			screen.blit(player_health, (700,30))
			screen.blit(timer, (450,30))

			Current_slot = ian.input(keys, delta_time,list_tile)
			#Determines if the user can be hit again
			if invincibility_check + 2 < time//60:
				ian.invincibilty = False
			#Functiion checks if the current tile the player is on is a door type tile. If so, it returns true, the room they should go to, and the spawn point they should be in
			check, room, spawn = ian.map_change_check(list_tile)
			#map time is a variable updated every room switch, it prevents the user from being able to immediatley go back to the next room they came from.
			if len(list_monster) == 0 and map_time + 2 < time//60:
				if check:
					#updates current map time
					map_time = time//60
					#Fixes Boss habits
					boss_attack_cooldown = time//60

					#for i in list_tile: (Possible fading in and out idea)
						#while i.r >= 0 or i.g >=0 or i.g >= 0:
							#if i.r >= 0:
								#i.r -= 1
							#if i.g >= 0:
								#i.g -= 1
							#if i.b >= 0:
								#i.b -= 1
					#clears everything on screen besides player
					list_tile.clear()
					list_monster.clear()
					user_projectile_list.clear()
					enemy_projectile_list.clear()
					#Spawn is set to R or L values, determining which side of the room they should come out of.
					if spawn == 'R':
						ian.rect.x = 750
					if spawn == 'L':
						ian.rect.x = 150
					if room == "Game/Maps/TreasureRoom.txt":
						FinalRoom = True

					FinalRoom, Tutorial = create_tile(room, screen_length, screen_height)
					for i in list_tile:
						pygame.draw.rect(screen, (i.r, (i.g), i.b), i.rect)
			#puts surface that allows for transpoarency onto the screen
			screen.blit(surface,(0,0))
			#puts the item select bar onto the surface
			Bar()
			#Chooses what part of the bar to highlight.
			if Current_slot == 1:
				item_select(130)
				slot = 0
			elif Current_slot == 2:
				item_select(210)
				slot = 1
			elif Current_slot == 3:
				item_select(290)	
				slot = 2
			elif Current_slot == 4:
				item_select(370)
				slot = 3
			elif Current_slot == 5:
				item_select(450)
				slot = 4
			elif Current_slot == 6:
				item_select(530)
				slot = 5
			elif Current_slot == 7:
				item_select(610)
				slot = 6
			elif Current_slot == 8:
				item_select(690)	
				slot = 7
			#Loads an image of the weapon to he left of the item bar based off of slot chosen(currently in an exception handling for if the current key does'bt hold a value)
			try:
				itemDescription = pygame.image.load(list_items[slot][1]).convert_alpha()
				itemDescription = pygame.transform.scale(itemDescription, (70,70))
				screen.blit(itemDescription, (20, 800))
			except KeyError:
				pass
			#Displays item info bases off of the current item when the mouse hovers over the left of the item bar.
			if item_info.collidepoint(mpos):
				try:
					display_info = font.render(list_items[slot][2], True, (255, 255, 255))
					screen.blit(display_info, (130,780))
				except KeyError:
					pass
			if Tutorial:
				screen.blit(font.render('Press WASD to move | press Keys 1-9 to select Items!', True, (0, 0, 0)), (10,100))
				screen.blit(font.render('Move to the Item in the middle to collect it', True, (0, 0, 0)), (10,140))
				if rude_buster_collected:
					screen.blit(font.render('You may press space to attack, Now Press the Escape key!', True, (0, 0, 0)), (200,400))
		# ITEM COLLECTION
		#Base weapon spawns on start
		if not rude_buster_collected:
			screen.blit(rude_buster.image, (450,450))
		if not rude_buster_collected and ian.rect.colliderect(rude_buster.rect):
			rude_buster_collected = True
			list_items[current_slot] = [classes.base_weapon, 'Game/Images/rude_buster.webp', "Starter weapon: NO cooldown | Attack: 1 | Speed: 150"]
			current_slot+=1
		#Boomerang is only collectable after defeating boss
		if any(isinstance(item, classes.boss) for item in list_monster):
			goneAgainstBoss = True
		if not Boomerang_collected and goneAgainstBoss and bossKilled and len(list_monster) == 0:
			Boomerang = classes.item('Game/Images/boomerang.png', 450, 450, 50, 50)
			if not pause:
				screen.blit(Boomerang.image, (450,450))
		if bossKilled and not Boomerang_collected and ian.rect.colliderect(Boomerang.rect) and goneAgainstBoss and not any(isinstance(item, classes.boss) for item in list_monster):
			Boomerang_collected = True
			list_items[current_slot] = [classes.boomerang, 'Game/Images/boomerang.png', "Boomerang: Must comeback before thrown again | Attack: 2 | Speed: 200/350"]
			current_slot+=1
		#Cannon is Collectable after defeating final Boss
		if any(isinstance(item, classes.Final_Boss) for item in list_monster):
			GoneAgainstFinalBoss = True
		if not CannonCollected and GoneAgainstFinalBoss and FinalBossKilled:
			Cannon = classes.item('Game/Images/CannonBall.webp', 750, 450, 60, 60)
			if not pause:
				screen.blit(Cannon.image, (750,450))
		if FinalBossKilled and not CannonCollected and ian.rect.colliderect(Cannon.rect) and GoneAgainstFinalBoss and FinalBossKilled:
			CannonCollected = True
			list_items[current_slot] = [classes.Cannon, 'Game/Images/CannonBall.webp', "Cannon ball: Goes through Walls! | Attack: 7 | Speed: 500"]
			current_slot+=1
		#The display that appears when paused by pressing escape
		if pause:
			if Tutorial:
				screen.blit(font.render('Here is where you can see item descriptions.', True, (0, 0, 0)),(20, 250))
				screen.blit(font.render("Items enter the bar from left to right, make sure 1 is selected to use your new item.", True, (0, 0, 0)),(20, 280))
				screen.blit(font.render('Once you unpause, try hovering your mouse over your item!', True, (0, 0, 0)),(20, 310))
				screen.blit(font.render('To move into rooms, walk into the doors on the right and left of the room(In black)', True, (0, 0, 0)),(20, 340))
			screen.blit(paused, (700,30))
			screen.blit(font.render('Press any button to continue!', True, (0, 0, 0)),(300, 450))
			if rude_buster_collected:
				screen.blit(pygame.transform.scale(pygame.image.load('Game/Images/rude_buster.webp').convert_alpha(), (50,50)), (50,50))
				screen.blit(font.render('Base Attack | Cooldown: None | Damage: 1 | Specialties: None', True, (0, 0, 0)),(100, 75))
			if Boomerang_collected:
				screen.blit(pygame.transform.scale(pygame.image.load('Game/Images/boomerang.png').convert_alpha(), (50,50)), (50,150))
				screen.blit(font.render('Boomerang | Cooldown: Until it comes Back | Damage: 2 | Damage in and out', True, (0, 0, 0)),(100, 175))
			if CannonCollected:
				screen.blit(pygame.transform.scale(pygame.image.load('Game./Images/CannonBall.webp').convert_alpha(), (50,50)), (50, 250))
				screen.blit(font.render('Cannon | Cooldown: 1 sec | Damage: 7 | Specialties: Goes Through Walls!', True, (0, 0, 0)),(100, 275))
		if FinalRoom and len(list_monster) == 0: #If there are no more monsters left in the final room, display you win!
			screen.blit(winFont.render("YOU WIN", True, (0,0,0)), (300, 450))
		again_collision = again.collidepoint(mpos)
		playing = done_playing.collidepoint(mpos)
		#Game Over screen
		if ian.health <= 0 and try_again:
			pygame.draw.rect(screen, (0, 0 , 0), game_over)
			screen.blit(death_text, (250, 300))
			#Changes color of Play again or Done rects based off if the mouse position colliding
			pygame.draw.rect(screen, (130, 255 * (not again_collision) , 150), again)
			screen.blit(attempt, (620, 500))
			pygame.draw.rect(screen, (255 * (not playing), 150 , 100), done_playing)
			screen.blit(done, (150, 500))
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and again_collision:
					running = False
				elif event.type == pygame.MOUSEBUTTONDOWN and playing:
					running = False
					try_again = False
		#Responsible for updating the screen.
		pygame.display.flip()

			#running = False