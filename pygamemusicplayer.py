import pygame
import sys

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("C:\\Users\\Asher\\Downloads\\poradovskyi-cozy-chill-lounge-music-469048.mp3")
pygame.mixer.music.load("C:\\Users\\Asher\\Downloads\\the_mountain-cool-138613.mp3")

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Musicplayer")

pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()