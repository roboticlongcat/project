import pygame
import sys
import random

from Classes import Wall, Ghost, Dot, Pacman, Score, Lives, Pause, Settings, variables

width, height = 800, 800


def get_cord_five(ar):
    fives = []
    for y in range(len(ar)):
        for x in range(len(ar[y])):
            if ar[y][x] == 5:
                fives.append([x, y])
    return fives


def get_cord_six(ar):
    six = []
    for y in range(len(ar)):
        for x in range(len(ar[y])):
            if ar[y][x] == 6:
                six.append([x, y])
    return six


def place_dots(ar, value_of_cord=2):
    dots = []
    for y in range(len(ar)):
        for x in range(len(ar[y])):
            if ar[y][x] == value_of_cord:
                dot = Dot.Dot(x, y, ar)
                dots.append(dot)
    return dots


def main():
    pygame.init()
    size = (width, height)
    screen = pygame.display.set_mode(size)
    settings = Settings.Settings()
    wall = Wall.Wall()
    score = Score.Score()
    lives = Lives.Lives()
    ar = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
        [1, 3, 1, 0, 1, 2, 1, 0, 0, 0, 1, 2, 1, 1, 2, 1, 0, 0, 0, 1, 2, 1, 0, 1, 3, 1],
        [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1],
        [1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 1, 5, 5, 5, 5, 1, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
        [1, 3, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 6, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 3, 1],
        [1, 2, 1, 0, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 0, 1, 2, 1],
        [1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1],
        [1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1],
        [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    dots = place_dots(ar)
    big_dots = place_dots(ar, 3)
    six = get_cord_six(ar)
    pacman = Pacman.Pacman(screen, 'pacman.png', six[0])
    fives = get_cord_five(ar)
    ghosts = [Ghost.Ghost('g1.png', fives[0]), Ghost.Ghost('g2.png', fives[1]), Ghost.Ghost('g3.png', fives[2]),
              Ghost.Ghost('g4.png', fives[3])]
    for ghost in ghosts:
        ghost.change_size_of_cell(ar)
    pacman.change_size_of_cell(ar)
    pause = Pause.Pause()
    is_menu = False
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause.show()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = event.pos
                # is_menu = pause.to_menu(mouse)
                pause.exit(mouse)
                pause.to_game(mouse)
            screen.fill(settings.background_color)
            pacman.mover(event, ar)
        screen.fill((0, 0, 0))
        if not pause.is_visible and not is_menu:
            for dot in dots:
                dot.draw(screen)
                if dot.collision(pacman):
                    dot.color = (0, 0, 0)
                    score.add_score_normal()
                    del dot
            for dot in big_dots:
                dot.draw_big(screen)
                if dot.collision(pacman):
                    dot.color_big = (0, 0, 0)
                    score.add_score_big()
                    del dot
            wall.draw(screen, ar)
            for ghost in ghosts:
                ghost.draw(screen)
                ghost.move(ar)
                if ghost.check_col_width_pac(pacman):
                    pacman.death()
                    lives.del_life()
                    if lives.lives == 0:
                        game_over = True
            # pacman.border_control(ar)
            pacman.draw()
            score.to_interface(screen)
            lives.to_interface(screen)
        pause.to_interface(screen)
        pygame.display.flip()
        pygame.time.wait(200)
    print('Ваш счет:', score.score)
    sys.exit()


if __name__ == '__main__':
    main()
