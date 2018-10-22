# Demonstrate how to setup a director, scene, and layer
# Create a Scene class with a Layer field

# import the cocos package
import cocos

# import the director from cocos package
from cocos.director import director

class DemoLayer02(cocos.layer.Layer):
    def __init__(self):
        super(DemoLayer02, self).__init__()
        self.demo_layer_setup()

    # just some quick code to show the layer is working
    def demo_layer_setup(self):
        label = cocos.text.Label(
            "Demo 2",
            font_name = "Times New Roman",
            font_size = 32,
            anchor_x = "center", anchor_y = "center")
        label.position = 320, 240
        self.add(label)

class DemoScene02(cocos.scene.Scene):
    def __init__(self):
        super(DemoScene02, self).__init__()
        self.demo_layer_02 = DemoLayer02()
        self.add(self.demo_layer_02)


if __name__ == "__main__":
    # initialize the window (running this first is required)
    director.init()

    # initialize the demo scene
    demo_scene_02 = DemoScene02()

    # have the director run the demo scene
    director.run(demo_scene_02)
