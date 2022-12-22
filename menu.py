'''
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/CatiorroPorgramador/Dino-Adventures-Run.git
git push -u origin main
'''

import pygame, sys
from os import getcwd, chdir, system
from random import randint, random

from data.objects.player_class import _player, transform_texture
from data.objects.platform_class import _platform
from data.objects.asteroid_class import _asteroid
from data.objects.coin_class import _coin
from data.objects.up_class import _up
from data.save import util

dirpath = getcwd()
sys.path.append(dirpath)

if getattr(sys, 'frozen', False):
    chdir(sys._MEIPASS)



def play():
    # init
    pygame.init()
    display = pygame.display.set_mode([900, 650])

    # framerate
    clock = pygame.time.Clock()

    # commons
    font = pygame.font.Font("data/Font.ttf", 21)

    loop = True

    # groups
    player_group = pygame.sprite.Group()
    platform_group = pygame.sprite.Group()
    fuel_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    # lists
    render_group = [
        player_group, platform_group, fuel_group, coin_group, asteroid_group
    ]
    update_group = [
        player_group, platform_group, fuel_group, coin_group, asteroid_group
    ]
    physics_group = [player_group, asteroid_group, fuel_group, coin_group]

    timers = [
        [0, 1, 100, '@'],
        [0, 0.6, 100, '%'],
        [0, 1, 100, '$'],
    ]

    maps = [
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        ],
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        ]

    ]

    # physics
    gravity = 2

    # player
    player = _player(player_group)

    counters = {
        'coins': 0,
    }

    index_particle = []

    def save_variables():
        file_name = 'variables/save.json'

        util.data_verification(file_name)

        data = util.read_json(file_name)

        data['coins'] += counters['coins']

        util.write_json(file_name, data)

        system('cd')

    def next_level():
        global index_particle

        if pygame.sprite.groupcollide(fuel_group, player_group, True, False):
            player.fuels += randint(10, 50)

            if player.fuels >= 100:
                player.fuels = 0

                for platform in platform_group:
                    platform.kill()

                for fuel in fuel_group:
                    fuel.kill()

                for asteroid in asteroid_group:
                    asteroid.kill()
                    index_particle.clear()

                for coin in coin_group:
                    coin.kill()

                player.jump = False

                player.rect.y = 10 * 50
                player.rect.centerx = display.get_width() / 2

                create_map(maps[randint(0, 3)])

    def particles(x, y):

        index_particle.append([[x, y], [randint(0, 20) / 10 - 1, -2],
                               randint(4, 6)])

        for p in index_particle:
            p[0][0] += p[1][0]
            p[0][1] += p[1][1]
            p[2] -= 0.1
            p[1][1] += 0.1
            pygame.draw.circle(display, (255, 255, 255),
                               [int(p[0][0]), int(p[0][1])], int(p[2]))
            if p[2] <= 0:
                index_particle.remove(p)

    def bigger_value(lst: list):
        i = 0

        for number in lst:
            if number.rect.x > i:
                i = number.rect.x

        print(i)

        return i

    def gravity_control():
        for group in physics_group:
            for obj in group:
                obj.rect.y += obj.gravity

    def create_map(mapping: list):
        for y, line in enumerate(mapping):
            for x, char in enumerate(line):
                if char == 1:
                    new_platform = _platform(platform_group)
                    new_platform.rect.x = x * 50
                    new_platform.rect.y = y * 50

    def platform_collisions():

        global first_platform, last_platform, index_particle
        a: list = []

        # Kill asteroid
        if pygame.sprite.groupcollide(platform_group, asteroid_group, True,
                                      True) or pygame.sprite.groupcollide(
            player_group, asteroid_group, True,
            True):
            index_particle = []

        # Show first and last platform
        if True:  # pygame.sprite.groupcollide(platform_group, asteroid_group, True, True):
            for p in platform_group:
                if p.rect.y < 600:
                    pass

                else:
                    pygame.draw.rect(display, (255, 255, 255),
                                     pygame.Rect(p.rect.x, p.rect.y, 50, 50))
                    first_platform = p.rect.x
                    break

            for p in platform_group:
                if p.rect.y < 600:
                    pass

                else:
                    a.append(p)
            last_platform = bigger_value(a)
            pygame.draw.rect(display, (255, 255, 255),
                             pygame.Rect(last_platform, 600, 50, 50))

            for group in physics_group:
                for o in group:
                    if not pygame.sprite.spritecollide(o, platform_group,
                                                       False, False):
                        pass
                    else:
                        o.rect.y -= o.gravity

    def collision_player():
        for p in platform_group:
            if player.rect.left == p.rect.right and p.rect.y + 60 > player.rect.y > p.rect.y - 60:
                player.rect.left += player.speed
                player.can_jump = True

            if player.rect.right == p.rect.left and p.rect.y + 60 > player.rect.y > p.rect.y - 60:
                player.rect.right -= player.speed
                player.can_jump = True

            if player.rect.bottom == p.rect.top and p.rect.x - 60 < player.rect.x < p.rect.x + 60:
                player.rect.bottom -= player.gravity
                player.can_jump = True

            if player.rect.top == p.rect.bottom and p.rect.x - 60 < player.rect.x < p.rect.x + 60:
                player.rect.top += player.gravity

            if pygame.sprite.collide_rect(p, player):
                player.jump = False

    def interface():
        global font
        # bg
        bg = pygame.Surface([200, 100])
        bg.fill((255, 255, 255))
        bg.set_alpha(50)

        # bar fuel
        pygame.draw.rect(display, (0, 255, 0),
                         [10, 10, player.fuels * 1.5, 15])
        pygame.draw.rect(display, (0, 0, 0), [10, 10, 100 * 1.5, 15], 5)

        # counters
        text_coin = {
            'text': font.render('coins: ' + str(counters['coins']), False, 0),
            'pos': [10, 30],
        }

        # blit
        display.blit(bg, (0, 0))

        display.blit(text_coin['text'], text_coin['pos'])

    def statistics():
        print('-=' * 24)
        print('fps: ', clock.get_fps())
        print('-' * 42)
        print('player can jump: ', player.can_jump)
        print('-' * 42)
        print('player rect', player.rect.x)

    def spawner():

        print(last_platform)

        for t in timers:
            t[0] += t[1]

            if t[0] > t[2]:
                if t[3] == '@':
                    new = _asteroid(display, asteroid_group)
                    try:
                        new.rect.x = randint(int(first_platform) - 50, last_platform + 50)
                        print(last_platform)
                    except ValueError:
                        new.kill()
                        print(ValueError)
                    t[0] = 0

                elif t[3] == '%':
                    new = _up(fuel_group)
                    try:
                        new.rect.x = randint(first_platform - 50,
                                             last_platform + 50)

                    except:
                        new.kill()
                    t[0] = 0

                elif t[3] == '$':
                    new = _coin(coin_group)
                    try:
                        new.rect.x = randint(first_platform - 50,
                                             last_platform + 50)
                    except:
                        new.kill()
                    t[0] = 0

    def die():
        global loop
        if pygame.sprite.groupcollide(player_group, asteroid_group, True, True):
            save_variables()
            loop = False

        if player.rect.y > 650:
            save_variables()
            loop = False

    def get():
        if pygame.sprite.groupcollide(player_group, coin_group, False, True):
            counters['coins'] += 1

    def kill_items():
        for group in render_group:
            for item in group:
                try:
                    item.hp -= 1

                    if item.hp <= 0:
                        item.kill()
                except:
                    pass

    def render_control():
        global i
        for group in render_group:
            group.draw(display)

        for a in asteroid_group:
            particles(a.rect.centerx, a.rect.y)

        interface()

    def update_control():
        for group in update_group:
            group.update()

        gravity_control()
        platform_collisions()
        collision_player()
        die()
        get()
        kill_items()
        spawner()
        next_level()

    # statistics()

    create_map(maps[0])

    # loop
    while loop:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("oi")

                    loop = False  # sys.exit()

                if event.key == pygame.K_SPACE:
                    player.jump = True

        # draw
        display.blit(
            transform_texture(pygame.image.load('data/backgrounds/01.png'),
                              [display.get_width(),
                               display.get_height()], False, False), (0, 0))

        render_control()

        # update
        update_control()

        pygame.display.update()


if __name__ == '__main__':
    pygame.init()

    display = pygame.display.set_mode([900, 650])

    font = pygame.font.Font("data/Font.ttf", 30)
    font2 = pygame.font.Font("data/Font.ttf", 21)

    util.data_verification('variables/save.json')
    data = util.read_json('variables/save.json')

    textures = [
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
    player_image = textures[0]
    player_pos = [0, 211 - 75]
    player_side = True
    frame = 0
    frame_speed = 6

    color_play_button = (235, 235, 235)

    online = 'off'

    text_coins = {
        'text': font.render('coins: ' + str(util.read_json('variables/save.json')['coins']), False, 0),
        'pos': [10, 10],
    }

    text_play = {
        'text': font.render('Press P to play', False, 0),
        'pos': [20, 211],
    }

    text_online = {
        'text': font.render('online: ' + online, False, 0),
        'pos': [720, 10],
    }

    text_online_screen = {
        'text': font2.render(online, False, 0),
        'pos': [470, 120]
    }

    text_author = {
        'text': font2.render('Made by Gustavo Cavalcanti (Catiorro Programador)', False, 0),
        'pos': [5, 630],
    }

    render = [
        text_coins, text_play, text_online, text_author, text_online_screen
    ]


    def background():
        #  dinos
        display.blit(transform_texture(player_image, [72, 72], False, False), (player_pos[0], player_pos[1]))

        #  press p for player
        pygame.draw.rect(display, color_play_button, pygame.Rect(10, 200, 300, 50))


    def display_online():
        bg = pygame.draw.rect(display, (235, 235, 235), pygame.Rect(450, 100, 400, 400))


    def animation():
        global frame, player_image, frame_speed, player_side

        if player_side:
            player_pos[0] += 3

        else:
            player_pos[0] -= 3

        if player_pos[0] > 300 - 72:
            player_side = False

        elif player_pos[0] < 10:
            player_side = True

        if True:
            frame += 1
            if frame >= frame_speed:
                player_image = transform_texture(textures[4], [72, 72], not player_side, False)

                if frame >= frame_speed * 2:
                    player_image = transform_texture(textures[5], [72, 72], not player_side, False)

                    if frame >= frame_speed * 3:
                        player_image = transform_texture(textures[6], [72, 72], not player_side, False)

                        if frame >= frame_speed * 4:
                            player_image = transform_texture(textures[7], [72, 72], not player_side, False)

                            if frame >= frame_speed * 5:
                                player_image = transform_texture(textures[8], [72, 72], not player_side, False)

                                if frame >= frame_speed * 6:
                                    player_image = transform_texture(textures[9], [72, 72], not player_side, False)

                                    if frame >= frame_speed + 4:
                                        frame = 0


    while True:
        text_coins['text'] =  font.render('coins: ' + str(util.read_json('variables/save.json')['coins']), False, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    color_play_button = (71, 228, 252)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:

                    play()

                    color_play_button = (235, 235, 235)


        display.fill((215, 215, 215))
        display_online()
        background()
        animation()

        for item in render:
            display.blit(item['text'], item['pos'])

        pygame.display.update()
        pygame.time.Clock().tick(60)
