import os
import random

import arcade

from RazboiInitialView import RazboiInitialView

SPRITE_SCALING = 5

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Razboi"


class Razboi(arcade.View):
    def __init__(self):
        super().__init__()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.flipped_cards = None

        self.carte_player_current = None
        self.carte_pc_current = None

        self.carti_player = None
        self.carti_pc = None

        self.p_carti_count = 0
        self.c_carti_count = 0

        self.name_to_index_texture = None

        self.timer = 0

    def setup(self):
        pachet = [(x, y) for x in range(2, 15) for y in ['F', 'I', 'R', 'T']]
        random.shuffle(pachet)

        self.carti_player = pachet[0:int(len(pachet) / 2)]
        self.carti_pc = pachet[int(len(pachet) / 2):]

        self.p_carti_count = len(self.carti_player)
        self.c_carti_count = len(self.carti_pc)

        self.flipped_cards = arcade.Sprite("Images/back.png", SPRITE_SCALING)
        self.flipped_cards.append_texture(arcade.load_texture("Images/back1.png"))
        self.flipped_cards.center_x = 100

        self.carte_player_current = arcade.Sprite("Images/back.png", SPRITE_SCALING)
        self.carte_player_current.center_x = 850
        self.carte_player_current.center_y = 150

        self.carte_pc_current = arcade.Sprite("Images/back1.png", SPRITE_SCALING)
        self.carte_pc_current.center_x = 850
        self.carte_pc_current.center_y = 450

        self.name_to_index_texture = dict()
        self.timer = 0
        i = 1
        for carte in pachet:
            # dictionar.update({key: aparitii})
            key = str(carte[0]) + str(carte[1])
            self.carte_player_current.append_texture(
                arcade.load_texture("Images/" + key + ".png"))
            self.carte_pc_current.append_texture(
                arcade.load_texture("Images/" + key + ".png"))
            self.name_to_index_texture.update({key: i})
            i += 1

        arcade.set_background_color(arcade.color.AMAZON)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE and (len(self.carti_pc) > 0 and len(self.carti_player) > 0):
            self.play_round()
        if symbol == arcade.key.R:
            self.setup()

    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def play_round(self):
        current_p_card = self.carti_player.pop(0)

        self.carte_player_current.set_texture(
            self.name_to_index_texture.get(str(current_p_card[0]) + str(current_p_card[1])))

        current_c_card = self.carti_pc.pop(0)

        self.carte_pc_current.set_texture(
            self.name_to_index_texture.get(str(current_c_card[0]) + str(current_c_card[1])))
        print("Player: " + str(current_p_card))
        print("Player: " + str(current_c_card))
        if current_p_card[0] == current_c_card[0]:
            self.razboi(current_p_card, current_c_card)

        elif current_p_card[0] > current_c_card[0]:
            self.carti_player.append(current_p_card)
            self.carti_player.append(current_c_card)
        else:
            self.carti_pc.append(current_c_card)
            self.carti_pc.append(current_p_card)
        print("Nr carti jucator/pc: " + str(len(self.carti_player)) + "/" + str(len(self.carti_pc)))

    def razboi(self, carte_p, carte_c):
        print("Player: " + str(self.carti_player))
        print("Pc: " + str(self.carti_pc))
        t = carte_p[0]
        soldati_p = list()
        soldati_c = list()
        while t > 0:
            if len(self.carti_pc) > 0:
                soldati_c.append(self.carti_pc.pop(0))
            if len(self.carti_player) > 0:
                soldati_p.append(self.carti_player.pop(0))

            print("Player: " + str(soldati_p[int(len(soldati_p) - 1)]))
            print("Computer: " + str(soldati_c[int(len(soldati_c) - 1)]))
            self.carte_player_current.set_texture(
                self.name_to_index_texture.get(
                    str(soldati_p[int(len(soldati_p) - 1)][0]) + str(soldati_p[int(len(soldati_p) - 1)][1])))
            self.carte_pc_current.set_texture(
                self.name_to_index_texture.get(
                    str(soldati_c[int(len(soldati_c) - 1)][0]) + str(soldati_c[int(len(soldati_c) - 1)][1])))
            # time.sleep(0.5)
            t -= 1
            if t == 0:
                if soldati_p[int(len(soldati_p) - 1)][0] == soldati_c[int(len(soldati_c) - 1)][0]:
                    if len(self.carti_pc) == len(self.carti_player) == 0:
                        winner = "none"
                        razboi_result = RazboiInitialView(self, soldati_c.copy(), soldati_p.copy(), carte_p, carte_c,
                                                          winner, SPRITE_SCALING)
                        # razboi_result.setup()
                        self.window.show_view(razboi_result)
                    t = soldati_p[len(soldati_p) - 1][0]
                else:
                    if soldati_p[int(len(soldati_p) - 1)][0] < soldati_c[int(len(soldati_c) - 1)][0]:
                        winner = "pc"
                    else:
                        winner = "player"
                    razboi_result = RazboiInitialView(self, soldati_c.copy(), soldati_p.copy(), carte_p, carte_c,
                                                      winner, SPRITE_SCALING)
                    # razboi_result.setup()
                    self.window.show_view(razboi_result)
                    if soldati_p[int(len(soldati_p) - 1)][0] < soldati_c[int(len(soldati_c) - 1)][0]:
                        soldati_c.extend(soldati_p)
                        self.carti_pc.extend(soldati_c)
                        self.carti_pc.append(carte_p)
                        self.carti_pc.append(carte_c)
                    else:
                        soldati_c.extend(soldati_p)
                        self.carti_player.extend(soldati_c)
                        self.carti_player.append(carte_p)
                        self.carti_player.append(carte_c)
        print("Player: " + str(self.carti_player))
        print("Pc:     " + str(self.carti_pc))

    def on_draw(self):
        arcade.start_render()

        cy = self.flipped_cards.center_x
        self.flipped_cards.set_texture(1)
        self.flipped_cards.center_y = 450
        for i in range(0, len(self.carti_pc)):
            self.flipped_cards.center_x += 10
            self.flipped_cards.draw()

        self.flipped_cards.set_texture(0)
        self.flipped_cards.center_y = 150
        self.flipped_cards.center_x = cy
        for i in range(0, len(self.carti_player)):
            self.flipped_cards.center_x += 10
            self.flipped_cards.draw()

        self.flipped_cards.center_x = cy

        self.carte_player_current.draw()
        self.carte_pc_current.draw()
        text_p = f"Player cards: {len(self.carti_player)}"
        text_c = f"Computer cards: {len(self.carti_pc)}"

        yp = 150 + self.flipped_cards.height / 2 + 10
        yc = 450 + self.flipped_cards.height / 2 + 10
        arcade.draw_text(text_p, 100, yp, arcade.color.WHITE, bold=True, font_size=16)
        arcade.draw_text(text_c, 100, yc, arcade.color.WHITE, bold=True, font_size=16)
        if len(self.carti_pc) <= 0 or len(self.carti_player) <= 0:
            text = ("Ai Castigat", arcade.color.BUD_GREEN) if len(self.carti_pc) <= 0 else (
                "Ai pierdut!", arcade.color.CORNELL_RED)
            if len(self.carti_pc) <= 0 and len(self.carti_player) <= 0:
                text = ("DRAW!", arcade.color.ORANGE_PEEL)
            arcade.draw_text(text[0], SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                             text[1], bold=True, font_size=52, anchor_x="center")

    def on_update(self, delta_time: float):
        if len(self.carti_pc) <= 0 or len(self.carti_player) <= 0:
            self.timer += delta_time
        if self.timer > 2:
            self.setup()


window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

game = Razboi()
game.setup()
window.show_view(game)
arcade.run()
