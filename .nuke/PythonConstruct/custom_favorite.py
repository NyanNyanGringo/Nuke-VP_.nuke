"""
Module to add custom favourite menus to Nuke depending on operating system and version of Nuke.


Useful:
nuke.NUKE_VERSION_MAJOR  # return major version of Nuke
nuke.NUKE_VERSION_MINOR  # return minor version of Nuke
nuke.env ["WIN32"]  # return True if OS is Windows else False
nuke.env ["MACOS"]  # return True if OS is macOS else False
nuke.env ["LINUX"]  # return True if OS is Linux else False


"""


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


# VARIABLES
path_user = (os.environ['HOME']).replace("\\", "/")
path_desktop = path_user + "/Desktop"
path_nuke = path_user + '/.nuke'
path_icons = path_nuke + "/_other/icons"


# CLEAR FileChooser_Favorites.pref
FileChooser_Favorites = path_nuke + "/FileChooser_Favorites.pref"
if os.path.isfile(FileChooser_Favorites):
    file = open(FileChooser_Favorites, 'w')
    file.close()


# FUNCTIONS
def auto_add_path_to_favourite(path):
    if not os.path.exists(path):
        nuke.tprint("custom_favorite.py: My Lord, path " + str(path) + " doesn't exists! Can't create auto dirs for this path.")
        return

    for file in os.listdir(path):

        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):

            nuke.addFavoriteDir(name=file, directory=file_path)


# USER CONFIG: add favorite directories
if nuke.env["WIN32"]:
    nuke.addFavoriteDir(name='Desktop', directory=path_desktop, icon=path_icons + '/Desktop.png')

elif nuke.env["MACOS"]:
    nuke.addFavoriteDir(name='Desktop', directory=path_desktop, icon=path_icons + '/Desktop.png')

    MACOS_AUTO_ADD_DIRS = []

elif nuke.env["LINUX"]:
    nuke.addFavoriteDir(name='Desktop', directory=path_desktop, icon=path_icons + '/Desktop.png')

    LINUX_AUTO_ADD_DIRS = []


# USER CONFIG: automatically add favorite directories
if nuke.env["WIN32"]:
    dirs_to_add_files_from = []
    [auto_add_path_to_favourite(path) for path in dirs_to_add_files_from]

elif nuke.env["MACOS"]:
    dirs_to_add_files_from = []
    [auto_add_path_to_favourite(path) for path in dirs_to_add_files_from]

elif nuke.env["LINUX"]:
    dirs_to_add_files_from = []
    [auto_add_path_to_favourite(path) for path in dirs_to_add_files_from]
