import pygame
import sys

pygame.init()

BLACK = 0, 0, 0

# screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Colltst")
clock = pygame.time.Clock()

# clock
interval = 5000
lasttime = 0

collisioncheck = False

# player
playerspeed = 0.05
playerx = 400
playery = 300
playerscale = 50
playerpath = "C:\\Users\\Asher\\Downloads\\red square.jpg"
player = pygame.image.load(playerpath)
player = pygame.transform.scale(player, (playerscale, playerscale))
playerrect = player.get_rect(topleft=(playerx, playery))


# otherguy
otherguyx = 400
otherguyy = 150
otherguyscale = 50
other = pygame.image.load(playerpath)
other = pygame.transform.scale(other, (otherguyscale, otherguyscale))
otherrect = other.get_rect(topleft=(otherguyx, otherguyy)) 



# loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	currenttime = pygame.time.get_ticks()

	if currenttime - lasttime >= interval:
		lasttime = currenttime
		print("its been 5 seconds")


	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		playerx -= playerspeed
	if keys[pygame.K_RIGHT]:
		playerx += playerspeed
	if keys[pygame.K_UP]:
		playery -= playerspeed
	if keys[pygame.K_DOWN]:
		playery += playerspeed

	if playerrect.colliderect(otherrect):
		if not collisioncheck:
			print('collide!')
			collisioncheck = True
	else:
		collisioncheck = False	


	playerrect.topleft = (playerx, playery) 
	otherrect.topleft = (otherguyx, otherguyy)
	
	screen.fill(BLACK)



	screen.blit(player, (playerrect.x, playerrect.y))
	screen.blit(other, (otherrect.x, otherrect.y))

	pygame.display.flip()


	


