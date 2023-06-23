"""
Module to add custom callbacks to Nuke. Example of script that reload dot label*:


import nuke


def reload_label_for_dot():
    if nuke.thisKnob().name() == "inputChange" or nuke.thisKnob().name() == "hide_input":
        with nuke.root():
            for node in nuke.allNodes():
                if node.Class() == 'Dot':
                    label = node.knob('label').value()  # reload label
                    node.knob('label').setValue('')
                    node.knob('label').setValue(label)


nuke.addKnobChanged(reload_label_for_dot, nodeClass="Dot")


* for those who write some info in Dot label and want in to update properly.


"""