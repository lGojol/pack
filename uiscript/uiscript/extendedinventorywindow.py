import uiScriptLocale

BUTTON_ROOT = "d:/ymir work/ui/public/"

window = {
	"name" : "ExtendedInventoryWindow",
	"x" : 100 + 171,
	"y" : 20,
	"style" : ("movable", "float",),
	"width" : 176,
	"height" : 395+10+20-17,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"x" : 0,
			"y" : 0,
			"width" : 176,
			"height" : 395+10+20-17,
			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),
					"x" : 8,
					"y" : 7,
					"width" : 161,
					"color" : "yellow",
					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":77, "y":3, "text":uiScriptLocale.EXTENDED_INVENTORY_TITLE, "text_horizontal_align":"center" },
					),
				},
				
				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",
					"x" : 8,
					"y" : 35,
					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 9,
					"x_step" : 32,
					"y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub"
				},
				
				{
					"name" : "Inventory_Tab_01",
					"type" : "radio_button",

					"x" : 10,
					"y" : 328,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_1,

					"children" :
					(
						{
							"name" : "Inventory_Tab_01_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "I",
						},
					),
				},
				{
					"name" : "Inventory_Tab_02",
					"type" : "radio_button",

					"x" : 10 + 52,
					"y" : 328,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,

					"children" :
					(
						{
							"name" : "Inventory_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "II",
						},
					),
				},
				{
					"name" : "Inventory_Tab_03",
					"type" : "radio_button",

					"x" : 10 + 104,
					"y" : 328,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_3,

					"children" :
					(
						{
							"name" : "Inventory_Tab_03_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "III",
						},
					),
				},

				## Button
				{
					"name" : "SkillBookButton",
					"type" : "radio_button",
					"x" : 8,
					"y" : 47 + 48 - 26 - 13,
					"tooltip_text" : uiScriptLocale.SKILL_BOOK_INVENTORY,
					"vertical_align" : "bottom",
					"default_image" : "d:/ymir work/ui/ekenvanter/bk_env_1.tga",
					"over_image" : "d:/ymir work/ui/ekenvanter/bk_env_2.tga",
					"down_image" : "d:/ymir work/ui/ekenvanter/bk_env_3.tga",
				},
				{
					"name" : "UpgradeItemsButton",
					"type" : "radio_button",
					"x" : 35,
					"y" : 47 + 48 - 26 - 13,
					"tooltip_text" : uiScriptLocale.UPGRADE_ITEMS_INVENTORY,
					"vertical_align" : "bottom",
					"default_image" : "d:/ymir work/ui/ekenvanter/yuk_env_1.tga",
					"over_image" : "d:/ymir work/ui/ekenvanter/yuk_env_2.tga",
					"down_image" : "d:/ymir work/ui/ekenvanter/yuk_env_3.tga",
				},
				{
					"name" : "StoneButton",
					"type" : "radio_button",
					"x" : 35+27,
					"y" : 47 + 48 - 26 - 13,
					"tooltip_text" : uiScriptLocale.UPGRADE_STONE_INVENTORY,
					"vertical_align" : "bottom",
					"default_image" : "d:/ymir work/ui/ekenvanter/tas_env_1.tga",
					"over_image" : "d:/ymir work/ui/ekenvanter/tas_env_2.tga",
					"down_image" : "d:/ymir work/ui/ekenvanter/tas_env_3.tga",
				},
				{
					"name" : "BoxButton",
					"type" : "radio_button",
					"x" : 35+27+27,
					"y" : 47 + 48 - 26 - 13,
					"tooltip_text" : uiScriptLocale.UPGRADE_BOX_INVENTORY,
					"vertical_align" : "bottom",
					"default_image" : "d:/ymir work/ui/ekenvanter/sandik_env_1.tga",
					"over_image" : "d:/ymir work/ui/ekenvanter/sandik_env_2.tga",
					"down_image" : "d:/ymir work/ui/ekenvanter/sandik_env_3.tga",
				},
				{
					"name" : "EfsunButton",
					"type" : "radio_button",
					"x" : 35+27+27+27,
					"y" : 47 + 48 - 26 - 13,
					"tooltip_text" : uiScriptLocale.UPGRADE_EFSUN_INVENTORY,
					"vertical_align" : "bottom",
					"default_image" : "d:/ymir work/ui/ekenvanter/efsun_env_1.tga",
					"over_image" : "d:/ymir work/ui/ekenvanter/efsun_env_2.tga",
					"down_image" : "d:/ymir work/ui/ekenvanter/efsun_env_3.tga",
				},
				{
					"name" : "CicekButton",
					"type" : "radio_button",
					"x" : 35+27+27+27+27,
					"y" : 47 + 48 - 26 - 13,
					"tooltip_text" : uiScriptLocale.UPGRADE_CICEK_INVENTORY,
					"vertical_align" : "bottom",
					"default_image" : "d:/ymir work/ui/ekenvanter/cicek_env_1.tga",
					"over_image" : "d:/ymir work/ui/ekenvanter/cicek_env_2.tga",
					"down_image" : "d:/ymir work/ui/ekenvanter/cicek_env_3.tga",
				},
				{
					"name" : "MalzemeDeposuInfo",
					"type" : "button",

					"x" : 132,
					"y" : 8,

					"default_image" : "d:/ymir work/ui/pattern/q_mark_01.tga",
					"over_image" : "d:/ymir work/ui/pattern/q_mark_02.tga",
					"down_image" : "d:/ymir work/ui/pattern/q_mark_01.tga",
				},
			),
		},
	),
}
