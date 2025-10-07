import uiScriptLocale

MAINBOARD_WIDTH = 138
MAINBOARD_HEIGHT = 48 + 35
MAINBOARD_X = (SCREEN_WIDTH - MAINBOARD_WIDTH)
MAINBOARD_Y = 160

window = {
	"name" : "BattleRoyaleInfo",
	"style" : ("not_pick",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,
	
	"children" :
	(
		{ 
			"name":"toggleTerrainZoneArea", 
			"type" : "button", 
			"x" : SCREEN_WIDTH-50-32,
			"y" : SCREEN_HEIGHT-170,
			"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
			"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
			"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",

			"children" : 
			(
				{ 
					"name":"toggleTerrainZoneAreaText", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					# "text": uiScriptLocale.HIDE_TERRAIN_ZONE, 
					#"text": "Terrain Zone - Visible", 
					"text": uiScriptLocale.BATTLE_ROYALE_TERRAIN_VISIBLE, 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},	
			),
		},
	
		{
			"name" : "board",
			"type" : "thinboard",
			"style" : ("not_pick",),

			"x" : SCREEN_WIDTH - 290 + 10 - 4,
			"y" : 30,

			"width" : MAINBOARD_WIDTH,
			"height" : MAINBOARD_HEIGHT,
			
			"children" :
			(
			
			
				{
					"name" : "infoText",
					"type" : "text",

					"x" : MAINBOARD_WIDTH/2,
					"y" : 15,
					"text" : "",
					"text_horizontal_align":"center"
				},
				
				{
					"name":"remaining",
					"type":"text",
					"x":MAINBOARD_WIDTH/2,
					"y":30,
					#"text":"04:38",
					"text":uiScriptLocale.BATTLE_ROYALE_REMAINIG_TIME,
					"text_horizontal_align":"center"
				},
				
				{
					"name":"lineSeparator1",
					"type":"line",
					"x":2,
					"y":30 + 15,
					"width" : MAINBOARD_WIDTH-4,
					"height" : 0,
					"color" : 0xff777777,
				},
				
				{
					"name":"yourKills",
					"type":"text",
					"x":MAINBOARD_WIDTH/2,
					"y":30 + 15 + 5,
					#"text":"Your kills: 0",
					"text":uiScriptLocale.BATTLE_ROYALE_KILLS_PROCESED,
					"text_horizontal_align":"center"
				},
				
				{
					"name":"remainingPlayers",
					"type":"text",
					"x":MAINBOARD_WIDTH/2,
					"y":30 + 15 + 5 + 15,
					#"text":"Remaining players: 0",
					"text":uiScriptLocale.BATTLE_ROYALE_REMAINING_PLAYERS,
					"text_horizontal_align":"center"
				},
				

			),
		}, ## MainBoard End
	
		## Join Button
		{ 
			"name": "JoinButton", 
			"type" : "button", 
			"x" : SCREEN_WIDTH - 290,
			"y" : 8,
			"default_image" : "d:/ymir work/ui/game/battle_royale/br_button01.tga",
			"over_image" : "d:/ymir work/ui/game/battle_royale/br_button02.tga",
			"down_image" : "d:/ymir work/ui/game/battle_royale/br_button03.tga",
		},

		
	),
}