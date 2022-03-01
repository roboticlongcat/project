import pygame
import sys
import random

width, height = 800, 800

import Classes.variables


class Pacman:
    def __init__(self, screen, path_of_pacman, coords, color=(255, 255, 0)):
        self.start = coords
        self.x = coords[0]
        self.y = coords[1]
        self.alive = True
        self.lives_amount = 3
        self.score = 0
        self.width_of_cell = 0
        self.height_of_cell = 0
        self.block = True
        self.width = width
        self.height = height - 100
        self.x_shift = 0
        self.y_shift = 0
        self.surface = screen
        self.pacman_png = pygame.image.load(path_of_pacman)
        self.pacman_rect = self.pacman_png.get_rect()
        self.color = color
        self.rotate = 0

    def change_size_of_cell(self, ar):
        self.width_of_cell = self.width // len(ar)
        self.height_of_cell = self.height // len(ar[0])
        self.pacman_png = pygame.transform.scale(self.pacman_png, (self.width_of_cell, self.height_of_cell))
        self.pacman_rect = self.pacman_png.get_rect()

    def draw(self):
        self.pacman_rect.x = self.x * self.width_of_cell
        self.pacman_rect.y = (self.y + 2) * self.height_of_cell
        # print(self.y, self.height_of_cell, self.pacman_rect.y, self.height)
        # print(self.x, self.width_of_cell, self.pacman_rect.x, self.width)
        # ColorImage = Classes.variables.changeColor(self.pacman_png, self.color, Classes.variables.BLEND_RGBA_MULT, BLEND_RGBA_ADD)
        RotateImage = pygame.transform.rotate(self.pacman_png, self.rotate)
        self.surface.blit(RotateImage, self.pacman_rect)

    # def border_control(self, ar):
    #     if self.x + 1 == len(ar[0]):
    #         self.x = 1
    #     elif self.x - 1 == 0:
    #         self.x = len(ar[0]) - 2
    #     if self.pacman_rect.y >= self.height:
    #         self.y = 0
    #     elif self.y <= 0:
    #         self.y = self.height // self.height_of_cell

    def mover(self, event, ar):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ar[self.y - 1][self.x] == 1:
                    self.y_shift = 0
                else:
                    self.y_shift = -1
                self.x_shift = 0
                self.rotate = 90
            if event.key == pygame.K_DOWN:
                if ar[self.y + 1][self.x] == 1:
                    self.y_shift = 0
                else:
                    self.y_shift = 1
                self.x_shift = 0
                self.rotate = -90
            if event.key == pygame.K_LEFT:
                self.y_shift = 0
                if ar[self.y][self.x - 1] == 1:
                    self.x_shift = 0
                else:
                    self.x_shift = -1
                self.rotate = -180
            if event.key == pygame.K_RIGHT:
                self.y_shift = 0
                if ar[self.y][self.x + 1] == 1:
                    self.x_shift = 0
                else:
                    self.x_shift = 1
                self.rotate = 0
            self.x += self.x_shift
            self.y += self.y_shift

    def death(self):
        self.x = self.start[0]
        self.y = self.start[1]