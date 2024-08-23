# Toolbox the Ancient Griefman
# or any of it's variants, really. This is a game from SS13 that is infamously easy to code.  In the interest of gatekeeping, don't look into my obscure and niche interests

import pygame
import random

atk = False
heal = False
charge = False

verbnamecandidates = ["Pulverize", "Destroy", "Defile", "Gib", "Crush", "Annoy", "Defeat", "Annihilate", "Obliterate", "Slaughter"]
adjnamecandidates = ["Ancient", "Monstrous", "Vile", "Pompous", "Ugly", "Revolting", "Terrible", "Awful","Deceptive", "Insane"]
nounnamecandidates = ["Griefman", "Grifter", "Spacer", "Moth", "Lich King", "Greyshirt", "Monster", "Vampire", "Opponent", "Melee Attacker"]
verbname = verbnamecandidates[random.randint(0,9)]
adjname = adjnamecandidates[random.randint(0,9)]
nounname = nounnamecandidates[random.randint(0,9)]
pygame.init()
title = (verbname + " The " + adjname + " " + nounname)

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 128)
X = 800
Y = 800
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption(title)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(title, True, white, blue)
textRect = text.get_rect()
textRect.center = (400, 100)

while True:
    display_surface.fill(blue)
    display_surface.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            atk = True
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()