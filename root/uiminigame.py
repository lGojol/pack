import ui
import uiScriptLocale
import wndMgr
import player
import localeInfo
import net
import app
import constInfo

button_gap = 10 ## 버튼과 버튼 사이 공간
button_height = 25

if app.ENABLE_MINI_GAME_RUMI:
	import uiMiniGameRumi
	MINIGAME_RUMI = player.MINIGAME_RUMI

if app.ENABLE_MINI_GAME_CATCH_KING:
	import uiMiniGameCatchKing
	MINIGAME_CATCHKING = player.MINIGAME_CATCHKING

if app.ENABLE_SNOWFLAKE_STICK_EVENT:
	import uiSnowflakeStickEvent, chat
	SNOWFLAKE_STICK_EVENT = player.SNOWFLAKE_STICK_EVENT

MINIGAME_TYPE_MAX = player.MINIGAME_TYPE_MAX

class MiniGameDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = 0

		self.board = None
		self.close_button = None

		self.button_dict = {}

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		self.Destroy()

	def Destroy(self):
		self.isLoaded = 0

		self.board = None
		self.close_button = None

		self.button_dict = {}

	def Open(self):
		self.Show()

	def Show(self):
		self.__LoadWindow()
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/MiniGameDialog.py")
		except:
			import exception
			exception.Abort("MiniGameDialog.LoadWindow.LoadObject")

		try:
			self.board = self.GetChild("board")
			self.close_button = self.GetChild("close_button")
			self.close_button.SetEvent(ui.__mem_func__(self.Close))

		except:
			import exception
			exception.Abort("MiniGameDialog.LoadWindow.BindObject")

		self.Hide()

	def AppendButton(self, name, func):
		if self.button_dict.has_key(name):
			return

		button = ui.Button()
		button.SetParent(self.board)
		button_count = len(self.button_dict)
		pos_y = (button_gap * (button_count + 1)) + button_count * button_height
		button.SetPosition(10, pos_y)
		button.SetUpVisual("d:/ymir work/ui/public/XLarge_Button_01.sub")
		button.SetOverVisual("d:/ymir work/ui/public/XLarge_Button_02.sub")
		button.SetDownVisual("d:/ymir work/ui/public/XLarge_Button_03.sub")

		if name:
			button.SetText(name)

		if func:
			button.SetEvent(ui.__mem_func__(func))

		button.Show()
		self.button_dict[name] = button

	def DeleteButton(self, name):
		if not self.button_dict.has_key(name):
			return

		self.button_dict[name].Hide()
		del self.button_dict[name]

	def DeleteAllButton(self):
		for button in self.button_dict.values():
			button.Hide()
			del button

		self.button_dict.clear()

	def RefreshDialog(self):
		## board 의 height 값 계산
		## self.button_dict 에는 close 버튼이 포함되어 있지 않기 때문에 + 1 해준다.
		total_len = len(self.button_dict) + 1
		board_height = (button_height * total_len) + (button_gap * (total_len + 1))
		self.board.SetSize(200, board_height)
		self.SetSize(200, board_height)

		## close 버튼의 위치 갱신
		dict_len = len(self.button_dict)
		pos_y = (button_gap * (dict_len + 1)) + dict_len * button_height

		if localeInfo.IsARABIC():
			(lx, ly) = self.close_button.GetLocalPosition()
			self.close_button.SetPosition(lx, pos_y)
		else:
			self.close_button.SetPosition(10, pos_y)

# Mini Game Button Area
class MiniGameWindow(ui.ScriptWindow):
	def __init__(self):
		self.isLoaded = 0

		self.mini_game_dialog = None
		self.isshow_mini_game_dialog = False

		if app.ENABLE_MINI_GAME_RUMI:
			self.rumi_game = None

		if app.ENABLE_MINI_GAME_CATCH_KING:
			self.catch_king_game = None

		if app.ENABLE_SNOWFLAKE_STICK_EVENT:
			self.snowflake_stick_event = None

		self.game_type = MINIGAME_TYPE_MAX
		self.tooltipitem = None

		ui.ScriptWindow.__init__(self)

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.__LoadWindow()
		ui.ScriptWindow.Show(self)

		if self.mini_game_dialog and self.isshow_mini_game_dialog:
			self.mini_game_dialog.Show()

	def Close(self):
		self.Hide()

	def Hide(self):
		if self.mini_game_dialog:
			self.isshow_mini_game_dialog = self.mini_game_dialog.IsShow()
			self.mini_game_dialog.Hide()

		wndMgr.Hide(self.hWnd)

	def Destroy(self):
		self.isLoaded = 0

		if app.ENABLE_MINI_GAME_RUMI:
			if self.rumi_game:
				self.rumi_game.Destroy()
				self.rumi_game = None

		if app.ENABLE_MINI_GAME_CATCH_KING:
			if self.catch_king_game:
				self.catch_king_game.Destroy()
				self.catch_king_game = None

		if app.ENABLE_SNOWFLAKE_STICK_EVENT:
			if self.snowflake_stick_event:
				self.snowflake_stick_event.Destroy()
				self.snowflake_stick_event = None

		self.game_type = MINIGAME_TYPE_MAX
		self.tooltipitem = None

	def SetItemToolTip(self, tooltip):
		self.tooltipitem = tooltip

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			self.__LoadScript("UIScript/MiniGameWindow.py")
		except:
			import exception
			exception.Abort("MiniGameWindow.LoadWindow.LoadObject")

		try:
			## 2015 크리스마스 이벤트 미니게임 Okey
			self.GetChild("minigame_rumi_button").Hide()
			self.GetChild("minigame_rumi_button_effect").Hide()
		except:
			import exception
			exception.Abort("MiniGameWindow.LoadWindow.Okey.BindObject")

		try:
			mini_game_window = self.GetChild("mini_game_window")
			self.event_banner_button = ui.Button()
			self.event_banner_button.SetParent(mini_game_window)
			self.event_banner_button.SetPosition(0, 0)
			self.event_banner_button.SetUpVisual("d:/ymir work/ui/minigame/banner.sub")
			self.event_banner_button.SetOverVisual("d:/ymir work/ui/minigame/banner.sub")
			self.event_banner_button.SetDownVisual("d:/ymir work/ui/minigame/banner.sub")
			self.event_banner_button.SetEvent(ui.__mem_func__(self.__ClickIntegrationEventBannerButton))
			self.event_banner_button.Hide()
			self.event_banner_button_enable = False
		except:
			import exception
			exception.Abort("MiniGameWindow.LoadWindow.EventBannerButton.BindObject")

		try:
			## Mini Game Integration Event Button Dialog
			self.mini_game_dialog = MiniGameDialog()
			self.mini_game_dialog.Hide()
		except:
			import exception
			exception.Abort("MiniGameWindow.LoadWindow.MiniGameDialog")

		self.Show()

	def __LoadScript(self, fileName):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, fileName)

	def __ClickIntegrationEventBannerButton(self):
		if not self.mini_game_dialog:
			return

		if self.mini_game_dialog.IsShow():
			self.mini_game_dialog.Close()
		else:
			self.mini_game_dialog.Show()

	def IntegrationMiniGame(self, enable):
		if enable:
			self.event_banner_button.Show()
			self.event_banner_button_enable = True
		else:
			self.event_banner_button.Hide()
			self.event_banner_button_enable = False

		if app.ENABLE_MINI_GAME_RUMI:
			if self.rumi_game:
				self.rumi_game.Destroy()
				self.rumi_game = None

		if app.ENABLE_MINI_GAME_CATCH_KING:
			if self.catch_king_game:
				self.catch_king_game.Destroy()
				self.catch_king_game = None

		if app.ENABLE_SNOWFLAKE_STICK_EVENT:
			if self.snowflake_stick_event:
				self.snowflake_stick_event.Destroy()
				self.snowflake_stick_event = None

		if self.mini_game_dialog:
			self.mini_game_dialog.DeleteAllButton()

			if False == enable:
				self.mini_game_dialog.Hide()
			else:
				if app.ENABLE_MINI_GAME_RUMI:
					if player.GetRumiGame():
						self.mini_game_dialog.AppendButton(uiScriptLocale.BANNER_OKEY_BUTTON, self.__ClickRumiButton)

				if app.ENABLE_MINI_GAME_CATCH_KING:
					if player.GetCatchKingGame():
						self.mini_game_dialog.AppendButton(uiScriptLocale.BANNER_CATCHKING_BUTTON, self.__ClickCatchKingButton)

				if app.ENABLE_SNOWFLAKE_STICK_EVENT:
					if player.GetSnowflakeStickEvent():
						self.mini_game_dialog.AppendButton(uiScriptLocale.BANNER_SNOWFLAKE_STICK_EVENT_BUTTON, self.__ClickSnowflakeStickEventButton)

			self.mini_game_dialog.RefreshDialog()

			self.game_type = MINIGAME_TYPE_MAX
			self.main_game = None

	def __CloseAll(self, except_game = MINIGAME_TYPE_MAX):
		if app.ENABLE_MINI_GAME_RUMI:
			if self.rumi_game and except_game != MINIGAME_RUMI:
				self.rumi_game.Close()

		if app.ENABLE_MINI_GAME_CATCH_KING:
			if self.catch_king_game and except_game != MINIGAME_CATCHKING:
				self.catch_king_game.Close()

		if app.ENABLE_SNOWFLAKE_STICK_EVENT:
			if self.snowflake_stick_event and except_game != SNOWFLAKE_STICK_EVENT:
				self.snowflake_stick_event.Close()

	def hide_mini_game_dialog(self):
		if self.event_banner_button:
			if self.event_banner_button.IsShow():
				self.event_banner_button.Hide()

		if self.mini_game_dialog:
			if self.mini_game_dialog.IsShow():
				self.mini_game_dialog.Hide()

	def show_mini_game_dialog(self):
		if self.event_banner_button:
			if self.event_banner_button_enable:
				self.event_banner_button.Show()

	if app.ENABLE_MINI_GAME_RUMI:
		def __ClickRumiButton(self):
			self.__CloseAll(MINIGAME_RUMI)

			if self.mini_game_dialog:
				self.mini_game_dialog.Close()

			if not self.rumi_game:
				self.rumi_game = uiMiniGameRumi.MiniGameRumi()
				self.rumi_game.SetItemToolTip(self.tooltipitem)

			self.game_type = MINIGAME_RUMI
			self.main_game = self.rumi_game
			self.main_game.Open()

		def MiniGameRumiStart(self):
			if self.rumi_game:
				self.rumi_game.GameStart()

		def MiniGameRumiMoveCard(self, srcCard, dstCard):
			if MINIGAME_RUMI != self.game_type:
				return

			if self.rumi_game:
				self.rumi_game.RumiMoveCard(srcCard, dstCard)

		def MiniGameRumiSetDeckCount(self, deck_card_count):
			if MINIGAME_RUMI != self.game_type:
				return

			if self.rumi_game:
				self.rumi_game.SetDeckCount(deck_card_count)

		def MiniGameRumiIncreaseScore(self, score, total_score):
			if MINIGAME_RUMI != self.game_type:
				return

			if self.rumi_game:
				self.rumi_game.RumiIncreaseScore(score, total_score)

		def MiniGameRumiEnd(self):
			if self.rumi_game:
				self.rumi_game.GameEnd()

		def SetOkeyNormalBG(self):
			if self.rumi_game:
				self.rumi_game.SetOkeyNormalBG()

	if app.ENABLE_MINI_GAME_CATCH_KING:
		def __ClickCatchKingButton(self):
			self.__CloseAll(MINIGAME_CATCHKING)

			if self.mini_game_dialog:
				self.mini_game_dialog.Close()

			if not self.catch_king_game:
				self.catch_king_game = uiMiniGameCatchKing.MiniGameCatchKing()

			self.game_type = MINIGAME_CATCHKING
			self.main_game = self.catch_king_game
			self.main_game.Open()

		def MiniGameCatchKingEventStart(self, bigScore):
			if self.catch_king_game:
				self.catch_king_game.GameStart(bigScore)

		def MiniGameCatchKingSetHandCard(self, cardNumber):
			if self.catch_king_game:
				self.catch_king_game.CatchKingSetHandCard(cardNumber)

		def MiniGameCatchKingResultField(self, score, rowType, cardPos, cardValue, keepFieldCard, destroyHandCard, getReward, isFiveNear):
			if self.catch_king_game:
				self.catch_king_game.CatchKingResultField(score, rowType, cardPos, cardValue, keepFieldCard, destroyHandCard, getReward, isFiveNear)

		def MiniGameCatchKingSetEndCard(self, cardPos, cardNumber):
			if self.catch_king_game:
				self.catch_king_game.CatchKingSetEndCard(cardPos, cardNumber)

		def MiniGameCatchKingReward(self, rewardCode):
			if self.catch_king_game:
				self.catch_king_game.CatchKingReward(rewardCode)

	if app.ENABLE_SNOWFLAKE_STICK_EVENT:
		def __ClickSnowflakeStickEventButton(self):
			if player.GetLevel() < 60:
				uiSnowflakeStickEvent.SnowflakeStickEventUtil.AppendChat(self, chat.CHAT_TYPE_INFO, localeInfo.SNOWFLAKE_STICK_EVENT_MESSAGE_NOT_ENOUGH_LEVEL)
				return

			self.__CloseAll(SNOWFLAKE_STICK_EVENT)

			if self.mini_game_dialog:
				self.mini_game_dialog.Close()

			if not self.snowflake_stick_event:
				self.snowflake_stick_event = uiSnowflakeStickEvent.SnowflakeStickEvent()
				self.snowflake_stick_event.SetItemToolTip(self.tooltipitem)

			self.game_type = SNOWFLAKE_STICK_EVENT
			self.main_game = self.snowflake_stick_event
			self.main_game.Open()

		def SnowflakeStickEventProcess(self, type, data):
			if type == net.SNOWFLAKE_STICK_EVENT_GC_SUBHEADER_ADD_SNOW_BALL:
				uiSnowflakeStickEvent.SnowflakeStickEventUtil.AppendChat(self, chat.CHAT_TYPE_INFO, localeInfo.SNOWFLAKE_STICK_EVENT_MESSAGE_ADD_SNOW_BALL)

			elif type == net.SNOWFLAKE_STICK_EVENT_GC_SUBHEADER_ADD_TREE_BRANCH:
				uiSnowflakeStickEvent.SnowflakeStickEventUtil.AppendChat(self, chat.CHAT_TYPE_INFO, localeInfo.SNOWFLAKE_STICK_EVENT_MESSAGE_ADD_TREE_BRANCH)

			elif type == net.SNOWFLAKE_STICK_EVENT_GC_SUBHEADER_MESSAGE_SNOW_BALL_MAX:
				uiSnowflakeStickEvent.SnowflakeStickEventUtil.AppendChat(self, chat.CHAT_TYPE_INFO, localeInfo.SNOWFLAKE_STICK_EVENT_MESSAGE_SNOW_BALL_MAX)

			elif type == net.SNOWFLAKE_STICK_EVENT_GC_SUBHEADER_MESSAGE_TREE_BRANCH_MAX:
				uiSnowflakeStickEvent.SnowflakeStickEventUtil.AppendChat(self, chat.CHAT_TYPE_INFO, localeInfo.SNOWFLAKE_STICK_EVENT_MESSAGE_TREE_BRANCH_MAX)

			elif type == net.SNOWFLAKE_STICK_EVENT_GC_SUBHEADER_MESSAGE_USE_STICK_FAILED:
				if data:
					uiSnowflakeStickEvent.SnowflakeStickEventUtil.AppendChat(self, chat.CHAT_TYPE_INFO, localeInfo.SNOWFLAKE_STICK_EVENT_MESSAGE_CANNOT_USE_STICK_COOLTIME % max(0, data - app.GetGlobalTimeStamp()))
				else:
					uiSnowflakeStickEvent.SnowflakeStickEventUtil.AppendChat(self, chat.CHAT_TYPE_INFO, localeInfo.SNOWFLAKE_STICK_EVENT_MESSAGE_USE_STICK_FAILED_1)
					uiSnowflakeStickEvent.SnowflakeStickEventUtil.AppendChat(self, chat.CHAT_TYPE_INFO, localeInfo.SNOWFLAKE_STICK_EVENT_MESSAGE_USE_STICK_FAILED_2)

			elif type == net.SNOWFLAKE_STICK_EVENT_GC_SUBHEADER_MESSAGE_GET_RANK_BUFF:
				uiSnowflakeStickEvent.SnowflakeStickEventUtil.AppendChat(self, chat.CHAT_TYPE_INFO, localeInfo.SNOWFLAKE_STICK_EVENT_MESSAGE_RANK_BUFF_GET)

			elif type == net.SNOWFLAKE_STICK_EVENT_GC_SUBHEADER_MESSAGE_GET_SNOWFLAKE_BUFF:
				uiSnowflakeStickEvent.SnowflakeStickEventUtil.AppendChat(self, chat.CHAT_TYPE_INFO, localeInfo.SNOWFLAKE_STICK_EVENT_MESSAGE_SNOWFLAKE_BUFF_GET)

			elif type == net.SNOWFLAKE_STICK_EVENT_GC_SUBHEADER_ENABLE:
				if data:
					uiSnowflakeStickEvent.SnowflakeStickEventUtil.AppendChat(self, chat.CHAT_TYPE_NOTICE, localeInfo.SNOWFLAKE_STICK_EVENT_MESSAGE_EVENT_START)
				else:
					uiSnowflakeStickEvent.SnowflakeStickEventUtil.AppendChat(self, chat.CHAT_TYPE_NOTICE, localeInfo.SNOWFLAKE_STICK_EVENT_MESSAGE_EVENT_END)

			if SNOWFLAKE_STICK_EVENT != self.game_type:
				return

			if not self.snowflake_stick_event:
				return

			self.snowflake_stick_event.InGameEventProcess(type, data)
