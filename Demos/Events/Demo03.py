# Create an application that displays a random phrase every 5 seconds.  Create a
# Scene class that contains a Layer object and an EventDispatcher object.  Have
# the Scene trigger an event every 5 seconds to display a new phrase.  The Scene
# will pass the new phrase to the EventDispatcher and the Layer will listen for
# the event and display the new phrase. 

import cocos
import pyglet
from cocos.director import director
import random

class AppDispatcher(pyglet.event.EventDispatcher):
    def trigger_event(self, phrase):
        self.phrase = phrase
        self.dispatch_event("on_exercise_event", self)

class AppLayer(cocos.layer.Layer):
    def __init__(self):
        super(AppLayer, self).__init__()
        self.setup_label("Event Demo")

    def setup_label(self, phrase):
        self.label = cocos.text.Label(
            phrase,
            font_name = "Times New Roman",
            font_size = 32,
            anchor_x = "center", anchor_y = "center")
        self.label.position = 320, 240
        self.add(self.label)

    def on_exercise_event(self, disp):
        self.remove(self.label)
        self.setup_label(disp.phrase)


class AppScene(cocos.scene.Scene):
    def __init__(self):
        super(AppScene, self).__init__()
        self.setup_scene()

    def setup_scene(self):
        self.app_layer = AppLayer()
        self.app_dispatcher = AppDispatcher()
        AppDispatcher.register_event_type("on_exercise_event")
        self.app_dispatcher.set_handler(
                "on_exercise_event", self.app_layer.on_exercise_event)
        self.add(self.app_layer)
        self.schedule_interval(self.loop, 1)

    def get_phrase(self):
        phrases = [
            "phrase 1",
            "phrase 2",
            "phrase 3",
            "phrase 4",
            "phrase 5"
        ]

        index = random.randint(0, 4)
        return phrases[index]

    def loop(self, dt, *args, **kwargs):
        phrase = self.get_phrase()
        self.app_dispatcher.trigger_event(phrase)

def run():
    director.init()
    app_scene = AppScene()
    director.run(app_scene)


if __name__ == "__main__":
    run()
