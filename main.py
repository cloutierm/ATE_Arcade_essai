import arcade


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """

        arcade.start_render()

        arcade.draw_circle_filled(10, 10, 20, (255, 54, 34))


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Tutoriel Arcade")
    arcade.run()



main()
