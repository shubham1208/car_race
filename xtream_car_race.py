'''
to install pygame:
type "pip install pygame" in CMD or terminal

github link:
https://github.com/shubham1208/car_race
'''

import pygame
import random
import time
import os

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
width = 800
height = 600

screen = pygame.display.set_mode((width, height))

# font = pygame.font.SysFont(None, size)

pygame.display.set_caption("Xtream car race")

car1 = pygame.image.load("car1.png")
car2 = pygame.image.load("car2.png")
car3 = pygame.image.load("car3.png")
car4 = pygame.image.load("car4.png")
car5 = pygame.image.load("car5.png")
grass = pygame.image.load("grass.jpg")
strip1 = pygame.image.load("yellow_strip.png")
strip2  = pygame.image.load("strip.png") 
rekt = pygame.image.load("explosion.png")
menu = pygame.image.load("bg1.jpg")
pause = pygame.image.load("bg2.png")
title = pygame.image.load("title2.png")

# def show_file( filename ):  
#     if (sys.stdout.isatty()): 
#         if (os.environ['PAGER']): 
#             os.system('"{0}" "{1}"'.format( os.environ['PAGER'], filename )) 
#         else: 
#             os.system('less "{0}"'.format( filename )) 
#     else: 
#         if (os.environ['EDITOR']): 
#             os.system('"{0}" "{1}"'.format( os.environ['EDITOR'], filename )) 
#         else: 
#             os.system('xdg-open "{0}" || gedit "{0}"'.format(filename)) 


def rules():
    rule = True

    while rule:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                rule = False
                quit()
                sys.exit()
        font = pygame.font.SysFont(None, 60)
        font1 = pygame.font.SysFont(None, 40)
        rule_txt = font.render("Rules", True, (255,255,255))
        movement = font.render("Movement:-", True, (150,150,150))
        move_left = font1.render("Press left arrow key to move left.", True, (255,255,255))
        move_right = font1.render("Press right arrow key to move right.", True, (255,255,255))
        pause = font1.render("Press P to pause.", True, (255,255,255))
        dont_crash = font1.render("Don't crash into other cars.", True, (255,255,255))
        enjoy = font.render("Enjoy! :D", True, (255,255,255))
        screen.blit(menu, (0,0))  
        screen.blit(movement, (width/8 - 60, 90))
        screen.blit(move_left, (width/8 - 60, 130))
        screen.blit(move_right, (width/8 - 60, 160))
        screen.blit(pause, (width/8 - 60, 190))
        screen.blit(dont_crash, (width/8 - 60, 220))
        screen.blit(enjoy, (width/2 - 60, 260))
        screen.blit(rule_txt, (width/2 - 60, 50))
        pygame.display.update()

def main_menu():
    run = True
    pygame.mixer.init()
    pygame.mixer.music.load("main_menu.ogg")
    pygame.mixer.music.play(0)
    while run:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(menu, (0,0))    
        
        screen.blit(title, (135, -50))
        # font2 = pygame.font.SysFont(None,60)
        # menu_txt = font2.render("XTREAM_RACE", True, (200,0,0))
        # screen.blit(menu_txt, (width/2 - 140, 50))
        btn1 = pygame.draw.rect(screen, (0,119,0), (width/2 - 75, height/2 - 100, 150, 50))
        btn2 = pygame.draw.rect(screen, (200,200,0), (width/2 - 75, height/2, 150, 50))
        btn3 = pygame.draw.rect(screen, (119,0,0), (width/2 - 75, height/2 + 100, 150, 50))

        mouse = pygame.mouse.get_pos()
        
        click = pygame.mouse.get_pressed()
        


        if mouse[0] > (width/2 - 75) and mouse[0] < (width/2 + 75) and mouse[1] > (height/2 - 100) and mouse[1] < (height/2 - 50):
            pygame.draw.rect(screen, (0,255,0), (width/2 - 75, height/2 - 100, 150, 50))
            
            if click == (1,0,0):
                main()

        smalltext = pygame.font.SysFont("comicsacs", 40)
        btn1text = smalltext.render("START", True, (0,0,0))
        screen.blit(btn1text, ((width/2 - 42.5), (height/2 - 87.5)))
        
        if mouse[0] > (width/2 - 75) and mouse[0] < (width/2 + 75) and mouse[1] > (height/2) and mouse[1] < (height/2 + 50):
            pygame.draw.rect(screen, (255,255,0), (width/2 - 75, height/2, 150, 50))
            if click == (1,0,0):
                rules()

        btn2text = smalltext.render("RULES", True, (0,0,0))
        screen.blit(btn2text, ((width/2 - 42.5), (height/2 + 10)))

        if mouse[0] > (width/2 - 75) and mouse[0] < (width/2 + 75) and mouse[1] > (height/2 + 100) and mouse[1] < (height/2 + 150):
            pygame.draw.rect(screen, (255,0,0), (width/2 - 75, height/2 + 100, 150, 50))

            if click == (1,0,0):
                exit()
        btn3text = smalltext.render("QUIT", True, (0,0,0))
        screen.blit(btn3text, ((width/2 - 32.5), (height/2 + 110)))

        pygame.display.update()

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

def crashed():
    pygame.mixer.init()
    pygame.mixer.music.load("explosion.wav")
    pygame.mixer.music.play(0)
    a = 0
    game_over = screen.blit(rekt, ((width/2 - rekt.get_width()/2), height/2 - rekt.get_height()/2 ))
    while a <= 1:    
        game_over
        a += 1
        pygame.display.update()
        time.sleep(1)
    
    main_menu()

def score_board(passed, score):
    font = pygame.font.SysFont(None, 40)
    passed_ = font.render("Passed: " + str(passed), True, (255,255,255))
    score_ = font.render("Score: " + str(score), True, (0,0,0))
    screen.blit(passed_, (0, 10))
    screen.blit(score_, (0, 40))


def car(x,y):
    screen.blit(car1,(x,y))

def main():
    crash = False   
    x_change = 0
    obs_speed = 3
    obs_x = random.randrange((grass.get_width() + strip2.get_width()), (width - grass.get_width() - strip2.get_width() - 20))
    obs_y = -car2.get_height() - height
    obs = 0
    y_change = 0
    enemy_height = 142
    enemy_width = 76
    passed = 0
    score = 0 
    level = 0
    
    while not crash:
        screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash = True
         
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 30

                if event.key == pygame.K_RIGHT:
                    x_change += 30
            

        
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

            passed += 1
            score += 10

            if int(passed) % 10 == 0:
                level += 1
                obs_speed += 0.75
                font1 = pygame.font.SysFont(None, 60)
                level_txt = font1.render("Level: " + str(level), True, (0,0,0))
                screen.blit(level_txt, (width/2 - 60, 200))
                pygame.display.update()
                time.sleep(3)


        if (height - car1.get_height()) < obs_y + enemy_height:
            if (width/2 - car1.get_width()/2 + x_change) > obs_x and (width/2 - car1.get_width()/2 + x_change) < obs_x + 62 or (width/2 - car1.get_width()/2 + x_change)+car1.get_width() > obs_x and (width/2 - car1.get_width()/2 + x_change)+car1.get_width() < obs_x+62:
                crashed()
                pygame.display.update()

        score_board(passed, score)

        pygame.display.update()


        clock.tick(144)
main_menu()
main()
pygame.quit()
quit()

