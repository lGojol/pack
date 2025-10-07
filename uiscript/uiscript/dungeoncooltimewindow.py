import localeInfo

MINIMAP_WITH = 150
BOARD_WIDTH = 136
BOARD_HEIGHT = 170
ASSET_PATH = "d:/ymir work/ui/shadow_cooltime/"

window = {
	"name" : "DungeonCoolTimeWindow",
	"style" : ("float",),

	"x" : SCREEN_WIDTH - MINIMAP_WITH - BOARD_WIDTH,
	"y" : 0,

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name": "bg",
			"type": "image",

			"x": 0,
			"y": 0,

			"image": ASSET_PATH + "cooltime_bg.tga",

			"children": (
				{
					"name": "floorText",
					"type": "text",

					"x": 74,
					"y": 41,

					"text_horizontal_align": "center",

					"text": "1",
				},
				{
					"name": "coolTimeText",
					"type": "text",

					"x": 75,
					"y": 60,

					"text_horizontal_align": "center",

					"text": "1",
				},
				{
					"name": "coolTimeImage",
					"type": "expanded_image",

					"x": 16,
					"y": 9,

					"image": ASSET_PATH + "cooltime_bar.tga",
				},
				{
					"name": "spActiveImage",
					"type": "image",

					"x": 29,
					"y": 148,

					"image": ASSET_PATH + "shadow_potion_active.tga",
				},
				{
					"name": "spCoolTimeText",
					"type": "text",

					"x": 75,
					"y": 184,

					"text_horizontal_align": "center",

					"text": "",
				},
			),
		},
	),
}
