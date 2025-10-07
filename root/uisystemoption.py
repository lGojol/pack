import dbg
import ui
import snd
import systemSetting
import net
import chat
import app
import localeInfo
import constInfo
import chrmgr
if app.ENABLE_GRAPHIC_ON_OFF:
	import grp
import game  # Importar módulo game para acceder a self.curtain si es necesario

import player
import musicInfo
if app.ENABLE_ENVIRONMENT_EFFECT_OPTION:
	import uiPhaseCurtain

import uiSelectMusic
import background

if app.__BL_MULTI_LANGUAGE__:
	import uiScriptLocale

MUSIC_FILENAME_MAX_LEN = 25

blockMode = 0

class OptionDialog(ui.ScriptWindow):

	if app.__BL_MULTI_LANGUAGE__:
		LANG_VIEW_COUNT = 5

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()

		if app.__BL_MULTI_LANGUAGE__:
			self.__LoadLocaleListFile()

		if app.ENABLE_ENVIRONMENT_EFFECT_OPTION:
			self.curtain = uiPhaseCurtain.PhaseCurtain()
			self.curtain.speed = 0.03
			self.curtain.Hide()

		self.__Load()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print " -------------------------------------- DELETE SYSTEM OPTION DIALOG"

	def __Initialize(self):
		if not app.ENABLE_DISABLE_SOFTWARE_TILING:
			self.tilingMode = 0
		#self.tilingMode = 0
		self.titleBar = 0
		self.changeMusicButton = 0
		self.selectMusicFile = 0
		self.ctrlMusicVolume = 0
		self.ctrlSoundVolume = 0
		self.musicListDlg = 0
		if app.ENABLE_FOG_FIX:
			self.fogButtonList = []
		if not app.ENABLE_DISABLE_SOFTWARE_TILING:
			self.tilingApplyButton = 0

		if app.ENABLE_SHADOW_RENDER_QUALITY_OPTION:
			self.shadowQualityButtonList = []
			self.shadowTargetButtonList = []

		if app.ENABLE_FOV_OPTION:
			self.fovController = None
			self.fovResetButton = None
			self.fovValueText = None
		if not app.ENABLE_DISABLE_SOFTWARE_TILING:
			self.tilingModeButtonList = []

		if app.ENABLE_GRAPHIC_ON_OFF:
			self.effectOnOffButtonList = []
			self.effectApplyButton = None
			self.effectLevelIndex = None

			self.privateShopOnOffButtonList = []
			self.privateShopApplyButton = None
			self.privateShopLevelIndex = None

			self.dropItemOnOffButtonList = []
			self.dropItemApplyButton = None
			self.dropItemLevelIndex = None

			self.petOnOffButtonList = []
			self.npcNameOnOffButtonList = []

		if app.__BL_MULTI_LANGUAGE__:
			self.language_list = []
			self.language_button_list = []
			self.language_select_is_open = False
			self.selected_language_index = -1
			self.scroll_bar = None
			self.cur_language_text_window = None
			self.cur_language_text = None
			self.language_select_button = None
			self.language_change_button = None
			self.language_select_pivot_window = None
			self.language_over_img = None
			self.language_select_window = None

		if app.__BL_MULTI_LANGUAGE_ULTIMATE__:
			self.show_country_flag_button = None
			self.show_empire_flag_button = None
			self.anonymous_button = None

		#self.tilingApplyButton = 0
		self.cameraModeButtonList = []
		self.fogModeButtonList = []
		#self.tilingModeButtonList = []
		self.ctrlShadowQuality = 0

		if app.ENABLE_ENVIRONMENT_EFFECT_OPTION:
			self.nightModeButtonList = []
			self.snowModeButtonList = []
			self.snowTextureModeButtonList = []

		self.IsShow = False

	def Destroy(self):
		self.ClearDictionary()

		self.__Initialize()
		print " -------------------------------------- DESTROY SYSTEM OPTION DIALOG"

	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("System.OptionDialog.__Load_LoadScript")

	def __Load_BindObject(self):
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("titlebar")
			self.selectMusicFile = GetObject("bgm_file")
			self.changeMusicButton = GetObject("bgm_button")
			self.ctrlMusicVolume = GetObject("music_volume_controller")
			self.ctrlSoundVolume = GetObject("sound_volume_controller")
			self.cameraModeButtonList.append(GetObject("camera_short"))
			self.cameraModeButtonList.append(GetObject("camera_long"))

			if app.__BL_MULTI_LANGUAGE__:
				self.cur_language_text_window = GetObject("cur_language_text_window")
				self.cur_language_text = GetObject("cur_language_text")
				self.language_select_button = GetObject("language_select_button")
				self.language_change_button = GetObject("language_change_button")
				self.language_select_pivot_window = GetObject("language_select_pivot_window")

			if app.__BL_MULTI_LANGUAGE_ULTIMATE__:
				self.show_country_flag_button = GetObject("show_country_flag_button")
				self.show_empire_flag_button = GetObject("show_empire_flag_button")
				self.anonymous_button = GetObject("anonymous_button")

			if app.ENABLE_FOG_FIX:
				self.fogButtonList.append(GetObject("fog_off"))
				self.fogButtonList.append(GetObject("fog_on"))
			else:
				self.fogModeButtonList.append(GetObject("fog_level0"))
				self.fogModeButtonList.append(GetObject("fog_level1"))
				self.fogModeButtonList.append(GetObject("fog_level2"))

			if not app.ENABLE_DISABLE_SOFTWARE_TILING:
				self.tilingModeButtonList.append(GetObject("tiling_cpu"))
				self.tilingModeButtonList.append(GetObject("tiling_gpu"))
				self.tilingApplyButton = GetObject("tiling_apply")

			if app.ENABLE_GRAPHIC_ON_OFF:
				for i in xrange(1, 6):
					self.effectOnOffButtonList.append(GetObject("effect_level%d" % i))
					self.privateShopOnOffButtonList.append(GetObject("privateShop_level%d" % i))
					self.dropItemOnOffButtonList.append(GetObject("dropItem_level%d" % i))

				self.effectApplyButton = GetObject("effect_apply")
				self.privateShopApplyButton = GetObject("privateShop_apply")
				self.dropItemApplyButton = GetObject("dropItem_apply")

				self.petOnOffButtonList.append(GetObject("pet_on"))
				self.petOnOffButtonList.append(GetObject("pet_off"))

				self.npcNameOnOffButtonList.append(GetObject("npcName_on"))
				self.npcNameOnOffButtonList.append(GetObject("npcName_off"))

			if app.ENABLE_FOV_OPTION:
				self.fovController = GetObject("fov_controller")
				self.fovController.SetButtonVisual("d:/ymir work/ui/game/windows/",\
					"sliderbar_cursor_button01.tga",\
					"sliderbar_cursor_button01.tga",\
					"sliderbar_cursor_button01.tga")
				self.fovController.SetBackgroundVisual("d:/ymir work/ui/game/windows/sliderbar_small.tga")
				self.fovResetButton = GetObject("fov_reset_button")
				self.fovValueText = GetObject("fov_value_text")

				if localeInfo.IsARABIC():
					self.fovController.SetPosition(234, 5)

			if app.ENABLE_SHADOW_RENDER_QUALITY_OPTION:
				self.shadowQualityButtonList.append(GetObject("shadow_quality_bad"))
				self.shadowQualityButtonList.append(GetObject("shadow_quality_average"))
				self.shadowQualityButtonList.append(GetObject("shadow_quality_good"))

				self.shadowTargetButtonList.append(GetObject("shadow_target_none"))
				self.shadowTargetButtonList.append(GetObject("shadow_target_ground"))
				self.shadowTargetButtonList.append(GetObject("shadow_target_ground_and_solo"))
				self.shadowTargetButtonList.append(GetObject("shadow_target_all"))

			if app.ENABLE_ENVIRONMENT_EFFECT_OPTION:
				self.nightModeButtonList.append(GetObject("night_mode_off"))
				self.nightModeButtonList.append(GetObject("night_mode_on"))
				self.snowModeButtonList.append(GetObject("snow_mode_off"))
				self.snowModeButtonList.append(GetObject("snow_mode_on"))
				self.snowTextureModeButtonList.append(GetObject("snow_texture_mode_off"))
				self.snowTextureModeButtonList.append(GetObject("snow_texture_mode_on"))

			# self.tilingModeButtonList.append(GetObject("tiling_cpu"))
			# self.tilingModeButtonList.append(GetObject("tiling_gpu"))
			# self.tilingApplyButton=GetObject("tiling_apply")
			#self.ctrlShadowQuality = GetObject("shadow_bar")
		except:
			import exception
			exception.Abort("OptionDialog.__Load_BindObject")

	def __Load(self):
		self.__Load_LoadScript("uiscript/systemoptiondialog.py")
		self.__Load_BindObject()

		self.SetCenterPosition()

		if app.__BL_MULTI_LANGUAGE__:
			self.__CreateLanguageSelectWindow()

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

		self.ctrlMusicVolume.SetSliderPos(float(systemSetting.GetMusicVolume()))
		self.ctrlMusicVolume.SetEvent(ui.__mem_func__(self.OnChangeMusicVolume))

		self.ctrlSoundVolume.SetSliderPos(float(systemSetting.GetSoundVolume()) / 5.0)
		self.ctrlSoundVolume.SetEvent(ui.__mem_func__(self.OnChangeSoundVolume))

#		self.ctrlShadowQuality.SetSliderPos(float(systemSetting.GetShadowLevel()) / 5.0)
#		self.ctrlShadowQuality.SetEvent(ui.__mem_func__(self.OnChangeShadowQuality))

		self.changeMusicButton.SAFE_SetEvent(self.__OnClickChangeMusicButton)

		self.cameraModeButtonList[0].SAFE_SetEvent(self.__OnClickCameraModeShortButton)
		self.cameraModeButtonList[1].SAFE_SetEvent(self.__OnClickCameraModeLongButton)

		if app.ENABLE_FOG_FIX:
			self.fogButtonList[0].SAFE_SetEvent(self.__OnClickFogModeOffButton)
			self.fogButtonList[1].SAFE_SetEvent(self.__OnClickFogModeOnButton)
		else:
			self.fogModeButtonList[0].SAFE_SetEvent(self.__OnClickFogModeLevel0Button)
			self.fogModeButtonList[1].SAFE_SetEvent(self.__OnClickFogModeLevel1Button)
			self.fogModeButtonList[2].SAFE_SetEvent(self.__OnClickFogModeLevel2Button)

		#self.tilingModeButtonList[0].SAFE_SetEvent(self.__OnClickTilingModeCPUButton)
		#self.tilingModeButtonList[1].SAFE_SetEvent(self.__OnClickTilingModeGPUButton)
		#
		#self.tilingApplyButton.SAFE_SetEvent(self.__OnClickTilingApplyButton)
		#
		#self.__SetCurTilingMode()

		if not app.ENABLE_DISABLE_SOFTWARE_TILING:
			self.tilingModeButtonList[0].SAFE_SetEvent(self.__OnClickTilingModeCPUButton)
			self.tilingModeButtonList[1].SAFE_SetEvent(self.__OnClickTilingModeGPUButton)

			self.tilingApplyButton.SAFE_SetEvent(self.__OnClickTilingApplyButton)

			self.__SetCurTilingMode()

		self.__ClickRadioButton(self.fogModeButtonList, constInfo.GET_FOG_LEVEL_INDEX())
		self.__ClickRadioButton(self.cameraModeButtonList, constInfo.GET_CAMERA_MAX_DISTANCE_INDEX())

		if app.ENABLE_FOV_OPTION:
			if self.fovController:
				self.fovController.SetSliderPos(float(systemSetting.GetFOV()) / float(app.MAX_CAMERA_PERSPECTIVE))
				self.fovController.SetEvent(ui.__mem_func__(self.__OnChangeFOV))

			if self.fovValueText:
				self.fovValueText.SetText(str(int(systemSetting.GetFOV())))

			if self.fovResetButton:
				self.fovResetButton.SetEvent(ui.__mem_func__(self.__OnClickFOVResetButton))

		if app.ENABLE_FOG_FIX:
			self.__ClickRadioButton(self.fogButtonList, background.GetFogMode())

		if app.ENABLE_GRAPHIC_ON_OFF:
			self.__ClickRadioButton(self.effectOnOffButtonList, grp.GetEffectOnOffLevel())
			self.__ClickRadioButton(self.privateShopOnOffButtonList, grp.GetPrivateShopOnOffLevel())
			self.__ClickRadioButton(self.dropItemOnOffButtonList, grp.GetDropItemOnOffLevel())

			self.__ClickRadioButton(self.petOnOffButtonList, grp.GetPetOnOffStatus())
			self.__ClickRadioButton(self.npcNameOnOffButtonList, grp.GetNPCNameOnOffStatus())

		if app.ENABLE_SHADOW_RENDER_QUALITY_OPTION:
			self.shadowQualityButtonList[background.SHADOW_QUALITY_BAD].SAFE_SetEvent(self.__OnClickChangeShadowQuality, background.SHADOW_QUALITY_BAD)
			self.shadowQualityButtonList[background.SHADOW_QUALITY_AVERAGE].SAFE_SetEvent(self.__OnClickChangeShadowQuality, background.SHADOW_QUALITY_AVERAGE)
			self.shadowQualityButtonList[background.SHADOW_QUALITY_GOOD].SAFE_SetEvent(self.__OnClickChangeShadowQuality, background.SHADOW_QUALITY_GOOD)
			self.__ClickRadioButton(self.shadowQualityButtonList, systemSetting.GetShadowQualityLevel())

			self.shadowTargetButtonList[background.SHADOW_TARGET_NONE].SAFE_SetEvent(self.__OnClickChangeShadowTarget, background.SHADOW_TARGET_NONE)
			self.shadowTargetButtonList[background.SHADOW_TARGET_GROUND].SAFE_SetEvent(self.__OnClickChangeShadowTarget, background.SHADOW_TARGET_GROUND)
			self.shadowTargetButtonList[background.SHADOW_TARGET_GROUND_AND_SOLO].SAFE_SetEvent(self.__OnClickChangeShadowTarget, background.SHADOW_TARGET_GROUND_AND_SOLO)
			self.shadowTargetButtonList[background.SHADOW_TARGET_ALL].SAFE_SetEvent(self.__OnClickChangeShadowTarget, background.SHADOW_TARGET_ALL)
			self.__ClickRadioButton(self.shadowTargetButtonList, systemSetting.GetShadowTargetLevel())

		if app.__BL_MULTI_LANGUAGE__:
			self.language_select_button.SetEvent( ui.__mem_func__(self.__OnClickLanguageSelectButton) )
			self.cur_language_text_window.SetOnMouseLeftButtonUpEvent( ui.__mem_func__(self.__OnClickLanguageSelectButton) )
			self.language_change_button.SetEvent( ui.__mem_func__(self.__OnClickLanguageChangeButton) )

		if app.__BL_MULTI_LANGUAGE_ULTIMATE__:
			self.show_country_flag_button.SetToggleDownEvent(ui.__mem_func__(self.__EventShowFlags), "country")
			self.show_country_flag_button.SetToggleUpEvent(ui.__mem_func__(self.__EventShowFlags), "country")

			self.show_empire_flag_button.SetToggleDownEvent(ui.__mem_func__(self.__EventShowFlags), "empire")
			self.show_empire_flag_button.SetToggleUpEvent(ui.__mem_func__(self.__EventShowFlags), "empire")

			self.anonymous_button.SetEvent( ui.__mem_func__(self.__OnClickAnonymousButton) )

			self.RefreshLanguageSettings()

		if musicInfo.fieldMusic==musicInfo.METIN2THEMA:
			self.selectMusicFile.SetText(uiSelectMusic.DEFAULT_THEMA)
		else:
			self.selectMusicFile.SetText(musicInfo.fieldMusic[:MUSIC_FILENAME_MAX_LEN])

		if app.ENABLE_GRAPHIC_ON_OFF:
			for i in range(5):
				self.effectOnOffButtonList[i].SAFE_SetEvent(self.__OnClickEffectLevelButton, i)
				self.privateShopOnOffButtonList[i].SAFE_SetEvent(self.__OnClickPrivateShopLevelButton, i)
				self.dropItemOnOffButtonList[i].SAFE_SetEvent(self.__OnClickDropItemLevelButton, i)

			self.effectApplyButton.SAFE_SetEvent(self.__OnClickEffectApplyButton)
			self.privateShopApplyButton.SAFE_SetEvent(self.__OnClickPrivateShopApplyButton)
			self.dropItemApplyButton.SAFE_SetEvent(self.__OnClickDropItemApplyButton)

			self.petOnOffButtonList[0].SAFE_SetEvent(self.__OnClickPetButton, 0)
			self.petOnOffButtonList[1].SAFE_SetEvent(self.__OnClickPetButton, 1)

			self.npcNameOnOffButtonList[0].SAFE_SetEvent(self.__OnClickNPCNameButton, 0)
			self.npcNameOnOffButtonList[1].SAFE_SetEvent(self.__OnClickNPCNameButton, 1)

		if app.ENABLE_ENVIRONMENT_EFFECT_OPTION:
			self.nightModeButtonList[0].SAFE_SetEvent(self.__OnClickNightModeOffButton)
			self.nightModeButtonList[1].SAFE_SetEvent(self.__OnClickNightModeOnButton)
			self.__InitNightModeOption()

			self.snowModeButtonList[0].SAFE_SetEvent(self.__OnClickSnowModeOffButton)
			self.snowModeButtonList[1].SAFE_SetEvent(self.__OnClickSnowModeOnButton)
			self.__InitSnowModeOption()

			self.snowTextureModeButtonList[0].SAFE_SetEvent(self.__OnClickSnowTextureModeOffButton)
			self.snowTextureModeButtonList[1].SAFE_SetEvent(self.__OnClickSnowTextureModeOnButton)
			self.__InitSnowTextureModeOption()

	#def __OnClickTilingModeCPUButton(self):
	#	self.__NotifyChatLine(localeInfo.SYSTEM_OPTION_CPU_TILING_1)
	#	self.__NotifyChatLine(localeInfo.SYSTEM_OPTION_CPU_TILING_2)
	#	self.__NotifyChatLine(localeInfo.SYSTEM_OPTION_CPU_TILING_3)
	#	self.__SetTilingMode(0)
	#
	#def __OnClickTilingModeGPUButton(self):
	#	self.__NotifyChatLine(localeInfo.SYSTEM_OPTION_GPU_TILING_1)
	#	self.__NotifyChatLine(localeInfo.SYSTEM_OPTION_GPU_TILING_2)
	#	self.__NotifyChatLine(localeInfo.SYSTEM_OPTION_GPU_TILING_3)
	#	self.__SetTilingMode(1)
	#
	#def __OnClickTilingApplyButton(self):
	#	self.__NotifyChatLine(localeInfo.SYSTEM_OPTION_TILING_EXIT)
	#	if 0==self.tilingMode:
	#		background.EnableSoftwareTiling(1)
	#	else:
	#		background.EnableSoftwareTiling(0)
	#
	#	net.ExitGame()

	if not app.ENABLE_DISABLE_SOFTWARE_TILING:
		def __OnClickTilingModeCPUButton(self):
			self.__NotifyChatLine(localeInfo.SYSTEM_OPTION_CPU_TILING_1)
			self.__NotifyChatLine(localeInfo.SYSTEM_OPTION_CPU_TILING_2)
			self.__NotifyChatLine(localeInfo.SYSTEM_OPTION_CPU_TILING_3)
			self.__SetTilingMode(0)

		def __OnClickTilingModeGPUButton(self):
			self.__NotifyChatLine(localeInfo.SYSTEM_OPTION_GPU_TILING_1)
			self.__NotifyChatLine(localeInfo.SYSTEM_OPTION_GPU_TILING_2)
			self.__NotifyChatLine(localeInfo.SYSTEM_OPTION_GPU_TILING_3)
			self.__SetTilingMode(1)

		def __OnClickTilingApplyButton(self):
			self.__NotifyChatLine(localeInfo.SYSTEM_OPTION_TILING_EXIT)
			if 0 == self.tilingMode:
				background.EnableSoftwareTiling(1)
			else:
				background.EnableSoftwareTiling(0)

			net.ExitGame()

	def __OnClickChangeMusicButton(self):
		if not self.musicListDlg:

			self.musicListDlg=uiSelectMusic.FileListDialog()
			self.musicListDlg.SAFE_SetSelectEvent(self.__OnChangeMusic)

		self.musicListDlg.Open()


	def __ClickRadioButton(self, buttonList, buttonIndex):
		try:
			selButton=buttonList[buttonIndex]
		except IndexError:
			return

		for eachButton in buttonList:
			eachButton.SetUp()

		selButton.Down()


	#def __SetTilingMode(self, index):
	#	self.__ClickRadioButton(self.tilingModeButtonList, index)
	#	self.tilingMode=index

	def __SetCameraMode(self, index):
		constInfo.SET_CAMERA_MAX_DISTANCE_INDEX(index)
		self.__ClickRadioButton(self.cameraModeButtonList, index)

	def __SetFogLevel(self, index):
		constInfo.SET_FOG_LEVEL_INDEX(index)
		self.__ClickRadioButton(self.fogModeButtonList, index)

	def __OnClickCameraModeShortButton(self):
		self.__SetCameraMode(0)

	def __OnClickCameraModeLongButton(self):
		self.__SetCameraMode(1)

	def __OnClickFogModeLevel0Button(self):
		self.__SetFogLevel(0)

	def __OnClickFogModeLevel1Button(self):
		self.__SetFogLevel(1)

	def __OnClickFogModeLevel2Button(self):
		self.__SetFogLevel(2)

	if app.ENABLE_FOG_FIX:
		def __OnClickFogModeOnButton(self):
			background.SetFogMode(True)
			self.__ClickRadioButton(self.fogButtonList, 1)

		def __OnClickFogModeOffButton(self):
			background.SetFogMode(False)
			self.__ClickRadioButton(self.fogButtonList, 0)

	def __OnChangeMusic(self, fileName):
		self.selectMusicFile.SetText(fileName[:MUSIC_FILENAME_MAX_LEN])

		if musicInfo.fieldMusic != "":
			snd.FadeOutMusic("BGM/"+ musicInfo.fieldMusic)

		if fileName==uiSelectMusic.DEFAULT_THEMA:
			musicInfo.fieldMusic=musicInfo.METIN2THEMA
		else:
			musicInfo.fieldMusic=fileName

		musicInfo.SaveLastPlayFieldMusic()

		if musicInfo.fieldMusic != "":
			snd.FadeInMusic("BGM/" + musicInfo.fieldMusic)

	if app.ENABLE_SHADOW_RENDER_QUALITY_OPTION:
		def __OnClickChangeShadowQuality(self, shadow_quality):
			self.__ClickRadioButton(self.shadowQualityButtonList, shadow_quality)
			self.__SetShadowQualityLevel(shadow_quality)

		def __SetShadowQualityLevel(self, index):
			systemSetting.SetShadowQualityLevel(index)
			background.SetShadowQualityLevel(index)

		def __OnClickChangeShadowTarget(self, shadow_target):
			self.__ClickRadioButton(self.shadowTargetButtonList, shadow_target)
			self.__SetShadowTargetLevel(shadow_target)

		def __SetShadowTargetLevel(self, index):
			systemSetting.SetShadowTargetLevel(index)
			background.SetShadowTargetLevel(index)

	if app.ENABLE_ENVIRONMENT_EFFECT_OPTION:
		def __InitNightModeOption(self):
			if not hasattr(self, 'nightModeButtonList') or not self.nightModeButtonList:
				return
			self.NightModeOn = systemSetting.GetNightModeOption()
			self.__ClickRadioButton(self.nightModeButtonList, self.NightModeOn)
			background.SetNightModeOption(self.NightModeOn)
			self.__SetNightMode(self.NightModeOn)
	
		def __InitSnowModeOption(self):
			if not hasattr(self, 'snowModeButtonList') or not self.snowModeButtonList:
				return
			self.SnowModeOn = systemSetting.GetSnowModeOption()
			self.__ClickRadioButton(self.snowModeButtonList, self.SnowModeOn)
			background.SetSnowModeOption(self.SnowModeOn)
			background.EnableSnowMode(self.SnowModeOn)
	
		def __InitSnowTextureModeOption(self):
			if not hasattr(self, 'snowTextureModeButtonList') or not self.snowTextureModeButtonList:
				return
			self.SnowTextureModeOn = systemSetting.GetSnowTextureModeOption()
			self.__ClickRadioButton(self.snowTextureModeButtonList, self.SnowTextureModeOn)
			background.SetSnowTextureModeOption(self.SnowTextureModeOn)
			background.EnableSnowTextureMode()
	
		def __OnClickNightModeOffButton(self):
			self.__ClickRadioButton(self.nightModeButtonList, 0)
			self.__SetNightMode(0)
	
		def __OnClickNightModeOnButton(self):
			self.__ClickRadioButton(self.nightModeButtonList, 1)
			self.__SetNightMode(1)
	
		def __OnClickSnowModeOffButton(self):
			self.__ClickRadioButton(self.snowModeButtonList, 0)
			self.__SetSnowMode(0)
	
		def __OnClickSnowModeOnButton(self):
			self.__ClickRadioButton(self.snowModeButtonList, 1)
			self.__SetSnowMode(1)
	
		def __OnClickSnowTextureModeOffButton(self):
			self.__ClickRadioButton(self.snowTextureModeButtonList, 0)
			self.__SetSnowTextureMode(0)
	
		def __OnClickSnowTextureModeOnButton(self):
			self.__ClickRadioButton(self.snowTextureModeButtonList, 1)
			self.__SetSnowTextureMode(1)
	
		def __SetNightMode(self, index):
			systemSetting.SetNightModeOption(index)
			background.SetNightModeOption(index)
			try:
				systemSetting.SaveConfig()
			except AttributeError:
				pass
	
			if not hasattr(self, 'curtain'):
				try:
					import game
					self.curtain = game.GameWindow.curtain
				except (AttributeError, ImportError):
					return
	
			if index == 1:
				self.__DayMode_Update("dark")
			else:
				self.__DayMode_Update("light")
	
		def __SetSnowMode(self, index):
			systemSetting.SetSnowModeOption(index)
			background.SetSnowModeOption(index)
			background.EnableSnowMode(index)
	
		def __SetSnowTextureMode(self, index):
			systemSetting.SetSnowTextureModeOption(index)
			background.SetSnowTextureModeOption(index)
			background.EnableSnowTextureMode()
	
		def __DayMode_Update(self, mode):
			if not hasattr(self, 'curtain'):
				try:
					import game
					self.curtain = game.GameWindow.curtain
				except (AttributeError, ImportError):
					return
	
			if "light" == mode:
				self.curtain.SAFE_FadeOut(self.__DayMode_OnCompleteChangeToLight)
			elif "dark" == mode:
				self.curtain.SAFE_FadeOut(self.__DayMode_OnCompleteChangeToDark)
	
		def __DayMode_OnCompleteChangeToLight(self):
			background.SetEnvironmentData(0)
			self.curtain.FadeIn()
	
		def __DayMode_OnCompleteChangeToDark(self):
			background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
			background.SetEnvironmentData(1)
			self.curtain.FadeIn()
	
		def __PRESERVE_DayMode_Update(self, mode):
			if app.ENABLE_ENVIRONMENT_EFFECT_OPTION:
				if not background.IsBoomMap():
					return
			else:
				if not self.__IsXMasMap():
					return
	
			if "light" == mode:
				background.SetEnvironmentData(background.DAY_MODE_LIGHT)
			elif "dark" == mode:
				background.RegisterEnvironmentData(background.DAY_MODE_DARK, constInfo.ENVIRONMENT_NIGHT)
				background.SetEnvironmentData(background.DAY_MODE_DARK)
	
		def __XMasBoom_Update(self):
			self.BOOM_DATA_LIST = ((2, 5), (5, 2), (7, 3), (10, 3), (20, 5))
			if self.indexXMasBoom >= len(self.BOOM_DATA_LIST):
				return
	
			boomTime = self.BOOM_DATA_LIST[self.indexXMasBoom][0]
			boomCount = self.BOOM_DATA_LIST[self.indexXMasBoom][1]
	
			if app.GetTime() - self.startTimeXMasBoom > boomTime:
				self.indexXMasBoom += 1
				for i in range(boomCount):
					self.__XMasBoom_Boom()
	
		def __XMasBoom_Boom(self):
			x, y, z = player.GetMainCharacterPosition()
			randX = app.GetRandom(-150, 150)
			randY = app.GetRandom(-150, 150)
			snd.PlaySound3D(x + randX, -y + randY, z, "sound/common/etc/salute.mp3")
	
		def __XMasBoom_Enable(self, mode):
			if "1" == mode:
				if app.ENABLE_ENVIRONMENT_EFFECT_OPTION:
					if not background.IsBoomMap():
						return
				else:
					if not self.__IsXMasMap():
						return
	
				self.__DayMode_Update("dark")
				self.enableXMasBoom = True
				self.startTimeXMasBoom = app.GetTime()
			else:
				self.__DayMode_Update("light")
				self.enableXMasBoom = False
	
		def __IsXMasMap(self):
			return True

	if app.ENABLE_GRAPHIC_ON_OFF:
		# Effect
		def __OnClickEffectLevelButton(self, effectLevelIdx):
			self.__ClickRadioButton(self.effectOnOffButtonList, effectLevelIdx)
			self.effectLevelIndex = effectLevelIdx

		def __OnClickEffectApplyButton(self):
			grp.SetEffectOnOffLevel(self.effectLevelIndex)

		# PrivateShop
		def __OnClickPrivateShopLevelButton(self, privateShopLevelIdx):
			self.__ClickRadioButton(self.privateShopOnOffButtonList, privateShopLevelIdx)
			self.privateShopLevelIndex = privateShopLevelIdx

		def __OnClickPrivateShopApplyButton(self):
			grp.SetPrivateShopOnOffLevel(self.privateShopLevelIndex)

		# DropItem
		def __OnClickDropItemLevelButton(self, dropItemLevelIdx):
			self.__ClickRadioButton(self.dropItemOnOffButtonList, dropItemLevelIdx)
			self.dropItemLevelIndex = dropItemLevelIdx

		def __OnClickDropItemApplyButton(self):
			grp.SetDropItemOnOffLevel(self.dropItemLevelIndex)

		# Pet
		def __OnClickPetButton(self, buttonIndex):
			self.__ClickRadioButton(self.petOnOffButtonList, buttonIndex)
			grp.SetPetOnOffStatus(buttonIndex)

		# NPC
		def __OnClickNPCNameButton(self, buttonIndex):
			self.__ClickRadioButton(self.npcNameOnOffButtonList, buttonIndex)
			grp.SetNPCNameOnOffStatus(buttonIndex)

	if app.ENABLE_FOV_OPTION:
		def __OnChangeFOV(self):
			pos = self.fovController.GetSliderPos()
			systemSetting.SetFOV(pos * float(app.MAX_CAMERA_PERSPECTIVE))

			if self.fovValueText:
				self.fovValueText.SetText(str(int(systemSetting.GetFOV())))

		def __OnClickFOVResetButton(self):
			self.fovController.SetSliderPos(float(app.DEFAULT_CAMERA_PERSPECTIVE) / float(app.MAX_CAMERA_PERSPECTIVE))
			systemSetting.SetFOV(float(app.DEFAULT_CAMERA_PERSPECTIVE))

			if self.fovValueText:
				self.fovValueText.SetText(str(int(systemSetting.GetFOV())))

	def OnChangeMusicVolume(self):
		pos = self.ctrlMusicVolume.GetSliderPos()
		snd.SetMusicVolume(pos * net.GetFieldMusicVolume())
		systemSetting.SetMusicVolume(pos)

	def OnChangeSoundVolume(self):
		pos = self.ctrlSoundVolume.GetSliderPos()
		snd.SetSoundVolumef(pos)
		systemSetting.SetSoundVolumef(pos)

	def OnChangeShadowQuality(self):
		pos = self.ctrlShadowQuality.GetSliderPos()
		systemSetting.SetShadowLevel(int(pos / 0.2))

	def OnCloseInputDialog(self):
		self.inputDialog.Close()
		self.inputDialog = None
		return True

	def OnCloseQuestionDialog(self):
		self.questionDialog.Close()
		self.questionDialog = None
		return True

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Show(self):
		ui.ScriptWindow.Show(self)

		if app.__BL_MULTI_LANGUAGE__:
			self.__LanguageSelectShowHide(False)
			self.selected_language_index = -1
			self.cur_language_text.SetText(self.__GetStringCurLanguage())

	def Close(self):
		#self.__SetCurTilingMode()
		if not app.ENABLE_DISABLE_SOFTWARE_TILING:
			self.__SetCurTilingMode()

		self.Hide()
		if app.__BL_MULTI_LANGUAGE__:
			self.__LanguageSelectShowHide(False)

		self.IsShow = False

	#def __SetCurTilingMode(self):
	#	if background.IsSoftwareTiling():
	#		self.__SetTilingMode(0)
	#	else:
	#		self.__SetTilingMode(1)

	if not app.ENABLE_DISABLE_SOFTWARE_TILING:
		def __SetCurTilingMode(self):
			if background.IsSoftwareTiling():
				self.__SetTilingMode(0)
			else:
				self.__SetTilingMode(1)

	def __NotifyChatLine(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, text)

	if app.__BL_MULTI_LANGUAGE__:
		def OnTop(self):
			if self.language_select_window:
				self.language_select_window.SetTop()

		def OnMoveWindow(self, x, y):
			if self.language_select_window and self.language_select_pivot_window:
				(x, y) = self.language_select_pivot_window.GetGlobalPosition()
				self.language_select_window.SetPosition(x, y)

		def __AdjustLanguageSelectWindowPosition(self):
			pos = int(self.scroll_bar.GetPos() * self.Diff)

			for i in xrange(len(self.language_button_list)) :
				idx = i + pos
				if idx >= len(self.language_list):
					return

				text = self.language_list[idx]["name"]
				self.language_button_list[i].SetText(text)
				self.language_button_list[i].SetEvent(ui.__mem_func__(self.__OnClickLanguageSelect), idx)
				self.language_button_list[i].SetOverEvent(ui.__mem_func__(self.__OnClickLanguageButtonOver), i)
				self.language_button_list[i].SetOverOutEvent(ui.__mem_func__(self.__OnClickLanguageButtonOverOut), i)

		def __CreateLanguageSelectWindow(self):
			self.language_select_window = ui.Window()
			self.language_select_window.AddFlag("float")
			self.language_select_window.SetSize(210, 80)
			(x, y) = self.language_select_pivot_window.GetGlobalPosition()
			self.language_select_window.SetPosition(x, y)

			count = min(self.LANG_VIEW_COUNT, len(self.language_list))
			for i in range(count):
				btn = ui.Button()
				btn.SetParent(self.language_select_window)
				btn.SetPosition(0, i * 15)
				if i == 0:
					btn.SetUpVisual("d:/ymir work/ui/quest_re/button_top.sub")
					btn.SetDownVisual("d:/ymir work/ui/quest_re/button_top.sub")
					btn.SetOverVisual("d:/ymir work/ui/quest_re/button_top.sub")
				elif i == (count - 1):
					btn.SetUpVisual("d:/ymir work/ui/quest_re/button_bottom.sub")
					btn.SetDownVisual("d:/ymir work/ui/quest_re/button_bottom.sub")
					btn.SetOverVisual("d:/ymir work/ui/quest_re/button_bottom.sub")
				else:
					btn.SetUpVisual("d:/ymir work/ui/quest_re/button_middle.sub")
					btn.SetDownVisual("d:/ymir work/ui/quest_re/button_middle.sub")
					btn.SetOverVisual("d:/ymir work/ui/quest_re/button_middle.sub")
				btn.Show()
				self.language_button_list.append(btn)

			self.language_over_img = ui.ImageBox()
			self.language_over_img.LoadImage("d:/ymir work/ui/quest_re/button_over.sub")
			self.language_over_img.SetParent(self.language_select_window)
			self.language_over_img.AddFlag("not_pick")

			self.scroll_bar = ui.ScrollBar()
			self.scroll_bar.SetParent(self.language_select_window)
			self.scroll_bar.AddFlag("float")
			self.scroll_bar.SetPosition(195, 0)
			self.scroll_bar.SetScrollBarSize(75)
			self.scroll_bar.SetScrollEvent(ui.__mem_func__(self.__OnLanguageSelectScroll))

			self.Diff = len(self.language_list) - self.LANG_VIEW_COUNT
			stepSize = 1.0 / self.Diff
			self.scroll_bar.SetScrollStep( stepSize )

			self.__AdjustLanguageSelectWindowPosition()

		def __LanguageSelectShowHide(self, is_show):
			self.language_select_is_open = is_show

			if True == is_show:
				self.language_select_window.Show()

				if self.LANG_VIEW_COUNT < len(self.language_list):
					self.scroll_bar.SetPos(0.0)
					self.scroll_bar.Show()
				else:
					self.scroll_bar.Hide()
			else:
				self.language_select_window.Hide()
				self.scroll_bar.Hide()

		def __LoadLocaleListFile(self):
			try:
				with open("locale_list.txt", "rt") as file:
					lines = file.readlines()
			except:
				import dbg
				dbg.LogBox("__LoadLocaleListFile error locale_list.txt")
				app.Abort()

			lineIndex = 1
			for line in lines:
				try:
					tokens = line[:-1].split(" ")
					if len(tokens) == 3:
						name = tokens[0]
						code_page = tokens[1]
						locale = tokens[2]

						if locale in uiScriptLocale.LOCALE_NAME_DICT:
							name = uiScriptLocale.LOCALE_NAME_DICT[locale]

						self.language_list.append({"name" : name, "code_page" : code_page, "locale" : locale})
					else:
						raise RuntimeError, "Unknown TokenSize"

					lineIndex += 1
				except:
					import dbg
					dbg.LogBox("%s: line(%d): %s" % ("locale_list.txt", lineIndex, line), "Error")
					raise

		def __OnClickLanguageButtonOver(self, index):
			if index >= len(self.language_button_list):
				return

			btn = self.language_button_list[index]
			(x, y) = btn.GetLocalPosition()
			self.language_over_img.SetPosition(x, y)
			self.language_over_img.Show()

		def __OnClickLanguageButtonOverOut(self, index):
			self.language_over_img.Hide()

		def __OnClickLanguageChangeButton(self):
			if self.__GetStringCurLanguage() == self.cur_language_text.GetText():
				return

			net.SendChatPacket("/language_change")

		def __OnClickLanguageSelect(self, index):
			if index >= len(self.language_list):
				return

			self.__LanguageSelectShowHide( False )
			self.selected_language_index = index

			if self.cur_language_text:
				self.cur_language_text.SetText( self.language_list[index]["name"] )

		def __OnClickLanguageSelectButton(self):
			self.__LanguageSelectShowHide( not self.language_select_is_open )

		def __OnLanguageSelectScroll(self):
			self.__AdjustLanguageSelectWindowPosition()

		def __SaveLoca(self, code_page, locale):
			try:
				with open("loca.cfg", "wt") as file:
					file.write("{} {}".format(code_page, locale))
			except:
				import dbg
				dbg.LogBox("__SaveLoca error")
				app.Abort()

		def __GetStringCurLanguage(self):
			cur_locale = app.GetLocaleName()
			for lang in self.language_list:
				if lang["locale"] == cur_locale:
					return lang["name"]

			return "-"

		def LanguageChange(self):
			if self.selected_language_index == -1:
				return

			if self.selected_language_index >= len(self.language_list):
				return

			lang = self.language_list[self.selected_language_index]
			self.__SaveLoca(lang["code_page"], lang["locale"])
			app.SetReloadLocale(True)

	if app.__BL_MULTI_LANGUAGE_ULTIMATE__:
		def __EventShowFlags(self, type):
			if type == "country":
				systemSetting.SetShowCountryFlag(not systemSetting.IsShowCountryFlag())
			elif type == "empire":
				systemSetting.SetShowEmpireFlag(not systemSetting.IsShowEmpireFlag())

			self.RefreshLanguageSettings()

		def __OnClickAnonymousButton(self):
			net.SendChatPacket("/language_anonymous")

		def LanguageChangeAnonymous(self):
			systemSetting.SetAnonymousCountryMode(not systemSetting.GetAnonymousCountryMode())
			self.RefreshLanguageSettings()

		def RefreshLanguageSettings(self):
			if systemSetting.IsShowCountryFlag():
				self.show_country_flag_button.Down()
			else:
				self.show_country_flag_button.SetUp()

			if systemSetting.IsShowEmpireFlag():
				self.show_empire_flag_button.Down()
			else:
				self.show_empire_flag_button.SetUp()

			if systemSetting.GetAnonymousCountryMode():
				self.anonymous_button.SetText(uiScriptLocale.LANGUAGE_SETTINGS_ANON_OFF)
			else:
				self.anonymous_button.SetText(uiScriptLocale.LANGUAGE_SETTINGS_ANON_ON)
