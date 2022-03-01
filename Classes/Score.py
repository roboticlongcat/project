import pygame

pygame.font.init()


class Score:
    def __init__(self, font_family='Arial', color=(0, 255, 0)):
        self.text_form = pygame.font.SysFont(font_family, 30, True)
        self.score = 0
        self.color = color

    def add_score_normal(self):
        # начисляет очки за обычные зёрна
        self.score += 10

    def add_score_big(self):
        # начисляет очки за большие зёрна
        self.score += 50

    # def change_settings(self, settings: Settings):
    #     self.color = settings.text_color
    #     self.font_family = settings.text_font

    def to_interface(self, screen):
        ts = self.text_form.render('Score: ' + str(self.score), False, self.color)
        screen.blit(ts, (30, 10))
