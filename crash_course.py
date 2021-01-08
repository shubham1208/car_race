import pygame
pygame.init()

#vars
width = 800
height = 600

#screen
screen = pygame.display.set_mode((width, height))

#caption and colour
pygame.display.set_caption("CRASH_COURSE")

#loading assets
carimg = pygame.image.load("car1.png")



#image appearing
def car(x,y):
    screen.blit(carimg,(x,y))

#main loop
def main():
    crash = False   
    x_change = 0
    while not crash:
        screen
        #closing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash = True
        
    #moving in x-y pos
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                x_change -= 5

            if event.key ==pygame.K_RIGHT:
                x_change += 5

    #background colour
        screen.fill((119,119,119))
        car((width/2 - carimg.get_width()/2 + x_change  ), (height - carimg.get_height()))
        pygame.display.update()
main()
pygame.quit()
quit()
