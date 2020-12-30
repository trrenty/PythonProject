import arcade

from RazboiResult import RazboiResult


class RazboiInitialView(arcade.View):
    def __init__(self, razboi_game, soldati_pc, soldati_player, carte_player, carte_pc, winner, sprite_scaling):
        super().__init__()
        url_carte_p = "Images/" + str(carte_player[0]) + str(carte_player[1]) + ".png"
        url_carte_c = "Images/" + str(carte_pc[0]) + str(carte_pc[1]) + ".png"

        self.sprite_scaling = sprite_scaling

        self.carte_player = arcade.Sprite(url_carte_p, sprite_scaling)
        self.carte_player.center_x = self.window.width / 3
        self.carte_player.center_y = self.window.height / 2

        self.carte_pc = arcade.Sprite(url_carte_c, sprite_scaling)
        self.carte_pc.center_x = self.window.width * 2 / 3
        self.carte_pc.center_y = self.window.height / 2

        self.soldati_pc = soldati_pc
        self.soldati_player = soldati_player
        self.razboi_game = razboi_game
        self.winner = winner

    def on_show(self):
        arcade.set_background_color(arcade.color.ARSENIC)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text("This is WAR!",
                         self.window.width / 2,
                         self.window.height - 100,
                         arcade.color.CORNELL_RED,
                         bold=True,
                         anchor_x="center", font_size=52)
        arcade.draw_text("Apasa SPACE pentru a continua jocul",
                         self.window.width / 2,
                         10,
                         arcade.color.WHITE,
                         bold=True,
                         anchor_x="center")

        arcade.draw_text("Cartea ta",
                         self.carte_player.center_x,
                         self.carte_player.center_y - self.carte_player.height / 2 - 25,
                         arcade.color.WHITE, anchor_x="center")

        arcade.draw_text("Carte PC",
                         self.carte_pc.center_x,
                         self.carte_pc.center_y - self.carte_pc.height / 2 - 25,
                         arcade.color.WHITE, anchor_x="center")

        self.carte_pc.draw()
        self.carte_player.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            razboi_result = RazboiResult(self.razboi_game, self.soldati_pc, self.soldati_player, self.winner, self.sprite_scaling)
            razboi_result.setup()
            self.window.show_view(razboi_result)
