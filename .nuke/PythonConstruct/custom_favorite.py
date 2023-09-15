"""
Module to add custom favourite menus to Nuke depending on operating system and version of Nuke.


Useful:
nuke.NUKE_VERSION_MAJOR  # return major version of Nuke
nuke.NUKE_VERSION_MINOR  # return minor version of Nuke
nuke.env ["WIN32"]  # return True if OS is Windows else False
nuke.env ["MACOS"]  # return True if OS is macOS else False
nuke.env ["LINUX"]  # return True if OS is Linux else False


"""


import nuke
import os


# get some paths
path_user = (os.environ['HOME']).replace("\\", "/")
path_desktop = path_user + "/Desktop"
path_nuke = path_user + '/.nuke'
path_icons = path_nuke + "/_other/icons"


# clear FileChooser_Favorites.pref
# FileChooser_Favorites = path_nuke + "/FileChooser_Favorites.pref"
# if os.path.isfile(FileChooser_Favorites):
#     file = open(FileChooser_Favorites, 'w')
#     file.close()


# USER CONFIG: add favorite directories
if nuke.env["WIN32"]:
    nuke.addFavoriteDir(name='Desktop', directory=path_desktop, icon=path_icons + '/Desktop.png')

elif nuke.env["MACOS"]:
    nuke.addFavoriteDir(name='Desktop', directory=path_desktop, icon=path_icons + '/Desktop.png')

elif nuke.env["LINUX"]:
    nuke.addFavoriteDir(name='Desktop', directory=path_desktop, icon=path_icons + '/Desktop.png')
