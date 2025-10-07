import uiScriptLocale
BOARD_W = (680-60-75+230-7-12-12-10-8)-300-150+85
BOARD_H = 376+9

LEFTBOARD_X = 13
LEFTBOARD_Y = 36

LEFTBOARD_WIDTH = (680-60-75+230-7-12-12-10-8)-300-150+85-15-5
LEFTBOARD_HEIGHT = 382-55+9

EK_Y = 4

window ={
	"name" : "SpeedButtonWindow",
	"style" : ("movable", "float"),

	"x"		: 0,
	"y"		: 0,

	"width"	: BOARD_W,
	"height" : BOARD_H,

	"children" : 
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach"),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_W,
			"height" : BOARD_H,

			"title" : uiScriptLocale.SPEED_BUTTON_TITLE,

			"children" : 
			(
				{
					"name" : "dataManagerButtonThinBoard",
					"type" : "thinboard",

					"x" : LEFTBOARD_X - 4,
					"y" : LEFTBOARD_Y - 4,

					"width" : LEFTBOARD_WIDTH + 8,
					"height" : LEFTBOARD_HEIGHT + 8,
				},
				{
					"name" : "dataManagerButtonBoard",
					"type" : "thinboard_circle",

					"x" : LEFTBOARD_X,
					"y" : LEFTBOARD_Y,

					"width" : LEFTBOARD_WIDTH,
					"height" : LEFTBOARD_HEIGHT,
				},

				{
					"name" : "backGround",
					"type" : "expanded_image",
					
					"x" : 10,
					"y" : 29+5,
					
					"image" : "menu_2341/bg.png",
					
					"children" : 
					(
						{"name" : "Button1","type" : "button","x" : 16,"y" : 40+EK_Y,"default_image" : "menu_2341/offline_shop_1.png","over_image" : "menu_2341/offline_shop_2.png","down_image" : "menu_2341/offline_shop_3.png",},				
						{"name" : "Button1Text","type" : "text","x" : 16+46,"y" : 40+12+EK_Y, "text" : uiScriptLocale.BUTTON_1,},

						{"name" : "Button2","type" : "button","x" : 177,"y" : 40+EK_Y,"default_image" : "menu_2341/shop_search_1.png","over_image" : "menu_2341/shop_search_2.png","down_image" : "menu_2341/shop_search_3.png",},				
						{"name" : "Button1Text","type" : "text","x" : 177+42+66,"y" : 40+12+EK_Y, "text" : uiScriptLocale.BUTTON_2,"text_horizontal_align" : "right",},

						{"name" : "Button3","type" : "button","x" : 16,"y" : 85+EK_Y,"default_image" : "menu_2341/average_search_1.png","over_image" : "menu_2341/average_search_2.png","down_image" : "menu_2341/average_search_3.png",},				
						{"name" : "Button1Text","type" : "text","x" : 16+46,"y" : 85+12+EK_Y, "text" : uiScriptLocale.BUTTON_3,},

						{"name" : "Button4","type" : "button","x" : 177,"y" : 85+EK_Y,"default_image" : "menu_2341/range_shop_1.png","over_image" : "menu_2341/range_shop_2.png","down_image" : "menu_2341/range_shop_3.png",},				
						{"name" : "Button1Text","type" : "text","x" : 177+42+66,"y" : 85+12+EK_Y, "text" : uiScriptLocale.BUTTON_4,"text_horizontal_align" : "right",},

						{"name" : "Button5","type" : "button","x" : 16,"y" : 85+45+EK_Y,"default_image" : "menu_2341/trade_shop_log_1.png","over_image" : "menu_2341/trade_shop_log_2.png","down_image" : "menu_2341/trade_shop_log_3.png",},				
						{"name" : "Button1Text","type" : "text","x" : 16+46,"y" : 85+45+12+EK_Y, "text" : uiScriptLocale.BUTTON_5,},

						{"name" : "Button6","type" : "button","x" : 177,"y" : 85+45+EK_Y,"default_image" : "menu_2341/won_gold_transfer_1.png","over_image" : "menu_2341/won_gold_transfer_2.png","down_image" : "menu_2341/won_gold_transfer_3.png",},				
						{"name" : "Button1Text","type" : "text","x" : 177+42+66,"y" : 85+45+12+EK_Y, "text" : uiScriptLocale.BUTTON_6,"text_horizontal_align" : "right",},

						{"name" : "Button7","type" : "button","x" : 16,"y" : 85+45+45+EK_Y,"default_image" : "menu_2341/boss_ranked_1.png","over_image" : "menu_2341/boss_ranked_2.png","down_image" : "menu_2341/boss_ranked_3.png",},				
						{"name" : "Button1Text","type" : "text","x" : 16+46,"y" : 85+45+45+12+EK_Y, "text" : uiScriptLocale.BUTTON_7,},

						{"name" : "Button8","type" : "button","x" : 177,"y" : 85+45+45+EK_Y,"default_image" : "menu_2341/boss_manager_1.png","over_image" : "menu_2341/boss_manager_2.png","down_image" : "menu_2341/boss_manager_3.png",},				
						{"name" : "Button1Text","type" : "text","x" : 177+42+66,"y" : 85+45+45+12+EK_Y, "text" : uiScriptLocale.BUTTON_8,"text_horizontal_align" : "right",},

						{"name" : "Button9","type" : "button","x" : 16,"y" : 85+45+45+45+EK_Y,"default_image" : "menu_2341/attr_button_1.png","over_image" : "menu_2341/attr_button_2.png","down_image" : "menu_2341/attr_button_3.png",},				
						{"name" : "Button1Text","type" : "text","x" : 16+46,"y" : 85+45+45+45+12+EK_Y, "text" : uiScriptLocale.BUTTON_9,},

						{"name" : "Button10","type" : "button","x" : 177,"y" : 85+45+45+45+EK_Y,"default_image" : "menu_2341/range_biyolog_1.png","over_image" : "menu_2341/range_biyolog_2.png","down_image" : "menu_2341/range_biyolog_3.png",},				
						{"name" : "Button1Text","type" : "text","x" : 177+42+66,"y" : 85+45+45+45+12+EK_Y, "text" : uiScriptLocale.BUTTON_10,"text_horizontal_align" : "right",},

						{"name" : "Button11","type" : "button","x" : 16,"y" : 85+45+45+45+45+EK_Y,"default_image" : "menu_2341/dungeon_info_1.png","over_image" : "menu_2341/dungeon_info_2.png","down_image" : "menu_2341/dungeon_info_3.png",},				
						{"name" : "Button1Text","type" : "text","x" : 16+46,"y" : 85+45+45+45+45+12+EK_Y, "text" : uiScriptLocale.BUTTON_11,},

						{"name" : "Button12","type" : "button","x" : 177,"y" : 85+45+45+45+45+EK_Y,"default_image" : "menu_2341/guild_ranked_1.png","over_image" : "menu_2341/guild_ranked_2.png","down_image" : "menu_2341/guild_ranked_3.png",},				
						{"name" : "Button1Text","type" : "text","x" : 177+42+66,"y" : 85+45+45+45+45+12+EK_Y, "text" : uiScriptLocale.BUTTON_12,"text_horizontal_align" : "right",},

					),
				},
			),
		},
	),
}