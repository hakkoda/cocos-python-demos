[[index|HOME]]

= BASIC CONCEPTS =

= CONTENTS =
    - [[#BASIC CONCEPTS|BASIC CONCEPTS]]
    - [[#CONTENTS|CONTENTS]]
        - [[#CONTENTS#SCENES|SCENES]]
        - [[#CONTENTS#DIRECTOR|DIRECTOR]]
        - [[#CONTENTS#LAYERS|LAYERS]]
        - [[#CONTENTS#CODE EXAMPLES|CODE EXAMPLES]]


== SCENES ==

*Scenes* - independent piece of the app

- the app can have multiple scenes
- only one scene is active at a time

Example:

Intro --> Menu --> Level 1 --> Cutscene --> etc...

Note: each scene can be defined as a separate app

A Scene is the root of a tree of CocosNodes:

{{{
           Scene
          /     \
         /       \
        /         \
       /           \
    Layer 1      Layer 2
     /  \          /  \
    /    \        /    \
sprite sprite  sprite sprite
}}}


== DIRECTOR ==

*Director* - handles going back and forth between scenes

- singleton object in a cocos2d app
- push, replacement, end of current scene is made by director
- resposible for initializing the main window

{{{python
import cocos
from cocos.director import director
}}}


== LAYERS ==

*Layer* - helps organize the scene in the back to front axis

{{{
+-------------+
|.............| Background Layer
|.............|
|...+-------------+
|...|.............| Animation Layer
+---|.............|
    |...+-------------+
    |...|.............| Menu Layer
    +---|.............|
        |.............|
        |.............|
        +-------------+
}}}
        
- Most programming time will be spent coding Layer sub-classes
- The Layer is where event handlers are defined

== CODE EXAMPLES ==

{{{python
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
}}}
