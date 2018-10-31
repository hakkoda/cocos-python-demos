import cocos
from cocos.director import director
import random
from cocos.actions import *

class DemoScene(cocos.scene.Scene):
    def __init__(self):
        super(DemoScene, self).__init__()
        label = self.setup_label()
        layer = self.setup_layer(label)
        self.setup_scene(layer)

        label.do(MoveTo( (100, 100), 5 ) | RotateBy(360, 5))

    def setup_label(self):
        label = cocos.text.Label(
            "Action Demo 01",
            font_name = "Times New Roman",
            font_size = 32,
            anchor_x = "center", anchor_y = "center")
        label.position = 320, 240
        return label

    def setup_layer(self, label):
        layer = cocos.layer.Layer()
        layer.add(label)
        return layer

    def setup_scene(self, layer):
        self.add(layer)


def run():
    director.init()
    director.run(DemoScene())

if __name__ == "__main__":
    run()
