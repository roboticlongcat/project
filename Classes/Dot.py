import pygame
import sys
import random

width, height = 800, 800


class Dot:
    def __init__(self, x, y, ar, color=(255, 255, 0)):
        self.width_of_cell = width // len(ar)
        self.height_of_cell = (height-100) // len(ar[0])
        self.start_x = x
        self.start_y = y
        self.x = self.start_x * self.width_of_cell
        self.y = (self.start_y + 2) * self.height_of_cell
        self.color = color
        self.color_big = color
        self.r_big = 10
        self.r = 5
        self.is_ate = False

    def collision(self, pacman):
        if not self.is_ate:
            if pacman.x == self.start_x and pacman.y == self.start_y:
                self.is_ate = True
                return True
        return False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x + self.width_of_cell // 2, self.y + self.height_of_cell // 2),
                           self.r, 0)

    def draw_big(self, screen):
        pygame.draw.circle(screen, self.color_big, (self.x + self.width_of_cell // 2, self.y + self.height_of_cell // 2),
                           self.r_big, 0)
