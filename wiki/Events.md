[[index|HOME]]

= CONTENTS =
    - [[#EVENTS|EVENTS]]
        - [[#EVENTS#EVENT DISPATCHERS|EVENT DISPATCHERS]]
        - [[#EVENTS#AN EXAMPLE|AN EXAMPLE]]

----


= EVENTS =

    Cocos2D uses the pyglet Event Framework to handle events.  The following
    section demonstrates how to set up a simple event.


== EVENT DISPATCHERS ==

Objects that inherit from pyglet.event.EventDispatcher have the ability to
broadcast an event to any other object that is registered to listen for an
event.  

Some of the useful methods of the EventDispatcher are shown below:

{{{
                     +-----------------------------------+
                     | pyglet.event.EventDispatcher      |
                     +-----------------------------------+
                     | dispatch_event(event_type, *args) |
                     | set_handler(name, handler)        |
                     | remove_handler(name, handler)     |
                     | register_event_type(name)  static |
                     +-----------------------------------+
}}}

- *dispatch_event* - this method is used to broadcast an event to all listeners
- *push_handlers* - this method allows an object to be registered to an
  EventDispatcher object as a listener
- *remove_handlers* - this method is used to deregister a listener from
  EventDispatcher 
- *register_event_type* - this is a static method that tell the application
  which events an EventDispatcher instance can broadcast
  
  
== AN EXAMPLE ==

{{local:../wiki_html/img/Events-Example.gif}}

{{{class="brush: python prettyprint"
import cocos
from cocos.director import director
import pyglet
import random

# This is the Dispatcher object definition for this demo.  Note that the object
# will inherit from pyglet.event.EventDispatcher.  
class SampleDispatcher(pyglet.event.EventDispatcher):
    def trigger_event(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        # This class will broadcast the "on_sample_event" when the trigger_event
        # method is called.  Note that the object itself is passed into the
        # dispatch_event method.  In this case, x_pos and y_pos will be
        # available to the listener when this event is broadcast.
        self.dispatch_event("on_sample_event", self)


# This is the object definition for the layer that will be used in this demo.
# This layer will become a listener for the "on_sample_event".
class SampleLayer(cocos.layer.Layer):
    def __init__(self):
        super(SampleLayer, self).__init__()
        self.setup_layer()

    def setup_layer(self):
        self.label = cocos.text.Label(
            "Event Demo",
            font_name = "Times New Roman",
            font_size = 32,
            anchor_x = "center", anchor_y = "center")
        self.label.position = 320, 240
        self.add(self.label)

    # Because this layer will become a listener for the "on_sample_event", a
    # method must be defined with that event's name.  Note that the dispatcher
    # object will be passed back to the layer in this method.  Any properties
    # avialable in the dispatcher object will be available to the layer.  For
    # this particular method, the label for this layer will move to a new,
    # randomly generated x,y coordinate.
    def on_sample_event(self, disp):
        self.label.x = disp.x_pos
        self.label.y = disp.y_pos
        print(f"Move label to x: {self.label.x}, y: {self.label.y}")

# This is the object definition for the scene in this demo.  Note that
# SampleLayer and SampleDispatcher are properties of the scene and the scene
# will handle setting up registration of the "on_sample_event".  
class SampleScene(cocos.scene.Scene):
    def __init__(self):
        super(SampleScene, self).__init__()
        self.setup_scene()

    def setup_scene(self):
        self.sample_layer = SampleLayer()
        self.add(self.sample_layer)

        # Setup the SampleDispatcher object and register the event type
        # "on_sample_event".
        self.sample_dispatcher = SampleDispatcher()
        SampleDispatcher.register_event_type("on_sample_event")

        # The SampleLayer object now becomes a listener for the "on_sample_event"
        self.sample_dispatcher.push_handlers(self.sample_layer)

        # Some demo code to allow the scene to trigger the "on_sample_event" to
        # be broadcasted
        self.schedule_interval(self.loop, 1)

    def loop(self, dt, *args, **kwargs):
        x_pos = random.randint(0, 640)
        y_pos = random.randint(0, 480)
        self.sample_dispatcher.trigger_event(x_pos, y_pos)


def run():
    director.init()
    sample_scene = SampleScene()
    director.run(sample_scene)

run()
}}}


== STUDY QUESTIONS ==

:question-01:
What method is used by the pyglet.event.EventDispatcher class to broadcast an
event? [[#question-01-solution|answer]]

:question-02:
What method is used to add a new listeners to a pyglet.event.EventDispatcher
object? [[#question-02-solution|answer]]

:question-0X:
Create an application that displays a random phrase every 5 seconds.  Create a
Scene class that contains a Layer object and an EventDispatcher object.  Have
the Scene trigger an event every 5 seconds to display a new phrase.  The Scene
will pass the new phrase to the EventDispatcher and the Layer will listen for
the event and display the new phrase. [[#question-0X-solution|solution]]


== SOLUTIONS ==

:question-01-solution:
dispatch_event

:question-02-solution:
set_handler

:question-0X-solution:
TODO
