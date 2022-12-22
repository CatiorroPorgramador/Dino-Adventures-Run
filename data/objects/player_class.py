import pygame


def transform_texture(image, size: list, flip_x: bool, flip_y: bool):
    image = image.convert_alpha()

    return (
        pygame.transform.scale(
            pygame.transform.flip(image, flip_x, flip_y), size
        )
    )


class _player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        # texture
        self.textures = [
            pygame.image.load('data/dino/dino_00.png').convert_alpha(),
            pygame.image.load('data/dino/dino_01.png').convert_alpha(),
            pygame.image.load('data/dino/dino_02.png').convert_alpha(),
            pygame.image.load('data/dino/dino_03.png').convert_alpha(),
            pygame.image.load('data/dino/dino_04.png').convert_alpha(),
            pygame.image.load('data/dino/dino_05.png').convert_alpha(),
            pygame.image.load('data/dino/dino_06.png').convert_alpha(),
            pygame.image.load('data/dino/dino_07.png').convert_alpha(),
            pygame.image.load('data/dino/dino_08.png').convert_alpha(),
            pygame.image.load('data/dino/dino_09.png').convert_alpha(),
        ]

        self.image = transform_texture(self.textures[0], [72, 72], True, False)

        self.side = False  # left

        self.fuels = 0

        # animation
        self.in_movement = False

        self.frame = 0
        self.max_frame = 200

        self.frame_speed = 6

        # rect
        self.rect = pygame.Rect(400, 10 * 50, 60, 60)

        self.speed = 5

        # jump
        self.gravity: int = 4

        self.on_ground: bool = True
        self.can_jump = False

        self.index_jump = 0
        self.jump_force = 20

        self.jump = False

    def movement_control(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.side = False
            self.in_movement = True

        elif keys[pygame.K_d]:
            self.rect.x += self.speed
            self.side = True
            self.in_movement = True

        else:
            self.in_movement = False

    def animation_control(self):
        if self.in_movement:
            self.frame += 1
            if self.frame >= self.frame_speed:
                self.image = transform_texture(self.textures[4], [72, 72], not self.side, False)

                if self.frame >= self.frame_speed * 2:
                    self.image = transform_texture(self.textures[5], [72, 72], not self.side, False)

                    if self.frame >= self.frame_speed * 3:
                        self.image = transform_texture(self.textures[6], [72, 72], not self.side, False)

                        if self.frame >= self.frame_speed * 4:
                            self.image = transform_texture(self.textures[7], [72, 72], not self.side, False)

                            if self.frame >= self.frame_speed * 5:
                                self.image = transform_texture(self.textures[8], [72, 72], not self.side, False)

                                if self.frame >= self.frame_speed * 6:
                                    self.image = transform_texture(self.textures[9], [72, 72], not self.side, False)

                                    if self.frame >= self.frame_speed + 4:
                                        self.frame = 0

    def jump_control(self):
        if self.jump and self.can_jump:
            self.index_jump += 1

            self.gravity = -6

            if self.index_jump >= self.jump_force:
                self.jump = False
                self.index_jump = 0
                self.can_jump = False

        else:
            self.gravity: int = 2

    def update(self, *args):
        self.movement_control()
        self.animation_control()
        self.jump_control()
