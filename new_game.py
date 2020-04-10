import pygame as pg
from time import sleep



pg.init()
pg.display.init()
pg.display.set_caption('Blob Game')

WIDTH_ = 2000
HEIGHT_ = 1000
pg.display.set_mode([WIDTH_,HEIGHT_])
DISPLAY_ = pg.display.get_surface()

FPS_=30.
DT_=1./FPS_
D_ = 20.

COLOURS_ = {'white':(255,255,255),'red':(255,0,0),'green':(0,255,0),'blue':(0,0,255),'cyan':(0,255,255),'yellow':(255,255,0),'pink':(255,0,255)}
COLOUR_ = 'cyan'

MOVE_SPEED_BASE_ = 10.
MOVE_SPEED_ = MOVE_SPEED_BASE_


message='Hello Mauro'
message2='Hello Robin'


class gravity:
	def __init__(self,env,charactor):
		self.env = env
		self.char = charactor
		self.g = 4.

	def fall(self):
		self.char.fall_speed += self.g
		self.char.y += self.char.fall_speed
		if self.char.y>self.env.floor_height - self.char.height/2.:
			self.char.y = self.env.floor_height - self.char.height/2.
			self.char.fall_speed = 0.
			self.char.grounded = True
		else:
			self.char.grounded = False

	def jump(self):
		if self.char.grounded:
			self.char.fall_speed = -self.char.jump
			self.char.y += self.char.fall_speed

class environment:
	def __init__(self, display):
		self.floor_height = 800
		self.display = display
		self.grasscolour = (20,190,55)

	def draw_floor(self):
		pg.draw.rect(self.display, self.grasscolour,[0,self.floor_height,2000,200])


class charactor:
	def __init__(self, x, y, images):
		self.x = x
		self.y = y
		self.width=72.
		self.height=84.
		self.images = images
		self.image = 21
		self.direction = 'right'
		self.fall_speed = 0.
		self.jump = 40
		self.grounded = False
		self.max_hp = 100
		self.hp = self.max_hp
		self.alive = True

	def set_image(self):
		if self.direction == 'left':
			self.image = self.images[0]
		elif self.direction == 'right':
			self.image = self.images[1]
		else:
			print('marios direction is not left or right')
			exit()

	def draw_healthbar(self,colours,display):
		if self.alive:
			pg.draw.rect(display, colours['red'],[self.x-self.width/2.+5, self.y - self.height,self.width,12])
			if self.hp > 0:
				pg.draw.rect(display, colours['green'],[self.x-self.width/2.+5, self.y - self.height,(self.hp/self.max_hp)*self.width,12])

	def check_alive(self):
		if self.hp <= 0:
			self.alive = False

	def draw(self,display):
		if self.alive:
			display.blit(self.image,[self.x-self.width/2., self.y-mario.height/2.])


grass = environment(DISPLAY_)
mario = charactor(300., 700., [pg.image.load('mario_left_small_clean.png').convert(),pg.image.load('mario_right_small_clean.png').convert()])
grav = gravity(grass,mario)
goomba = charactor(1000., 700., [pg.image.load('mario_enemy_small.png').convert(),pg.image.load('mario_enemy_small.png').convert()])
goombda_grav = gravity(grass,goomba)

while True:

	
	MOUSE_ = pg.mouse.get_pos()

	for event in pg.event.get():

		if event.type == pg.QUIT:
			exit()

		if event.type == pg.KEYDOWN:
			if event.key == pg.K_ESCAPE:
				exit()
			if event.key == pg.K_SPACE:
				grav.jump()
			if event.key == pg.K_q:
				goomba.hp -= 30
			if event.key == pg.K_s:
				mario.hp -= 5
	
	
	key = pg.key.get_pressed()
	if key[pg.K_LEFT]:
		mario.x -= MOVE_SPEED_
		mario.direction = 'left'
	if key[pg.K_RIGHT]:
		mario.x += MOVE_SPEED_
		mario.direction = 'right'

	if mario.x<0.: 
		mario.x=0.
	if mario.x>WIDTH_: 
		mario.x=WIDTH_
	if mario.y<0.: 
		mario.y=0.
	if mario.y>HEIGHT_: 
		mario.y=HEIGHT_

	if MOVE_SPEED_ > MOVE_SPEED_BASE_:
		MOVE_SPEED_ -= 0.2


	mario.set_image()
	goomba.set_image()

	mario.check_alive()
	goomba.check_alive()

	DISPLAY_.fill(COLOURS_['white'])

	grass.draw_floor()
	grav.fall()
	goombda_grav.fall()

	goomba.draw(DISPLAY_)
	goomba.draw_healthbar(COLOURS_,DISPLAY_)
	mario.draw(DISPLAY_)
	mario.draw_healthbar(COLOURS_,DISPLAY_)

	pg.display.update()
	if not mario.alive:
		exit()

	sleep(DT_)

