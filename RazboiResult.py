import arcade


class RazboiResult(arcade.View):
    def __init__(self, razboi_game, soldati_pc, soldati_player, winner, sprite_scaling):
        super().__init__()
        self.razboi_game = razboi_game

        self.sprite_scaling = sprite_scaling

        self.soldati_pc = arcade.Sprite(scale=sprite_scaling)
        self.soldati_player = arcade.Sprite(scale=sprite_scaling)

        self.soldati_player.center_y = self.window.height * 1 / 4
        self.soldati_player.center_x = 100
        self.soldati_pc.center_y = self.window.height * 3 / 4
        self.soldati_pc.center_x = 100

        i = len(self.soldati_player.textures) - 1
        self.winner = winner

        for i in range(0, len(soldati_player)):
            key_p = str(soldati_player[i][0]) + str(soldati_player[i][1])
            self.soldati_player.append_texture(arcade.load_texture("Images/" + key_p + ".png"))

        for i in range(0, len(soldati_pc)):
            key_c = str(soldati_pc[i][0]) + str(soldati_pc[i][1])
            self.soldati_pc.append_texture(arcade.load_texture("Images/" + key_c + ".png"))

    def setup(self):
        # CENTER THE CARDS NICELY
        new_scale = self.sprite_scaling
        break_condition = False
        while not break_condition:
            cards_width = 0
            for i in range(0, max(len(self.soldati_player.textures), len(self.soldati_pc.textures))):
                cards_width += 33 * new_scale + 10
            if cards_width <= self.window.width - 100:
                print(cards_width)
                break_condition = True
            else:
                new_scale -= 0.5
                print(new_scale)
        self.soldati_pc.scale = new_scale
        self.soldati_player.scale = new_scale

    def on_show(self):
        arcade.set_background_color(arcade.color.ARSENIC)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Carti folosite in Razboi ale Playerului:",
                         self.window.width / 2,
                         self.soldati_player.center_y + self.soldati_player.height / 2 + 10,
                         arcade.color.WHITE, anchor_x="center")
        arcade.draw_text("Carti folosite in Razboi ale PC-ului:",
                         self.window.width / 2,
                         self.soldati_pc.center_y + self.soldati_pc.height / 2 + 10,
                         arcade.color.WHITE,
                         anchor_x="center")
        px = self.soldati_pc.center_x
        cx = self.soldati_player.center_x
        for i in range(0, len(self.soldati_pc.textures)):
            self.soldati_pc.set_texture(i)
            self.soldati_pc.draw()
            self.soldati_pc.center_x += self.soldati_pc.width + 10

        for i in range(0, len(self.soldati_player.textures)):
            self.soldati_player.set_texture(i)
            self.soldati_player.draw()
            self.soldati_player.center_x += self.soldati_player.width + 10

        self.soldati_player.center_x = px
        self.soldati_pc.center_x = cx
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
            self.window.show_view(self.razboi_game)
