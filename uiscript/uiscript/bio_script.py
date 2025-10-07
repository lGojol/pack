import uiScriptLocale

WINDOW_HEIGHT = 270+145
WINDOW_WIDTH = 330

window = {
	"name" : "BioW",
	"style" : ("movable", "float",),

	"x" : 200,
	"y" : 100,

	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : WINDOW_WIDTH,
			"height" : WINDOW_HEIGHT,
			
			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 1,
					"y" : 1,

					"width" : WINDOW_WIDTH - 2,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":(WINDOW_WIDTH - 2) / 2, "y":1, "text":uiScriptLocale.BIO_SYSTEM_TITLE, "text_horizontal_align":"center" },
					),
				},
			),
		},
	),
}
