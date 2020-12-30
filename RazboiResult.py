import arcade

class RazboiResult(arcade.View):
    def __init__(self, razboiGame, soldatiPc, soldatiPlayer, winner, SPRITE_SCALING):
        super().__init__()
        self.razboiGame = razboiGame

        self.SPRITE_SCALING = SPRITE_SCALING

        self.soldatiPc = arcade.Sprite(scale=SPRITE_SCALING)
        self.soldatiPlayer = arcade.Sprite(scale=SPRITE_SCALING)

        self.soldatiPlayer.center_y = self.window.height * 1 / 4
        self.soldatiPlayer.center_x = 100
        self.soldatiPc.center_y = self.window.height * 3 / 4
        self.soldatiPc.center_x = 100

        i = len(self.soldatiPlayer.textures) - 1
        self.winner = winner

        for i in range(0, len(soldatiPlayer)):
            keyP = str(soldatiPlayer[i][0]) + str(soldatiPlayer[i][1])
            self.soldatiPlayer.append_texture(arcade.load_texture("Images/" + keyP + ".png"))

        for i in range(0, len(soldatiPc)):
            keyC = str(soldatiPc[i][0]) + str(soldatiPc[i][1])
            self.soldatiPc.append_texture(arcade.load_texture("Images/" + keyC + ".png"))

    def setup(self):
        # CENTER THE CARDS NICELY
        newScale = self.SPRITE_SCALING
        break_condition = False
        while not break_condition:
            cards_width = 0
            for i in range(0, len(self.soldatiPlayer.textures)):
                cards_width += 33 * newScale + 10
            if cards_width <= self.window.width - 100:
                print(cards_width)
                break_condition = True
            else:
                newScale -= 0.5
                print(newScale)
        self.soldatiPc.scale = newScale
        self.soldatiPlayer.scale = newScale

    def on_show(self):
        arcade.set_background_color(arcade.color.ARSENIC)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Carti folosite in Razboi ale Playerului:",
                         self.window.width / 2,
                         self.soldatiPlayer.center_y + self.soldatiPlayer.height / 2 + 10,
                         arcade.color.WHITE, anchor_x="center")
        arcade.draw_text("Carti folosite in Razboi ale PC-ului:",
                         self.window.width / 2,
                         self.soldatiPc.center_y + self.soldatiPc.height / 2 + 10,
                         arcade.color.WHITE,
                         anchor_x="center")
        px = self.soldatiPc.center_x
        cx = self.soldatiPlayer.center_x
        for i in range(0, len(self.soldatiPc.textures)):
            self.soldatiPc.set_texture(i)
            self.soldatiPc.draw()
            self.soldatiPc.center_x += self.soldatiPc.width + 10

        for i in range(0, len(self.soldatiPlayer.textures)):
            self.soldatiPlayer.set_texture(i)
            self.soldatiPlayer.draw()
            self.soldatiPlayer.center_x += self.soldatiPlayer.width + 10

        self.soldatiPlayer.center_x = px
        self.soldatiPc.center_x = cx
        arcade.draw_text("Apasa SPACE pentru a continua jocul",
                         self.window.width / 2,
                         10,
                         arcade.color.WHITE,
                         bold=True,
                         anchor_x="center")

        if self.winner == "player":
            winner = "Ai castigat razboiul!"
        elif self.winner == "pc":
            winner = "Computerul a castigat razboiul!"
        else:
            winner = "DRAW!"
        arcade.draw_text(winner,
                         self.window.width / 2,
                         self.window.height / 2,
                         arcade.color.CORNFLOWER_BLUE,
                         bold=True,
                         anchor_x="center", font_size=32)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.window.show_view(self.razboiGame)

