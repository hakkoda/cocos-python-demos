[[index|HOME]]

= Contents =
    - [[#Basic Concepts|Basic Concepts]]
        - [[#Basic Concepts#Scenes|Scenes]]
        - [[#Basic Concepts#Director|Director]]


= Basic Concepts =

== Scenes ==

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


== Director ==

*Director* - handles going back and forth between scenes

- singleton object in a cocos2d app
- push, replacement, end of current scene is made by director
- resposible for initializing the main window

{{{python
import cocos
from cocos.director import director
}}}


== Layers ==

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
