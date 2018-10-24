import cocos
from cocos.director import director
import pyglet
import random

class DemoEventDispatcher01(pyglet.event.EventDispatcher):
    def trigger_event(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.dispatch_event("on_demo_event_01", self)


class DemoLayer01(cocos.layer.Layer):
    def __init__(self):
        super(DemoLayer01, self).__init__()
        self.setup_layer()

    def setup_layer(self):
        self.label = cocos.text.Label(
            "Event Demo 1",
            font_name = "Times New Roman",
            font_size = 32,
            anchor_x = "center", anchor_y = "center")
        self.label.position = 320, 240
        self.add(self.label)

    def on_demo_event_01(self, disp):
        self.label.x = disp.x_pos
        self.label.y = disp.y_pos
        print(f"Move label to x: {self.label.x}, y: {self.label.y}")

class DemoScene01(cocos.scene.Scene):
    def __init__(self):
        super(DemoScene01, self).__init__()
        self.setup_scene()

    def setup_scene(self):
        self.demo_layer_01 = DemoLayer01()
        self.add(self.demo_layer_01)

        self.demo_event_dispatcher_01 = DemoEventDispatcher01()
        DemoEventDispatcher01.register_event_type("on_demo_event_01")
        self.demo_event_dispatcher_01.set_handler("on_demo_event_01", self.demo_layer_01.on_demo_event_01)

        self.schedule_interval(self.loop, 1)

    def loop(self, dt, *args, **kwargs):
        x_pos = random.randint(0, 640)
        y_pos = random.randint(0, 480)
        self.demo_event_dispatcher_01.trigger_event(x_pos, y_pos)


def run():
    director.init()
    demo_scene_01 = DemoScene01()
    director.run(demo_scene_01)

run()
