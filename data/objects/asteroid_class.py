import pygame


class _asteroid(pygame.sprite.Sprite):
    def __init__(self, display, *groups):
        super().__init__(*groups)

        self.display = display

        self.image = pygame.image.load('data/items/asteroid.png')
        self.image = pygame.transform.scale(self.image, [40, 40])
        self.image = pygame.transform.rotate(self.image, 100)

        self.rect = pygame.Rect(0, 0, 40, 40)

        self.gravity = 6

        self.hp = [0, 60 * 5]

    def update(self, *args):
        if self.hp[0] > self.hp[1]:
            self.kill()
