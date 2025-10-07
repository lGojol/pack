import uiScriptLocale
import item
import app

COSTUME_START_INDEX = item.COSTUME_SLOT_START

window = {
	"name" : "CostumeWindow",

	"x" : SCREEN_WIDTH - 175 - 140,
	"y" : SCREEN_HEIGHT - 37 - 565,

	"style" : ("float",),

	"width" : 140,
	"height" : (180 + 47), #기존보다 47 길어짐

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			# "style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 140,
			"height" : (180 + 47),
		
			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 6,

					"width" : 130,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":60, "y":3, "text":uiScriptLocale.COSTUME_WINDOW_TITLE, "text_horizontal_align":"center" },
					),
				},

				## Equipment Slot
				{
					"name" : "Costume_Base",
					"type" : "image",

					"x" : 13,
					"y" : 38,
				
					"image" : uiScriptLocale.LOCALE_UISCRIPT_PATH + "costume/new_costume_bg.jpg",					

					"children" :
					(

						{
							"name" : "CostumeSlot",
							"type" : "slot",

							"x" : 3,
							"y" : 3,

							"width" : 127,
							"height" : 160,

							"slot" : (
										{"index":item.COSTUME_SLOT_BODY, "x":62, "y":45, "width":32, "height":64},
										{"index":item.COSTUME_SLOT_HAIR, "x":62, "y": 8, "width":32, "height":32},
										{"index":item.COSTUME_SLOT_WEAPON, "x":12, "y":14, "width":32, "height":96},
										{"index":item.COSTUME_SLOT_MOUNT, "x":6, "y":127, "width":32, "height":32},
										{"index":item.COSTUME_SLOT_ACCE, "x":70, "y":127, "width":32, "height":32},
										{"index":item.COSTUME_SLOT_AURA, "x":38, "y":127, "width":32, "height":32},
									),

						},
						## ENABLE_HIDE_COSTUME_SYSTEM
						{ "name" : "VisibleBodySlotImg", "type" : "expanded_image", "x" : 62+4, "y" : 45+4, "image" : "d:/ymir work/ui/game/costume/hideslot_02.tga" },
						{ "name" : "VisibleHairSlotImg", "type" : "expanded_image", "x" : 62+4, "y" : 8+4, "image" : "d:/ymir work/ui/game/costume/hideslot_01.tga" },
						{ "name" : "VisibleAcceSlotImg", "type" : "expanded_image", "x" : 70+4, "y" : 127+4, "image" : "d:/ymir work/ui/game/costume/hideslot_01.tga" },
						{ "name" : "VisibleAuraSlotImg", "type" : "expanded_image", "x" : 40, "y" : 127+4, "image" : "d:/ymir work/ui/game/costume/hideslot_01.tga" },
						{ "name" : "VisibleWeaponSlotImg", "type" : "expanded_image", "x" : 12+4, "y" : 14+4, "image" : "d:/ymir work/ui/game/costume/hideslot_03.tga" },
						## ENABLE_HIDE_COSTUME_SYSTEM
						{
							"name" : "BodyToolTipButton",
							"type" : "toggle_button",

							"x" : 62 + 32,
							"y" : 45,
							"tooltip_text" : uiScriptLocale.STRUCTURE_VIEW_TYPE_STRUCTURE,

							"default_image" : "d:/ymir work/ui/game/costume/eye_normal_01.tga",
							"over_image" : "d:/ymir work/ui/game/costume/eye_normal_02.tga",
							"down_image" : "d:/ymir work/ui/game/costume/eye_normal_02.tga",
						},
						{
							"name" : "HairToolTipButton",
							"type" : "toggle_button",

							"x" : 62 + 32,
							"y" : 9,
							"tooltip_text" : uiScriptLocale.STRUCTURE_VIEW_TYPE_STRUCTURE,

							"default_image" : "d:/ymir work/ui/game/costume/eye_normal_01.tga",
							"over_image" : "d:/ymir work/ui/game/costume/eye_normal_02.tga",
							"down_image" : "d:/ymir work/ui/game/costume/eye_normal_02.tga",
						},
						{
							"name" : "AcceToolTipButton",
							"type" : "toggle_button",

							"x" : 62 + 32,
							"y" : 126,
							"tooltip_text" : uiScriptLocale.STRUCTURE_VIEW_TYPE_STRUCTURE,

							"default_image" : "d:/ymir work/ui/game/costume/eye_normal_01.tga",
							"over_image" : "d:/ymir work/ui/game/costume/eye_normal_02.tga",
							"down_image" : "d:/ymir work/ui/game/costume/eye_normal_02.tga",
						},
						{
							"name" : "AuraToolTipButton",
							"type" : "toggle_button",

							"x" : 62,
							"y" : 126,
							"tooltip_text" : uiScriptLocale.STRUCTURE_VIEW_TYPE_STRUCTURE,

							"default_image" : "d:/ymir work/ui/game/costume/eye_normal_01.tga",
							"over_image" : "d:/ymir work/ui/game/costume/eye_normal_02.tga",
							"down_image" : "d:/ymir work/ui/game/costume/eye_normal_02.tga",
						},
						{
							"name" : "WeaponToolTipButton",
							"type" : "toggle_button",

							"x" : 13 + 32,
							"y" : 13,
							"tooltip_text" : uiScriptLocale.STRUCTURE_VIEW_TYPE_STRUCTURE,

							"default_image" : "d:/ymir work/ui/game/costume/eye_normal_01.tga",
							"over_image" : "d:/ymir work/ui/game/costume/eye_normal_02.tga",
							"down_image" : "d:/ymir work/ui/game/costume/eye_normal_02.tga",
						},
						## END_ENABLE_HIDE_COSTUME_SYSTEM
					),
				},
			),
		},
	),
}
