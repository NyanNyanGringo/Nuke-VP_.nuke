import nuke


# USERCONFIG


nuke_3de4_menu_name = "3DE4"


# import lens to Nuke in GUI mode


dlls = ["LD_3DE4_All_Parameter_Types",
		"LD_3DE4_Anamorphic_Degree_6",
		"LD_3DE4_Anamorphic_Rescaled_Degree_4",
		"LD_3DE4_Anamorphic_Rescaled_Degree_6",
		"LD_3DE4_Anamorphic_Standard_Degree_4",
		"LD_3DE4_Anamorphic_Standard_Degree_6",
		"LD_3DE4_Radial_Fisheye_Degree_8",
		"LD_3DE4_Radial_Fisheye_Equidistant_Degree_8",
		"LD_3DE4_Radial_Fisheye_Equisolid_Degree_8",
		"LD_3DE4_Radial_Fisheye_Orthographic_Degree_8",
		"LD_3DE4_Radial_Fisheye_Stereographic_Degree_8",
		"LD_3DE4_Radial_Homomorphic_Degree_2",
		"LD_3DE4_Radial_Standard_Degree_4",
		"LD_3DE_Classic_LD_Model"]


for dll in dlls:
	nuke.menu("Nodes").addCommand(nuke_3de4_menu_name + "/" + dll, "nuke.createNode('" + dll + "')")
