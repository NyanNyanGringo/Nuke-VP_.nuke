"""
Module to modify Root Node and add custom Guides.


"""


import nuke
import guides


# GUIDES


viewer_guides = [
  guides.Guide("title safe", 1, 1, 1, 0.1, guides.kGuideMasked),
  guides.Guide("action safe", 1, 1, 1, 0.05, guides.kGuideMasked),
  guides.FormatCenterGuide("format center", 1, 1, 1, 0.1, guides.kGuideSequence),
  guides.Guide("Format", 1, 0, 0, 0, guides.kGuideSequence),
]

viewer_masks = [
  guides.MaskGuide("square", 1.0),
  guides.MaskGuide("4:3", 4.0/3.0),
  guides.MaskGuide("16:9", 16.0/9.0),
  guides.MaskGuide("14:9", 14.0/9.0),
  guides.MaskGuide("1.66:1", 1.66),
  guides.MaskGuide("1.85:1", 1.85),
  guides.MaskGuide("2.35:1", 2.35),
  guides.MaskGuide("2048x858", 2048/858),  # example how to add custom mask guide
]
