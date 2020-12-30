import arcade

from RazboiResult import RazboiResult


class RazboiInitialView(arcade.View):
    def __init__(self, razboiGame, soldatiPc, soldatiPlayer, cartePlayer, cartePc, winner, SPRITE_SCALING):
        super().__init__()
        urlCarteP = "Images/" + str(cartePlayer[0]) + str(cartePlayer[1]) + ".png"
        urlCarteC = "Images/" + str(cartePc[0]) + str(cartePc[1]) + ".png"

        self.SPRITE_SCALING = SPRITE_SCALING

        self.cartePlayer = arcade.Sprite(urlCarteP, SPRITE_SCALING)
        self.cartePlayer.center_x = self.window.width / 3
        self.cartePlayer.center_y = self.window.height / 2

        self.cartePc = arcade.Sprite(urlCarteC, SPRITE_SCALING)
        self.cartePc.center_x = self.window.width * 2 / 3
        self.cartePc.center_y = self.window.height / 2

        self.soldatiPc = soldatiPc
        self.soldatiPlayer = soldatiPlayer
        self.razboiGame = razboiGame
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
                         self.cartePlayer.center_x,
                         self.cartePlayer.center_y - self.cartePlayer.height / 2 - 25,
                         arcade.color.WHITE, anchor_x="center")

        arcade.draw_text("Carte PC",
                         self.cartePc.center_x,
                         self.cartePc.center_y - self.cartePc.height / 2 - 25,
                         arcade.color.WHITE, anchor_x="center")

        self.cartePc.draw()
        self.cartePlayer.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            razboiResult = RazboiResult(self.razboiGame, self.soldatiPc, self.soldatiPlayer, self.winner, self.SPRITE_SCALING)
            razboiResult.setup()
            self.window.show_view(razboiResult)
