import pygame, sys
from bullet import Bullet

def events(screen, gun, bullets):
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ranning = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # to right
            if event.key == pygame.K_d:
                gun.mright = True
            # to left
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # to right
            if event.key == pygame.K_d:
                gun.mright = False
            # to left
            elif event.key == pygame.K_a:
                gun.mleft = False

def screen_update(bg_color, screen, gun, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output_to_screen()
    pygame.display.flip()