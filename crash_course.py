import pygame
import random
import time

pygame.init()
 
clock = pygame.time.Clock()
width = 800
height = 600

screen = pygame.display.set_mode((width, height))


pygame.display.set_caption("CRASH_COURSE")

car1 = pygame.image.load("car1.png")
car2 = pygame.image.load("car2.png")
car3 = pygame.image.load("car3.png")
car4 = pygame.image.load("car4.png")
car5 = pygame.image.load("car5.png")
grass = pygame.image.load("grass.jpg")
strip1 = pygame.image.load("yellow_strip.png")
strip2  = pygame.image.load("strip.png") 

def bg():
    screen.blit(grass,(0,0))
    screen.blit(grass,((width - grass.get_width()) ,0))
    screen.blit(strip2,((grass.get_width() + strip2.get_width()), 0))
    screen.blit(strip2,((width - grass.get_width() - strip2.get_width() - 5), 0))

def yellow_stripes():
    i = 0
    j = 0
    while j <= 6:
        screen.blit(strip1,((width/2 - strip1.get_width()/2), 10+i))
        i += 100
        j += 1

def obstacle(obs_x, obs_y, obs):

    if obs == 0:
        obs_pic = car2
    elif obs == 1:
        obs_pic = car3
    elif obs == 2:
        obs_pic = car4
    elif obs == 3:
        obs_pic = car5
    
    screen.blit(obs_pic, (obs_x, obs_y))

 
def car(x,y):
    screen.blit(car1,(x,y))

def main():
    crash = False   
    x_change = 0
    obs_speed = 10
    obs_x = random.randrange((grass.get_width() + strip2.get_width()), (width - grass.get_width() - strip2.get_width() - 20))
    obs_y = -car2.get_height() - height
    obs = 0
    y_change = 0
    enemy_height = 142
    enemy_width = 76

    while not crash:
        screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change -= 5

            if event.key == pygame.K_RIGHT:
                x_change += 5
        
        if (width/2 + car1.get_width()/2 + x_change) > (width - grass.get_width() - strip2.get_width() - 5):
            x_change -= 5

        if (width/2 - car1.get_width()/2 + x_change) < (grass.get_width() + strip2.get_width()):
            x_change += 5


        screen.fill((119,119,119))
        bg()
        yellow_stripes()

        obs_y -= (obs_speed/4)

        obstacle(obs_x, obs_y, obs)

        obs_y += obs_speed

        car((width/2 - car1.get_width()/2 + x_change), (height - car1.get_height()))

        if obs_y > height:
            obs_y = 0 - enemy_height
            obs_x = random.randrange((grass.get_width() + strip2.get_width()), (width - grass.get_width() - strip2.get_width() - 20)) 
            obs = random.randrange(0,3)

        if (height - car1.get_height()) < obs_y + enemy_height:
            print((height - car1.get_height()), obs_y, enemy_height )
            time.sleep(0.2)
            # if (width/2 - car1.get_width()/2 + x_change) > obs_x or car1.get_width() > obs_x:

        pygame.display.update()


        clock.tick(144)

main()
pygame.quit()
quit()

