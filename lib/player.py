import pygame


    # Je n'arrive pas à mettre le code sur deux fichiers différents ça me saoul

def PLAYER(action,aim,screen):
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
    if a == 0 : current_sprite_index = (current_sprite_index + 1) % len(sprite_images)
    if current_sprite_index >= len(sprite_images) : current_sprite_index = 0
    if r == 2: sprite_images[current_sprite_index] = pygame.transform.flip(sprite_images[current_sprite_index],True,False)
    if action == 2 and current_sprite_index == 7: shooting=True
    return sprite_images[current_sprite_index]

    screen.blit(update_sprite(action,a,rotation), sprite_position)

    