# Demonstrate how to setup a director, scene, and layer

# import the cocos package
import cocos

# import the director from cocos package
from cocos.director import director

class DemoLayer01(cocos.layer.Layer):
    def __init__(self):
        super(DemoLayer01, self).__init__()
        self.demo_layer_setup()

    # just some quick code to show the layer is working
    def demo_layer_setup(self):
        label = cocos.text.Label(
            "This is the demo layer",
            font_name = "Times New Roman",
            font_size = 32,
            anchor_x = "center", anchor_y = "center")
        label.position = 320, 240
        self.add(label)


if __name__ == "__main__":
    # initialize the window (running this first is required)
    director.init()

    # initialize a demo layer
    demo_layer_01 = DemoLayer01()

    # create a scene that contains a demo layer
    demo_scene_01 = cocos.scene.Scene(demo_layer_01)

    # have the director run the demo scene
    director.run(demo_scene_01)
