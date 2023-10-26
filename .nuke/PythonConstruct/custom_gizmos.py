"""
Module to automatically add .gizmo and .nk files from /.nuke/Gizmos (and sub-folders) to Nuke Nodes menu.


"""


import nuke
import os


# CUSER CONFIG
_gizmos_folder_name = "Gizmos"
_nuke_menu_name = "Gizmos"


# VARIABLES
nuke_plugin_path = ((os.environ['HOME']) + '/.nuke').replace("\\", "/")
gizmos_path = nuke_plugin_path + "/" + _gizmos_folder_name


# FUNCTIONS


def get_menu_name(root):
    menu_name = root.replace("\\", "/").replace(gizmos_path, "")
    if menu_name:
        return _nuke_menu_name + menu_name
    return _nuke_menu_name


# MAIN CODE
for root, dirs, files in os.walk(gizmos_path):

    menu_name = get_menu_name(root)
    path_to_menu = nuke_plugin_path + "/" + menu_name

    nuke.pluginAddPath(path_to_menu)

    if nuke.env["gui"]:
        for file in files:
            if ".gizmo" in file:
                command_name = menu_name + "/" + file.replace(".gizmo", "")
                nuke.menu("Nodes").addCommand(command_name, "nuke.createNode('" + file + "')")

            elif ".nk" in file and os.path.basename(path_to_menu).lower() != 'toolsets':
                toolset_path = path_to_menu + "/" + file
                command_name = menu_name + "/" + file
                nuke.menu("Nodes").addCommand(command_name, "nuke.loadToolset('" + toolset_path + "')")
