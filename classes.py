import pygame
import math
screen_length = 900
screen_height = 900
#Tile class
class tile(object):
	def __init__(self, x, y, width, height, r, g ,b, isWall, isDoor, room = 'no room attacthed', spawn = 'no spawn'):
		'''DocString
			parameters:
				Self: the individual tile object
				x: x Coordinate 	(int)
				y: y Coordinate		(int)
				width: How wide the tile is		(int)
				height: How tall the tile is	(int)
				r,g,b: The color codes for each tile	(int)
				isWall: Whether the tile is a wall		(boolean)
				isDoor: Whether the tile is a door		(boolean)
				room: determines what map should be spawned in		(string)
				spawn: determines where the player should go to once a door is entered		(string)

					'''
		self.rect = pygame.Rect(x, y, width, height)
		self.wall = isWall
		self.r = r
		self.b = b
		self.g = g
		self.isDoor = isDoor
		self.room = room
		self.spawn = spawn

#Creates entity class that is the parent for Projectiles, players, and monsters
class entity(object):
	#Detects for if some enetity(Monsters, players, projectils) hit a wall space or the edge of the screen
	def collision(self, list_tile):
		'''DocString
			parameters:
				self - allows the function to get access of whatever attriubtes is applied to itself

				list_tile - a list of tile objects with their own locations, colors, and other attributes like if they're a wall

					'''
		wall_collision = False
		for i in list_tile:
				#Sorts through list of tiles, checking for whether their wall attribute is true.
				if (i.wall and i.rect.colliderect(self.rect)) or self.rect.x > screen_length - self.rect.width or self.rect.y > screen_height - self.rect.height or self.rect.x < 0 or self.rect.y < 0:
					wall_collision = True
		return wall_collision
		
#Creates monester class that inherits from entity
class base_monster(entity):
	
	#function that automatically runs when created, creating an object of this class requires the input of __init__ parameters
	def __init__(self, x, y, width, height):
		'''DocString
			parameters:
				self - allows the function to get access of whatever attriubtes is applied to itself
				
				x - x location

				y - y location

				width - how wide the hitbox of the monster should be
				
				height - how tall the monster should be
					'''
		self.float_x = x
		self.float_y = y
		self.rect = pygame.Rect(x, y, width, height)
		self.health = 5
		self.damage = 2
		self.type = 'base'
		self.speed = 80
		self.image = pygame.image.load('Images/chicken.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, (width,height))
		self.status = 9999999999
	#When called, moves the monster towards the player
	def move(self, player_x, player_y, delta_time, list_tile):
		self.length =  math.sqrt((self.rect.x - player_x)**2+(self.rect.y - player_y)**2)
		self.dx = self.rect.x - player_x
		self.dy = self.rect.y - player_y
		#Prevents divide by zero error in case 
		try:
			self.float_x -= self.dx/self.length * self.speed * delta_time
			self.rect.x = int(self.float_x)
			if self.collision(list_tile):
				self.float_x += self.dx/self.length * self.speed * delta_time
				self.rect.x = int(self.float_x)

			self.float_y -= self.dy/self.length * self.speed * delta_time
			self.rect.y = int(self.float_y)
			if self.collision(list_tile):
				self.float_y += self.dy/self.length * self.speed * delta_time
				self.rect.y = int(self.float_y)
		except ZeroDivisionError:
			self.length += .000000001
			self.float_x -= self.dx/self.length * self.speed * delta_time
			self.rect.x = int(self.float_x)
			if self.collision(list_tile):
				self.float_x += self.dx/self.length * self.speed * delta_time
				self.rect.x = int(self.float_x)

			self.float_y -= self.dy/self.length * self.speed * delta_time
			self.rect.y = int(self.float_y)
			if self.collision(list_tile):
				self.float_y += self.dy/self.length * self.speed * delta_time
				self.rect.y = int(self.float_y)
	def hit(self, projectile):
		hit = False
		if projectile.rect.colliderect(self.rect):
			hit = True
		return hit
#Boss
class boss(entity):
	def __init__(self, x, y, width, height):
		'''DocString
			parameters:
				self - allows the function to get access of whatever attriubtes is applied to itself
				
				x - x location

				y - y location

				width - how wide the hitbox of the monster should be
				
				height - how tall the monster should be
					'''
		self.cooldown = 0
		self.float_x = x
		self.float_y = y
		self.rect = pygame.Rect(x, y, width, height)
		self.health = 22
		self.damage = 3
		self.type = 'boss'
		self.speed = 40
		self.image = pygame.image.load('Images/ghast.jpeg').convert_alpha()
		self.image = pygame.transform.scale(self.image, (width,height))
		self.status = 'boss'
	def move(self, player_x, player_y, delta_time, list_tile):
		self.length =  math.sqrt((self.rect.x - player_x)**2+(self.rect.y - player_y)**2)
		if self.length > 200:
			self.dx = self.rect.x - player_x
			self.dy = self.rect.y - player_y
			#Prevents divide by zero error in case 
			try:
				self.float_x -= self.dx/self.length * self.speed * delta_time
				self.rect.x = int(self.float_x)
				if self.collision(list_tile):
					self.float_x += self.dx/self.length * self.speed * delta_time
					self.rect.x = int(self.float_x)

				self.float_y -= self.dy/self.length * self.speed * delta_time
				self.rect.y = int(self.float_y)
				if self.collision(list_tile):
					self.float_y += self.dy/self.length * self.speed * delta_time
					self.rect.y = int(self.float_y)
			except ZeroDivisionError:
				self.length += .000000001
				self.float_x -= self.dx/self.length * self.speed * delta_time
				self.rect.x = int(self.float_x)
				if self.collision(list_tile):
					self.float_x += self.dx/self.length * self.speed * delta_time
					self.rect.x = int(self.float_x)

				self.float_y -= self.dy/self.length * self.speed * delta_time
				self.rect.y = int(self.float_y)
				if self.collision(list_tile):
					self.float_y += self.dy/self.length * self.speed * delta_time
					self.rect.y = int(self.float_y)
	def hit(self, projectile):
		hit = False
		if projectile.rect.colliderect(self.rect):
			hit = True
		return hit
class Final_Boss(entity):
	def __init__(self,xloc, yloc, width, height):
		self.rect = pygame.Rect(xloc, yloc, width, height)
		self.health = 15
		self.speed = 30
		if self.health < 5:
			self.speed = 90
		elif self.health < 10:
			self.speed = 60
		self.cooldown = 0
		self.float_x = xloc
		self.float_y = yloc
		self.type = "Final Boss"
		self.downleft = False
		self.downright = False
		self.upleft = False
		self.upright =  False
		if yloc > 450:
			self.downright = True
		else:
			self.upleft = True
		self.image = pygame.image.load('Images/finalboss.jpeg')
		self.image = pygame.transform.scale(self.image, (width, height))
		self.status =  'Final Boss'
	def move(self, deltatime):
		if self.downleft:
			self.float_x -= self.speed * deltatime
			self.rect.x = int(self.float_x)
			self.float_y -= self.speed * deltatime
			self.rect.y = int(self.float_y)
			if self.rect.y <= 450 and self.rect.x <= 450:
				self.downleft = False
				self.upleft = True
		elif self.downright:
			self.float_x += self.speed * deltatime
			self.rect.x = int(self.float_x)
			self.float_y -= self.speed * deltatime
			self.rect.y = int(self.float_y)
			if self.rect.x >= 450 and self.rect.y <=450:
				self.downright = False
				self.downleft = True
		elif self.upright:
			self.float_x += self.speed * deltatime
			self.rect.x = int(self.float_x)
			self.float_y += self.speed * deltatime
			self.rect.y = int(self.float_y)
			if self.rect.x >= 450 and self.rect.y >= 450:
				self.upright = False
				self.downright = True
		elif self.upleft:
			self.float_x -= self.speed * deltatime
			self.rect.x = int(self.float_x)
			self.float_y += self.speed * deltatime
			self.rect.y = int(self.float_y)
			if self.rect.x <= 450 and self.rect.y >= 450:
				self.upleft = False
				self.upright = True
	def hit(self, projectile):
		hit = False
		if projectile.rect.colliderect(self.rect):
			hit = True
		return hit

#Creates player entity
class player(entity):
	def __init__(self):
		'''DocString
		Initializes different values that are accesible 
			parameters: Self
					'''
		self.width = 45
		self.height = 45
		self.rect = pygame.Rect(200, screen_height/2, self.width, self.height)
		self.speed = 150
		self.health = 20
		self.image = pygame.image.load('Images/sword.gif').convert()
		self.image = pygame.transform.scale(self.image, (self.width, self.height))
		self.invincibilty = False
		self.currentSlot = 1
		self.pause = False
	def map_change_check(self, list_tile):
		for i in list_tile:
			if i.rect.colliderect(self.rect) and i.isDoor:
				room = i.room
				spawn = i.spawn
				return True, i.room, spawn
		return False, 'no room', i.spawn
	def input(self, keys, delta_time, list_tile):
		'''DocString
			Function to move the player repeated in a direction based on key pressed
			parameters:
					'''
		if keys[pygame.K_d]:
			self.rect.x+= self.speed*delta_time
			if self.collision(list_tile):	
				self.rect.x-= self.speed*delta_time				
		if keys[pygame.K_w]:
			self.rect.y-= self.speed*delta_time
			if self.collision(list_tile):	
				self.rect.y+= self.speed*delta_time
				
		if keys[pygame.K_a]:
			self.rect.x-= self.speed*delta_time
			if self.collision(list_tile):	
				self.rect.x+= self.speed*delta_time
				
		if keys[pygame.K_s]:
			self.rect.y+= self.speed*delta_time
			if self.collision(list_tile):	
				self.rect.y-= self.speed*delta_time
		if keys[pygame.K_1]:
			self.currentSlot = 1
		if keys[pygame.K_2]:
			self.currentSlot = 2
		if keys[pygame.K_3]:
			self.currentSlot = 3
		if keys[pygame.K_4]:
			self.currentSlot = 4
		if keys[pygame.K_5]:
			self.currentSlot = 5
		if keys[pygame.K_6]:
			self.currentSlot = 6
		if keys[pygame.K_7]:
			self.currentSlot = 7
		if keys[pygame.K_8]:
			self.currentSlot = 8
		return self.currentSlot
	def hit(self, enemy):
		hit = False
		if self.rect.colliderect(enemy.rect):
			hit = True
		return hit
def hit(player, damage, time):
		player.health -= damage
		player.invincibilty = True
		return time//60
#creats projectile entity
class projectile(entity):
	def vector(self, self_x, self_y, target_x, target_y):
		'''DocString
			parameters:
					'''
		self.length = math.sqrt((self_x-target_x)**2 + (self_y-target_y)**2)
		self.dx = self_x-target_x
		self.dy = self_y-target_y
		self.float_x = self_x
		self.float_y = self_y
		self.x = int(self.float_x)
		self.y = int(self.float_y)
		self.status = 0
class base_weapon(projectile):
	def __init__(self, player_x, player_y, mouse_x, mouse_y):
		'''DocString
			parameters:
					'''
		self.type = 'base_weapon'
		self.vector(player_x, player_y, mouse_x, mouse_y)
		self.rect = pygame.Rect(self.x, self.y, 15, 15 )
		self.dmg = 1
		self.speed = 150
		self.image = pygame.image.load('Images/rude_buster.webp').convert_alpha()
		self.image = pygame.transform.scale(self.image, (15,15))
	def movement(self, delta_time):
		try:
			self.float_x -= self.dx/self.length * self.speed * delta_time
			self.rect.x = int(self.float_x)
			self.float_y -= self.dy/self.length * self.speed * delta_time
			self.rect.y = int(self.float_y)
		except ZeroDivisionError:
			self.length += .0000000001
			self.rect.x -= self.dx/self.length * self.speed * delta_time
			self.rect.y -= self.dy/self.length * self.speed * delta_time

#Boomerang weapon
class boomerang(projectile):
	def __init__(self, player_x, player_y, mouse_x, mouse_y):
		self.rotated_image = 'placeholder'
		self.type = 'Boomerang'
		self.vector(player_x, player_y, mouse_x, mouse_y)
		self.rect = pygame.Rect(self.x, self.y, 30, 30)
		self.speed = 200
		self.range = 150
		self.image = pygame.image.load('Images/boomerang.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, (60,60))
		self.start =  (player_x, player_y)
		self.distance = 0
		self.reached_range = False
		self.angle = 0
		self.dmg = 2
	def forward(self, delta_time):
			self.status = 1
			self.angle += 3
			self.distance = math.sqrt((self.rect.x - (self.start[0]))**2 + (self.rect.y - (self.start[1]))**2)
			self.float_x -= self.dx/self.length * self.speed * delta_time
			self.rect.x = int(self.float_x)
			self.float_y -= self.dy/self.length * self.speed * delta_time
			self.rect.y = int(self.float_y)
			if self.distance > self.range:
				self.reached_range = True
	def back_to_player(self, player_x, player_y, delta_time, list_tile):
		self.status = 2
		self.angle += 15
		self.speed = 350
		length =  math.sqrt((self.rect.x - player_x)**2+(self.rect.y - player_y)**2)
		self.dx = self.rect.x - player_x
		self.dy = self.rect.y - player_y
		#Prevents divide by zero error in case 
		self.float_x -= self.dx/length * self.speed * delta_time
		self.rect.x = int(self.float_x)
		if self.collision(list_tile):
			self.float_x += self.dx/length * self.speed * delta_time
			self.rect.x = int(self.float_x)

		self.float_y -= self.dy/length * self.speed * delta_time
		self.rect.y = int(self.float_y)
		if self.collision(list_tile):
			self.float_y += self.dy/length * self.speed * delta_time
			self.rect.y = int(self.float_y)
class Cannon(projectile):
	def __init__(self, player_x, player_y, mouse_x, mouse_y):
		'''DocString
			parameters:
					'''
		self.type = "Cannon"
		self.vector(player_x, player_y, mouse_x, mouse_y)
		self.rect = pygame.Rect(self.x, self.y, 70, 70)
		self.dmg = 7
		self.speed = 500
		self.image = pygame.image.load('Images/CannonBall.webp').convert_alpha()
		self.image = pygame.transform.scale(self.image, (80,80))
	def movement(self, delta_time):
		try:
			self.float_x -= self.dx/self.length * self.speed * delta_time
			self.rect.x = int(self.float_x)
			self.float_y -= self.dy/self.length * self.speed * delta_time
			self.rect.y = int(self.float_y)
		except ZeroDivisionError:
			self.length += .0000000001
			self.rect.x -= self.dx/self.length * self.speed * delta_time
			self.rect.y -= self.dy/self.length * self.speed * delta_time
			
class boss_attack(projectile):
	def __init__(self, boss_x, boss_y, player_x, player_y,boss_health):
		'''DocString
			parameters:
					'''
		self.type = 'boss_attack'
		self.rect = pygame.Rect(boss_x, boss_y, 30, 30)
		self.dmg = 3
		self.speed = 150
		self.image = pygame.image.load('Images/fireBall.webp').convert_alpha()
		self.image = pygame.transform.scale(self.image, (30,30))
		if boss_health <= 5:
			self.speed = 300
			self.image = pygame.transform.scale(self.image, (50,50))
			self.rect = pygame.Rect(boss_x, boss_y, 50, 50)
		self.vector(self.rect.x, self.rect.y, player_x, player_y)
		self.status = 'enemy1'
	def movement(self, delta_time):
		try:
			self.float_x -= self.dx/self.length * self.speed * delta_time
			self.rect.x = int(self.float_x)
			self.float_y -= self.dy/self.length * self.speed * delta_time
			self.rect.y = int(self.float_y)
		except ZeroDivisionError:
			self.length += .0000000001
			self.rect.x -= self.dx/self.length * self.speed * delta_time
			self.rect.y -= self.dy/self.length * self.speed * delta_time
class item(object):
	def __init__(self, image, xloc, yloc, width, height):
		self.rect = pygame.Rect(xloc,yloc, width, height)
		self.image = pygame.image.load(image).convert_alpha()
		self.image = pygame.transform.scale(self.image, (50,50))