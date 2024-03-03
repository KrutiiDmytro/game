import pygame

class Gun():
    def __init__(self, screen): # инициализация пушки
        self.screen = screen
        self.image = pygame.image.load('Image/pixil-frame-0.png')  # image load
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx   # местополместоположение  пушки
        self.center = float(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output_to_screen(self):
        # отрисовывание пушки
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        # обновление позиции пушки
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 4
        if self.mleft and self.rect.left > 0:
            self.center -= 4

        self.rect.centerx = self.center