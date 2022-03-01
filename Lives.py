import pygame
import sys

width, height = 800, 800


class Lives:
    # класс создаёт три пакмана в интерфейсе, то есть три жизнм
    def __init__(self):
        self.lives = 3
        self.yellow = (255, 255, 0)

    # метод отнимает жизнь
    def del_life(self):
        if self.lives > 0:
            self.lives -= 1

    def to_interface(self, screen):
        for live in range(self.lives):
            point_x, point_y = width // 2 - live * 50 + 50, height - 30
            pygame.draw.circle(screen, self.yellow, (point_x, point_y), 20, 0)
            pygame.draw.polygon(screen, (0, 0, 0), [[point_x - 20, point_y - 20], [point_x, point_y],
                                                    [point_x - 20, point_y + 20]])


def main():
    pygame.init()
    size = (width, height)
    screen = pygame.display.set_mode(size)
    lives = Lives()
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill((0, 0, 0))
        lives.to_interface(screen)
        pygame.display.flip()
        pygame.time.wait(60)
    sys.exit()


if __name__ == '__main__':
    main()
