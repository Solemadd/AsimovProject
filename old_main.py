import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


# Découpez les sprites individuels de la feuille de sprite


global shooting
shooting = False
rotation= 1
a = 0
current_sprite_index = 0
sprite_position = (100, 100)
animation_speed = 60  # Vitesse de l'animation (plus la valeur est petite, plus l'animation est rapide)

camera = (0,0)



def update_sprite(action, a,r):
# CHARGE LE SPRITE EN FONCTION DE L'ACTION
    if action == 2: 
        sprite_sheet = pygame.image.load('ressources/Destroyer/Shot_1.png').convert_alpha()
        frames = 8
    elif action == 1: 
        sprite_sheet = pygame.image.load('ressources/Destroyer/Walk.png').convert_alpha()
        frames = 8
    else: 
        sprite_sheet = pygame.image.load('ressources/Destroyer/Idle.png').convert_alpha()
        frames = 5

    sprite_width = sprite_sheet.get_width() // frames
    sprite_height = sprite_sheet.get_height()
    sprite_images = [sprite_sheet.subsurface((i * sprite_width, 0, sprite_width, sprite_height)) for i in range(frames)]
    
    global current_sprite_index

    # Change de frame uniquement une frame sur 6
    if a == 0 : current_sprite_index = (current_sprite_index + 1) % len(sprite_images)
    if current_sprite_index >= len(sprite_images) : current_sprite_index = 0
    if r == 2: sprite_images[current_sprite_index] = pygame.transform.flip(sprite_images[current_sprite_index],True,False)
    if action == 2 and current_sprite_index == 7: shooting=True


    return sprite_images[current_sprite_index]

def update_camera():
    #Change la position des sprites de fond
    level = pygame.image.load('ressources/level/test.png').convert_alpha()
    background = pygame.image.load('ressources/bg/1/Night/3.png').convert_alpha()
    foreground = pygame.image.load('ressources/bg/3/Night/2.png').convert_alpha()

    
    

    new_width = 900
    ratio = new_width / background.get_width()
    new_height = int(background.get_height() * ratio)
    background= pygame.transform.scale(background, (new_width, new_height))
    ratio = new_width / foreground.get_width()
    new_height = int(foreground.get_height()*ratio)
    foreground= pygame.transform.scale(foreground,(new_width,new_height))

    

    return(level,background,foreground)

#pas encore utilisé
def SHOOT(action,a,r):
    if action == 3: obj_sheet = pygame.image.load('ressources/Destroyer/Charge_1.png').convert_alpha()
    up = False

# initialisation de quelques variables avant l'execution de la boucle
gravity = 1
falling = True
vertical_speed = 0
up = True
x = 100
y = 100
camx = 0
camy=50
running = True
while running:
    action =0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #compteur pour vérifier si il faut changer les frames du sprite joueur
    a = a + 1
    if a == 5: a = 0
    
    sprite_position = (x, y)
    camera = (camx,camy)
    keys = pygame.key.get_pressed()



    offset = (int(camx - x), int(camy - y))

    
    
    
    # Verifie si le robot est allumé et effectue les actions en conséquence
    if up == True:  
        if keys[pygame.K_RIGHT] and keys[pygame.K_UP] == False: 
            if x < 150 : x+=2
            if x > 150 : x = 150
            if x > 145 and camx>-500:camx = camx-2
            action = 1
            rotation=1

        if keys[pygame.K_LEFT] and keys[pygame.K_UP] == False: 
            if x > 50 : x-=2
            if x < 50 : x = 50
            if x < 55 and camx<0:camx = camx+2
            action = 1
            rotation=2
        
        if keys[pygame.K_UP]: 
            action = 2
    
    #initialise les sprite

    player = update_sprite(action,a,rotation)
    level = update_camera()[0]
    foreground = update_camera()[2]
    background = update_camera()[1]
    level_above = update_camera()[0]
    
    #creation des masques de collision
    player_mask = pygame.mask.from_surface(player)
    level_mask= pygame.mask.from_surface(level)
    level_above_mask = pygame.mask.from_surface(level_above)

    #gestion de la collision avec le sol et de la gravité

    #PARTIE QUI POSE PROBLEME
    y+=vertical_speed
    if player_mask.overlap(level_above_mask, offset):
        vertical_speed= 0
        if player_mask.overlap(level_mask,offset):
            y-=2
    else: vertical_speed = 5



    #affiche tout ce qu'on a calculé à l'écran
    screen.fill((0, 0, 0))

    
    screen.blit(background,(camera[0]/4, 0))
    screen.blit(foreground,(camera[0]/2+100, 50))
    screen.blit(level,camera)
    screen.blit(level_above,(camera[0],45))
    screen.blit(player, sprite_position)

    pygame.display.flip()

    clock.tick(animation_speed)

    

pygame.quit()
sys.exit()
