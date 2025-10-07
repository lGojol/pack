import uiScriptLocale
import app

ROOT_PATH			= "d:/ymir work/ui/game/premium_private_shop/"

WINDOW_WIDTH		= 196
WINDOW_HEIGHT		= 445

INFORMATION_GROUP_X		= 16
INFORMATION_GROUP_Y		= 361

BUTTON_GROUP_X			= 12
BUTTON_GROUP_Y			= 410

window = {
	"name" : "PremiumPrivateShopDialog",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - 475,
	"y" : SCREEN_HEIGHT - 605,

	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach", "ltr",),

			"x" : 0,
			"y" : 0,

			"width" : WINDOW_WIDTH,
			"height" : WINDOW_HEIGHT,
			"title" : uiScriptLocale.PREMIUM_PRIVATE_SHOP_TITLE,

			"children" :
			(
				# Shop Position Icon
				{
					"name" : "location_button",
					"type" : "button",

					"x" : 7,
					"y" : 39,

					"default_image" : ROOT_PATH + "position_icon.sub",
					"over_image" : ROOT_PATH + "position_icon.sub",
					"down_image" : ROOT_PATH + "position_icon.sub",
				},

				# Shop Title
				{
					"name" : "shop_name_text_window",
					"type" : "window",
					"style" : ("attach",),

					"x" : 27,
					"y" : 36,

					"width" : 158,
					"height" : 19,

					"children" :
					(
						{
							"name" :"shop_name_text_button",
							"type":"button",

							"x":0,
							"y":0,

							"default_image" : ROOT_PATH + "shop_name_text_bg.sub",
							"over_image" : ROOT_PATH + "shop_name_text_bg.sub",
							"down_image" : ROOT_PATH + "shop_name_text_bg.sub",
						},

						{
							"name" : "shop_name_text",
							"type" : "text",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 0,

							"all_align" : "center",
							"text" : "",
						},
					),
				},

				# Shop Notice Text
				{
					"name" : "shop_notice_window",
					"type" : "window",
					"style" : ("attach",),

					"x" : 11,
					"y" : 55,

					"width" : 173,
					"height" : 19,

					"children" :
					(
						{
							"name" : "shop_notice_bg",
							"type":"image",

							"x":0,
							"y":0,

							"image" : ROOT_PATH + "notice_bg.sub",
						},

						{
							"name" : "shop_notice_text",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",
							"text" : "",
						},
					),
				},

				## Item Slot
				{
					"name" : "item_slot",
					"type" : "grid_table",

					"x" : 17,
					"y" : 75,

					"start_index" : 0,

					"x_count" : 5,
					"y_count" : 8,

					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},

				# Tab Button Group
				{
					"name" : "TabButtonGroup",
					"type" : "window",

					"x" : 0,
					"y" : 337,

					"style" : ("attach",),

					"horizontal_align" : "center",

					"width" : 66,
					"height" : 18,

					"children":
					(
						## Tab 1
						{
							"name" : "tab1",
							"type" : "radio_button",

							"x" : 0,
							"y" : 0,

							"text" : "I",

							"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
							"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
							"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
						},

						## Tab 2
						{
							"name" : "tab2",
							"type" : "radio_button",

							"x" : 34,
							"y" : 0,

							"text" : "II",

							"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
							"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
							"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
						},
					),
				},

				# Information Group
				{
					"name" : "information_group",
					"type" : "window",

					"x" : INFORMATION_GROUP_X,
					"y" : INFORMATION_GROUP_Y,

					"style" : ("attach",),

					"width" : 200,
					"height" : 18 + 26 + 18,

					"children" :
					(
						# Sandglass Icon
						{
							"name" : "sandglass_icon",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"style" : ("attach",),

							"image" : ROOT_PATH + "sandglass_icon.sub",
						},

						# Remanining Time Text
						{
							"name" : "remain_time_text_window",
							"type" : "window",
							"style" : ("attach",),

							"x" : 24,
							"y" : 0,

							"width" : 137,
							"height" : 18,

							"children" :
							(
								{
									"name" : "remain_time_text_bg",
									"type":"image",

									"x":0,
									"y":0,

									"image" : ROOT_PATH + "remain_time_text_bg.sub"
								},

								{
									"name" : "remain_time_text",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : "center",
									"text" : "",
								},
							),
						},

						# Won Icon
						{
							"name":"cheque_icon",
							"type":"image",

							"x": 0,
							"y": 2 + 26,

							"image":"d:/ymir work/ui/game/windows/cheque_icon.sub",
						},

						# Won Text
						{
							"name" : "cheque_text_window",
							"type" : "window",
							"style" : ("attach",),

							"x" : 24,
							"y" : 26,

							"width" : 19,
							"height" : 18,

							"children" :
							(
								{
									"name" : "cheque_text_bg",
									"type":"image",

									"x":0,
									"y":0,

									"image" : ROOT_PATH + "won_text_bg.sub"
								},

								{
									"name" : "cheque_text",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : "center",
									"text" : "",
								},
							),
						},

						# Yang Icon
						{
							"name":"gold_icon",
							"type":"image",

							"x": 50,
							"y": 2 + 26,

							"image":"d:/ymir work/ui/game/windows/money_icon.sub",
						},

						## Yang Text
						{
							"name" : "gold_text_window",
							"type" : "window",
							"style" : ("attach",),

							"x" : 71,
							"y" : 26,

							"width" : 88,
							"height" : 18,

							"children" :
							(
								{
									"name" : "gold_text_bg",
									"type":"image",

									"x":0,
									"y":0,

									"image" : ROOT_PATH + "yang_text_bg.sub"
								},

								{
									"name" : "gold_text",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : "center",
									"text" : "",
								},
							),
						},
					),
				},

				# Button Group
				{
					"name" : "button_group",
					"type" : "window",

					"x" : BUTTON_GROUP_X,
					"y" : BUTTON_GROUP_Y,

					"style" : ("attach",),

					"width" : 243,
					"height" : 25,

					"children" :
					(
						# Modify Button
						{
							"name" : "modify_button",
							"type" : "button",

							"x" : 0,
							"y" : 0,

							"default_image" : ROOT_PATH + "modify_button_default.sub",
							"over_image" : ROOT_PATH + "modify_button_over.sub",
							"down_image" : ROOT_PATH + "modify_button_down.sub",
						},

						# Reopen Button
						{
							"name" : "reopen_button",
							"type" : "button",

							"x" : -33,
							"y" : 0,

							"horizontal_align" : "center",

							"default_image" : ROOT_PATH + "reopen_button_default.sub",
							"over_image" : ROOT_PATH + "reopen_button_over.sub",
							"down_image" : ROOT_PATH + "reopen_button_down.sub",
						},

						# Tax Adjustment Button
						{
							"name" : "tax_adjustment_button",
							"type" : "button",

							"x" : 58,
							"y" : 0,

							"default_image" : ROOT_PATH + "tax_adjustment_button_default.sub",
							"over_image" : ROOT_PATH + "tax_adjustment_button_over.sub",
							"down_image" : ROOT_PATH + "tax_adjustment_button_down.sub",
						},

						# Shop Close Button
						{
							"name" : "shop_close_button",
							"type" : "button",

							"x" : (58) * 2,
							"y" : 0,

							"default_image" : ROOT_PATH + "shop_close_button_default.sub",
							"over_image" : ROOT_PATH + "shop_close_button_over.sub",
							"down_image" : ROOT_PATH + "shop_close_button_down.sub",
						},
					),
				},
			),
		},
	),
}