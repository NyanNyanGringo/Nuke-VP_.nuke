"""
Module helps to import 3DE4 lens to Nuke depending on
version of Nuke and operating system.


How to install module:
1. Add 3DE4 folder to your .nuke directory, like: "/.nuke/3DE4"

2. In "/.nuke/init.py" file add next commands:

> import nuke
> nuke.pluginAddPath("./3DE4")

3. If you want to update lenses:

- Got to: https://www.3dequalizer.com/?site=tech_docs&id=110216_01
- Download archieve "Lens Distortion Plugin Kit"
- From archieve "/compiled/nuke/..." copy [linux, osx, windows] folders to "/.nuke/3DE4/..." with replacement

"""

import nuke
import os


# add folder with 3DE4 lens to plugin path

def get_operating_system():
    if nuke.env["WIN32"]:
        return "windows"
    elif nuke.env["MACOS"]:
        return "osx"
    else:
        return "linux"


path = "./{operating_system}/Nuke{major}.{minor}".format(
    operating_system=get_operating_system(),
    major=str(nuke.NUKE_VERSION_MAJOR),
    minor=str(nuke.NUKE_VERSION_MINOR))
nuke.pluginAddPath(path)


# delete .zip, .tgz files from 3DE4 folder if exists


def delete_files_with_extensions_from_path(path, extensions):
    """
    Recursively go through path and delete files with certain extension
    :
    :param path: str
    :param extensions: list of strings
    :
    :return: None
    """
    if not os.path.exists(path):
        raise Exception("Path {} doesn't exists!".format(path))

    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            if file.split(".")[-1] in extensions:
                filepath = os.path.join(dirpath, file)
                os.remove(filepath)


this_path = os.path.dirname(os.path.abspath(__file__))
delete_files_with_extensions_from_path(path=this_path, extensions=["zip", "tgz"])