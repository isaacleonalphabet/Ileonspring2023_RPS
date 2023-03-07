#File created by Isaac leon 
#import libraries

from time import sleep

from random import randint 

import pygame as pg

import os

game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

choices = ["rock", "paper", "scissors"]

# function that allows cpu to choose randomly and tells us if we win or lose 
def cpu_randchoice():
    choice = choices[randint(0,2)]
    print("computer randomly decides..." + choice)
    return choice


pg.init()
pg.mixer.init()
#The size of the images that will be displayed on the draw board, (such as RPS)
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors...")
clock = pg.time.Clock()
#The rock, papper,and sicssors images are beign programmed to be the exact same for the computer to fucuntion it and implement it as theirs. 
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
cpu_rock_image_rect = rock_image.get_rect()

paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
cpu_paper_image_rect = paper_image.get_rect()

scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
cpu_scissors_image_rect = scissors_image.get_rect()

start_screen= True
# We can choose and the cimputer will choose any of the given three choices for the RPS game 
player_choice = ""
cpu_choice = ""
running = True 


while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # ########## input ###########
        # HCI - human computer interaction...
        # keyboard, mouse, controller, vr headset
        if event.type == pg.MOUSEBUTTONUP:
            
            print(pg.mouse.get_pos()[0])
        
            print(pg.mouse.get_pos()[1])
            mouse_coords = pg.mouse.get_pos()
            # if pg.mouse.get_pos()[0] <= my_image_rect.width and pg.mouse.get_pos()[1] < my_image_rect.height:
            #     print("i clicked the rock")
            # else:
            #     print("no rock....")
            # This tells us that if we click on the iamge, the computer will randomly slelct one the three choices in the RPS pictures. 
            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords):
                print("you clicked on rock..")
                player_choice = "rock"
                cpu = cpu_randchoice()
                # call a function that gets the cpu choice...
            elif paper_image_rect.collidepoint(mouse_coords):
                print("you clicked on paper...")
                player_choice = "paper"       
                cpu = cpu_randchoice()
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("you clicked on scissors...")
                player_choice = "scissors"       
                cpu = cpu_randchoice()
            else:
                print("you didn't click on anything")

    ############ draw ###################
    screen.fill(BLACK)
    # screen.blit(scissors_image, scissors_image_rect)
    screen.blit(rock_image, rock_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(scissors_image, scissors_image_rect)
#This will guide us where and how big the images will be dispalyed on the drawing board. Y stays the smae, X is to sperate them
    if not start_screen and player_choice == "":
        rock_image_rect.y = 50
        rock_image_rect.x = 100
        paper_image_rect.y = 200
        paper_image_rect.x = 80
        scissors_image_rect.y = 80
        scissors_image.x = 50

#This will guide us where and how big the images will be dispalyed on the drawing board. Y stays the smae, X is to sperate them
    if start_screen: 
        rock_image_rect.x = 100
        rock_image_rect.y = 100
        paper_image_rect.x = 300
        paper_image_rect.y = 100
        scissors_image_rect.x = 500
        scissors_image_rect.y = 100

# This program the cimputer that if we choose one of the choices, and itrandmoly chooses a choice, the results will pop out on the temrinal
#This is how player wins 
    if player_choice == "rock":
        if cpu_choice == "scissors":
            print("You win")
            screen.blit(rock_image,rock_image_rect)
            screen.blit(scissors_image, cpu_scissors_image_rect)

    if player_choice == "paper" and cpu_choice == "rock":
        screen.blit(paper_image, paper_image_rect)
        screen.blit(rock_image, cpu_rock_image_rect)
        ("You WON!!!")
   
    if player_choice == "scissors" and cpu_choice == "paper":
        print("You win")
        screen.blit(scissors_image, scissors_image_rect)
        screen.blit(paper_image, paper_image_rect)
    
    
    #This is the process of how player looses
    if cpu_choice == "rock" and player_choice == "scissors":
        print ("YOU LOSE!!!")
        screen.blit(rock_image, cpu_rock_image_rect)
        screen.blit(scissors_image, scissors_image_rect)
    
    if cpu_choice == "paper" and player_choice == "rock":
        print("You just lost")
        screen.blit(paper_image, cpu_paper_image_rect)
        screen.blit(rock_image, rock_image_rect)
    
    if cpu_choice == "scissors" and player_choice == "paper":
        print("You just lost!")
        screen.blit(scissors_image, cpu_scissors_image_rect)
        screen.blit(paper_image, paper_image_rect)

    # This is for ties operations 
    if cpu_choice == "paper" and player_choice == "paper":
        print("You TIED")
        screen.blit(paper_image, cpu_paper_image_rect)

    if cpu_choice == "rock" and player_choice == "paper":
        print ("WE TIED")
        screen.blit(rock_image, cpu_rock_image_rect)
    
    if cpu_choice == "scissors" and player_choice == "scissors":
        print ("WE TIES")
        screen.blit(scissors_image, cpu_scissors_image_rect)
    pg.display.flip()

pg.quit()