import pygame
import random
pygame.init()

turn = 0
decidetimer = 0
second_choice_is = True
last_move = False
running = True
resolution = (800,800)
white = (255,255,255)
black = (0,0,0)
grey = (128,128,128)
non_player_choice = False
player_choice = False
wallet = 30
screen = pygame.display.set_mode(resolution)
width = screen.get_width()
height = screen.get_height()
font = pygame.font.SysFont('comicsansms',20) 
bigfont = pygame.font.SysFont('comicsansms',33) 
button_width = 140
button_height = 40
button_x = (660)
button_y = (height - button_height) // 2
other_button_width = 140
second_players = ["Copycat","Bowler Hat Guy","Texan","Flowerhat","Spork Chumbly"]
current_second_player = second_players[0]
last_last_move = True
other_button_height = 40
other_button_x = (0)
other_button_y = (height - button_height) // 2
quit_button_width = 140
quit_button_height = 40
quit_button_x = (470 - quit_button_width)
quit_button_y = (height - button_height) // 2

def non_player_input():
    global second_choice_is, last_last_move, texan_trust
    if current_second_player == "Copycat":
        second_choice_is = last_last_move
    if current_second_player == "Bowler Hat Guy":
        second_choice_is = False
    if current_second_player == "Texan":
        if last_last_move == False:
            texan_trust = False
        if texan_trust == True:
            second_choice_is = True
        else:
            second_choice_is = False
    if current_second_player == "Flowerhat":
        second_choice_is = True
    if current_second_player == "Spork Chumbly":
        second_choice_is = bool(random.randint(0,1))
    blackbox_computes()
def blackbox_computes():
    global wallet
    if last_move == True:
        if second_choice_is == True:
            wallet += 1
        if second_choice_is == False:
            wallet -= 2
    if last_move == False:
        if second_choice_is == True:
            wallet += 3
        if second_choice_is == False:
            wallet = wallet
def quit():
    global running
    pygame.quit()
    running = False

def deciding():
    global decidetimer, turn
    if turn == 5:
        turn = 0
        decidetimer += 1
    current_second_player = second_players[decidetimer]

while running == True: 
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: 
            quit() 
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if quit_button_x <= mouse[0] <= quit_button_x + quit_button_width and quit_button_y <= mouse[1] <= button_y + quit_button_height:
                quit()
            if other_button_x <= mouse[0] <= other_button_x + other_button_width and other_button_y <= mouse[1] <= button_y + other_button_height:
                last_last_move = last_move
                last_move = False
                turn +=1
                deciding()
                non_player_input()
            if button_x <= mouse[0] <= button_x + button_width and button_y <= mouse[1] <= button_y + button_height:
                last_last_move = last_move
                last_move = True
                turn +=1
                deciding()
                non_player_input()
    if running == True:
        mouse = pygame.mouse.get_pos()
        screen.fill(black) 
        if button_x <= mouse[0] <= button_x + button_width and button_y <= mouse[1] <= button_y + button_height: 
            pygame.draw.rect(screen,white,[button_x,button_y,button_width,button_height]) 
        else: 
            pygame.draw.rect(screen,grey,[button_x,button_y,button_width,button_height])
        if other_button_x <= mouse[0] <= other_button_x + other_button_width and other_button_y <= mouse[1] <= other_button_y + other_button_height: 
            pygame.draw.rect(screen,white,[other_button_x,other_button_y,other_button_width,other_button_height]) 
        else: 
            pygame.draw.rect(screen,grey,[other_button_x,other_button_y,other_button_width,other_button_height]) 
        if quit_button_x <= mouse[0] <= quit_button_x + quit_button_width and quit_button_y <= mouse[1] <= quit_button_y + quit_button_height: 
            pygame.draw.rect(screen,white,[quit_button_x,quit_button_y,quit_button_width,quit_button_height]) 
        else: 
            pygame.draw.rect(screen,grey,[quit_button_x,quit_button_y,quit_button_width,quit_button_height]) 
        quittext = font.render('quit' , True , black) 
        screen.blit(quittext, (quit_button_x + 50, button_y)) 
        stealtext = font.render('Steal' , True , black) 
        screen.blit(stealtext, (other_button_x + 50, button_y)) 
        sharetext = font.render('Share' , True , black) 
        screen.blit(sharetext, (button_x + 50, button_y))
        sharetext = font.render(str(last_move), True ,white) 
        screen.blit(sharetext, (500, 0))
        sharetext = font.render(str(mouse), True , white) 
        screen.blit(sharetext, (0, 0))
        cointext = bigfont.render("Wallet: "+ str(wallet), True , white) 
        screen.blit(cointext, (327, 150)) 
        charactertext = font.render(str(current_second_player), True , white) 
        screen.blit(charactertext, (400, 600))
        pygame.display.update()