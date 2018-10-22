import cocos
from cocos.director import director

class DemoLayer03(cocos.layer.Layer):
    def __init__(self):
        super(DemoLayer03, self).__init__()
        self.demo_layer_setup()

    # just some quick code to show the layer is working
    def demo_layer_setup(self):
        label = cocos.text.Label(
            "Demo 3",
            font_name = "Times New Roman",
            font_size = 32,
            anchor_x = "center", anchor_y = "center")
        label.position = 320, 240
        self.add(label)

class DemoScene03(cocos.scene.Scene):
    def __init__(self):
        super(DemoScene03, self).__init__()
        self.add(DemoLayer03())

def run():
    director.init()
    demo_scene_03 = DemoScene03()
    director.run(demo_scene_03)


if __name__ == "__main__":
    run()
