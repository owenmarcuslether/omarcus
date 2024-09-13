import pygame
pygame.init()

running = True
resolution = (800,800)
white = (255,255,255)
black = (0,0,0)
grey = (128,128,128)
non_player_choice = False
player_choice = False
coin_damage = 0
screen = pygame.display.set_mode(resolution)
width = screen.get_width()
height = screen.get_height()
font = pygame.font.SysFont('comicsansms',20) 

def player_input():
    pass

def non_player_input():
    pass

def quit():
    pygame.quit()
    running = False
while running == True: 
    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT: 
            quit() 
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                quit()
                break
    if running == False:
        break
    mouse = pygame.mouse.get_pos()
    screen.fill(black) 
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,white,[width/2,height/2,140,40]) 
    else: 
        pygame.draw.rect(screen,grey,[width/2,height/2,140,40]) 
    text = font.render('quit' , True , black) 
    screen.blit(text, (width/2+50,height/2)) 
    pygame.display.update()