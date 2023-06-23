"""
Module to set up Nuke Hotkeys.

I use it for some functions that can't be released with VP_Lord_of_Nodes.


Example of clear cache hotkey:
nuke.menu('Nodes').addMenu('HotKeys').addCommand(name='@;Clear All Cache',
                                                 command='nukescripts.clearAllCaches()',
                                                 shortcut='shift+Delete')


"""
