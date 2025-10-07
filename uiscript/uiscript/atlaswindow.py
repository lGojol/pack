import uiScriptLocale

ROOT = "d:/ymir work/ui/minimap/"

window = {
	"name" : "AtlasWindow",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - 136 - 256 - 10,
	"y" : 0,

	"width" : 256 + 15,
	"height" : 256 + 38,

	"children" :
	(
		## BOARD
		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 256 + 15,
			"height" : 256 + 38,

			"title" : uiScriptLocale.ZONE_MAP,
		},
		{
			"name" : "info",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 10,
			"height" : 10,

			"children" : 
			(
				{
					"name" : "info_text1",
					"type" : "text",

					"x" : 15,
					"y" : 17,

					"text" : uiScriptLocale.NAME_MAP_ATLAS,
				},
				{
					"name" : "info_text2",
					"type" : "text",

					"x" : 15,
					"y" : 32,

					"text" : uiScriptLocale.CORDINATE_MAP_ATLAS,
				}
			),
		},
	),
}
