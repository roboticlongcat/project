import pygame
import sys
import random

width, height = 800, 800


class Ghost:
    def __init__(self, path_of_ghost, start_cord):
        self.ghost_png = pygame.image.load(path_of_ghost)
        self.width_of_cell = 0
        self.height_of_cell = 0
        self.ghost_rect = self.ghost_png.get_rect()
        self.y = start_cord[1]
        self.x = start_cord[0]
        self.next_direction = 'up'

    # для начального обозначения размеров поля и призрака
    def change_size_of_cell(self, ar):
        self.width_of_cell = width // len(ar)
        self.height_of_cell = (height - 100) // len(ar[0])
        self.ghost_png = pygame.transform.scale(self.ghost_png, (self.width_of_cell, self.height_of_cell))
        self.ghost_rect = self.ghost_png.get_rect()

    def draw(self, screen):
        self.ghost_rect.x = self.x * self.width_of_cell
        self.ghost_rect.y = (self.y + 2) * self.height_of_cell
        screen.blit(self.ghost_png, self.ghost_rect)

    def move(self, ar):
        if self.y != len(ar) and self.x != len(ar) and self.y != 0 and self.x != 0:
            if self.next_direction == 'up':
                self.y -= 1
            elif self.next_direction == 'down':
                self.y += 1
            elif self.next_direction == 'left':
                self.x -= 1
            elif self.next_direction == 'right':
                self.x += 1

            if self.next_direction == 'up' and ar[self.y - 1][self.x] == 1:
                if ar[self.y][self.x - 1] == 1 and ar[self.y][self.x + 1] != 1:
                    self.next_direction = random.choice(['right'])
                elif ar[self.y][self.x - 1] != 1 and ar[self.y][self.x + 1] == 1:
                    self.next_direction = random.choice(['left'])
                elif ar[self.y][self.x - 1] != 1 and ar[self.y][self.x + 1] != 1:
                    self.next_direction = random.choice(['left', 'right'])
                elif ar[self.y][self.x - 1] == 1 and ar[self.y][self.x + 1] == 1:
                    self.next_direction = 'down'
            elif self.next_direction == 'left' and ar[self.y][self.x - 1] == 1:
                if ar[self.y - 1][self.x] == 1 and ar[self.y + 1][self.x] != 1:
                    self.next_direction = random.choice(['down'])
                elif ar[self.y - 1][self.x] != 1 and ar[self.y + 1][self.x] == 1:
                    self.next_direction = random.choice(['up'])
                elif ar[self.y - 1][self.x] != 1 and ar[self.y + 1][self.x] != 1:
                    self.next_direction = random.choice(['up', 'down'])
                elif ar[self.y - 1][self.x] == 1 and ar[self.y + 1][self.x] == 1:
                    self.next_direction = 'right'
            elif self.next_direction == 'right' and ar[self.y][self.x + 1] == 1:
                if ar[self.y - 1][self.x] == 1 and ar[self.y + 1][self.x] != 1:
                    self.next_direction = random.choice(['down'])
                elif ar[self.y - 1][self.x] != 1 and ar[self.y + 1][self.x] == 1:
                    self.next_direction = random.choice(['up'])
                elif ar[self.y - 1][self.x] != 1 and ar[self.y + 1][self.x] != 1:
                    self.next_direction = random.choice(['up', 'down'])
                elif ar[self.y - 1][self.x] == 1 and ar[self.y + 1][self.x] == 1:
                    self.next_direction = 'left'
            elif self.next_direction == 'down' and ar[self.y + 1][self.x] == 1:
                if ar[self.y][self.x - 1] == 1 and ar[self.y][self.x + 1] != 1:
                    self.next_direction = random.choice(['right'])
                elif ar[self.y][self.x - 1] != 1 and ar[self.y][self.x + 1] == 1:
                    self.next_direction = random.choice(['left'])
                elif ar[self.y][self.x - 1] != 1 and ar[self.y][self.x + 1] != 1:
                    self.next_direction = random.choice(['left', 'right'])
                elif ar[self.y][self.x - 1] == 1 and ar[self.y][self.x + 1] == 1:
                    self.next_direction = 'up'

    # проверка столкновения с пакманом
    def check_col_width_pac(self, pacman):
        if self.x == pacman.x and self.y == pacman.y:
            return True
        return False


# функция для получения цифры 5 и распределения координат призрака
def get_cord_five(ar):
    fives = []
    for y in range(len(ar)):
        for x in range(len(ar[y])):
            if ar[y][x] == 5:
                fives.append([x, y])
    return fives


def main():
    pygame.init()
    size = (width, height)
    screen = pygame.display.set_mode(size)
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
        [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
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
    fives = get_cord_five(ar)
    ghosts = [Ghost('Sprites/g1.png', fives[0]), Ghost('Spries/g2.png', fives[1]), Ghost('Sprites/g3.png', fives[2]),
              Ghost('Sprites/g4.png', fives[3])]
    for ghost in ghosts:
        ghost.change_size_of_cell(ar)
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill((0, 0, 0))
        for ghost in ghosts:
            ghost.draw(screen)
            ghost.move(ar)
        pygame.display.flip()
        pygame.time.wait(200)
    sys.exit()


if __name__ == '__main__':
    main()
