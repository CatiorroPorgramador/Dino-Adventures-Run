import pygame


class _up(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.transform.scale(
            pygame.image.load('data/items/fuel.png'), [30, 30]
        )

        self.gravity = 4

        self.rect = pygame.Rect(50 * 5, 0, 30, 30)

    def update(self, *args: any, **kwargs: any) -> None:
        self.rect.y += self.gravity