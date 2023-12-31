"""
Module to set up Nuke Knob Defaults.

I use it for some functions that can't be released with VP_Lord_of_Nodes.


Example of Knob Default №1:
nuke.knobDefault("AppendClip.label", "[value firstFrame] - [value lastFrame]")

Example of Knob Default №2:
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setExpression('[value first_frame]'), nodeClass='FrameRange')
nuke.addOnUserCreate(lambda:nuke.thisNode()['last_frame'].setExpression('[value last_frame]'), nodeClass='FrameRange')

Example of Knob Default #3:
nuke.addFormat("2048 858 1.0 Scope2048")  # example hot to add custom format to Root
nuke.knobDefault("Root.format", "Scope2048")  # example hot to set default format to Root
"""
