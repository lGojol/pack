import ui
import interfaceModule

import chat
import app
import chr

if app.ENABLE_DUNGEON_COOL_TIME:
	class DungeonCoolTimeWindow(ui.ScriptWindow):
		def __init__(self, layer = "UI"):
			ui.ScriptWindow.__init__(self, layer)

			self.__Initialize()
			self.__LoadWindow()

		def __Initialize(self):	
			self.floorText = None
			self.coolTimeImage = None
			self.coolTimeText = None
			self.spActiveImage = None
			self.spCoolTimeText = None
			self.startTime = 0.0
			self.endTime = 0.0
			self.shadowPotionEndTime = 0.0
			self.floor = 0

		def __Load_LoadScript(self, fileName):
			try:
				pyScriptLoader = ui.PythonScriptLoader()
				pyScriptLoader.LoadScriptFile(self, fileName)
			except:
				import exception
				exception.Abort("DungeonCoolTimeWindow.__Load_LoadScript")

		def __Load_BindObject(self):
			try:
				self.floorText = self.GetChild("floorText")
				self.coolTimeImage = self.GetChild("coolTimeImage")
				self.coolTimeText = self.GetChild("coolTimeText")
				self.spActiveImage = self.GetChild("spActiveImage")
				self.spCoolTimeText = self.GetChild("spCoolTimeText")
			except:
				import exception
				exception.Abort("DungeonCoolTimeWindow.__Load_BindObject")

		def __Load_BindEvents(self):
			try:
				pass
			except:
				import exception
				exception.Abort("DungeonCoolTimeWindow.__Load_BindEvents")

		def GetLeftTime(self, leftTime):
			leftMin = int(leftTime / 60)
			leftSecond = int(leftTime % 60)

			return leftMin, leftSecond

		def Start(self, cooltime):
			self.startTime = float(app.GetTime())
			self.endTime = self.startTime + cooltime

			self.coolTimeImage.SetCoolTime(cooltime)
			self.coolTimeImage.SetStartCoolTime(self.startTime)

			if cooltime:
				self.coolTimeImage.Show()
			else:
				self.coolTimeImage.Hide()

		def SetShadowPotionEndTime(self, endTime):
			self.shadowPotionEndTime = endTime

		def Clear(self):
			self.SetCoolTime(0)

		def OnUpdate(self):
			self.RefreshAffects()
			self.RefreshLeftTime()
			self.RefreshShadowPotionLeftTime()

		def RefreshAffects(self):
			affect = interfaceModule.GetInstance().GetGameInstance().GetAffectList().get(chr.AFFECT_SHADOW_POTION)

			if affect:
				self.spActiveImage.Show()
			else:
				self.spActiveImage.Hide()

		def RefreshLeftTime(self):
			leftTime = max(0, self.endTime - app.GetTime() + 0.5)
			(leftMin, leftSecond) = self.GetLeftTime(leftTime)
			self.coolTimeText.SetText("%02d:%02d" % (leftMin, leftSecond))

		def RefreshShadowPotionLeftTime(self):
			leftTime = max(0, self.shadowPotionEndTime - app.GetGlobalTimeStamp() + 0.5)
			(leftMin, leftSecond) = self.GetLeftTime(leftTime)
			self.spCoolTimeText.SetText("%02d:%02d" % (leftMin, leftSecond))

		def __LoadWindow(self):
			self.__Load_LoadScript("uiscript/dungeoncooltimewindow.py")
			self.__Load_BindObject()
			self.__Load_BindEvents()

		def Open(self):
			self.Show()
			self.SetTop()

		def SetFloor(self, floor):
			self.floor = floor
			self.floorText.SetText(str(floor))

		def SetCoolTime(self, cooltime):
			self.Start(cooltime)

		def Close(self):
			self.Hide()

		def Destroy(self):
			self.ClearDictionary()
			self.__Initialize()

		def __del__(self):
			ui.ScriptWindow.__del__(self)
