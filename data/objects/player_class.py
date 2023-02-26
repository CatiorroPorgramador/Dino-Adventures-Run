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
        txtr = pygame.image.load('data/dino/dino_00.png').convert_alpha()
        self.image = transform_texture(txtr, [72, 72], True, False)
        self.run_sheet = [
            pygame.image.load(f'data/dino/dino_0{i}.png').convert_alpha() for i in range(4, 10)
        ]

        self.side = False  # left

        self.fuels = 0

        # animation
        self.motion:pygame.Vector2 = pygame.Vector2()
        self.in_movement = False

        self.frame = 0

        self.frame_speed = 6

        # rect
        self.rect = pygame.Rect(0, 0, 15*2.5, 17*2.5)
        

        self.speed = 5

        # jump
        self.gravity:float = 0.25

        self.on_ground: bool = True
        self.can_jump:bool = True
        self.can_fall:bool = False

        self.index_jump = 0
        self.jump_force = 20

    def movement_control(self):
        self.rect.x += self.motion.x
        self.rect.y += self.motion.y

        keys = pygame.key.get_pressed()
        
        self.motion.x = (int(keys[pygame.K_d]) - int(keys[pygame.K_a])) * self.speed
        
        self.motion.y += self.gravity
        
        self.in_movement = self.motion.x != 0

    def animation_control(self):
        if self.motion.x != 0:
            print(f'frame {self.frame}')
            self.frame += 1
            try:
                self.image = transform_texture(self.run_sheet[int(self.frame/self.frame_speed)], [15*2.5, 17*2.5], self.side, False)
                print(f'side = {self.side}\r')
            except Exception as e:
                self.frame = 0
                print(e)

    def update(self, *args):
        self.movement_control()
        self.animation_control()
