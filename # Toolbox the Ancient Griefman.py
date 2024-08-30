import pygame
import random
import sys

atk = False
heal = False
charge = False

verbnamecandidates = ["Pulverize", "Destroy", "Defile", "Gib", "Crush", "Annoy", "Defeat", "Annihilate", "Obliterate", "Slaughter"]
adjnamecandidates = ["Ancient", "Monstrous", "Vile", "Pompous", "Ugly", "Revolting", "Terrible", "Awful","Deceptive", "Insane"]
nounnamecandidates = ["Villain", "Vagabond", "Hobo", "Cyborg", "Lich King", "Janitor", "Monster", "Vampire", "Opponent", "Melee Attacker"]
verbname = verbnamecandidates[random.randint(0,9)]
adjname = adjnamecandidates[random.randint(0,9)]
nounname = nounnamecandidates[random.randint(0,9)]
pygame.init()
title = (verbname + " The " + adjname + " " + nounname)

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 128)
width = 800
height = 800
screen = [width, height]
mouse = (0,0,0)
smallfont = pygame.font.SysFont('Corbel',35) 
display_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(title, True, white, blue)
textRect = text.get_rect()
textRect.center = (width // 2, height // 4)  # Moved title text higher

while True: 
    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN: 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                pygame.quit() 
                sys.exit()
    
    display_surface.fill((60,25,123))
    mouse = pygame.mouse.get_pos() 
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(display_surface,white,[width/2,height/2,140,40]) 
    else: 
        pygame.draw.rect(display_surface,black,[width/2,height/2,140,40]) 
    display_surface.blit(text, textRect)
    pygame.display.update()