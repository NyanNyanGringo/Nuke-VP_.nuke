"""
Module to add custom autolabels for nodes. Example of Merge2 autolabel:

import nuke


def set_merge_autolabel():
    node = nuke.thisNode()

    autolabel = node["operation"].value().title()  # Set operation as label

    bchannels = node["Bchannels"].value()
    if bchannels not in ["rgba", "rgb", "r", "g", "b"]:
        autolabel = bchannels  # If custom channel in Merge2 -> replace label with this channel

    # check if Merge2.label has any value and try to convert it to TCL else just add string
    if node["label"].value():
        try:
            autolabel += "\n" + nuke.tcl("subst", node["label"].value())
        except:
            autolabel += "\n" + node["label"].value()

    return autolabel


nuke.addAutolabel(set_merge_autolabel, nodeClass="Merge2")  # add autolabel to node


"""
