BASE_PATH = "mt2services/images/login/"
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
	
			# Background
		{
			"name" : "full", 
			"type" : "expanded_image",

			"x" : 0, 
			"y" : 0,

			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,

			"image" : BASE_PATH + "full.tga",
		},
		{
			"name" : "background", "type" : "image",
			"x" : SCREEN_WIDTH / 2 - 1920 / 2, "y" : 0 + height,
			"image" : BASE_PATH + "background.tga",
			"children" :
			(
				{
					"name" : "betaserver", "type" : "radio_button",
					"x" : 415+53*3, "y" : 620,
					"default_image" : CHANNEL_PATH + "butonbeta.tga",
					"over_image" : CHANNEL_PATH + "butonbeta.tga",
					"down_image" : CHANNEL_PATH + "butonbetaselectat.tga",
				},
				# ID	x=Orizontal y=Vertical
				{
					"name" : "edit_id", "type" : "editline",
					"x" : 875, "y" : 511, "width" : 150, "height" : 16,
					"input_limit" : 24,
				},
				# Parola	x=Orizontal y=Vertical
				{
					"name" : "edit_pwd", "type" : "editline",
					"x" : 875, "y" : 528+53, "width" : 150, "height" : 16,
					"secret_flag" : 1,
					"input_limit" : 24,
				},
				# BUTOANE PENTRU LINKURI	x=Orizontal y=Vertical
				{
					"name" : "instagram_buton", "type" : "button",
					"x" : 1410, "y" : 544,
					"default_image" : CHANNEL_PATH + "instagram_0.tga",
					"over_image" :  CHANNEL_PATH + "instagram_1.tga",
					"down_image" : CHANNEL_PATH + "instagram_1.tga",
				},
				{
					"name" : "discord_buton", "type" : "button",
					"x" : 1408, "y" : 495,
					"default_image" : CHANNEL_PATH + "discord_0.tga",
					"over_image" :  CHANNEL_PATH + "discord_1.tga",
					"down_image" : CHANNEL_PATH + "discord_1.tga",
				},
				{
					"name" : "youtube_buton", "type" : "button",
					"x" : 1410, "y" : 598,
					"default_image" : CHANNEL_PATH + "youtube_0.tga",
					"over_image" : CHANNEL_PATH + "youtube_1.tga",
					"down_image" : CHANNEL_PATH + "youtube_1.tga",
				},
				{
					"name" : "web_buton", "type" : "button",
					"x" : 1410, "y" : 649,
					"default_image" : CHANNEL_PATH + "web_0.tga",
					"over_image" :  CHANNEL_PATH + "web_1.tga",
					"down_image" : CHANNEL_PATH + "web_1.tga",
				},
				# Logare	x=Orizontal y=Vertical
				{
					"name" : "btn_exit", "type" : "button",
					"x" : -10, "y" : 745,
					"horizontal_align" : "center",
					"default_image" : BTN_PATH + "conectare_0.tga",
					"over_image" : BTN_PATH + "conectare_1.tga",
					"down_image" : BTN_PATH + "conectare_1.tga",
				},
				{
					"name" : "btn_login", "type" : "button",
					"x" : -10, "y" : 685,
					"horizontal_align" : "center",
					"default_image" : BTN_PATH + "iesire_0.tga",
					"over_image" : BTN_PATH + "iesire_1.tga",
					"down_image" : BTN_PATH + "iesire_1.tga",
				},
				# Canale	x=Orizontal y=Vertical
				{
					"name" : "btn_channel_01", "type" : "radio_button",
					"x" : 382+53*3, "y" : 508,
					"default_image" : CHANNEL_PATH + "ch1_off.tga",
					"over_image" : CHANNEL_PATH + "ch1_activate.tga",
					"down_image" : CHANNEL_PATH + "ch1_on.tga",
				},
				{
					"name" : "btn_channel_02", "type" : "radio_button",
					"x" : 382+53*3, "y" : 553,
					"default_image" : CHANNEL_PATH + "ch2_off.tga",
					"over_image" : CHANNEL_PATH + "ch2_activate.tga",
					"down_image" : CHANNEL_PATH + "ch2_on.tga",
				},
				{
					"name" : "btn_channel_03", "type" : "radio_button",
					"x" : 382+53*3, "y" : 598,
					"default_image" : CHANNEL_PATH + "ch3_off.tga",
					"over_image" : CHANNEL_PATH + "ch3_activate.tga",
					"down_image" : CHANNEL_PATH + "ch3_on.tga",
				},
				{
					"name" : "btn_channel_04", "type" : "radio_button",
					"x" : 382+53*3, "y" : 643,
					"default_image" : CHANNEL_PATH + "ch4_off.tga",
					"over_image" : CHANNEL_PATH + "ch4_activate.tga",
					"down_image" : CHANNEL_PATH + "ch4_on.tga",
				},
				# Stergere Conturi	x=Orizontal y=Vertical
				{
					"name" : "btn_delete_01", "type" : "button",
					"default_image" : BTN_PATH + "stergere_00.tga",
					"x" : 1360, "y" : 440+55*1,
					"over_image" : BTN_PATH + "stergere_01.tga",
					"down_image" : BTN_PATH + "stergere_01.tga",
				},
				{
					"name" : "btn_delete_02", "type" : "button",
					"x" : 1360, "y" : 440+55*2,
					"default_image" : BTN_PATH + "stergere_00.tga",
					"over_image" : BTN_PATH + "stergere_01.tga",
					"down_image" : BTN_PATH + "stergere_01.tga",
				},
				{
					"name" : "btn_delete_03", "type" : "button",
					"x" : 1360, "y" : 440+55*3,
					"default_image" : BTN_PATH + "stergere_00.tga",
					"over_image" : BTN_PATH + "stergere_01.tga",
					"down_image" : BTN_PATH + "stergere_01.tga",
				},
				{
					"name" : "btn_delete_04", "type" : "button",
					"x" : 1360, "y" : 440+55*4,
					"default_image" : BTN_PATH + "stergere_00.tga",
					"over_image" : BTN_PATH + "stergere_01.tga",
					"down_image" : BTN_PATH + "stergere_01.tga",
				},
				# Salvare Conturi	x=Orizontal y=Vertical
				{
					"name" : "btn_add_01", "type" : "button",
					"x" : 1160, "y" : 438+55*1,
					"default_image" : BTN_PATH + "salvare_00.tga",
					"over_image" : BTN_PATH + "salvare_01.tga",
					"down_image" : BTN_PATH + "salvare_01.tga",
				},
				{
					"name" : "btn_add_02", "type" : "button",
					"x" : 1160, "y" : 438+55*2,
					"default_image" : BTN_PATH + "salvare_00.tga",
					"over_image" : BTN_PATH + "salvare_01.tga",
					"down_image" : BTN_PATH + "salvare_01.tga",
				},
				{
					"name" : "btn_add_03", "type" : "button",
					"x" : 1160, "y" : 438+55*3,
					"default_image" : BTN_PATH + "salvare_00.tga",
					"over_image" : BTN_PATH + "salvare_01.tga",
					"down_image" : BTN_PATH + "salvare_01.tga",
				},
				{
					"name" : "btn_add_04", "type" : "button",
					"x" : 1160, "y" : 438+55*4,
					"default_image" : BTN_PATH + "salvare_00.tga",
					"over_image" : BTN_PATH + "salvare_01.tga",
					"down_image" : BTN_PATH + "salvare_01.tga",
				},
				# Selectare Conturi		x=Orizontal y=Vertical
				{
					"name" : "btn_select_01", "type" : "button",
					"x" : 1188, "y" : 438+55*1,
					"default_image" : BTN_PATH + "1_button_00.tga",
					"over_image" : BTN_PATH + "1_button_01.tga",
					"down_image" : BTN_PATH + "1_button_01.tga",
				},
				{
					"name" : "text_account_01", "type" : "text",
					"x" : 1208, "y" : 451+55*1,
					"text" : "#01 - " + " Slot",
				},
				{
					"name" : "btn_select_02", "type" : "button",
					"x" : 1188, "y" : 438+55*2,
					"default_image" : BTN_PATH + "2_button_00.tga",
					"over_image" : BTN_PATH + "2_button_01.tga",
					"down_image" : BTN_PATH + "2_button_01.tga",
				},
				{
					"name" : "text_account_02", "type" : "text",
					"x" : 1208, "y" : 451+55*2,
					"text" : "#02 - " + " Slot",
				},
				{
					"name" : "btn_select_03", "type" : "button",
					"x" : 1188, "y" : 438+55*3,
					"default_image" : BTN_PATH + "3_button_00.tga",
					"over_image" : BTN_PATH + "3_button_01.tga",
					"down_image" : BTN_PATH + "3_button_01.tga",
				},
				{
					"name" : "text_account_03", "type" : "text",
					"x" : 1208, "y" : 451+55*3,
					"text" : "#03 - " + " Slot",
				},
				{
					"name" : "btn_select_04", "type" : "button",
					"x" : 1188, "y" : 438+55*4,
					"default_image" : BTN_PATH + "4_button_00.tga",
					"over_image" : BTN_PATH + "4_button_01.tga",
					"down_image" : BTN_PATH + "4_button_01.tga",
				},
				{
					"name" : "text_account_04", "type" : "text",
					"x" : 1208, "y" : 451+55*4,
					"text" : "#04 - " + " Slot",
				},
			),
		},
	),
}