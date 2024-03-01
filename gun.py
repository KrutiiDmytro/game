import pygame

class Gun():
    def __init__(self, screen): # инициализация пушки
        self.screen = screen
        self.image = pygame.image.load('Image/pixil-frame-0.png')  # image load
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx  # местополместоположение  пушки
        self.rect.bottom = self.screen_rect.bottom

    def output_to_screen(self):
        self.screen.blit(self.image, self.rect)