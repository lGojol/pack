import uiScriptLocale

window = {
	"name" : "FastInventoryWindow",
	"x" : 0,
	"y" : 0,
	"width" : 10,
	"height" : 225,
	"children" :({
			"name" : "FastInventoryLayer",
			"type" : "invisibleboard",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width" : 10,
			"height" : 225,
			"children" :(
				{"name" : "Menu_3","type" : "button","x" : 10,"y" : 10,"default_image" : "locale/common/ui/buttons/button_switch_bot_01.tga","over_image" : "locale/common/ui/buttons/button_switch_bot_02.tga","down_image" : "locale/common/ui/buttons/button_switch_bot_03.tga",},
				{"name" : "Menu_4","type" : "button","x" : 10,"y" : 10 + 35,"default_image" : "locale/common/ui/buttons/inventaire_special_button_01.tga","over_image" : "locale/common/ui/buttons/inventaire_special_button_02.tga","down_image" : "locale/common/ui/buttons/inventaire_special_button_03.tga",},
				{"name" : "Menu_5","type" : "button","x" : 10,"y" : 10 + 70,"default_image" : "locale/common/ui/buttons/tobol1.tga","over_image" : "locale/common/ui/buttons/tobol2.tga","down_image" : "locale/common/ui/buttons/tobol3.tga",},
				{"name" : "Menu_6","type" : "button","x" : 10,"y" : 45 + 70,"default_image" : "locale/common/ui/buttons/wiki1.tga","over_image" : "locale/common/ui/buttons/wiki2.tga","down_image" : "locale/common/ui/buttons/wiki3.tga",},
			),
		},
	),
}
