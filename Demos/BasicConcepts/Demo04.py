import cocos
from cocos.director import director

class DemoLayer04(cocos.layer.Layer):
    def __init__(self):
        super(DemoLayer04, self).__init__()
        self.setup_layer()

        # experimenting with having something happen during a set interval
        self.schedule_interval(self.loop, 1)

    def setup_layer(self):
        self.label = cocos.text.Label(
            "Demo 4",
            font_name = "Times New Roman",
            font_size = 32,
            anchor_x = "center", anchor_y = "center")
        self.label.position = 320, 240
        self.add(self.label)

    def loop(self, dt, *args, **kwargs):
        old_y = self.label.position[1]
        old_x = self.label.position[0]
        new_x = old_x + 5
        self.label.position = new_x, old_y

director.init()
demo_layer_04 = DemoLayer04()
demo_scene_04 = cocos.scene.Scene(demo_layer_04)
director.run(demo_scene_04)
