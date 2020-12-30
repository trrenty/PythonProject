import os
import random

import arcade

SPRITE_SCALING = 5

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Razboi"

class Razboi(arcade.View):
    def __init__(self):
        super().__init__()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.flippedCards = None

        self.cartePlayerCurrent = None
        self.cartePCCurrent = None

        self.cartiPlayer = None
        self.cartiPc = None

        self.p_carti_count = 0
        self.c_carti_count = 0

        self.name_to_index_texture = None

        self.timer = 0

    def setup(self):
        pachet = [(x, y) for x in range(2, 15) for y in ['F', 'I', 'R', 'T']]
        random.shuffle(pachet)

        self.cartiPlayer = pachet[0:int(len(pachet) / 2)]
        self.cartiPc = pachet[int(len(pachet) / 2):]

        self.p_carti_count = len(self.cartiPlayer)
        self.c_carti_count = len(self.cartiPc)

        self.flippedCards = arcade.Sprite("Images/back.png", SPRITE_SCALING)
        self.flippedCards.append_texture(arcade.load_texture("Images/back1.png"))
        self.flippedCards.center_x = 100

        self.cartePlayerCurrent = arcade.Sprite("Images/back.png", SPRITE_SCALING)
        self.cartePlayerCurrent.center_x = 850
        self.cartePlayerCurrent.center_y = 150

        self.cartePCCurrent = arcade.Sprite("Images/back1.png", SPRITE_SCALING)
        self.cartePCCurrent.center_x = 850
        self.cartePCCurrent.center_y = 450

        self.name_to_index_texture = dict()
        self.timer = 0
        i = 1
        for carte in pachet:
            # dictionar.update({key: aparitii})
            key = str(carte[0]) + str(carte[1])
            self.cartePlayerCurrent.append_texture(
                arcade.load_texture("Images/" + key + ".png"))
            self.cartePCCurrent.append_texture(
                arcade.load_texture("Images/" + key + ".png"))
            self.name_to_index_texture.update({key: i})
            i += 1

        arcade.set_background_color(arcade.color.AMAZON)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE and (len(self.cartiPc) > 0 and len(self.cartiPlayer) > 0):
            self.playRound()
        if symbol == arcade.key.R:
            self.setup()

    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def playRound(self):
        currentPCard = self.cartiPlayer.pop(0)

        self.cartePlayerCurrent.set_texture(self.name_to_index_texture.get(str(currentPCard[0]) + str(currentPCard[1])))

        currentCCard = self.cartiPc.pop(0)

        self.cartePCCurrent.set_texture(self.name_to_index_texture.get(str(currentCCard[0]) + str(currentCCard[1])))
        print("Player: " + str(currentPCard))
        print("Player: " + str(currentCCard))
        if currentPCard[0] == currentCCard[0]:
            self.razboi(currentPCard, currentCCard)

        elif currentPCard[0] > currentCCard[0]:
            self.cartiPlayer.append(currentPCard)
            self.cartiPlayer.append(currentCCard)
        else:
            self.cartiPc.append(currentCCard)
            self.cartiPc.append(currentPCard)
        print("Nr carti jucator/pc: " + str(len(self.cartiPlayer)) + "/" + str(len(self.cartiPc)))


    def razboi(self, carteP, carteC):
        print("Player: " + str(self.cartiPlayer))
        print("Pc: " + str(self.cartiPc))
        t = carteP[0]
        soldatiP = list()
        soldatiC = list()
        while t > 0:
            if len(self.cartiPc) > 0: soldatiC.append(self.cartiPc.pop(0))
            if len(self.cartiPlayer) > 0: soldatiP.append(self.cartiPlayer.pop(0))

            print("Player: " + str(soldatiP[int(len(soldatiP) - 1)]))
            print("Computer: " + str(soldatiC[int(len(soldatiC) - 1)]))
            self.cartePlayerCurrent.set_texture(
                self.name_to_index_texture.get(
                    str(soldatiP[int(len(soldatiP) - 1)][0]) + str(soldatiP[int(len(soldatiP) - 1)][1])))
            self.cartePCCurrent.set_texture(
                self.name_to_index_texture.get(
                    str(soldatiC[int(len(soldatiC) - 1)][0]) + str(soldatiC[int(len(soldatiC) - 1)][1])))
            # time.sleep(0.5)
            t -= 1
            if t == 0:
                if soldatiP[int(len(soldatiP) - 1)][0] == soldatiC[int(len(soldatiC) - 1)][0]:
                    t = soldatiP[len(soldatiP) - 1][0]
                else:
                    if soldatiP[int(len(soldatiP) - 1)][0] < soldatiC[int(len(soldatiC) - 1)][0]:
                        soldatiC.extend(soldatiP)
                        self.cartiPc.extend(soldatiC)
                        self.cartiPc.append(carteP)
                        self.cartiPc.append(carteC)
                    else:
                        soldatiC.extend(soldatiP)
                        self.cartiPlayer.extend(soldatiC)
                        self.cartiPlayer.append(carteP)
                        self.cartiPlayer.append(carteC)
        print("Player: " + str(self.cartiPlayer))
        print("Pc:     " + str(self.cartiPc))

    def on_draw(self):
        arcade.start_render()

        cy = self.flippedCards.center_x
        self.flippedCards.set_texture(1)
        self.flippedCards.center_y = 450
        for i in range(0, len(self.cartiPc)):
            self.flippedCards.center_x += 10
            self.flippedCards.draw()

        self.flippedCards.set_texture(0)
        self.flippedCards.center_y = 150
        self.flippedCards.center_x = cy
        for i in range(0, len(self.cartiPlayer)):
            self.flippedCards.center_x += 10
            self.flippedCards.draw()

        self.flippedCards.center_x = cy

        self.cartePlayerCurrent.draw()
        self.cartePCCurrent.draw()
        textP = f"Player cards: {len(self.cartiPlayer)}"
        textC = f"Computer cards: {len(self.cartiPc)}"

        yp = 150 + self.flippedCards.height / 2 + 10
        yc = 450 + self.flippedCards.height / 2 + 10
        arcade.draw_text(textP, 100, yp, arcade.color.WHITE, bold=True, font_size=16)
        arcade.draw_text(textC, 100, yc, arcade.color.WHITE, bold=True, font_size=16)
        if len(self.cartiPc) <= 0 or len(self.cartiPlayer) <= 0:
            text = ("Ai Castigat", arcade.color.BUD_GREEN) if len(self.cartiPc) <= 0 else (
            "Ai pierdut!", arcade.color.CORNELL_RED)
            if len(self.cartiPc) <= 0 and len(self.cartiPlayer) <= 0:
                text = ("DRAW!", arcade.color.ORANGE_PEEL)
            arcade.draw_text(text[0], SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                             text[1], bold=True, font_size=52, anchor_x="center")

    def on_update(self, delta_time: float):
        if len(self.cartiPc) <= 0 or len(self.cartiPlayer) <= 0:
            self.timer += delta_time
        if self.timer > 2:
            self.setup()


window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

game = Razboi()
game.setup()
window.show_view(game)
arcade.run()