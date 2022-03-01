from pygame import draw, font, image, transform, init, display, time, QUIT as quit, K_ESCAPE, KEYDOWN, event as events, MOUSEBUTTONDOWN
from sys import exit, path as syspath
from os import path as ospath

syspath.append(ospath.dirname(ospath.dirname(ospath.realpath(__file__))))
from Classes.Settings import Settings
from Classes.variables import width, height

class Ball:
    def __init__(self):
        self.width = width
        self.height = height
        self.x = self.width // 2
        self.y = self.height // 2
        self.dx = 6
        self.dy = 5

    def draw(self, screen):
        draw.circle(screen, (255, 255, 0), (self.x, self.y), 30, 0)
        self.x += self.dx
        self.y += self.dy

    def check_collision(self):
        if self.x > self.width - 15 or self.x < 15:
            self.dx *= -1
        if self.y > self.height - 15 or self.y < 15:
            self.dy *= -1


class Pause:
    def __init__(self, font_family='Arial', background_color=(0,0,0), text_color=(255,255,0)):
        self.is_visible = False
        self.font_family = font_family
        self.font_format = font.SysFont(self.font_family, 20, True)
        self.data = 'MENU'
        self.yellow = (255, 255, 0)
        self.text_color = text_color
        self.ts = self.font_format.render(self.data, False, self.text_color)
        self.pos_of_ts = (33, 80)
        self.background_color = background_color
        self.width = width
        self.height = height
        self.background_coordinates = (0, 0, self.width, self.height)
        self.pause_coordinates = [[self.width // 2 + 50, self.height // 2], [self.width // 2 - 50,
                                                                             self.height // 2 + 50],
                                  [self.width // 2 - 50, self.height // 2 - 50]]
        self.point_x, self.point_y = 60, 50
        self.close = image.load('close.png')
        self.close = transform.scale(self.close, (50, 50))
        self.close_rect = self.close.get_rect()
        self.close_rect.x = self.width - 60
        self.close_rect.y = 25
        self.menu_button = None
        self.close_button = None
        self.pause_button = None

    def show(self):
        if not self.is_visible:
            self.is_visible = True
        else:
            self.is_visible = False

    def to_interface(self, screen):
        if self.is_visible:
            draw.rect(screen, self.background_color, self.background_coordinates, 0)
            self.pause_button = draw.polygon(screen, self.yellow, self.pause_coordinates)
            # draw.circle(screen, self.yellow, (self.point_x, self.point_y), 20, 0)
            # draw.polygon(screen, (0, 0, 0), [[self.point_x - 20, self.point_y - 20], [self.point_x,
                                                                                            # self.point_y],
                                                   # [self.point_x - 20, self.point_y + 20]])
            # screen.blit(self.ts, self.pos_of_ts)
            # self.menu_button = draw.rect(screen, (0, 0, 0), (20, 20, 90,
                                                                    # 100), 1)
            self.close_button = screen.blit(self.close, self.close_rect)

    # переход в меню
    def to_menu(self, mouse):
        if self.menu_button:
            if self.menu_button.collidepoint(mouse):
                self.is_visible = False
                return True
            return False
        return False

    # выход из игры
    def exit(self, mouse):
        if self.close_button:
            if self.close_button.collidepoint(mouse):
                exit()

    def to_game(self, mouse):
        if self.pause_button:
            if self.pause_button.collidepoint(mouse):
                self.is_visible = False


def test():
    font.init()
    init()
    size = (width, height)
    screen = display.set_mode(size)
    settings = Settings()
    pause = Pause(settings.text_font, settings.background_color, settings.text_color)
    ball = Ball()
    is_menu = False
    game_over = False
    while not game_over:
        for event in events.get():
            if event.type == quit:
                game_over = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause.show()
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                is_menu = pause.to_menu(mouse)
                pause.exit(mouse)
                pause.to_game(mouse)
        screen.fill(settings.background_color)
        # какой-то код
        if is_menu:
            # методы, предназначенные для меню
            pass
        if not pause.is_visible and not is_menu:
            ball.draw(screen)
            ball.check_collision()

        pause.to_interface(screen)
        display.flip()
        time.wait(60)
    exit()


if __name__ == '__main__':
    test()
