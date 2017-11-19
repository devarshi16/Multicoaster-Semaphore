import pygame, sys
from pygame.locals import *
from math import sin,cos,pi
pygame.init()
# set up the window
DISPLAYSURF = pygame.display.set_mode((1000, 500), 0, 32)
pygame.display.set_caption('Multi Coster')
# set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
BROWN = (165, 42, 42)
FPS = 30
fpsClock = pygame.time.Clock()
# draw on the surface object
max_capacity=2
class RollerCoaster:
	peopleOn = 0
	position=(300,250)
	seats = []
	def load(self):
		self.peopleOn=self.peopleOn+1
		self.peopleOn-=1

car1 = RollerCoaster()
	
"""
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277),(56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))
pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj
"""
platform = []
carImg = pygame.image.load('car.png')
#faces = [pygame.image.load('face1.png'),pygame.image.load('face2.png'),pygame.image.load('face3.png'),pygame.image.load('face4.png')]
faces = list([pygame.image.load('face{0}.png'.format(i)) for i in range(1,5)])
for i in range(len(faces)):
	faces[i] = pygame.transform.scale(faces[i], (30, 30))
	platform.append(faces[i])
radius=200
angle=-pi
center = (500,250)
#carImg = pygame.transform.scale(carImg, (100, 100))
#rect = carImg.get_rect()
#rect.center = ((50,50))
#car1.position=rect
#rect = rect.move((center,center))
#screen.blit(carImg,rect)
#car1.position=(500,50)

# run the game loop
while True:
	DISPLAYSURF.fill(WHITE)
	pygame.draw.circle(DISPLAYSURF, BROWN, (500, 250), 200, 1)
	pygame.draw.circle(DISPLAYSURF, BROWN, (500, 250), 180, 1)
	carPrintPosition = (car1.position[0]-50,car1.position[1]-50)
	DISPLAYSURF.blit(carImg, carPrintPosition)
	car1.position=(center[0]+radius*cos(angle),center[1]+radius*sin(angle))

	
	if (carPrintPosition==(250,200)):
		del car1.seats[:]
	while True:
	    if(carPrintPosition==(250,200) and len(platform)!=0 and len(car1.seats)<max_capacity):
	    	car1.seats.append(platform.pop(0))
	    else:
	    	break
	count = 0
	for x in car1.seats:
		DISPLAYSURF.blit(x, (carPrintPosition[0]+count*50+10,carPrintPosition[1]+10))
		count+=1
	count = 0
	dist = 40
	for x in platform:
		DISPLAYSURF.blit(x, (260-count*dist,235))
		count+=1
	angle+=pi/180
	#DISPLAYSURF.blit(carImg,rect)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	fpsClock.tick(FPS)
