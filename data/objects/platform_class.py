import pygame


class _platform(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/platforms/platform_00.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [50, 50])

        self.rect = pygame.Rect(100, 300, 50, 50)
