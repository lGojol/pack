import chat
import grp
import net
import app
import wndMgr
import uiCommon
import uiGuild
import uiToolTip
import ui
import constInfo
import locale

def CalculateTimeLeft(iTime):
	A, B = divmod(iTime, 60)
	C, A = divmod(A, 60)
	return "%02d:%02d" % (A, B)

class CrystalEventWindow(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.Initialize()

	def __del__(self):
		ui.Window.__del__(self)

	def Initialize(self):
		self.main = {}

		# Fondo
		self.main_background = ui.ExpandedImageBox()
		self.main_background.SetParent(self)
		self.main_background.LoadImage("d:/ymir work/ui/crystal/background.tga")
		self.main_background.SetPosition(wndMgr.GetScreenWidth() / 2 - 750 / 2, -5)
		self.main_background.SetScale(0.9, 0.9)
		self.main_background.Show()

		# Cantidad de jugadores en el equipo rojo
		self.main_text_red_players = ui.TextLine()
		self.main_text_red_players.SetParent(self)
		self.main_text_red_players.SetPosition(wndMgr.GetScreenWidth() / 2 - 750 / 2 + 240, 27)
		self.main_text_red_players.SetFontName("Roman:20")
		self.main_text_red_players.SetPackedFontColor(0xffff0000)  # Color rojo
		self.main_text_red_players.SetHorizontalAlignLeft()
		self.main_text_red_players.Show()

		# Cantidad de jugadores en el equipo azul
		self.main_text_blue_players = ui.TextLine()
		self.main_text_blue_players.SetParent(self)
		self.main_text_blue_players.SetPosition(wndMgr.GetScreenWidth() / 2 - 750 / 2 + 500, 27)
		self.main_text_blue_players.SetFontName("Roman:20")
		self.main_text_blue_players.SetPackedFontColor(0xff0000ff)  # Color azul
		self.main_text_blue_players.SetHorizontalAlignLeft()
		self.main_text_blue_players.Show()

		# Cantidad de cristales del equipo rojo
		self.main_text_crystals_red = ui.TextLine()
		self.main_text_crystals_red.SetParent(self)
		self.main_text_crystals_red.SetPosition(wndMgr.GetScreenWidth()/2 - 750 / 2 + 180, 22)
		self.main_text_crystals_red.SetFontName("Roman:20")
		self.main_text_crystals_red.SetPackedFontColor(0xffff0000)  # Color rojo
		self.main_text_crystals_red.SetHorizontalAlignLeft()
		self.main_text_crystals_red.Show()

		# Cantidad de cristales del equipo azul
		self.main_text_crystals_blue = ui.TextLine()
		self.main_text_crystals_blue.SetParent(self)
		self.main_text_crystals_blue.SetPosition(wndMgr.GetScreenWidth()/2 - 750 / 2 + 565, 22)
		self.main_text_crystals_blue.SetFontName("Roman:20")
		self.main_text_crystals_blue.SetPackedFontColor(0xff0000ff)  # Color azul
		self.main_text_crystals_blue.SetHorizontalAlignLeft()
		self.main_text_crystals_blue.Show()

		# Temporizador
		self.main_text_clock = ui.TextLine()
		self.main_text_clock.SetParent(self)
		self.main_text_clock.SetPosition(wndMgr.GetScreenWidth() / 2 - 750 / 2 + 350, 22)
		self.main_text_clock.SetFontName("Roman:25")
		self.main_text_clock.SetPackedFontColor(0xff948b7d)
		self.main_text_clock.SetHorizontalAlignLeft()
		self.main_text_clock.Show()

		self.leftTime = 0
		self.lastUpdateTime = 0  # Para rastrear la última actualización del tiempo

	def Append(self, tokens):
		if len(tokens) != 5:
			return

		currentTime = app.GetGlobalTimeStamp()
		remainingTime = int(tokens[4])

		# Establecer el tiempo solo si es la primera vez o si el tiempo restante es mayor al actual
		if constInfo.CRYSTAL_EVENT_WINDOW_IS_SHOWED < 1 or remainingTime > (self.leftTime - currentTime):
			self.leftTime = currentTime + remainingTime
			self.lastUpdateTime = currentTime
		self.Show()

		# Actualizar los datos de la interfaz
		self.main_text_red_players.SetText(str(tokens[0]))  # Solo el número de jugadores en rojo
		self.main_text_blue_players.SetText(str(tokens[1]))  # Solo el número de jugadores en azul
		self.main_text_crystals_red.SetText(str(tokens[2]))  # Solo el número de cristales en rojo
		self.main_text_crystals_blue.SetText(str(tokens[3]))  # Solo el número de cristales en azul
		constInfo.CRYSTAL_EVENT_WINDOW_IS_SHOWED = 1

	def SetTime(self, iLeft):
		currentTime = app.GetGlobalTimeStamp()
		leftTime = iLeft - currentTime
		
		if leftTime <= 0:
			leftTime = 0
			self.Hide()
			constInfo.CRYSTAL_EVENT_WINDOW_IS_SHOWED = 0
		
		self.main_text_clock.SetText(CalculateTimeLeft(leftTime))

	def OnUpdate(self):
		if self.leftTime > 0 and app.GetGlobalTimeStamp() > self.lastUpdateTime:
			self.SetTime(self.leftTime)

	def Destroy(self):
		self.ClearDictionary()
		self.main = {}
		self.leftTime = 0
		self.lastUpdateTime = 0
		constInfo.CRYSTAL_EVENT_WINDOW_IS_SHOWED = 0
