"""
Module to set up plugin path.


Use to control import depending on Nuke version and operating system:
- nuke.NUKE_VERSION_MAJOR  # return major version of Nuke
- nuke.NUKE_VERSION_MINOR  # return minor version of Nuke
- nuke.env ["WIN32"]  # return True if OS is Windows else False
- nuke.env ["MACOS"]  # return True if OS is macOS else False
- nuke.env ["LINUX"]  # return True if OS is Linux else False


"""


import nuke


# set up plugin path for any versions of Nuke and operating system:
nuke.pluginAddPath("./Python/3DE4")


# set up plugin path for certain versions of Nuke and operating systems:
if nuke.NUKE_VERSION_MAJOR <= 12:
    pass

elif nuke.NUKE_VERSION_MAJOR >= 13:
    pass
