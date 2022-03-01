from pygame import Color as color, key
from typing import Union


class Settings:
    def __init__(self, pacman_color='#fffe14',
                 ghosts_color={"first": "#fec341", "second": "#fb0001", "third": "#feb2fc", "fourth": "#10fcff",
                               "death": "#1411ff"}, cherry_color="#f25b68", background_color="#000000",
                 text_color="#b5feff", text_font="Arial", wall_color="#0100bc", music=True,
                 controls={'right': 'D', 'left': 'A', 'up': 'W', 'down': 'S'}) -> None:
        self.pacman_color = color(pacman_color)
        self.ghost_color = {"first": color(ghosts_color['first']), "second": color(ghosts_color['second']),
                            "third": color(ghosts_color['third']), "fourth": color(ghosts_color['fourth']),
                            "death": color(ghosts_color['death'])}
        self.cherry_color = color(cherry_color)
        self.background_color = color(background_color)
        self.text_color = color(text_color)
        self.text_font = text_font
        self.wall_color = color(wall_color)
        self.controls = controls
        # self.controls = {'right': key.key_code(controls['right']), 'left': key.key_code(controls['left']),
        #                  'up': key.key_code(controls['up']), 'down': key.key_code(controls['down'])}
        self.music = True

    def load_settings(self, sets: dict):
        for set in sets.keys():
            print(set, self.__dict__[set], sets[set])
            self.__dict__[set] = sets[set]
            print(set, self.__dict__[set], sets[set])

    def change_settings(self, setting_name, setting_value):
        if type(setting_value) == str:
            if setting_value.startswith('#'):
                self.__dict__[setting_name] = color(setting_value)
            else:
                self.__dict__[setting_name] = setting_value
        else:
            self.__dict__[setting_name] = setting_value

    def get_settings(self):
        return self.__dict__


def console_test():
    set = Settings()
    print(set.get_settings)
    set.change_settings('background_color', '#ffffff')
    print(set.get_settings)


if __name__ == "__main__":
    console_test()
