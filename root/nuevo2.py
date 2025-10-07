import ui
import uiScriptLocale
import localeInfo
import constInfo
import wndMgr
import uiToolTip
import app
import player
import net
import bio_window
import uiSwitchbot
import uiSpecialInventory
import uiPrivateShop
import uiHunting
import uiBuffNPC
import uiFlowerEvent
import uiAuto
import ui_bpass
import ingamewiki

class SpeedButtonWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.__Load()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __Initialize(self):
		self.titleBar = None
		self.buttons = {}
		self.toolTip = uiToolTip.ToolTip()
		self.wndBio = None
		self.wndSwitchbot = None
		self.wndSpecialInventory = None
		self.wndPrivateShopPanel = None
		self.wndHunting = None
		self.wndHuntingSelect = None
		self.wndBuffNPCWindow = None
		self.wndFlowerEvent = None
		self.wndBattlePass = None
		self.wndAutoWindow = None
		self.wndWiki = None

	def Destroy(self):
		self.ClearDictionary()
		self.titleBar = None
		self.buttons = {}
		self.toolTip = None
		self.wndBio = None
		self.wndSwitchbot = None
		self.wndSpecialInventory = None
		self.wndPrivateShopPanel = None
		self.wndHunting = None
		self.wndHuntingSelect = None
		self.wndBuffNPCWindow = None
		self.wndFlowerEvent = None
		self.wndBattlePass = None
		self.wndAutoWindow = None
		self.wndWiki = None

	def __GetInterface(self):
		"""Inicializa todas las ventanas directamente, solo si no están inicializadas."""
		try:
			if not self.wndBio:
				self.wndBio = bio_window.BioWindow()
			if not self.wndWiki:
				self.wndWiki = ingamewiki.InGameWiki()
			if not self.wndSwitchbot:
				self.wndSwitchbot = uiSwitchbot.SwitchbotWindow()
			if not self.wndSpecialInventory:
				self.wndSpecialInventory = uiSpecialInventory.SpecialInventoryWindow()
			if not self.wndPrivateShopPanel:
				self.wndPrivateShopPanel = uiPrivateShop.PrivateShopPanel()
			if not self.wndHunting or not self.wndHuntingSelect:
				self.wndHunting = uiHunting.HuntingWindow()
				self.wndHuntingSelect = uiHunting.HuntingSelectWindow()
			if not self.wndBuffNPCWindow:
				self.wndBuffNPCWindow = uiBuffNPC.BuffNPCWindow()
			if not self.wndFlowerEvent:
				self.wndFlowerEvent = uiFlowerEvent.UiFlowerEventWindow()
			if not self.wndBattlePass:
				self.wndBattlePass = ui_bpass.BattlePassWindow()
			if not self.wndAutoWindow:
				self.wndAutoWindow = uiAuto.AutoWindow()
		except Exception, e:
			pass

	def __LoadScript(self, fileName):
		"""Carga el archivo de script UI."""
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)
		except Exception, e:
			import exception
			exception.Abort("SpeedButtonWindow.__LoadScript: %s" % str(e))

	def __BindObjects(self):
		"""Enlaza los objetos de la UI y configura los eventos de los botones."""
		try:
			self.titleBar = self.GetChild("board")

			# Diccionario de botones y sus configuraciones
			button_config = {
				"Button1": {"event": self.__ToggleBioWindow, "tooltip": "Bio Window (F5)"},
				"Button2": {"event": self.__ToggleSwitchbotWindow, "tooltip": "Switchbot (F6)"},
				"Button3": {"event": self.__ToggleSpecialInventoryWindow, "tooltip": "Special Inventory (F7)"},
				"Button4": {"event": self.__TogglePrivateShopPanelWindow, "tooltip": "Private Shop (F8)"},
				"Button5": {"event": self.__ToggleWikiWindow, "tooltip": "Wiki Window (I)"},
				"Button6": {"event": self.__ToggleHuntingWindow, "tooltip": "Hunting Window (F11)"},
				"Button7": {"event": self.__ToggleBuffNPCWindow, "tooltip": "Buff NPC (F12)"},
				"Button8": {"event": self.__ToggleFlowerEvent, "tooltip": "Flower Event (U)"},
				"Button9": {"event": self.__ToggleBattlePass, "tooltip": "Battle Pass (P)"},
				"Button10": {"event": self.__ToggleAutoWindow, "tooltip": "Auto Window (K)"},
			}

			# Enlazar botones y configurar eventos
			for button_name, config in button_config.iteritems():
				try:
					button = self.GetChild(button_name)
					button.SAFE_SetEvent(config["event"])
					button.SetToolTipText(config["tooltip"])
					self.buttons[button_name] = button
				except Exception, e:
					pass

			self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		except Exception, e:
			import exception
			exception.Abort("SpeedButtonWindow.__BindObjects: %s" % str(e))

	def __ToggleBioWindow(self):
		"""Alterna la ventana del Biólogo (F5)."""
		try:
			if self.wndBio:
				if not self.wndBio.IsShow():
					self.wndBio.Show()
					self.wndBio.SetTop()
				else:
					self.wndBio.Close()
		except Exception, e:
			pass

	def __ToggleSwitchbotWindow(self):
		"""Alterna la ventana Switchbot (F6)."""
		try:
			if self.wndSwitchbot:
				if self.wndSwitchbot.IsShow():
					self.wndSwitchbot.Close()
				else:
					self.wndSwitchbot.Open()
		except Exception, e:
			pass

	def __ToggleSpecialInventoryWindow(self):
		"""Alterna la ventana de inventario especial (F7)."""
		try:
			if self.wndSpecialInventory and not player.IsObserverMode():
				if not self.wndSpecialInventory.IsShow():
					self.wndSpecialInventory.Show()
					self.wndSpecialInventory.SetTop()
				else:
					self.wndSpecialInventory.OverOutItem()
					self.wndSpecialInventory.Close()
		except Exception, e:
			pass

	def __TogglePrivateShopPanelWindow(self):
		"""Alterna la ventana de tienda privada (F8)."""
		try:
			if self.wndPrivateShopPanel and not player.IsObserverMode():
				if not self.wndPrivateShopPanel.RequestOpen():
					self.wndPrivateShopPanel.Close()
		except Exception, e:
			pass

	def __ToggleWikiWindow(self):
		"""Alterna la ventana Wiki (I)."""
		try:
			net.ToggleWikiWindow()
		except Exception, e:
			pass

	def __ToggleHuntingWindow(self):
		"""Alterna la ventana de caza (F11)."""
		try:
			if self.wndHunting and self.wndHuntingSelect:
				if self.wndHunting.IsShow():
					self.wndHunting.Close()
				elif self.wndHuntingSelect.IsShow():
					self.wndHuntingSelect.Close()
				else:
					net.SendHuntingAction(1, 0)
		except Exception, e:
			pass

	def __ToggleBuffNPCWindow(self):
		"""Alterna la ventana de Buff NPC (F12)."""
		try:
			if self.wndBuffNPCWindow:
				if not self.wndBuffNPCWindow.IsShow():
					self.wndBuffNPCWindow.Show()
					self.wndBuffNPCWindow.SetTop()
				else:
					self.wndBuffNPCWindow.Close()
		except Exception, e:
			pass

	def __ToggleFlowerEvent(self):
		"""Alterna la ventana de Flower Event (U)."""
		try:
			if self.wndFlowerEvent:
				if not self.wndFlowerEvent.IsShow():
					self.wndFlowerEvent.Show()
				else:
					self.wndFlowerEvent.Close()
		except Exception, e:
			pass

	def __ToggleBattlePass(self):
		"""Muestra la ventana de Battle Pass (P)."""
		try:
			if self.wndBattlePass:
				if not self.wndBattlePass.IsShow():
					self.wndBattlePass.Show()
				else:
					self.wndBattlePass.Close()
		except Exception, e:
			pass

	def __ToggleAutoWindow(self):
		"""Alterna la ventana de Auto Window (K)."""
		try:
			if self.wndAutoWindow and not player.IsObserverMode():
				if not self.wndAutoWindow.IsShow():
					self.wndAutoWindow.Show()
				else:
					self.wndAutoWindow.Close()
		except Exception, e:
			pass

	def __Load(self):
		"""Carga el script y enlaza objetos."""
		try:
			self.__GetInterface()
			self.__LoadScript("uiscript/speedbutton.py")
			self.__BindObjects()
		except Exception, e:
			import exception
			exception.Abort("SpeedButtonWindow.__Load: %s" % str(e))

	def Open(self):
		self.Show()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True