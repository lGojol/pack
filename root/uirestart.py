import dbg
import app
import net

import ui

if app.ENABLE_ELEMENTAL_WORLD:
	import uiCommon
	import localeInfo

###################################################################################################
## Restart
class RestartDialog(ui.ScriptWindow):

	if app.ENABLE_ELEMENTAL_WORLD:
		ELEMENTAL_WORLD_MAP_IDX = {140}

	def __init__(self):
		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/restartdialog.py")
		except Exception, msg:
			import sys
			(type, msg, tb)=sys.exc_info()
			dbg.TraceError("RestartDialog.LoadDialog - %s:%s" % (type, msg))
			app.Abort()
			return 0

		try:
			self.restartHereButton=self.GetChild("restart_here_button")
			self.restartTownButton=self.GetChild("restart_town_button")
		except:
			import sys
			(type, msg, tb)=sys.exc_info()
			dbg.TraceError("RestartDialog.LoadDialog - %s:%s" % (type, msg))
			app.Abort()
			return 0

		self.restartHereButton.SetEvent(ui.__mem_func__(self.RestartHere))
		self.restartTownButton.SetEvent(ui.__mem_func__(self.RestartTown))

		return 1

	def Destroy(self):
		self.restartHereButton=0
		self.restartTownButton=0
		self.ClearDictionary()

	if app.ENABLE_ELEMENTAL_WORLD:
		def OpenDialog(self, mapidx):
			if mapidx in self.ELEMENTAL_WORLD_MAP_IDX:
				self.Hide()

				restartQuestionDialog = uiCommon.QuestionDialogElemental()
				restartQuestionDialog.SetText1(localeInfo.RESTART_POPUP_GIVEUP_ELEMENTAL_DUNGEON1)
				restartQuestionDialog.SetText2(localeInfo.RESTART_POPUP_GIVEUP_ELEMENTAL_DUNGEON2)
				restartQuestionDialog.SetAcceptText(localeInfo.MOVE_CHANNEL_SELECT)
				restartQuestionDialog.SetAcceptEvent(lambda arg = True: self.AnswerRestartElementalWorld(arg))
				restartQuestionDialog.Open()
				self.restartQuestionDialog = restartQuestionDialog
			else:
				self.Show()
	else:
		def OpenDialog(self):
			self.Show()

	def Close(self):
		self.Hide()
		return True

	def RestartHere(self):
		net.SendChatPacket("/restart_here")

	def RestartTown(self):
		net.SendChatPacket("/restart_town")

	def OnPressExitKey(self):
		return True

	def OnPressEscapeKey(self):
		return True

	if app.ENABLE_ELEMENTAL_WORLD:
		def AnswerRestartElementalWorld(self, answer):
			if not self.restartQuestionDialog:
				return

			net.SendChatPacket("/dll_warp_exit_elemental")

			self.restartQuestionDialog.Close()
			self.restartQuestionDialog = None
