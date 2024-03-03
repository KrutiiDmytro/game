import pygame

class Bullet(pygame.sprite.Sprite):

    def __int__(self, screen, gun):
        #   создаём пулю в позиции пушки
        super(Bullet, self).__int__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 46, 230, 30
        self.speed = 1
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        # перемещение пули
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        #   рисуем пулю на экране
        pygame.draw.rect(self.screen, self.color, self.rect)