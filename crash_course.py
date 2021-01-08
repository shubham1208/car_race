import pygame
pygame.init()

#vars
width = 800
height = 600

#screen
screen = pygame.display.set_mode((height, width))

#caption and colour
pygame.display.set_caption("CRASH_COURSE")

#loading assets

#main loop
def main():
    crash = False   
    while not crash:
    screen
    #closing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
            pygame.quit()

    #moving in x-y pos


    #background colour
    screen.fill((119,119,119))
    pygame.display.update()