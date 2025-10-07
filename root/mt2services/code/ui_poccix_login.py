BASE_PATH = "jack_work/images/login/"
BTN_PATH = BASE_PATH + "btn/"
CHANNEL_PATH = BTN_PATH + "ch/"

height = 0
if SCREEN_HEIGHT <= 1000:
	height = -120

window = {
	"name" : "LoginWindow",
	"x" : 0, "y" : 0, "width" : SCREEN_WIDTH, "height" : SCREEN_HEIGHT,
	"style" : ("float",),
	"children" :
	(
		{
			"name" : "background", "type" : "image",
			"x" : SCREEN_WIDTH / 2 - 1920 / 2, "y" : 0 + height,
			"image" : BASE_PATH + "background.tga",
			"children" :
			(
				# ID - Field
				{
					"name" : "edit_id", "type" : "editline",
					"x" : 865, "y" : 420, "width" : 150, "height" : 16,
					"input_limit" : 24,
				},
				# PWD - Field
				{
					"name" : "edit_pwd", "type" : "editline",
					"x" : 865, "y" : 420+57, "width" : 150, "height" : 16,
					"secret_flag" : 1,
					"input_limit" : 24,
				},
				# LOGINBTN - Field
				{
					"name" : "btn_login", "type" : "button",
					"x" : 0, "y" : 530,
					"horizontal_align" : "center",
					"default_image" : BTN_PATH + "btn_login_normal.tga",
					"over_image" : BTN_PATH + "btn_login_hover.tga",
					"down_image" : BTN_PATH + "btn_login_active.tga",
				},
				# CHANNEL - Field
				{
					"name" : "btn_channel_01", "type" : "radio_button",
					"x" : 590, "y" : 368,
					"default_image" : CHANNEL_PATH + "btn_channel_01_normal.tga",
					"over_image" : CHANNEL_PATH + "btn_channel_01_hover.tga",
					"down_image" : CHANNEL_PATH + "btn_channel_01_active.tga",
				},
				{
					"name" : "btn_channel_02", "type" : "radio_button",
					"x" : 590, "y" : 375+60*1,
					"default_image" : CHANNEL_PATH + "btn_channel_02_normal.tga",
					"over_image" : CHANNEL_PATH + "btn_channel_02_hover.tga",
					"down_image" : CHANNEL_PATH + "btn_channel_02_active.tga",
				},
				{
					"name" : "btn_channel_03", "type" : "radio_button",
					"x" : 590, "y" : 372+60*2,
					"default_image" : CHANNEL_PATH + "btn_channel_03_normal.tga",
					"over_image" : CHANNEL_PATH + "btn_channel_03_hover.tga",
					"down_image" : CHANNEL_PATH + "btn_channel_03_active.tga",
				},
				{
					"name" : "btn_channel_04", "type" : "radio_button",
					"x" : 590, "y" : 370+60*3,
					"default_image" : CHANNEL_PATH + "btn_channel_04_normal.tga",
					"over_image" : CHANNEL_PATH + "btn_channel_04_hover.tga",
					"down_image" : CHANNEL_PATH + "btn_channel_04_active.tga",
				},
				# ACCOUNTDELETE - Field
				{
					"name" : "btn_delete_01", "type" : "button",
					"default_image" : BTN_PATH + "btn_delete_normal.tga",
					"x" : 1320, "y" : 410+40*0,
					"over_image" : BTN_PATH + "btn_delete_hover.tga",
					"down_image" : BTN_PATH + "btn_delete_active.tga",
				},
				{
					"name" : "btn_delete_02", "type" : "button",
					"x" : 1320, "y" : 410+40*1,
					"default_image" : BTN_PATH + "btn_delete_normal.tga",
					"over_image" : BTN_PATH + "btn_delete_hover.tga",
					"down_image" : BTN_PATH + "btn_delete_active.tga",
				},
				{
					"name" : "btn_delete_03", "type" : "button",
					"x" : 1320, "y" : 410+40*2,
					"default_image" : BTN_PATH + "btn_delete_normal.tga",
					"over_image" : BTN_PATH + "btn_delete_hover.tga",
					"down_image" : BTN_PATH + "btn_delete_active.tga",
				},
				{
					"name" : "btn_delete_04", "type" : "button",
					"x" : 1320, "y" : 410+40*3,
					"default_image" : BTN_PATH + "btn_delete_normal.tga",
					"over_image" : BTN_PATH + "btn_delete_hover.tga",
					"down_image" : BTN_PATH + "btn_delete_active.tga",
				},
				{
					"name" : "btn_delete_05", "type" : "button",
					"x" : 1320, "y" : 410+40*4,
					"default_image" : BTN_PATH + "btn_delete_normal.tga",
					"over_image" : BTN_PATH + "btn_delete_hover.tga",
					"down_image" : BTN_PATH + "btn_delete_active.tga",
				},
				# ACCOUNTADD - Field
				{
					"name" : "btn_add_01", "type" : "button",
					"x" : 1300, "y" : 410+40*0,
					"default_image" : BTN_PATH + "btn_add_normal.tga",
					"over_image" : BTN_PATH + "btn_add_hover.tga",
					"down_image" : BTN_PATH + "btn_add_active.tga",
				},
				{
					"name" : "btn_add_02", "type" : "button",
					"x" : 1300, "y" : 410+40*1,
					"default_image" : BTN_PATH + "btn_add_normal.tga",
					"over_image" : BTN_PATH + "btn_add_hover.tga",
					"down_image" : BTN_PATH + "btn_add_active.tga",
				},
				{
					"name" : "btn_add_03", "type" : "button",
					"x" : 1300, "y" : 410+40*2,
					"default_image" : BTN_PATH + "btn_add_normal.tga",
					"over_image" : BTN_PATH + "btn_add_hover.tga",
					"down_image" : BTN_PATH + "btn_add_active.tga",
				},
				{
					"name" : "btn_add_04", "type" : "button",
					"x" : 1300, "y" : 410+40*3,
					"default_image" : BTN_PATH + "btn_add_normal.tga",
					"over_image" : BTN_PATH + "btn_add_hover.tga",
					"down_image" : BTN_PATH + "btn_add_active.tga",
				},
				{
					"name" : "btn_add_05", "type" : "button",
					"x" : 1300, "y" : 410+40*4,
					"default_image" : BTN_PATH + "btn_add_normal.tga",
					"over_image" : BTN_PATH + "btn_add_hover.tga",
					"down_image" : BTN_PATH + "btn_add_active.tga",
				},
				# ACCOUNTSELECT - Field
				{
					"name" : "text_account_01", "type" : "text",
					"x" : 1155, "y" : 410+40*0,
					"text" : "#01 - " + "Freier Slot",
				},
				{
					"name" : "btn_select_01", "type" : "button",
					"x" : 1150, "y" : 406+40*0,
					"default_image" : BTN_PATH + "btn_select_blank.tga",
					"over_image" : BTN_PATH + "btn_select.tga",
					"down_image" : BTN_PATH + "btn_select.tga",
				},
				{
					"name" : "text_account_02", "type" : "text",
					"x" : 1155, "y" : 410+40*1,
					"text" : "#02 - " + "Freier Slot",
				},
				{
					"name" : "btn_select_02", "type" : "button",
					"x" : 1150, "y" : 406+40*1,
					"default_image" : BTN_PATH + "btn_select_blank.tga",
					"over_image" : BTN_PATH + "btn_select.tga",
					"down_image" : BTN_PATH + "btn_select.tga",
				},
				{
					"name" : "text_account_03", "type" : "text",
					"x" : 1155, "y" : 410+40*2,
					"text" : "#03 - " + "Freier Slot",
				},
				{
					"name" : "btn_select_03", "type" : "button",
					"x" : 1150, "y" : 406+40*2,
					"default_image" : BTN_PATH + "btn_select_blank.tga",
					"over_image" : BTN_PATH + "btn_select.tga",
					"down_image" : BTN_PATH + "btn_select.tga",
				},
				{
					"name" : "text_account_04", "type" : "text",
					"x" : 1155, "y" : 410+40*3,
					"text" : "#04 - " + "Freier Slot",
				},
				{
					"name" : "btn_select_04", "type" : "button",
					"x" : 1150, "y" : 406+40*3,
					"default_image" : BTN_PATH + "btn_select_blank.tga",
					"over_image" : BTN_PATH + "btn_select.tga",
					"down_image" : BTN_PATH + "btn_select.tga",
				},
				{
					"name" : "text_account_05", "type" : "text",
					"x" : 1155, "y" : 410+40*4,
					"text" : "#05 - " + "Freier Slot",
				},
				{
					"name" : "btn_select_05", "type" : "button",
					"x" : 1150, "y" : 406+40*4,
					"default_image" : BTN_PATH + "btn_select_blank.tga",
					"over_image" : BTN_PATH + "btn_select.tga",
					"down_image" : BTN_PATH + "btn_select.tga",
				},
			),
		},
	),
}