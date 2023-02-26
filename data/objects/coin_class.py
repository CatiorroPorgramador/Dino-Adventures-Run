import pygame


class _coin(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/items/coin.png')
        self.image = pygame.transform.scale(self.image, [30, 30])

        self.rect = pygame.Rect(0, 0, 30, 30)

        self.gravity = 4

        self.hp = 600
    
    def update(self, *args: any, **kwargs: any) -> None:
        self.rect.y += self.gravity