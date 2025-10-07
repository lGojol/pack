import ui
import player
import mouseModule
import net
import app
import snd
import item
import player
import chat
import grp
import uiScriptLocale
import uiRefine
import uiToolTip
import uiAttachMetin
import uiPickMoney
#import uiPickItem
import uiCommon
if app.BL_67_ATTR:
	import uiAttr67Add
import uiPrivateShopBuilder
import localeInfo
import constInfo
import uiPreviewCostume
import ime
import wndMgr
if app.ENABLE_CHEQUE_SYSTEM:
	import uiToolTip
	import uiPickETC
if app.ENABLE_ACCE_SYSTEM:
	import acce
if app.ENABLE_PREMIUM_PRIVATE_SHOP:
	import uiPrivateShop
	import privateShop

ITEM_MALL_BUTTON_ENABLE = True



ITEM_FLAG_APPLICABLE = 1 << 14

class CostumeWindow(ui.ScriptWindow):

	def __init__(self, wndInventory):
		import exception

		if not app.ENABLE_COSTUME_SYSTEM:
			exception.Abort("What do you do?")
			return

		if not wndInventory:
			exception.Abort("wndInventory parameter must be set to InventoryWindow")
			return

		ui.ScriptWindow.__init__(self)

		self.isLoaded = 0
		self.wndInventory = wndInventory;

		if app.ENABLE_HIDE_COSTUME_SYSTEM:
			self.visibleBtnList = []
			self.visibleSlotList = []

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.__LoadWindow()
		self.RefreshCostumeSlot()

		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/CostumeWindow.py")
		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.LoadObject")

		try:
			wndEquip = self.GetChild("CostumeSlot")
			if app.ENABLE_HIDE_COSTUME_SYSTEM:
				self.visibleBtnList.append(self.GetChild("BodyToolTipButton")) ## 0
				self.visibleBtnList.append(self.GetChild("HairToolTipButton")) ## 1
				self.visibleBtnList.append(self.GetChild("AcceToolTipButton")) ## 2
				self.visibleBtnList.append(self.GetChild("WeaponToolTipButton")) ## 3
				self.visibleBtnList.append(self.GetChild("AuraToolTipButton")) ## 4

				self.visibleSlotList.append(self.GetChild("VisibleBodySlotImg")) ## 0
				self.visibleSlotList.append(self.GetChild("VisibleHairSlotImg")) ## 1
				self.visibleSlotList.append(self.GetChild("VisibleAcceSlotImg")) ## 2
				self.visibleSlotList.append(self.GetChild("VisibleWeaponSlotImg")) ## 3
				self.visibleSlotList.append(self.GetChild("VisibleAuraSlotImg")) ## 4
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))

		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.BindObject")

		## Equipment
		wndEquip.SetOverInItemEvent(ui.__mem_func__(self.wndInventory.OverInItem))
		wndEquip.SetOverOutItemEvent(ui.__mem_func__(self.wndInventory.OverOutItem))
		wndEquip.SetUnselectItemSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
		wndEquip.SetUseSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
		wndEquip.SetSelectEmptySlotEvent(ui.__mem_func__(self.wndInventory.SelectEmptySlot))
		wndEquip.SetSelectItemSlotEvent(ui.__mem_func__(self.wndInventory.SelectItemSlot))

		self.wndEquip = wndEquip

		if app.ENABLE_HIDE_COSTUME_SYSTEM:
			self.visibleBtnList[0].SetToggleUpEvent(ui.__mem_func__(self.VisibleCostume), 1, 0)
			self.visibleBtnList[0].SetToggleDownEvent(ui.__mem_func__(self.VisibleCostume), 1, 1)

			self.visibleBtnList[1].SetToggleUpEvent(ui.__mem_func__(self.VisibleCostume), 2, 0)
			self.visibleBtnList[1].SetToggleDownEvent(ui.__mem_func__(self.VisibleCostume), 2, 1)

			if app.ENABLE_ACCE_SYSTEM:
				self.visibleBtnList[2].SetToggleUpEvent(ui.__mem_func__(self.VisibleCostume), 3, 0)
				self.visibleBtnList[2].SetToggleDownEvent(ui.__mem_func__(self.VisibleCostume), 3, 1)

			if app.ENABLE_WEAPON_COSTUME_SYSTEM:
				self.visibleBtnList[3].SetToggleUpEvent(ui.__mem_func__(self.VisibleCostume), 4, 0)
				self.visibleBtnList[3].SetToggleDownEvent(ui.__mem_func__(self.VisibleCostume), 4, 1)

			if app.ENABLE_AURA_SYSTEM:
				self.visibleBtnList[4].SetToggleUpEvent(ui.__mem_func__(self.VisibleCostume), 5, 0)
				self.visibleBtnList[4].SetToggleDownEvent(ui.__mem_func__(self.VisibleCostume), 5, 1)

			for slot in xrange(5):
				self.visibleSlotList[slot].Hide()

	if app.ENABLE_HIDE_COSTUME_SYSTEM:
		def RefreshVisibleCostume(self):
			body = constInfo.HIDDEN_BODY_COSTUME
			self.SetHideEvent(0, body)

			hair = constInfo.HIDDEN_HAIR_COSTUME
			self.SetHideEvent(1, hair)

			if app.ENABLE_ACCE_SYSTEM:
				acce = constInfo.HIDDEN_ACCE_COSTUME
				self.SetHideEvent(2, acce)

			if app.ENABLE_WEAPON_COSTUME_SYSTEM:
				weapon = constInfo.HIDDEN_WEAPON_COSTUME
				self.SetHideEvent(3, weapon)

			if app.ENABLE_AURA_SYSTEM:
				aura = constInfo.HIDDEN_AURA_COSTUME
				self.SetHideEvent(4, aura)

		def SetHideEvent(self, slot, hide = False):
			if hide:
				self.visibleBtnList[slot].SetToolTipText(localeInfo.SHOW_COSTUME)
				self.visibleBtnList[slot].SetUpVisual("d:/ymir work/ui/game/costume/eye_closed_01.tga")
				self.visibleBtnList[slot].SetOverVisual("d:/ymir work/ui/game/costume/eye_closed_02.tga")
				self.visibleBtnList[slot].SetDownVisual("d:/ymir work/ui/game/costume/eye_closed_02.tga")
				self.visibleSlotList[slot].Show()
			else:
				self.visibleBtnList[slot].SetToolTipText(localeInfo.HIDE_COSTUME)
				self.visibleBtnList[slot].SetUpVisual("d:/ymir work/ui/game/costume/eye_normal_01.tga")
				self.visibleBtnList[slot].SetOverVisual("d:/ymir work/ui/game/costume/eye_normal_02.tga")
				self.visibleBtnList[slot].SetDownVisual("d:/ymir work/ui/game/costume/eye_normal_02.tga")
				self.visibleSlotList[slot].Hide()

		def VisibleCostume(self, part, hidden):
			net.SendChatPacket("/hide_costume %d %d" % (part, hidden))

	def RefreshCostumeSlot(self):
		getItemVNum=player.GetItemIndex

		for i in xrange(item.COSTUME_SLOT_COUNT):
			slotNumber = item.COSTUME_SLOT_START + i
			self.wndEquip.SetItemSlot(slotNumber, getItemVNum(slotNumber), 0)

			if app.BL_TRANSMUTATION_SYSTEM:
				if not player.GetChangeLookVnum(player.EQUIPMENT, slotNumber) == 0:
					self.wndEquip.SetSlotCoverImage(slotNumber,"icon/item/ingame_convert_Mark.tga")
				else:
					self.wndEquip.EnableSlotCoverImage(slotNumber,False)

		if app.ENABLE_WEAPON_COSTUME_SYSTEM:
			self.wndEquip.SetItemSlot(item.COSTUME_SLOT_WEAPON, getItemVNum(item.COSTUME_SLOT_WEAPON), 0)

		self.wndEquip.RefreshSlot()

class BeltInventoryWindow(ui.ScriptWindow):

	def __init__(self, wndInventory):
		import exception

		if not app.ENABLE_NEW_EQUIPMENT_SYSTEM:
			exception.Abort("What do you do?")
			return

		if not wndInventory:
			exception.Abort("wndInventory parameter must be set to InventoryWindow")
			return

		ui.ScriptWindow.__init__(self)

		self.isLoaded = 0
		self.wndInventory = wndInventory;

		self.wndBeltInventoryLayer = None
		self.wndBeltInventorySlot = None
		self.expandBtn = None
		self.minBtn = None

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self, openBeltSlot = False):
		self.__LoadWindow()
		self.RefreshSlot()

		ui.ScriptWindow.Show(self)

		if openBeltSlot:
			self.OpenInventory()
		else:
			self.CloseInventory()

	def Close(self):
		self.Hide()

	def IsOpeningInventory(self):
		return self.wndBeltInventoryLayer.IsShow()

	def OpenInventory(self):
		self.wndBeltInventoryLayer.Show()
		self.expandBtn.Hide()

		if localeInfo.IsARABIC() == 0:
			self.AdjustPositionAndSize()

	def CloseInventory(self):
		self.wndBeltInventoryLayer.Hide()
		self.expandBtn.Show()

		if localeInfo.IsARABIC() == 0:
			self.AdjustPositionAndSize()

	def GetBasePosition(self):
		x, y = self.wndInventory.GetGlobalPosition()
		return x - 148, y + 241

	def AdjustPositionAndSize(self):
		bx, by = self.GetBasePosition()

		if self.IsOpeningInventory():
			self.SetPosition(bx, by)
			self.SetSize(self.ORIGINAL_WIDTH, self.GetHeight())

		else:
			self.SetPosition(bx + 138, by);
			self.SetSize(10, self.GetHeight())

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/BeltInventoryWindow.py")
		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.LoadObject")

		try:
			self.ORIGINAL_WIDTH = self.GetWidth()
			wndBeltInventorySlot = self.GetChild("BeltInventorySlot")
			self.wndBeltInventoryLayer = self.GetChild("BeltInventoryLayer")
			self.expandBtn = self.GetChild("ExpandBtn")
			self.minBtn = self.GetChild("MinimizeBtn")

			self.expandBtn.SetEvent(ui.__mem_func__(self.OpenInventory))
			self.minBtn.SetEvent(ui.__mem_func__(self.CloseInventory))

			if localeInfo.IsARABIC() :
				self.expandBtn.SetPosition(self.expandBtn.GetWidth() - 2, 15)
				self.wndBeltInventoryLayer.SetPosition(self.wndBeltInventoryLayer.GetWidth() - 5, 0)
				self.minBtn.SetPosition(self.minBtn.GetWidth() + 3, 15)

			for i in xrange(item.BELT_INVENTORY_SLOT_COUNT):
				slotNumber = item.BELT_INVENTORY_SLOT_START + i
				wndBeltInventorySlot.SetCoverButton(slotNumber,	"d:/ymir work/ui/game/quest/slot_button_01.sub",\
												"d:/ymir work/ui/game/quest/slot_button_01.sub",\
												"d:/ymir work/ui/game/quest/slot_button_01.sub",\
												"d:/ymir work/ui/game/belt_inventory/slot_disabled.tga", False, False)

		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.BindObject")

		## Equipment
		wndBeltInventorySlot.SetOverInItemEvent(ui.__mem_func__(self.wndInventory.OverInItem))
		wndBeltInventorySlot.SetOverOutItemEvent(ui.__mem_func__(self.wndInventory.OverOutItem))
		wndBeltInventorySlot.SetUnselectItemSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
		wndBeltInventorySlot.SetUseSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
		wndBeltInventorySlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.wndInventory.SelectEmptySlot))
		wndBeltInventorySlot.SetSelectItemSlotEvent(ui.__mem_func__(self.wndInventory.SelectItemSlot))

		self.wndBeltInventorySlot = wndBeltInventorySlot

	def RefreshSlot(self):
		getItemVNum=player.GetItemIndex

		for i in xrange(item.BELT_INVENTORY_SLOT_COUNT):
			slotNumber = item.BELT_INVENTORY_SLOT_START + i
			self.wndBeltInventorySlot.SetItemSlot(slotNumber, getItemVNum(slotNumber), player.GetItemCount(slotNumber))
			self.wndBeltInventorySlot.SetAlwaysRenderCoverButton(slotNumber, True)

			avail = "0"

			if player.IsAvailableBeltInventoryCell(slotNumber):
				self.wndBeltInventorySlot.EnableCoverButton(slotNumber)
			else:
				self.wndBeltInventorySlot.DisableCoverButton(slotNumber)

		self.wndBeltInventorySlot.RefreshSlot()

if app.__RENEWAL_BRAVE_CAPE__:
	import os
	class BraveCapeWindow(ui.Board):
		__children={}
		class SliderBarNew(ui.Window):
			def __init__(self):
				ui.Window.__init__(self)
				self.curPos = 1.0
				self.pageSize = 1.0
				self.eventChange = None
				self.__Load()

			def __Load(self):
				IMG_DIR = "d:/ymir work/ui/game/bravery_cape/"

				img = ui.ImageBox()
				img.SetParent(self)
				img.LoadImage(IMG_DIR+"slider_bg.tga")
				img.Show()
				self.backGroundImage = img

				self.SetSize(self.backGroundImage.GetWidth(), self.backGroundImage.GetHeight())

				cursor = ui.DragButton()
				cursor.AddFlag("movable")
				cursor.AddFlag("restrict_y")
				cursor.SetParent(self)
				cursor.SetMoveEvent(ui.__mem_func__(self.__OnMove))
				cursor.SetUpVisual(IMG_DIR+"drag.tga")
				cursor.SetOverVisual(IMG_DIR+"drag.tga")
				cursor.SetDownVisual(IMG_DIR+"drag.tga")
				cursor.Show()
				self.cursor = cursor

				self.cursor.SetRestrictMovementArea(0, 0, self.backGroundImage.GetWidth(), 0)
				self.pageSize = self.backGroundImage.GetWidth() - self.cursor.GetWidth()

			def __OnMove(self):
				(xLocal, yLocal) = self.cursor.GetLocalPosition()
				self.curPos = float(xLocal) / float(self.pageSize)
				if self.eventChange:
					self.eventChange()
			def SetSliderPos(self, pos):
				self.curPos = pos
				self.cursor.SetPosition(int(self.pageSize * pos), 0)
			def GetSliderPos(self):
				return self.curPos
			def SetEvent(self, event):
				self.eventChange = event
			def Enable(self):
				self.cursor.Show()
			def Disable(self):
				self.cursor.Hide()

		def Destroy(self):
			self.SaveData()
			self.__children={}
		def CreateWindow(self, classPtr, parent, pos):
			window = classPtr
			window.SetParent(parent)
			window.SetPosition(*pos)
			window.Show()
			return window
		def __OverOutItem(self):
			interface = constInfo.GetInterfaceInstance()
			if interface:
				if interface.tooltipItem:
					interface.tooltipItem.HideToolTip()
		def __OverInItem(self, itemIdx):
			interface = constInfo.GetInterfaceInstance()
			if interface:
				if interface.tooltipItem:
					interface.tooltipItem.SetItemToolTip(itemIdx)
		def __init__(self):
			ui.Board.__init__(self)
			self.SetSize(140, 130 + 44)
			self.AddFlag("attach")
			self.AddFlag("float")

			self.__children["firstOpened"] = app.GetGlobalTimeStamp() + 5

			IMG_DIR = "d:/ymir work/ui/game/bravery_cape/"

			BRAVE_CAPE_ITEM_IDX = 20570

			item.SelectItem(BRAVE_CAPE_ITEM_IDX)

			bgImg = self.CreateWindow(ui.ImageBox(), self, (5, 6))
			bgImg.LoadImage(IMG_DIR+"bg.tga")
			self.__children["bgImg"] = bgImg

			timeTextVisual = self.CreateWindow(ui.TextLine(), bgImg, (13, 60))
			timeTextVisual.SetText(localeInfo.SECOND_BRAVE_CAPE)
			self.__children["timeTextVisual"] = timeTextVisual

			timeSlider = self.CreateWindow(self.SliderBarNew(), bgImg, (13, 73 + 5))
			timeSlider.SetEvent(ui.__mem_func__(self.OnChangeTimeSlider))
			self.__children["timeSlider"] = timeSlider

			timeBg = self.CreateWindow(ui.ImageBox(), bgImg, (77, 64))
			timeBg.LoadImage(IMG_DIR+"input_output.tga")
			self.__children["timeBg"] = timeBg

			timeText = self.CreateWindow(ui.TextLine(), timeBg, (0, 0))
			timeText.SetAllAlign()
			timeText.SetText("0")
			self.__children["timeText"] = timeText

			rangeTextVisual = self.CreateWindow(ui.TextLine(), bgImg, (13, 73 + 22 + 17 + 5 - 18))
			rangeTextVisual.SetText(localeInfo.RANGE_BRAVE_CAPE)
			self.__children["rangeTextVisual"] = rangeTextVisual

			rangeSlider = self.CreateWindow(self.SliderBarNew(), bgImg, (13, 73 + 22 + 17 + 5))
			rangeSlider.SetEvent(ui.__mem_func__(self.OnChangeRangeSlider))
			self.__children["rangeSlider"] = rangeSlider

			rangeBg = self.CreateWindow(ui.ImageBox(), bgImg, (77, 95 + 8))
			rangeBg.LoadImage(IMG_DIR+"input_output.tga")
			self.__children["rangeBg"] = rangeBg

			rangeText = self.CreateWindow(ui.TextLine(), rangeBg, (0, 0))
			rangeText.SetAllAlign()
			rangeText.SetText("0")
			self.__children["rangeText"] = rangeText

			itemIcon = self.CreateWindow(ui.ImageBox(), bgImg, (50, 13))
			itemIcon.LoadImage(item.GetIconImageFileName())
			itemIcon.SAFE_SetStringEvent("MOUSE_OVER_OUT",self.__OverOutItem)
			itemIcon.SAFE_SetStringEvent("MOUSE_OVER_IN",self.__OverInItem, BRAVE_CAPE_ITEM_IDX)
			self.__children["itemIcon"] = itemIcon

			startBtn = self.CreateWindow(ui.Button(), bgImg, (6, 95 + 39))
			startBtn.SetUpVisual(IMG_DIR+"start_btn_0.tga")
			startBtn.SetOverVisual(IMG_DIR+"start_btn_1.tga")
			startBtn.SetDownVisual(IMG_DIR+"start_btn_2.tga")
			startBtn.SetDisableVisual(IMG_DIR+"start_btn_2.tga")
			startBtn.SAFE_SetEvent(self.__ClickStatusBtn, "ACTIVE")
			startBtn.SetText(localeInfo.START_BRAVE_CAPE)
			self.__children["startBtn"] = startBtn

			stopBtn = self.CreateWindow(ui.Button(), bgImg, (66, 95 + 39))
			stopBtn.SetUpVisual(IMG_DIR+"start_btn_0.tga")
			stopBtn.SetOverVisual(IMG_DIR+"start_btn_1.tga")
			stopBtn.SetDownVisual(IMG_DIR+"start_btn_2.tga")
			stopBtn.SetDisableVisual(IMG_DIR+"start_btn_2.tga")
			stopBtn.SAFE_SetEvent(self.__ClickStatusBtn, "DEACTIVE")
			stopBtn.SetText(localeInfo.STOP_BRAVE_CAPE)
			self.__children["stopBtn"] = stopBtn

			expandBtn = self.CreateWindow(ui.Button(), self, (0, 10))
			expandBtn.SetUpVisual("d:/ymir work/ui/game/belt_inventory/btn_minimize_normal.tga")
			expandBtn.SetOverVisual("d:/ymir work/ui/game/belt_inventory/btn_minimize_over.tga")
			expandBtn.SetDownVisual("d:/ymir work/ui/game/belt_inventory/btn_minimize_down.tga")
			expandBtn.SAFE_SetEvent(self.Close)
			self.__children["expandBtn"] = expandBtn

			self.__children["second"] = 0
			self.__children["range"] = 0
			self.__children["status"] = False
			self.Refresh()

		def Refresh(self):
			(second, range, posTime, posSlider) = (self.__children["second"], self.__children["range"], 0.0, 0.0)
			if second > 5800:
				second = 5800
			if range > 14000:
				range = 14000

			self.__children["timeText"].SetText(str((second/100)+2))
			self.__children["rangeText"].SetText(str(range+1000))

			self.__children["timeSlider"].SetSliderPos((1.0/5800.0)*second)
			self.__children["rangeSlider"].SetSliderPos((1.0/14000.0)*range)

			self.__children["second"] = second
			self.__children["range"] = range

		def Open(self):
			interface = constInfo.GetInterfaceInstance()
			if interface:
				if interface.wndInventory:
					interface.wndInventory.disbandBtn.Hide()
			self.Show()

		def Close(self):
			interface = constInfo.GetInterfaceInstance()
			if interface:
				if interface.wndInventory:
					interface.wndInventory.disbandBtn.Show()
			self.Hide()

		def __ClickStatusBtn(self, type):
			if type == "ACTIVE":
				net.SendChatPacket("/brave_cape active {} {}".format((self.__children["second"]/100)+2, self.__children["range"] + 1000))
			elif type == "DEACTIVE":
				net.SendChatPacket("/brave_cape deactive")

		def AdjustPosition(self, x, y):
			self.SetPosition(x + 10 - self.GetWidth(), 450)  # Alinear y con disbandBtn en 50

		def OnChangeRangeSlider(self):
			val = int(((1.0/14000.0)*(self.__children["rangeSlider"].GetSliderPos()*14000))*14000)
			self.__children["range"] = val
			self.Refresh()
		def OnChangeTimeSlider(self):
			val = int(((1.0/5800.0)*(self.__children["timeSlider"].GetSliderPos()*5800))*5800)
			self.__children["second"] = val
			self.Refresh()
		def SetStatus(self, status):
			self.__children["status"] = True if int(status) == 1 else False
			if self.__children["status"]:
				self.__children["startBtn"].Disable()
				self.__children["stopBtn"].Enable()
			else:
				self.__children["stopBtn"].Disable()
				self.__children["startBtn"].Enable()
			self.Refresh()
		def SaveData(self):
			try:
				file = open("lib/{}_brave_cape".format(player.GetName()), "w+")
				file.write("{}#{}#{}\n".format(1 if (self.__children["status"] if self.__children.has_key("status") else False) == True else 0, self.__children["second"], self.__children["range"]))
				file.close()
			except:
				pass
		def LoadData(self):
			try:
				splitList = open("lib/{}_brave_cape".format(player.GetName()), "r").readlines()[0].split("#")
				self.__children["status"] = True if int(splitList[0]) == 1 else False
				self.__children["second"] = int(splitList[1])
				self.__children["range"] = int(splitList[2])
				self.Refresh()
				if self.__children["status"]:
					self.__ClickStatusBtn("ACTIVE")
				os.remove("lib/{}_brave_cape".format(player.GetName()))
			except:
				pass

class InventoryWindow(ui.ScriptWindow):

	if app.BL_67_ATTR:
		USE_TYPE_TUPLE = ("USE_CLEAN_SOCKET", "USE_CHANGE_ATTRIBUTE", "USE_CHANGE_ATTRIBUTE2", "USE_ADD_ATTRIBUTE", "USE_ADD_ATTRIBUTE2", "USE_ADD_ACCESSORY_SOCKET", "USE_PUT_INTO_ACCESSORY_SOCKET", "USE_PUT_INTO_BELT_SOCKET", "USE_PUT_INTO_RING_SOCKET")
	else:
		USE_TYPE_TUPLE = ("USE_CLEAN_SOCKET", "USE_CHANGE_ATTRIBUTE", "USE_ADD_ATTRIBUTE", "USE_ADD_ATTRIBUTE2", "USE_ADD_ACCESSORY_SOCKET", "USE_PUT_INTO_ACCESSORY_SOCKET", "USE_PUT_INTO_BELT_SOCKET", "USE_PUT_INTO_RING_SOCKET")
	if app.ENABLE_USE_COSTUME_ATTR:
		USE_TYPE_TUPLE = tuple(list(USE_TYPE_TUPLE) + ["USE_CHANGE_COSTUME_ATTR", "USE_RESET_COSTUME_ATTR", "USE_PUT_INTO_AURA_SOCKET"])
	if app.ELEMENT_SPELL_WORLDARD:
		spell_elements = list(USE_TYPE_TUPLE)
		spell_elements.append("USE_ELEMENT_UPGRADE")
		spell_elements.append("USE_ELEMENT_DOWNGRADE")
		spell_elements.append("USE_ELEMENT_CHANGE")
		USE_TYPE_TUPLE = tuple(spell_elements)

	questionDialog = None
	tooltipItem = None
	wndCostume = None
	wndBelt = None
	dlgPickMoney = None
	if app.ENABLE_CHEQUE_SYSTEM:
		dlgPickETC = None

	interface = None
	bindWnds = []

	if app.ENABLE_PREMIUM_PRIVATE_SHOP:
		wndPrivateShop			= None
		wndPrivateShopSearch	= None

	sellingSlotNumber = -1
	isLoaded = 0
	isOpenedCostumeWindowWhenClosingInventory = 0
	isOpenedBeltWindowWhenClosingInventory = 0

	def __init__(self):

		if app.ENABLE_GEM_SYSTEM:
			self.wndExpandedMoneyBar = None
			self.wndGem = None

		if app.__RENEWAL_BRAVE_CAPE__:
			self.wndBraveCape = None
			self.disbandBtn = None

		ui.ScriptWindow.__init__(self)

		self.isOpenedBeltWindowWhenClosingInventory = 0

		self.inventoryPageIndex = 0

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

		if app.ENABLE_GEM_SYSTEM:
			self.wndExpandedMoneyBar = None
			self.wndGem = None

	def Show(self):
		self.__LoadWindow()

		ui.ScriptWindow.Show(self)

		if self.isOpenedCostumeWindowWhenClosingInventory and self.wndCostume:
			self.wndCostume.Show()

		if self.wndBelt:
			self.wndBelt.Show(self.isOpenedBeltWindowWhenClosingInventory)

		if app.ENABLE_GEM_SYSTEM:
			if self.wndExpandedMoneyBar:
				self.wndExpandedMoneyBar.Show()

	def BindInterfaceClass(self, interface):
		self.interface = interface

	def BindWindow(self, wnd):
		self.bindWnds.append(wnd)

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()

			if app.ENABLE_EXTEND_INVEN_SYSTEM:
				pyScrLoader.LoadScriptFile(self, "UIScript/InventoryWindowEx.py")
 			else:
				if ITEM_MALL_BUTTON_ENABLE:
					pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "InventoryWindow.py")
				else:
					pyScrLoader.LoadScriptFile(self, "UIScript/InventoryWindow.py")
		except:
			import exception
			exception.Abort("InventoryWindow.LoadWindow.LoadObject")

		try:
			wndItem = self.GetChild("ItemSlot")
			wndEquip = self.GetChild("EquipmentSlot")
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.wndMoney = self.GetChild("Money")
			self.wndMoneySlot = self.GetChild("Money_Slot")
			self.mallButton = self.GetChild2("MallButton")
			self.DSSButton = self.GetChild2("DSSButton")
			self.costumeButton = self.GetChild2("CostumeButton")


			if app.ENABLE_CHEQUE_SYSTEM:
				self.wndCheque = self.GetChild("Cheque")
				self.wndChequeSlot = self.GetChild("Cheque_Slot")

				if app.ENABLE_GEM_SYSTEM:
					self.wndMoneyIcon = self.GetChild("Money_Icon")
					self.wndChequeIcon = self.GetChild("Cheque_Icon")
					self.wndMoneyIcon.Hide()
					self.wndMoneySlot.Hide()
					self.wndChequeIcon.Hide()
					self.wndChequeSlot.Hide()

					## 높이 조절
					height = self.GetHeight()
					width = self.GetWidth()
					self.SetSize(width, height - 22)
					self.GetChild("board").SetSize(width, height - 22)

				else:
					self.wndMoneyIcon = self.GetChild("Money_Icon")
					self.wndChequeIcon = self.GetChild("Cheque_Icon")

					self.wndMoneyIcon.SetEvent(ui.__mem_func__(self.EventProgress), "mouse_over_in", 0)
					self.wndChequeIcon.SetEvent(ui.__mem_func__(self.EventProgress), "mouse_over_in", 1)

					self.wndMoneyIcon.SetEvent(ui.__mem_func__(self.EventProgress), "mouse_over_out", 0)
					self.wndChequeIcon.SetEvent(ui.__mem_func__(self.EventProgress), "mouse_over_out", 1)

					self.toolTip = uiToolTip.ToolTip()
					self.toolTip.ClearToolTip()

			self.inventoryTab = []
			for i in xrange(player.INVENTORY_PAGE_COUNT):
				self.inventoryTab.append(self.GetChild("Inventory_Tab_%02d" % (i+1)))

			self.equipmentTab = []
			self.equipmentTab.append(self.GetChild("Equipment_Tab_01"))
			self.equipmentTab.append(self.GetChild("Equipment_Tab_02"))

			if app.BL_TRANSMUTATION_SYSTEM:
				self.dlgQuestion = uiCommon.QuestionDialog2()
				self.dlgQuestion.Close()
				self.listHighlightedChangeLookSlot = []

			if self.costumeButton and not app.ENABLE_COSTUME_SYSTEM:
				self.costumeButton.Hide()
				self.costumeButton.Destroy()
				self.costumeButton = 0

			# Belt Inventory Window
			self.wndBelt = None

			if app.ENABLE_NEW_EQUIPMENT_SYSTEM:
				self.wndBelt = BeltInventoryWindow(self)

			if app.ENABLE_CUBE_RENEWAL:
				self.listHighlightedCubeSlot = []

			if app.ENABLE_ACCE_SYSTEM:
				self.listHighlightedAcceSlot = []

			if app.ENABLE_AURA_SYSTEM:
				self.listHighlightedAuraSlot = []

			if app.WJ_ENABLE_PICKUP_ITEM_EFFECT:
				self.listHighlightedSlot = []

			if app.ENABLE_GEM_CONVERTER:
				self.gem_converter_question_dialog = None
				self.gem_converter_item_pos = (-1, -1)
		except:
			import exception
			exception.Abort("InventoryWindow.LoadWindow.BindObject")

		## Item
		wndItem.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		wndItem.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		wndItem.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		## Equipment
		wndEquip.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		wndEquip.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		wndEquip.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndEquip.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndEquip.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndEquip.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		## PickMoneyDialog
		dlgPickMoney = uiPickMoney.PickMoneyDialog()
		#dlgPickMoney = uiPickItem.PickItemDialog()
		dlgPickMoney.LoadDialog()
		dlgPickMoney.Hide()

		## PickEtcDialog
		if app.ENABLE_CHEQUE_SYSTEM:
			dlgPickETC = uiPickETC.PickEtcDialog()
			dlgPickETC.LoadDialog()
			dlgPickETC.Hide()
			self.dlgPickETC = dlgPickETC

		## RefineDialog
		self.refineDialog = uiRefine.RefineDialog()
		self.refineDialog.Hide()

		## AttachMetinDialog

		self.attachMetinDialog = uiAttachMetin.AttachMetinDialog()
		self.attachMetinDialog.Hide()

		self.previewWindow = uiPreviewCostume.Window()
		self.previewWindow.Hide()

		## MoneySlot
		if app.ENABLE_CHEQUE_SYSTEM:
			self.wndChequeSlot.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog), 1)
			self.wndMoneySlot.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog), 0)
		else:
			self.wndMoneySlot.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog))

		for i in xrange(player.INVENTORY_PAGE_COUNT):
			self.inventoryTab[i].SetEvent(lambda arg=i: self.SetInventoryPage(arg))
		self.inventoryTab[0].Down()

		self.equipmentTab[0].SetEvent(lambda arg=0: self.SetEquipmentPage(arg))
		self.equipmentTab[1].SetEvent(lambda arg=1: self.SetEquipmentPage(arg))
		self.equipmentTab[0].Down()
		self.equipmentTab[0].Hide()
		self.equipmentTab[1].Hide()

		self.wndItem = wndItem
		self.wndEquip = wndEquip
		self.dlgPickMoney = dlgPickMoney

		# MallButton
		if self.mallButton:
			self.mallButton.SetEvent(ui.__mem_func__(self.ClickMallButton))

		if self.DSSButton:
			self.DSSButton.SetEvent(ui.__mem_func__(self.ClickDSSButton))

		# Costume Button
		if self.costumeButton:
			self.costumeButton.SetEvent(ui.__mem_func__(self.ClickCostumeButton))

		self.wndCostume = None
 		#####

		if app.ENABLE_ACCE_SYSTEM:
			self.listAttachedAcces = []

		if app.__RENEWAL_BRAVE_CAPE__:
			if not hasattr(self, "disbandBtn") or self.disbandBtn is None:
				disbandBtn = ui.Button()
				disbandBtn.SetParent(self)
				disbandBtn.SetPosition(0, 50)  # Posicion ajustada segun tu codigo
				disbandBtn.SetUpVisual("d:/ymir work/ui/game/belt_inventory/btn_expand_normal.tga")
				disbandBtn.SetOverVisual("d:/ymir work/ui/game/belt_inventory/btn_expand_over.tga")
				disbandBtn.SetDownVisual("d:/ymir work/ui/game/belt_inventory/btn_expand_down.tga")
				disbandBtn.SAFE_SetEvent(self.ClickBraveCape)
				disbandBtn.Show()
				self.disbandBtn = disbandBtn
	
				self.wndBraveCape = BraveCapeWindow()
				self.OnMoveWindow(*self.GetGlobalPosition())

		## Refresh
		self.SetInventoryPage(0)
		self.SetEquipmentPage(0)
		self.RefreshItemSlot()
		self.RefreshStatus()

	def Destroy(self):
		self.ClearDictionary()

		self.dlgPickMoney.Destroy()
		self.dlgPickMoney = 0

		if app.__RENEWAL_BRAVE_CAPE__:
			if hasattr(self, "disbandBtn") and self.disbandBtn:
				self.disbandBtn.Destroy()
				self.disbandBtn = None
			if self.wndBraveCape:
				self.wndBraveCape.Destroy()
				self.wndBraveCape = None

		if app.ENABLE_CHEQUE_SYSTEM:
			self.dlgPickETC.Destroy()
			self.dlgPickETC = 0

		self.refineDialog.Destroy()
		self.refineDialog = 0

		self.attachMetinDialog.Destroy()
		self.attachMetinDialog = 0

		self.tooltipItem = None
		self.wndItem = 0
		self.wndEquip = 0
		self.dlgPickMoney = 0
		self.wndMoney = 0
		self.wndMoneySlot = 0
		self.questionDialog = None
		self.mallButton = None
		self.DSSButton = None
		self.interface = None
		self.bindWnds = []

		if self.wndCostume:
			self.wndCostume.Destroy()
			self.wndCostume = 0

		if app.ENABLE_CHEQUE_SYSTEM:
			self.wndCheque = 0
			self.wndChequeSlot = 0
			self.dlgPickETC = 0

		if self.wndBelt:
			self.wndBelt.Destroy()
			self.wndBelt = None

		if app.ENABLE_PREMIUM_PRIVATE_SHOP:
			if self.wndPrivateShop:
				self.wndPrivateShop = None

			if self.wndPrivateShopSearch:
				self.wndPrivateShopSearch = None

		if app.BL_TRANSMUTATION_SYSTEM:
			self.dlgQuestion = None

		self.inventoryTab = []
		self.equipmentTab = []

		if app.ENABLE_GEM_CONVERTER:
			if self.gem_converter_question_dialog:
				self.gem_converter_question_dialog.Close()
			self.gem_converter_question_dialog = None

		if app.ENABLE_GEM_SYSTEM:
			self.wndExpandedMoneyBar = None

	def Hide(self):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS():
			self.OnCloseQuestionDialog()
			return
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()

		if self.wndCostume:
			self.isOpenedCostumeWindowWhenClosingInventory = self.wndCostume.IsShow()
			self.wndCostume.Close()

		if self.wndBelt:
			self.isOpenedBeltWindowWhenClosingInventory = self.wndBelt.IsOpeningInventory()
			print "Is Opening Belt Inven?? ", self.isOpenedBeltWindowWhenClosingInventory
			self.wndBelt.Close()

		if self.dlgPickMoney:
			self.dlgPickMoney.Close()

		if app.ENABLE_CHEQUE_SYSTEM:
			if self.dlgPickETC:
				self.dlgPickETC.Close()

		if app.ENABLE_GEM_SYSTEM:
			if self.wndExpandedMoneyBar:
				self.wndExpandedMoneyBar.Close()

		if app.__RENEWAL_BRAVE_CAPE__:
			if self.wndBraveCape:
				self.wndBraveCape.Close()

		wndMgr.Hide(self.hWnd)

	def Close(self):
		self.Hide()

	if app.ENABLE_GEM_SYSTEM:
		def SetExpandedMoneyBar(self, wndBar):
			self.wndExpandedMoneyBar = wndBar

			if self.wndExpandedMoneyBar:
				self.wndMoneySlot = self.wndExpandedMoneyBar.GetMoneySlot()
				self.wndMoney = self.wndExpandedMoneyBar.GetMoney()

				if app.ENABLE_CHEQUE_SYSTEM:
					## 양 관련
					self.wndMoneyIcon = self.wndExpandedMoneyBar.GetMoneyIcon()
					if self.wndMoneyIcon:
						self.wndMoneyIcon.SetEvent(ui.__mem_func__(self.EventProgress), "mouse_over_in", 0)
						self.wndMoneyIcon.SetEvent(ui.__mem_func__(self.EventProgress), "mouse_over_out", 0)
					if self.wndMoneySlot:
						self.wndMoneySlot.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog), 0)

					## 2차화폐 관련
					self.wndChequeIcon = self.wndExpandedMoneyBar.GetChequeIcon()
					if self.wndChequeIcon:
						self.wndChequeIcon.SetEvent(ui.__mem_func__(self.EventProgress), "mouse_over_in", 1)
						self.wndChequeIcon.SetEvent(ui.__mem_func__(self.EventProgress), "mouse_over_out", 1)
					self.wndChequeSlot = self.wndExpandedMoneyBar.GetChequeSlot()
					if self.wndChequeSlot:
						self.wndChequeSlot.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog), 1)
					self.wndCheque = self.wndExpandedMoneyBar.GetCheque()

					## 보석 관련
					self.wndGemIcon = self.wndExpandedMoneyBar.GetGemIcon()
					if self.wndGemIcon:
						self.wndGemIcon.SetEvent(ui.__mem_func__(self.EventProgress), "mouse_over_in", 2)
						self.wndGemIcon.SetEvent(ui.__mem_func__(self.EventProgress), "mouse_over_out", 2)
					self.wndGem = self.wndExpandedMoneyBar.GetGem()

					self.toolTip = uiToolTip.ToolTip()
					self.toolTip.ClearToolTip()
				else:
					if self.wndMoneySlot:
						self.wndMoneySlot.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog))

	def SetInventoryPage(self, page):
		self.inventoryPageIndex = page
		for i in xrange(player.INVENTORY_PAGE_COUNT):
			if i!=page:
				self.inventoryTab[i].SetUp()
		self.RefreshBagSlotWindow()

	def SetEquipmentPage(self, page):
		self.equipmentPageIndex = page
		self.equipmentTab[1-page].SetUp()
		self.RefreshEquipSlotWindow()

	def ClickMallButton(self):
		print "click_mall_button"
		net.SendChatPacket("/click_mall")

	# DSSButton
	def ClickDSSButton(self):
		print "click_dss_button"
		self.interface.ToggleDragonSoulWindow()

	if app.__RENEWAL_BRAVE_CAPE__:
		def ClickBraveCape(self):
			if self.wndBraveCape:
				if self.wndBraveCape.IsShow():
					self.wndBraveCape.Close()
				else:
					self.wndBraveCape.Open()

	def ClickCostumeButton(self):
		print "Click Costume Button"
		if self.wndCostume:
			if self.wndCostume.IsShow():
				self.wndCostume.Hide()
			else:
				self.wndCostume.Show()
		else:
			self.wndCostume = CostumeWindow(self)
			self.wndCostume.Show()

	if app.ENABLE_CHEQUE_SYSTEM:
		def OpenPickMoneyDialog(self, focus_idx = 0):
			if mouseModule.mouseController.isAttached():

				attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
				if player.SLOT_TYPE_SAFEBOX == mouseModule.mouseController.GetAttachedType():

					if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
						net.SendSafeboxWithdrawMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
						snd.PlaySound("sound/ui/money.wav")

				mouseModule.mouseController.DeattachObject()

			else:
				curMoney = player.GetElk()
				curCheque = player.GetCheque()

				if curMoney <= 0 and curCheque <= 0:
					return

				self.dlgPickMoney.SetTitleName(localeInfo.PICK_MONEY_TITLE)
				self.dlgPickMoney.SetAcceptEvent(ui.__mem_func__(self.OnPickMoney))
				self.dlgPickMoney.Open(curMoney, curCheque)
				self.dlgPickMoney.SetMax(9) # 인벤토리 990000 제한 버그 수정
				self.dlgPickMoney.SetFocus(0)
	else:
		def OpenPickMoneyDialog(self):

			if mouseModule.mouseController.isAttached():

				attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
				if player.SLOT_TYPE_SAFEBOX == mouseModule.mouseController.GetAttachedType():

					if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
						net.SendSafeboxWithdrawMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
						snd.PlaySound("sound/ui/money.wav")

				mouseModule.mouseController.DeattachObject()

			else:
				curMoney = player.GetElk()

				if curMoney <= 0:
					return

				self.dlgPickMoney.SetTitleName(localeInfo.PICK_MONEY_TITLE)
				self.dlgPickMoney.SetAcceptEvent(ui.__mem_func__(self.OnPickMoney))
				self.dlgPickMoney.Open(curMoney)
				self.dlgPickMoney.SetMax(9) # 인벤토리 990000 제한 버그 수정

	if app.ENABLE_CHEQUE_SYSTEM:
		def OnPickMoney(self, money, cheque):
			mouseModule.mouseController.AttachMoney(self, player.SLOT_TYPE_INVENTORY, money, cheque)
	else:
		def OnPickMoney(self, money):
			mouseModule.mouseController.AttachMoney(self, player.SLOT_TYPE_INVENTORY, money)

	def OnPickItem(self, count):
		if app.ENABLE_CHEQUE_SYSTEM:
			itemSlotIndex = self.dlgPickETC.itemGlobalSlotIndex
		else:
			itemSlotIndex = self.dlgPickMoney.itemGlobalSlotIndex
		selectedItemVNum = player.GetItemIndex(itemSlotIndex)
		mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum, count)

	def __InventoryLocalSlotPosToGlobalSlotPos(self, local):
		if player.IsEquipmentSlot(local) or player.IsCostumeSlot(local) or (player.IsBeltInventorySlot(local)):
			return local

		if app.ENABLE_SPECIAL_INVENTORY_SYSTEM:
			if player.IsSkillBookInventorySlot(local) or player.IsUpgradeItemsInventorySlot(local) or player.IsStoneInventorySlot(local) or player.IsGiftBoxInventorySlot(local):
				return local

		return self.inventoryPageIndex * player.INVENTORY_PAGE_SIZE + local

	if app.ENABLE_CHEQUE_SYSTEM:
		def GetInventoryPageIndex(self):
			## 0 or 1
			return self.inventoryPageIndex

	def GetAllCostumeItems(self):
		costumeItems = []
		for slot in xrange(player.INVENTORY_PAGE_COUNT * player.INVENTORY_PAGE_SIZE):
			vnum = player.GetItemIndex(slot)
			if vnum == 0:
				continue

			item.SelectItem(vnum)
			itemType = item.GetItemType()
			itemSubType = item.GetItemSubType()

			if itemType == item.ITEM_TYPE_COSTUME:
				costumeItems.append(vnum)
			elif itemSubType == item.PET_PAY:
				costumeItems.append(vnum)
		return costumeItems

	def RefreshMarkSlots(self, localIndex=None):
		if not self.interface:
			return

		onTopWnd = self.interface.GetOnTopWindow()
		if localIndex:
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(localIndex)
			if onTopWnd == player.ON_TOP_WND_NONE:
				self.wndItem.SetUsableSlotOnTopWnd(localIndex)

			elif onTopWnd == player.ON_TOP_WND_SHOP:
				if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SELL):
					self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
				else:
					self.wndItem.SetUsableSlotOnTopWnd(localIndex)

			elif onTopWnd == player.ON_TOP_WND_EXCHANGE:
				if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_GIVE):
					self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
				else:
					self.wndItem.SetUsableSlotOnTopWnd(localIndex)

			elif onTopWnd == player.ON_TOP_WND_PRIVATE_SHOP:
				if player.IsAntiFlagBySlot(slotNumber, item.ITEM_ANTIFLAG_MYSHOP):
					self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
				else:
					self.wndItem.SetUsableSlotOnTopWnd(localIndex)

			elif onTopWnd == player.ON_TOP_WND_SAFEBOX:
				if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SAFEBOX):
					self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
				else:
					self.wndItem.SetUsableSlotOnTopWnd(localIndex)

			return

		for i in xrange(player.INVENTORY_PAGE_SIZE):
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)

			if onTopWnd == player.ON_TOP_WND_NONE:
				self.wndItem.SetUsableSlotOnTopWnd(i)

			elif onTopWnd == player.ON_TOP_WND_SHOP:
				if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SELL):
					self.wndItem.SetUnusableSlotOnTopWnd(i)
				else:
					self.wndItem.SetUsableSlotOnTopWnd(i)

			elif onTopWnd == player.ON_TOP_WND_EXCHANGE:
				if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_GIVE):
					self.wndItem.SetUnusableSlotOnTopWnd(i)
				else:
					self.wndItem.SetUsableSlotOnTopWnd(i)

			elif onTopWnd == player.ON_TOP_WND_PRIVATE_SHOP:
				if player.IsAntiFlagBySlot(slotNumber, item.ITEM_ANTIFLAG_MYSHOP):
					self.wndItem.SetUnusableSlotOnTopWnd(i)
				else:
					self.wndItem.SetUsableSlotOnTopWnd(i)

			elif onTopWnd == player.ON_TOP_WND_SAFEBOX:
				if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SAFEBOX):
					self.wndItem.SetUnusableSlotOnTopWnd(i)
				else:
					self.wndItem.SetUsableSlotOnTopWnd(i)

	def GetSlotListByVnum(self, vnum, count = 1):
		itemSlots = list()

		counts = 0
		for special_index in range(player.INVENTORY_PAGE_COUNT):
			for page in xrange(0, 4):
				for i in xrange(player.INVENTORY_PAGE_SIZE):
					slotNumber = page * player.INVENTORY_PAGE_SIZE + i

					if player.GetItemIndex(slotNumber) == vnum:
						if app.ENABLE_CUBE_RENEWAL and app.ENABLE_SET_ITEM:
							if player.GetItemSetValue(player.INVENTORY, slotNumber):
								continue

						tempSlotNum = slotNumber
						itemSlots.append((tempSlotNum, page, special_index))

						counts += player.GetItemCount(slotNumber)

						if counts >= count:
							return itemSlots

		return itemSlots

	def RefreshBagSlotWindow(self):
		if not self.wndItem:
			return

		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setItemVNum=self.wndItem.SetItemSlot

		if app.WJ_ENABLE_TRADABLE_ICON:
			if self.interface:
				onTopWindow = self.interface.GetOnTopWindow()

		for i in xrange(player.INVENTORY_PAGE_SIZE):
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)

			itemCount = getItemCount(slotNumber)
			if 0 == itemCount:
				self.wndItem.ClearSlot(i)
				continue
			elif 1 == itemCount:
				itemCount = 0

			itemVnum = getItemVNum(slotNumber)
			setItemVNum(i, itemVnum, itemCount)

			if constInfo.IS_AUTO_POTION(itemVnum):
				metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]

				isActivated = 0 != metinSocket[0]

				if isActivated:
					self.wndItem.ActivateSlot(i)
					potionType = 0
					if constInfo.IS_AUTO_POTION_HP(itemVnum):
						potionType = player.AUTO_POTION_TYPE_HP
					elif constInfo.IS_AUTO_POTION_SP(itemVnum):
						potionType = player.AUTO_POTION_TYPE_SP

					usedAmount = int(metinSocket[1])
					totalAmount = int(metinSocket[2])
					player.SetAutoPotionInfo(potionType, isActivated, (totalAmount - usedAmount), totalAmount, self.__InventoryLocalSlotPosToGlobalSlotPos(i))

				else:
					self.wndItem.DeactivateSlot(i)

			if app.ENABLE_SOUL_SYSTEM:
				if item.IsSoulItem(itemVnum):
					metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
					tempSlotNum = slotNumber
					if tempSlotNum >= player.INVENTORY_PAGE_SIZE:
						tempSlotNum -= (self.inventoryPageIndex * player.INVENTORY_PAGE_SIZE)

					if 0 != metinSocket[1]:
						self.wndItem.ActivateSlot(tempSlotNum)
					else:
						self.wndItem.DeactivateSlot(tempSlotNum)

			#if app.ENABLE_EXTENDED_BLEND_AFFECT:
			#	currentItemVnum = player.GetItemIndex(slotNumber)
			#	
			#	tempSlotNum = slotNumber
			#	if tempSlotNum >= player.INVENTORY_PAGE_SIZE:
			#		tempSlotNum -= (self.inventoryPageIndex * player.INVENTORY_PAGE_SIZE)
			#	
			#	if currentItemVnum == 0:
			#		self.wndItem.DeactivateSlot(tempSlotNum)
			#	elif constInfo.IS_BLEND_POTION(currentItemVnum) or constInfo.IS_EXTENDED_BLEND_POTION(currentItemVnum):
			#		metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
			#		isActivated = 0 != metinSocket[3]
			#		
			#		if isActivated:
			#			self.wndItem.ActivateSlot(tempSlotNum)
			#			if constInfo.IS_EXTENDED_BLEND_POTION(currentItemVnum):
			#				self.wndItem.SetSlotDiffuseColor(tempSlotNum, wndMgr.COLOR_TYPE_PURPLE)
			#			else:
			#				self.wndItem.SetSlotDiffuseColor(tempSlotNum, wndMgr.COLOR_TYPE_DARK_BLUE)
			#		else:
			#			self.wndItem.DeactivateSlot(tempSlotNum)
			#	else:
			#		self.wndItem.DeactivateSlot(tempSlotNum)
			#
			#	if constInfo.IS_EXTENDED_BLEND_POTION(currentItemVnum):
			#		self.wndItem.DisableCoverButton(tempSlotNum)

			if app.ENABLE_EXTENDED_BLEND_AFFECT:
				currentItemVnum = player.GetItemIndex(slotNumber)
				tempSlotNum = slotNumber
				if tempSlotNum >= player.INVENTORY_PAGE_SIZE:
					tempSlotNum -= (self.inventoryPageIndex * player.INVENTORY_PAGE_SIZE)

				if currentItemVnum == 0:
					self.wndItem.DeactivateSlot(tempSlotNum)
				elif constInfo.IS_BLEND_POTION(currentItemVnum) or constInfo.IS_EXTENDED_BLEND_POTION(currentItemVnum):
					metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
					isActivated = 0 != metinSocket[3]

					if isActivated:
						self.wndItem.ActivateSlot(tempSlotNum)
						if constInfo.IS_EXTENDED_BLEND_POTION(currentItemVnum):
							self.wndItem.SetSlotDiffuseColor(tempSlotNum, wndMgr.COLOR_TYPE_PURPLE)
						else:
							self.wndItem.SetSlotDiffuseColor(tempSlotNum, wndMgr.COLOR_TYPE_DARK_BLUE)
					else:
						self.wndItem.DeactivateSlot(tempSlotNum)
				elif constInfo.IS_ELIXIR(currentItemVnum):
					metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
					isActivated = 0 != metinSocket[0]

					if isActivated:
						self.wndItem.ActivateSlot(tempSlotNum)
						self.wndItem.SetSlotDiffuseColor(tempSlotNum, wndMgr.COLOR_TYPE_YELLOW)
					else:
						self.wndItem.DeactivateSlot(tempSlotNum)
				else:
					self.wndItem.DeactivateSlot(tempSlotNum)

				if constInfo.IS_EXTENDED_BLEND_POTION(currentItemVnum):
					self.wndItem.DisableCoverButton(tempSlotNum)

			if app.WJ_ENABLE_TRADABLE_ICON:
				if itemVnum and self.interface and onTopWindow:
					if self.interface.MarkUnusableInvenSlotOnTopWnd(onTopWindow,slotNumber):
						self.wndItem.SetUnusableSlotOnTopWnd(i)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(i)
				else:
					self.wndItem.SetUsableSlotOnTopWnd(i)

			if app.ENABLE_GEM_CONVERTER:
				if slotNumber in self.gem_converter_item_pos:
					self.wndItem.SetCantMouseEventSlot(i)

			if app.ENABLE_ACCE_SYSTEM:
				slotNumberChecked = 0
				if not constInfo.IS_AUTO_POTION(itemVnum):
					self.wndItem.DeactivateAcceSlot(i)

				for j in xrange(acce.WINDOW_MAX_MATERIALS):
					(isHere, iCell) = acce.GetAttachedItem(j)
					if isHere:
						if iCell == slotNumber:
							self.wndItem.ActivateAcceSlot(i, (36.00 / 255.0), (222.00 / 255.0), (3.00 / 255.0), 1.0)
							if not slotNumber in self.listAttachedAcces:
								self.listAttachedAcces.append(slotNumber)

							slotNumberChecked = 1
					else:
						if slotNumber in self.listAttachedAcces and not slotNumberChecked:
							self.wndItem.DeactivateAcceSlot(i)
							self.listAttachedAcces.remove(slotNumber)


			if app.BL_TRANSMUTATION_SYSTEM:
				if not player.GetChangeLookVnum(player.INVENTORY, slotNumber) == 0:
					self.wndItem.SetSlotCoverImage(i,"icon/item/ingame_convert_Mark.tga")
				else:
					self.wndItem.EnableSlotCoverImage(i,False)

		self.__HighlightSlot_Refresh()

		self.wndItem.RefreshSlot()

		if self.wndBelt:
			self.wndBelt.RefreshSlot()

		map(lambda wnd:wnd.RefreshLockedSlot(), self.bindWnds)

		if app.ENABLE_PREMIUM_PRIVATE_SHOP:
			if self.wndPrivateShop and self.wndPrivateShop.IsShow():
				self.wndPrivateShop.RefreshLockedSlot()

	def RefreshEquipSlotWindow(self):
		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setItemVNum=self.wndEquip.SetItemSlot
		for i in xrange(player.EQUIPMENT_PAGE_COUNT):
			slotNumber = player.EQUIPMENT_SLOT_START + i
			itemCount = getItemCount(slotNumber)
			if itemCount <= 1:
				itemCount = 0
			setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)

			if app.BL_TRANSMUTATION_SYSTEM:
				if not player.GetChangeLookVnum(player.EQUIPMENT, slotNumber) == 0:
					self.wndEquip.SetSlotCoverImage(slotNumber,"icon/item/ingame_convert_Mark.tga")
				else:
					self.wndEquip.EnableSlotCoverImage(slotNumber,False)

			setItemVNum(item.EQUIPMENT_GLOVE, getItemVNum(item.EQUIPMENT_GLOVE), 0)
			setItemVNum(item.EQUIPMENT_PENDANT, getItemVNum(item.EQUIPMENT_PENDANT), 0)

		if app.ENABLE_NEW_EQUIPMENT_SYSTEM:
			for i in xrange(player.NEW_EQUIPMENT_SLOT_COUNT):
				slotNumber = player.NEW_EQUIPMENT_SLOT_START + i
				itemCount = getItemCount(slotNumber)
				if itemCount <= 1:
					itemCount = 0
				setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)
				print "ENABLE_NEW_EQUIPMENT_SYSTEM", slotNumber, itemCount, getItemVNum(slotNumber)



		self.wndEquip.RefreshSlot()

		if self.wndCostume:
			self.wndCostume.RefreshCostumeSlot()

		self.GetAllCostumeItems()

	def RefreshItemSlot(self):
		self.RefreshBagSlotWindow()
		self.RefreshEquipSlotWindow()

	def RefreshStatus(self):
		money = player.GetElk()
		self.wndMoney.SetText(localeInfo.NumberToMoney(money))

		if app.ENABLE_CHEQUE_SYSTEM:
			cheque = player.GetCheque()
			self.wndCheque.SetText(str(cheque))

		if app.ENABLE_GEM_SYSTEM:
			if self.wndGem:
				gem = player.GetGem()
				self.wndGem.SetText(localeInfo.NumberToMoneyString(gem))

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	if app.WJ_ENABLE_PICKUP_ITEM_EFFECT:
		# 슬롯 highlight 관련
		## 추가
		def HighlightSlot(self, slot):
			#slot값에 대한 예외처리.
			if slot > player.INVENTORY_PAGE_SIZE * player.INVENTORY_PAGE_COUNT:
				return

			if not slot in self.listHighlightedSlot:
				self.listHighlightedSlot.append(slot)

		## 삭제
		def DelHighlightSlot(self, inventorylocalslot):
			if inventorylocalslot in self.listHighlightedSlot:
				if inventorylocalslot >= player.INVENTORY_PAGE_SIZE:
					self.wndItem.DeactivateSlot(inventorylocalslot - (self.inventoryPageIndex * player.INVENTORY_PAGE_SIZE))
				else:
					self.wndItem.DeactivateSlot(inventorylocalslot)

				self.listHighlightedSlot.remove(inventorylocalslot)
		# 슬롯 highlight 관련 끝

	if app.BL_TRANSMUTATION_SYSTEM:
		def IsDlgQuestionShow(self):
			if self.dlgQuestion.IsShow():
				return True
			else:
				return False
		
		def CancelDlgQuestion(self):
			self.__Cancel()
		
		def __OpenQuestionDialog(self, srcItemPos, dstItemPos):
			if self.interface.IsShowDlgQuestionWindow():
				self.interface.CloseDlgQuestionWindow()
				
			getItemVNum=player.GetItemIndex
			self.srcItemPos = srcItemPos
			self.dstItemPos = dstItemPos
			
			self.dlgQuestion.SetAcceptEvent(ui.__mem_func__(self.__Accept))
			self.dlgQuestion.SetCancelEvent(ui.__mem_func__(self.__Cancel))

			self.dlgQuestion.SetText1("%s" % item.GetItemName(getItemVNum(srcItemPos)) )
			self.dlgQuestion.SetText2(localeInfo.INVENTORY_REALLY_USE_ITEM)

			self.dlgQuestion.Open()
			
		def __Accept(self):
			self.dlgQuestion.Close()
			self.__SendUseItemToItemPacket(self.srcItemPos, self.dstItemPos)
			self.srcItemPos = (0, 0)
			self.dstItemPos = (0, 0)

		def __Cancel(self):
			self.srcItemPos = (0, 0)
			self.dstItemPos = (0, 0)
			self.dlgQuestion.Close()

	def SetUseItemMode(self, bUse):
		self.wndItem.SetUseMode(bUse)

	def SellItem(self):
		if self.sellingSlotitemIndex == player.GetItemIndex(self.sellingSlotNumber):
			if self.sellingSlotitemCount == player.GetItemCount(self.sellingSlotNumber):
				net.SendShopSellPacketNew(self.sellingSlotNumber, self.questionDialog.count, player.INVENTORY)
				snd.PlaySound("sound/ui/money.wav")
		self.OnCloseQuestionDialog()

	def OnDetachMetinFromItem(self):
		if None == self.questionDialog:
			return

		#net.SendItemUseToItemPacket(self.questionDialog.sourcePos, self.questionDialog.targetPos)
		self.__SendUseItemToItemPacket(self.questionDialog.sourcePos, self.questionDialog.targetPos)
		self.OnCloseQuestionDialog()

	def OnCloseQuestionDialog(self):
		if not self.questionDialog:
			return

		self.questionDialog.Close()
		self.questionDialog = None
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

	## Slot Event
	def SelectEmptySlot(self, selectedSlotPos):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return
	
		if app.BL_TRANSMUTATION_SYSTEM:
			if player.GetChangeLookWindowOpen() == 1:
				return
	
		if app.ENABLE_AURA_SYSTEM:
			if player.IsAuraRefineWindowOpen():
				return
	
		selectedSlotPos = self.__InventoryLocalSlotPosToGlobalSlotPos(selectedSlotPos)
	
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()
			attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()
	
			if player.SLOT_TYPE_INVENTORY == attachedSlotType or \
			   player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedSlotType:
				# Mover items desde inventario normal o Dragon Soul
				itemCount = player.GetItemCount(attachedSlotPos)
				attachedCount = mouseModule.mouseController.GetAttachedItemCount()
				self.__SendMoveItemPacket(attachedSlotPos, selectedSlotPos, attachedCount)
	
				# Desactivar el modo de uso si es un scroll de refinamiento
				if item.IsRefineScroll(attachedItemIndex):
					self.wndItem.SetUseMode(False)
	
			elif player.SLOT_TYPE_SWITCHBOT == attachedSlotType:
				# Mover items desde Switchbot al inventario
				itemCount = player.GetItemCount(attachedSlotPos)
				attachedCount = mouseModule.mouseController.GetAttachedItemCount()
				net.SendItemMovePacket(player.SWITCHBOT, attachedSlotPos, player.INVENTORY, selectedSlotPos, attachedCount)
				if item.IsRefineScroll(attachedItemIndex):
					self.wndItem.SetUseMode(False)
	
			elif player.SLOT_TYPE_PRIVATE_SHOP == attachedSlotType:
				if app.ENABLE_PREMIUM_PRIVATE_SHOP:
					if not uiPrivateShopBuilder.IsBuildingPrivateShop():
						self.wndPrivateShop.SendItemCheckoutPacket(attachedSlotPos, selectedSlotPos)
						mouseModule.mouseController.DeattachObject()
						return
				mouseModule.mouseController.RunCallBack("INVENTORY")
	
			elif player.SLOT_TYPE_BUFF_EQUIPMENT == attachedSlotType and app.ENABLE_ASLAN_BUFF_NPC_SYSTEM:
				attachedCount = mouseModule.mouseController.GetAttachedItemCount()
				net.SendItemMovePacket(player.BUFF_EQUIPMENT, attachedSlotPos, player.INVENTORY, selectedSlotPos, attachedCount)
	
			elif player.SLOT_TYPE_SHOP == attachedSlotType:
				net.SendShopBuyPacket(attachedSlotPos)
	
			elif player.SLOT_TYPE_SAFEBOX == attachedSlotType:
				if player.ITEM_MONEY == attachedItemIndex:
					net.SendSafeboxWithdrawMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
					snd.PlaySound("sound/ui/money.wav")
				else:
					net.SendSafeboxCheckoutPacket(attachedSlotPos, selectedSlotPos)
	
			elif player.SLOT_TYPE_MALL == attachedSlotType:
				net.SendMallCheckoutPacket(attachedSlotPos, selectedSlotPos)
	
			elif app.ENABLE_AURA_SYSTEM and player.SLOT_TYPE_AURA == attachedSlotType:
				net.SendAuraRefineCheckOut(attachedSlotPos, player.GetAuraRefineWindowType())
	
			mouseModule.mouseController.DeattachObject()

	def SelectItemSlot(self, itemSlotIndex):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return
	
		itemSlotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(itemSlotIndex)
	
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemVID = mouseModule.mouseController.GetAttachedItemIndex()
	
			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				#@fixme011 BEGIN (block ds equip)
				attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
				if player.IsDSEquipmentSlot(attachedInvenType, attachedSlotPos):
					mouseModule.mouseController.DeattachObject()
					return
				#@fixme011 END
				self.__DropSrcItemToDestItemInInventory(attachedItemVID, attachedSlotPos, itemSlotIndex)
	
			mouseModule.mouseController.DeattachObject()
	
		else:
			curCursorNum = app.GetCursor()
			if app.SELL == curCursorNum:
				self.__SellItem(itemSlotIndex)
	
			elif app.BUY == curCursorNum:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_BUY_INFO)
	
			elif app.IsPressed(app.DIK_LALT):
				link = player.GetItemLink(itemSlotIndex)
				ime.PasteString(link)
	
			elif app.IsPressed(app.DIK_LSHIFT):
				itemCount = player.GetItemCount(itemSlotIndex)
	
				# Verificar si el slot pertenece al inventario especial o normal
				isSpecialInventory = (
					app.ENABLE_SPECIAL_INVENTORY_SYSTEM and
					(
						player.IsSkillBookInventorySlot(itemSlotIndex) or
						player.IsUpgradeItemsInventorySlot(itemSlotIndex) or
						player.IsStoneInventorySlot(itemSlotIndex) or
						player.IsGiftBoxInventorySlot(itemSlotIndex)
					)
				)
	
				if itemCount > 1:
					# Abrir el dialogo de separacion para items con mas de una unidad
					if app.ENABLE_CHEQUE_SYSTEM:
						self.dlgPickETC.SetTitleName(localeInfo.PICK_ITEM_TITLE)
						self.dlgPickETC.SetAcceptEvent(ui.__mem_func__(self.OnPickItem))
						self.dlgPickETC.Open(itemCount)
						self.dlgPickETC.itemGlobalSlotIndex = itemSlotIndex
					else:
						self.dlgPickMoney.SetTitleName(localeInfo.PICK_ITEM_TITLE)
						self.dlgPickMoney.SetAcceptEvent(ui.__mem_func__(self.OnPickItem))
						self.dlgPickMoney.Open(itemCount)
						self.dlgPickMoney.itemGlobalSlotIndex = itemSlotIndex
				elif itemCount == 1 and (isSpecialInventory or not player.IsEquipmentSlot(itemSlotIndex)):
					# Permitir seleccionar items individuales en el inventario especial o normal
					selectedItemVNum = player.GetItemIndex(itemSlotIndex)
					mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum, itemCount)
					snd.PlaySound("sound/ui/pick.wav")
	
			elif app.IsPressed(app.DIK_LCONTROL):
				itemIndex = player.GetItemIndex(itemSlotIndex)
	
				if app.ENABLE_PREMIUM_PRIVATE_SHOP:
					if self.wndPrivateShop and self.wndPrivateShop.IsShow():
						self.wndPrivateShop.AttachItemToPrivateShop(itemSlotIndex, player.SLOT_TYPE_INVENTORY)
						return
	
					if self.wndPrivateShopSearch and self.wndPrivateShopSearch.IsShow():
						self.wndPrivateShopSearch.SelectItem(itemIndex)
						return
	
				if True == item.CanAddToQuickSlotItem(itemIndex):
					player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_INVENTORY, itemSlotIndex)
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.QUICKSLOT_REGISTER_DISABLE_ITEM)
	
			else:
				selectedItemVNum = player.GetItemIndex(itemSlotIndex)
				itemCount = player.GetItemCount(itemSlotIndex)
				mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum, itemCount)
	
				if self.__IsUsableItemToItem(selectedItemVNum, itemSlotIndex):
					self.wndItem.SetUseMode(True)
				else:
					self.wndItem.SetUseMode(False)
	
				snd.PlaySound("sound/ui/pick.wav")

	if app.ENABLE_PREMIUM_PRIVATE_SHOP:
		def BindPrivateShopClass(self, window):
			self.wndPrivateShop = window

		def BindPrivateShopSearchClass(self, window):
			self.wndPrivateShopSearch = window

	def __DropSrcItemToDestItemInInventory(self, srcItemVID, srcItemSlotPos, dstItemSlotPos):
		if app.ENABLE_AURA_SYSTEM and player.IsAuraRefineWindowOpen():
			return

		if srcItemSlotPos == dstItemSlotPos:
			return

		if app.BL_TRANSMUTATION_SYSTEM:
			if player.GetChangeLookWindowOpen() == 1:
				return

		# cyh itemseal 2013 11 08
		if app.ENABLE_SOULBIND_SYSTEM and item.IsSealScroll(srcItemVID):
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)

		elif item.IsRefineScroll(srcItemVID):
			self.RefineItem(srcItemSlotPos, dstItemSlotPos)
			self.wndItem.SetUseMode(False)

		elif item.IsMetin(srcItemVID):
			self.AttachMetinToItem(srcItemSlotPos, dstItemSlotPos)

		elif item.IsDetachScroll(srcItemVID):
			self.DetachMetinFromItem(srcItemSlotPos, dstItemSlotPos)

		elif app.ELEMENT_SPELL_WORLDARD and item.IsElement(srcItemVID):
			self.ElementItem(srcItemSlotPos,dstItemSlotPos)

		elif item.IsKey(srcItemVID):
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)

		elif (player.GetItemFlags(srcItemSlotPos) & ITEM_FLAG_APPLICABLE) == ITEM_FLAG_APPLICABLE:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)

		elif item.GetUseType(srcItemVID) in self.USE_TYPE_TUPLE:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)

		else:
			#snd.PlaySound("sound/ui/drop.wav")

			if app.BL_TRANSMUTATION_SYSTEM:
				if item.IsChangeLookClearScroll(srcItemVID):
					if player.CanChangeLookClearItem(srcItemVID, player.INVENTORY, dstItemSlotPos):
						self.__OpenQuestionDialog(srcItemSlotPos, dstItemSlotPos)
						return

			if app.ENABLE_SET_ITEM:
				if item.IsSetItemScroll(srcItemVID):
					if player.CanSetItemClearItem(srcItemVID, dstItemSlotPos):
						self.__OpenQuestionDialog(srcItemSlotPos, dstItemSlotPos)
						return

			if app.ENABLE_GEM_CONVERTER:
				if srcItemVID == item.ITEM_VNUM_GEM_CONVERTER:
					if self.__CanUseGemConverter(srcItemVID, srcItemSlotWindow, srcItemSlotPos, dstItemSlotWindow, dstItemSlotPos):
						self.__UseGemConverter(srcItemSlotWindow, srcItemSlotPos, dstItemSlotWindow, dstItemSlotPos)
						return

			if player.IsEquipmentSlot(dstItemSlotPos):

				if item.IsEquipmentVID(srcItemVID):
					self.__UseItem(srcItemSlotPos)

			else:
				self.__SendMoveItemPacket(srcItemSlotPos, dstItemSlotPos, 0)
				#net.SendItemMovePacket(srcItemSlotPos, dstItemSlotPos, 0)

	def __SellItem(self, itemSlotPos):
		if not player.IsEquipmentSlot(itemSlotPos):
			self.sellingSlotNumber = itemSlotPos
			itemIndex = player.GetItemIndex(itemSlotPos)
			itemCount = player.GetItemCount(itemSlotPos)


			self.sellingSlotitemIndex = itemIndex
			self.sellingSlotitemCount = itemCount

			item.SelectItem(itemIndex)
			## 20140220
			if item.IsAntiFlag(item.ANTIFLAG_SELL):
				popup = uiCommon.PopupDialog()
				popup.SetText(localeInfo.SHOP_CANNOT_SELL_ITEM)
				popup.SetAcceptEvent(self.__OnClosePopupDialog)
				popup.Open()
				self.popup = popup
				return

			itemPrice = item.GetISellItemPrice()

			if item.Is1GoldItem():
				itemPrice = itemCount / itemPrice / 5
			else:
				itemPrice = itemPrice * itemCount / 5

			item.GetItemName(itemIndex)
			itemName = item.GetItemName()

			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText(localeInfo.DO_YOU_SELL_ITEM(itemName, itemCount, itemPrice))
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.SellItem))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
			self.questionDialog.Open()
			self.questionDialog.count = itemCount

			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

	def __OnClosePopupDialog(self):
		self.pop = None

	if app.ELEMENT_SPELL_WORLDARD:
		def ElementItem(self, srcItemSlotPos,dstItemSlotPos):
			itemElement = player.GetItemIndex(srcItemSlotPos)

			if player.ELEMENT_UPGRADE_CANT_ADD == player.GetElements(itemElement,dstItemSlotPos) or\
				player.ELEMENT_DOWNGRADE_CANT_ADD == player.GetElements(itemElement,dstItemSlotPos) or\
				player.ELEMENT_CANT_WORLDARD == player.GetElements(itemElement,dstItemSlotPos) or\
				player.ELEMENT_CHANGE_CANT_ADD == player.GetElements(itemElement,dstItemSlotPos):
				chat.AppendChat(chat.CHAT_TYPE_INFO, "No se puede realizar esta funcion.")
				return

			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)

	def RefineItem(self, scrollSlotPos, targetSlotPos):

		scrollIndex = player.GetItemIndex(scrollSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)

		if player.REFINE_OK != player.CanRefine(scrollIndex, targetSlotPos):
			return

		###########################################################
		self.__SendUseItemToItemPacket(scrollSlotPos, targetSlotPos)
		#net.SendItemUseToItemPacket(scrollSlotPos, targetSlotPos)
		return
		###########################################################

		###########################################################
		#net.SendRequestRefineInfoPacket(targetSlotPos)
		#return
		###########################################################

		result = player.CanRefine(scrollIndex, targetSlotPos)

		if player.REFINE_ALREADY_MAX_SOCKET_COUNT == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NO_MORE_SOCKET)

		elif player.REFINE_NEED_MORE_GOOD_SCROLL == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NEED_BETTER_SCROLL)

		elif player.REFINE_CANT_MAKE_SOCKET_ITEM == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_SOCKET_DISABLE_ITEM)

		elif player.REFINE_NOT_NEXT_GRADE_ITEM == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_UPGRADE_DISABLE_ITEM)

		elif player.REFINE_CANT_REFINE_METIN_TO_EQUIPMENT == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_EQUIP_ITEM)

		if player.REFINE_OK != result:
			return

		self.refineDialog.Open(scrollSlotPos, targetSlotPos)

	def DetachMetinFromItem(self, scrollSlotPos, targetSlotPos):
		scrollIndex = player.GetItemIndex(scrollSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)

		if not player.CanDetach(scrollIndex, targetSlotPos):
			if app.ENABLE_ACCE_SYSTEM:
				item.SelectItem(scrollIndex)
				if item.GetValue(0) == acce.CLEAN_ATTR_VALUE0:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.ACCE_FAILURE_CLEAN)
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_METIN_INSEPARABLE_ITEM)
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_METIN_INSEPARABLE_ITEM)
			return

		self.questionDialog = uiCommon.QuestionDialog()
		self.questionDialog.SetText(localeInfo.REFINE_DO_YOU_SEPARATE_METIN)
		if app.ENABLE_ACCE_SYSTEM:
			item.SelectItem(targetIndex)
			if item.GetItemType() == item.ITEM_TYPE_COSTUME and item.GetItemSubType() == item.COSTUME_TYPE_ACCE:
				item.SelectItem(scrollIndex)
				if item.GetValue(0) == acce.CLEAN_ATTR_VALUE0:
					self.questionDialog.SetText(localeInfo.ACCE_DO_YOU_CLEAN)

		self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnDetachMetinFromItem))
		self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		self.questionDialog.Open()
		self.questionDialog.sourcePos = scrollSlotPos
		self.questionDialog.targetPos = targetSlotPos

	def AttachMetinToItem(self, metinSlotPos, targetSlotPos):
		metinIndex = player.GetItemIndex(metinSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)

		item.SelectItem(metinIndex)
		itemName = item.GetItemName()

		result = player.CanAttachMetin(metinIndex, targetSlotPos)

		if player.ATTACH_METIN_NOT_MATCHABLE_ITEM == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_CAN_NOT_ATTACH(itemName))

		if player.ATTACH_METIN_NO_MATCHABLE_SOCKET == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NO_SOCKET(itemName))

		elif player.ATTACH_METIN_NOT_EXIST_GOLD_SOCKET == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NO_GOLD_SOCKET(itemName))

		elif player.ATTACH_METIN_CANT_ATTACH_TO_EQUIPMENT == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_EQUIP_ITEM)

		if player.ATTACH_METIN_OK != result:
			return

		self.attachMetinDialog.Open(metinSlotPos, targetSlotPos)



	def OverOutItem(self):
		self.wndItem.SetUsableItem(False)
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OverInItem(self, overSlotPos):
		overInvenSlotPos = self.__InventoryLocalSlotPosToGlobalSlotPos(overSlotPos)
		self.wndItem.SetUsableItem(False)

		getItemVNum = player.GetItemIndex
		itemVnum = getItemVNum(overInvenSlotPos)
		if app.WJ_ENABLE_PICKUP_ITEM_EFFECT:
			self.DelHighlightSlot(overInvenSlotPos)

		if mouseModule.mouseController.isAttached():
			attachedItemType = mouseModule.mouseController.GetAttachedType()
			if player.SLOT_TYPE_INVENTORY == attachedItemType:

				attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
				attachedItemVNum = mouseModule.mouseController.GetAttachedItemIndex()

				if self.__CanUseSrcItemToDstItem(attachedItemVNum, attachedSlotPos, overInvenSlotPos):
					self.wndItem.SetUsableItem(True)
					self.ShowToolTip(overInvenSlotPos)
					return

		self.ShowToolTip(overInvenSlotPos)


	def __IsUsableItemToItem(self, srcItemVNum, srcSlotPos):
		"다른 아이템에 사용할 수 있는 아이템인가?"
		if item.IsRefineScroll(srcItemVNum):
			return True
		elif item.IsMetin(srcItemVNum):
			return True
		elif item.IsDetachScroll(srcItemVNum):
			return True
		elif item.IsKey(srcItemVNum):
			return True
		elif app.ELEMENT_SPELL_WORLDARD and item.IsElement(srcItemVNum):
			return True
		elif (player.GetItemFlags(srcSlotPos) & ITEM_FLAG_APPLICABLE) == ITEM_FLAG_APPLICABLE:
			return True
		else:

			if app.BL_TRANSMUTATION_SYSTEM:
				if item.IsChangeLookClearScroll(srcItemVNum):
					return True

			if app.ENABLE_SET_ITEM:
				if item.IsSetItemScroll(srcItemVNum):
					return True

			if app.ENABLE_GEM_CONVERTER:
				if srcItemVNum == item.ITEM_VNUM_GEM_CONVERTER:
					return True

			if item.GetUseType(srcItemVNum) in self.USE_TYPE_TUPLE:
				return True

		return False

	def __CanUseSrcItemToDstItem(self, srcItemVNum, srcSlotPos, dstSlotPos):
		"대상 아이템에 사용할 수 있는가?"

		if srcSlotPos == dstSlotPos and not item.IsMetin(srcItemVNum):
			return False

		if item.IsRefineScroll(srcItemVNum):
			if player.REFINE_OK == player.CanRefine(srcItemVNum, dstSlotPos):
				return True
		elif item.IsMetin(srcItemVNum):
			if player.ATTACH_METIN_OK == player.CanAttachMetin(srcItemVNum, dstSlotPos):
				return True
		elif item.IsDetachScroll(srcItemVNum):
			if player.DETACH_METIN_OK == player.CanDetach(srcItemVNum, dstSlotPos):
				return True
		elif item.IsKey(srcItemVNum):
			if player.CanUnlock(srcItemVNum, dstSlotPos):
				return True

		elif app.ELEMENT_SPELL_WORLDARD and item.IsElement(srcItemVNum):
			if player.ELEMENT_UPGRADE_ADD == player.GetElements(srcItemVNum, dstSlotPos) or\
				player.ELEMENT_DOWNGRADE_ADD == player.GetElements(srcItemVNum, dstSlotPos) or\
				player.ELEMENT_CHANGE_ADD == player.GetElements(srcItemVNum, dstSlotPos):
				return True

		elif (player.GetItemFlags(srcSlotPos) & ITEM_FLAG_APPLICABLE) == ITEM_FLAG_APPLICABLE:
			return True

		else:

			if app.BL_TRANSMUTATION_SYSTEM:
				if player.CanChangeLookClearItem(srcItemVNum, player.INVENTORY, dstSlotPos):
					return True

			#if app.ENABLE_SET_ITEM:
			#	if item.IsSetItemScroll(srcItemVNum):
			#		if player.CanSetItemClearItem(srcItemVNum, dstSlotWindow, dstSlotPos):
			#			return True

			if app.ENABLE_SET_ITEM:
				if item.IsSetItemScroll(srcItemVNum):
					if player.CanSetItemClearItem(srcItemVNum, player.INVENTORY, dstSlotPos):
						return True

			if app.ENABLE_GEM_CONVERTER:
				if srcItemVNum == item.ITEM_VNUM_GEM_CONVERTER:
					if self.__CanUseGemConverter(srcItemVNum, dstSlotWindow, srcSlotPos, dstSlotWindow, dstSlotPos):
						return True

			useType=item.GetUseType(srcItemVNum)

			if "USE_CLEAN_SOCKET" == useType:
				if self.__CanCleanBrokenMetinStone(dstSlotPos):
					return True
			elif "USE_CHANGE_ATTRIBUTE" == useType:
				if self.__CanChangeItemAttrList(dstSlotPos):
					return True
			elif app.BL_67_ATTR and "USE_CHANGE_ATTRIBUTE2" == useType:
				if self.__CanChangeItemAttrList2(dstSlotPos):
					return True
			elif "USE_ADD_ATTRIBUTE" == useType:
				if self.__CanAddItemAttr(dstSlotPos):
					return True
			elif "USE_ADD_ATTRIBUTE2" == useType:
				if self.__CanAddItemAttr(dstSlotPos):
					return True
			elif "USE_ADD_ACCESSORY_SOCKET" == useType:
				if self.__CanAddAccessorySocket(dstSlotPos):
					return True
			elif "USE_PUT_INTO_ACCESSORY_SOCKET" == useType:
				if self.__CanPutAccessorySocket(dstSlotPos, srcItemVNum):
					return True;
			elif "USE_PUT_INTO_BELT_SOCKET" == useType:
				dstItemVNum = player.GetItemIndex(dstSlotPos)
				print "USE_PUT_INTO_BELT_SOCKET", srcItemVNum, dstItemVNum

				item.SelectItem(dstItemVNum)

				if item.ITEM_TYPE_BELT == item.GetItemType():
					return True
			elif app.ENABLE_USE_COSTUME_ATTR and "USE_CHANGE_COSTUME_ATTR" == useType:
				if self.__CanChangeCostumeAttrList(dstSlotPos):
					return True
			elif app.ENABLE_USE_COSTUME_ATTR and "USE_RESET_COSTUME_ATTR" == useType:
				if self.__CanResetCostumeAttr(dstSlotPos):
					return True

			if app.ENABLE_AURA_SYSTEM:
				if "USE_PUT_INTO_AURA_SOCKET" == useType:
					dstItemVnum = player.GetItemIndex(dstSlotPos)
					item.SelectItem(dstItemVnum)
					if item.ITEM_TYPE_COSTUME == item.GetItemType() and item.COSTUME_TYPE_AURA == item.GetItemSubType():
						if player.GetItemMetinSocket(dstSlotPos, player.ITEM_SOCKET_AURA_BOOST) == 0:
							return True

		return False

	def __CanCleanBrokenMetinStone(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(dstItemVNum)

		if item.ITEM_TYPE_WEAPON != item.GetItemType():
			return False

		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			if player.GetItemMetinSocket(dstSlotPos, i) == constInfo.ERROR_METIN_STONE:
				return True

		return False

	def __CanChangeItemAttrList(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(dstItemVNum)

		if not item.GetItemType() in (item.ITEM_TYPE_WEAPON, item.ITEM_TYPE_ARMOR):
			return False

		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			if player.GetItemAttribute(dstSlotPos, i)[0] != 0:
				return True

		return False

	if app.BL_67_ATTR:
		def __CanChangeItemAttrList2(self, dstSlotPos):
			return uiAttr67Add.Attr67AddWindow.CantAttachToAttrSlot(dstSlotPos, False)

	if app.ENABLE_USE_COSTUME_ATTR:
		def __CanChangeCostumeAttrList(self, dstSlotPos):
			dstItemVNum = player.GetItemIndex(dstSlotPos)
			if dstItemVNum == 0:
				return False

			item.SelectItem(dstItemVNum)

			if item.GetItemType() != item.ITEM_TYPE_COSTUME:
				return False

			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				if player.GetItemAttribute(dstSlotPos, i)[0] != 0:
					return True

			return False

		def __CanResetCostumeAttr(self, dstSlotPos):
			dstItemVNum = player.GetItemIndex(dstSlotPos)
			if dstItemVNum == 0:
				return False

			item.SelectItem(dstItemVNum)

			if item.GetItemType() != item.ITEM_TYPE_COSTUME:
				return False

			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				if player.GetItemAttribute(dstSlotPos, i)[0] != 0:
					return True

			return False

	def __CanPutAccessorySocket(self, dstSlotPos, mtrlVnum):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(dstItemVNum)

		if item.GetItemType() != item.ITEM_TYPE_ARMOR:
			return False

		if not item.GetItemSubType() in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):
			return False

		curCount = player.GetItemMetinSocket(dstSlotPos, 0)
		maxCount = player.GetItemMetinSocket(dstSlotPos, 1)

		if mtrlVnum != constInfo.GET_ACCESSORY_MATERIAL_VNUM(dstItemVNum, item.GetItemSubType()):
			return False

		if curCount>=maxCount:
			return False

		return True

	def __CanAddAccessorySocket(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(dstItemVNum)

		if item.GetItemType() != item.ITEM_TYPE_ARMOR:
			return False

		if not item.GetItemSubType() in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):
			return False

		curCount = player.GetItemMetinSocket(dstSlotPos, 0)
		maxCount = player.GetItemMetinSocket(dstSlotPos, 1)

		ACCESSORY_SOCKET_MAX_SIZE = 3
		if maxCount >= ACCESSORY_SOCKET_MAX_SIZE:
			return False

		return True

	def __CanAddItemAttr(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(dstItemVNum)

		if not item.GetItemType() in (item.ITEM_TYPE_WEAPON, item.ITEM_TYPE_ARMOR):
			return False

		attrCount = 0
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			if player.GetItemAttribute(dstSlotPos, i)[0] != 0:
				attrCount += 1

		if attrCount<4:
			return True

		return False

	def ShowToolTip(self, slotIndex):
		if None != self.tooltipItem:
			self.tooltipItem.SetInventoryItem(slotIndex)

	def OnTop(self):
		if None != self.tooltipItem:
			self.tooltipItem.SetTop()

		map(lambda wnd:wnd.RefreshLockedSlot(), self.bindWnds)
		self.RefreshMarkSlots()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def UseItemSlot(self, slotIndex):
		curCursorNum = app.GetCursor()
		if app.SELL == curCursorNum:
			return

		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS():
			return

		slotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(slotIndex)

		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			if self.wndDragonSoulRefine.IsShow():
				self.wndDragonSoulRefine.AutoSetItem((player.INVENTORY, slotIndex), 1)
				return
		if app.ENABLE_ACCE_SYSTEM:
			if self.isShowAcceWindow():
				acce.Add(player.INVENTORY, slotIndex, 255)
				return

		if app.ENABLE__SELL_ITEM:
			if app.IsPressed(app.DIK_LCONTROL) and app.IsPressed(app.DIK_X) and self.IsSellItems(slotIndex):
				self.__SendSellItemPacket(slotIndex)
				if uiPrivateShopBuilder.IsBuildingPrivateShop():
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
					return
	
				net.SendItemSellPacket(slotIndex, 0)
				snd.PlaySound("sound/ui/money.wav")
				return

		self.__UseItem(slotIndex)
		mouseModule.mouseController.DeattachObject()
		self.OverOutItem()

	def __UseItem(self, slotIndex):
		if app.ENABLE_AURA_SYSTEM:
			if player.IsAuraRefineWindowOpen():
				self.__UseItemAura(slotIndex)
				return

		ItemVNum = player.GetItemIndex(slotIndex)
		item.SelectItem(ItemVNum)

		if app.BL_TRANSMUTATION_SYSTEM:
			if player.GetChangeLookWindowOpen() == 1:
				return

		if app.WJ_ENABLE_TRADABLE_ICON:
			if self.interface.AttachInvenItemToOtherWindowSlot(slotIndex):
				return

		if app.__BL_CHEST_DROP_INFO__:
			if app.IsPressed(app.DIK_LCONTROL):
				if item.HasDropInfo(ItemVNum) and self.interface:
					self.interface.OpenChestDropWindow(ItemVNum)
				return

		if item.IsFlag(item.ITEM_FLAG_CONFIRM_WHEN_USE):
			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText(localeInfo.INVENTORY_REALLY_USE_ITEM)
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnAccept))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnCancel))
			self.questionDialog.Open()
			self.questionDialog.slotIndex = slotIndex

			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

		else:

			if app.ENABLE_FLOWER_EVENT:
				if 25121 == ItemVNum or 25122 == ItemVNum or 25123 == ItemVNum or 25124 == ItemVNum or 25125 == ItemVNum:
					value1 = item.GetValue(0) # dwType
					value2 = item.GetValue(1) # wApplyOn
					value3 = item.GetApplyPoint(value2)

					if player.CheckAffect(value1, value3):
						self.__SendUseItemPacket(slotIndex)
						return
					else:
						if player.CheckAffect(value1,0):
							self.questionDialog = uiCommon.QuestionDialog2()
							self.questionDialog.SetText1(localeInfo.FLOWER_EVENT_USE_ITEM_TEXT1)
							self.questionDialog.SetText2(localeInfo.FLOWER_EVENT_USE_ITEM_TEXT2)
							self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnAccept))
							self.questionDialog.SetCancelEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnCancel))
							self.questionDialog.Open()
							self.questionDialog.slotIndex = slotIndex
							constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)						
							return

			self.__SendUseItemPacket(slotIndex)
			#net.SendItemUsePacket(slotIndex)

	if app.ENABLE_GEM_CONVERTER:
		def __CanUseGemConverter(self, src_item_vnum, src_item_window, src_item_pos, dst_item_window, dst_item_pos):
			if src_item_window == dst_item_window and src_item_pos == dst_item_pos:
				return False

			if src_item_vnum != item.ITEM_VNUM_GEM_CONVERTER:
				return False

			item.SelectItem(src_item_vnum)

			gem_conv_count = player.GetItemCount(src_item_window, src_item_pos)
			gem_stone_vnum = player.GetItemIndex(dst_item_window, dst_item_pos)
			gem_stone_count = player.GetItemCount(dst_item_window, dst_item_pos)

			need_gem_stone_count = gem_conv_count * item.GetValue(0)

			if gem_stone_vnum != item.ITEM_VNUM_GEM_STONE:
				return False

			if gem_stone_count < need_gem_stone_count:
				return False

			return True

		def __UseGemConverter(self, src_item_window, src_item_pos, dst_item_window, dst_item_pos):
			if self.gem_converter_question_dialog:
				return

			self.gem_converter_item_pos = (src_item_pos, dst_item_pos)

			self.SetCantMouseEventSlot(src_item_pos)
			self.SetCantMouseEventSlot(dst_item_pos)

			question_dialog = uiCommon.QuestionDialog()
			question_dialog.SetText(localeInfo.GEM_CONVERTER_MESSAGE_USE_CONVERTER_QUESTION)
			question_dialog.SetAcceptEvent(ui.__mem_func__(self.__AcceptGemConverterUse))
			question_dialog.SetCancelEvent(ui.__mem_func__(self.__CancelGemConverterUse))
			question_dialog.Open()
			question_dialog.srcItemWindow = src_item_window
			question_dialog.srcItemPos = src_item_pos
			question_dialog.dstItemWindow = dst_item_window
			question_dialog.dstItemPos = dst_item_pos
			self.gem_converter_question_dialog = question_dialog
			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

		def __AcceptGemConverterUse(self):
			if not self.gem_converter_question_dialog:
				return

			gem_conv_vnum = player.GetItemIndex(self.gem_converter_question_dialog.srcItemWindow, self.gem_converter_question_dialog.srcItemPos)
			gem_conv_count = player.GetItemCount(self.gem_converter_question_dialog.srcItemWindow, self.gem_converter_question_dialog.srcItemPos)
			gem_stone_count = player.GetItemCount(self.gem_converter_question_dialog.dstItemWindow, self.gem_converter_question_dialog.dstItemPos)

			item.SelectItem(gem_conv_vnum)
			need_gem_stone_count = gem_conv_count * item.GetValue(0)
			conv_to_gem = need_gem_stone_count / item.GetValue(0)
			conv_cost = gem_conv_count * item.GetValue(1)

			if gem_stone_count < need_gem_stone_count:
				self.__CancelGemConverterUse()
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GEM_CONVERTER_MESSAGE_NOT_ENOUGH_GEMSTONE % localeInfo.NumberToMoneyString(need_gem_stone_count))
				return

			if player.GetElk() < conv_cost:
				self.__CancelGemConverterUse()
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GEM_CONVERTER_MESSAGE_NOT_ENOUGH_GOLD)
				return

			if player.GetGem() + conv_to_gem >= player.GEM_MAX:
				self.__CancelGemConverterUse()
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GEM_CONVERTER_MESSAGE_GEM_MAX)
				return

			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GEM_CONVERTER_MESSAGE_CONVERT_SUCCESS_GEM_STONE % gem_conv_count)
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GEM_CONVERTER_MESSAGE_CONVERT_SUCCESS_CONVERTER % need_gem_stone_count)

			self.__SendUseItemToItemPacket(\
				self.gem_converter_question_dialog.srcItemWindow,\
				self.gem_converter_question_dialog.srcItemPos,\
				self.gem_converter_question_dialog.dstItemWindow,\
				self.gem_converter_question_dialog.dstItemPos)

			self.__CancelGemConverterUse()

		def __CancelGemConverterUse(self):
			for i in self.gem_converter_item_pos:
				self.SetCanMouseEventSlot(i)
			self.gem_converter_item_pos = [-1, -1]

			self.__CloseGemConverterUseQuestionDialog()

		def __CloseGemConverterUseQuestionDialog(self):
			if self.gem_converter_question_dialog:
				self.gem_converter_question_dialog.Close()
			self.gem_converter_question_dialog = None
			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

	def __UseItemQuestionDialog_OnCancel(self):
		self.OnCloseQuestionDialog()

	def __UseItemQuestionDialog_OnAccept(self):
		self.__SendUseItemPacket(self.questionDialog.slotIndex)
		self.OnCloseQuestionDialog()

	def __SendUseItemToItemPacket(self, srcSlotPos, dstSlotPos):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		net.SendItemUseToItemPacket(srcSlotPos, dstSlotPos)

	def __SendUseItemPacket(self, slotPos):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		net.SendItemUsePacket(slotPos)

	def __SendMoveItemPacket(self, srcSlotPos, dstSlotPos, srcItemCount):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
			return
	
		# Verificar si el slot de origen pertenece al inventario especial
		isSpecialInventory = (
			app.ENABLE_SPECIAL_INVENTORY_SYSTEM and
			(
				player.IsSkillBookInventorySlot(srcSlotPos) or
				player.IsUpgradeItemsInventorySlot(srcSlotPos) or
				player.IsStoneInventorySlot(srcSlotPos) or
				player.IsGiftBoxInventorySlot(srcSlotPos)
			)
		)
	
		# Permitir mover items desde el inventario especial o normal
		net.SendItemMovePacket(player.INVENTORY, srcSlotPos, player.INVENTORY, dstSlotPos, srcItemCount)

	def RefreshHighlights(self):
		self.__HighlightSlot_Refresh()

	def HighlightSlot_Clear(self):
		self.__HighlightSlot_Clear()

	def __HighlightSlot_Refresh(self):
		for i in xrange(self.wndItem.GetSlotCount()):
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)
	
			if app.ENABLE_ACCE_SYSTEM and slotNumber in self.listHighlightedAcceSlot:
				self.wndItem.ActivateSlot(i)
				self.wndItem.SetSlotDiffuseColor(i, wndMgr.COLOR_TYPE_GREEN)
				self.wndItem.SetCantMouseEventSlot(i)
	
			if app.BL_TRANSMUTATION_SYSTEM and slotNumber in self.listHighlightedChangeLookSlot:
				self.wndItem.ActivateSlot(i)
				self.wndItem.SetSlotDiffuseColor(i, wndMgr.COLOR_TYPE_RED)
				self.wndItem.SetCantMouseEventSlot(i)
	
			if app.ENABLE_AURA_SYSTEM and slotNumber in self.listHighlightedAuraSlot:
				self.wndItem.ActivateSlot(i)
				self.wndItem.SetSlotDiffuseColor(i, wndMgr.COLOR_TYPE_GREEN)
	
			if app.ENABLE_CUBE_RENEWAL and (slotNumber, self.inventoryPageIndex) in self.listHighlightedCubeSlot:
				if not player.GetItemSetValue(player.INVENTORY, slotNumber):
					self.wndItem.ActivateSlot(i)
					self.wndItem.SetSlotDiffuseColor(i, wndMgr.COLOR_TYPE_RED)
				else:
					self.wndItem.DeactivateSlot(i)
					if (slotNumber, self.inventoryPageIndex) in self.listHighlightedCubeSlot:
						self.listHighlightedCubeSlot.remove((slotNumber, self.inventoryPageIndex))
	
			if app.WJ_ENABLE_PICKUP_ITEM_EFFECT and slotNumber in self.listHighlightedSlot:
				self.wndItem.ActivateSlot(i)


		### Early Improvement Highlights
		"""
		if app.WJ_ENABLE_PICKUP_ITEM_EFFECT:
			for i in xrange(self.wndItem.GetSlotCount()):
				slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)
				if slotNumber in self.listHighlightedSlot:
					self.wndItem.ActivateSlot(i)
		"""

	def __HighlightSlot_Clear(self):
		for i in xrange(self.wndItem.GetSlotCount()):
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)
	
			if app.ENABLE_ACCE_SYSTEM and slotNumber in self.listHighlightedAcceSlot:
				self.wndItem.DeactivateSlot(i)
				self.wndItem.SetCanMouseEventSlot(i)
				self.listHighlightedAcceSlot.remove(slotNumber)
	
			if app.BL_TRANSMUTATION_SYSTEM and slotNumber in self.listHighlightedChangeLookSlot:
				self.wndItem.DeactivateSlot(i)
				self.wndItem.SetCanMouseEventSlot(i)
				self.listHighlightedChangeLookSlot.remove(slotNumber)
	
			if app.ENABLE_AURA_SYSTEM and slotNumber in self.listHighlightedAuraSlot:
				self.wndItem.DeactivateSlot(i)
				self.listHighlightedAuraSlot.remove(slotNumber)
	
			if app.ENABLE_CUBE_RENEWAL and (slotNumber, self.inventoryPageIndex) in self.listHighlightedCubeSlot:
				self.wndItem.DeactivateSlot(i)
				self.wndItem.SetCanMouseEventSlot(i)
				self.listHighlightedCubeSlot.remove((slotNumber, self.inventoryPageIndex))
	
			if app.WJ_ENABLE_PICKUP_ITEM_EFFECT and slotNumber in self.listHighlightedSlot:
				self.wndItem.DeactivateSlot(i)
				self.listHighlightedSlot.remove(slotNumber)
	
		# Limpia completamente la lista despues de haber desactivado los slots
		if app.ENABLE_CUBE_RENEWAL:
			self.listHighlightedCubeSlot = []

		### Early Improvement Highlights
		"""
		if app.WJ_ENABLE_PICKUP_ITEM_EFFECT:
			for i in xrange(self.wndItem.GetSlotCount()):
				slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)
				if slotNumber in self.listHighlightedSlot:
					self.wndItem.DeactivateSlot(i)
					self.listHighlightedSlot.remove(slotNumber)
		"""

		if app.ENABLE_CUBE_RENEWAL:
			self.listHighlightedCubeSlot = []

	if app.ENABLE__SELL_ITEM:
		def IsSellItems(self, slotIndex):
			itemVnum = player.GetItemIndex(slotIndex)
			item.SelectItem(itemVnum)
			itemPrice = item.GetISellItemPrice()
			
			# if item.GetItemType() == item.ITEM_TYPE_WEAPON or item.GetItemType() == item.ITEM_TYPE_ARMOR:
				# return True
				
			if itemPrice > 1:
				return True
				
			return False
			
		def __SendSellItemPacket(self, itemVNum):
			if uiPrivateShopBuilder.IsBuildingPrivateShop():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
				return
				
			net.SendItemSellPacket(itemVNum)

	def SetDragonSoulRefineWindow(self, wndDragonSoulRefine):
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoulRefine = wndDragonSoulRefine

	if app.BL_TRANSMUTATION_SYSTEM:
		def __AddHighlightSlotChangeLook(self, slotIndex):
			if not slotIndex in self.listHighlightedChangeLookSlot:
				self.listHighlightedChangeLookSlot.append(slotIndex)

		def __DelHighlightSlotChangeLook(self, slotIndex):
			if slotIndex in self.listHighlightedChangeLookSlot:
				if slotIndex >= player.INVENTORY_PAGE_SIZE:
					self.wndItem.DeactivateSlot(slotIndex - (self.inventoryPageIndex * player.INVENTORY_PAGE_SIZE))
					self.wndItem.SetCanMouseEventSlot(slotIndex - (self.inventoryPageIndex * player.INVENTORY_PAGE_SIZE))
				else:
					self.wndItem.DeactivateSlot(slotIndex)
					self.wndItem.SetCanMouseEventSlot(slotIndex)
				self.listHighlightedChangeLookSlot.remove(slotIndex)

	if app.ENABLE_CUBE_RENEWAL:
		def __AddHighlightSlotCube(self, slotIndex):
			# Agrega el slot solo si no esta en la lista, tomando solo los valores relevantes
			if (slotIndex[0], slotIndex[1]) not in self.listHighlightedCubeSlot:
				self.listHighlightedCubeSlot.append((slotIndex[0], slotIndex[1]))
	
		def __DelHighlightSlotCube(self, slotIndex):
			# Confirma que el slot este en la lista y procede con la desactivacion
			if (slotIndex[0], slotIndex[1]) in self.listHighlightedCubeSlot:
				actualSlot = slotIndex[0] - (self.inventoryPageIndex * player.INVENTORY_PAGE_SIZE)
				
				# Desactiva el slot en funcion del indice calculado
				self.wndItem.DeactivateSlot(actualSlot)
				self.wndItem.SetCanMouseEventSlot(actualSlot)
	
				# Elimina el slot de la lista usando solo los valores relevantes
				self.listHighlightedCubeSlot.remove((slotIndex[0], slotIndex[1]))

	if app.ENABLE_AURA_SYSTEM:
		def __AddHighlightSlotAura(self, slotIndex):
			if not slotIndex in self.listHighlightedAuraSlot:
				self.listHighlightedAuraSlot.append(slotIndex)

		def __DelHighlightSlotAura(self, slotIndex):
			if slotIndex in self.listHighlightedAuraSlot:

				if slotIndex >= player.INVENTORY_PAGE_SIZE:
					self.wndItem.DeactivateSlot(slotIndex - (self.inventoryPageIndex * player.INVENTORY_PAGE_SIZE) )
					self.wndItem.SetCanMouseEventSlot(slotIndex - (self.inventoryPageIndex * player.INVENTORY_PAGE_SIZE))
				else:
					self.wndItem.DeactivateSlot(slotIndex)
					self.wndItem.SetCanMouseEventSlot(slotIndex)

				self.listHighlightedAuraSlot.remove(slotIndex)

	if app.ENABLE_ACCE_SYSTEM:
		def __AddHighlightSlotAcce(self, slotIndex):
			if not slotIndex in self.listHighlightedAcceSlot:
				self.listHighlightedAcceSlot.append(slotIndex)

		def __DelHighlightSlotAcce(self, slotIndex):
			if slotIndex in self.listHighlightedAcceSlot:
				if slotIndex >= player.INVENTORY_PAGE_SIZE:
					self.wndItem.DeactivateSlot(slotIndex - (self.inventoryPageIndex * player.INVENTORY_PAGE_SIZE))
					self.wndItem.SetCanMouseEventSlot(slotIndex - (self.inventoryPageIndex * player.INVENTORY_PAGE_SIZE))
				else:
					self.wndItem.DeactivateSlot(slotIndex)
					self.wndItem.SetCanMouseEventSlot(slotIndex)

				self.listHighlightedAcceSlot.remove(slotIndex)

	if app.ENABLE_ACCE_SYSTEM:
		def SetAcceWindow(self, wndAcceCombine, wndAcceAbsorption):
			self.wndAcceCombine = wndAcceCombine
			self.wndAcceAbsorption = wndAcceAbsorption

		def isShowAcceWindow(self):
			if self.wndAcceCombine:
				if self.wndAcceCombine.IsShow():
					return 1

			if self.wndAcceAbsorption:
				if self.wndAcceAbsorption.IsShow():
					return 1

			return 0

	if app.ENABLE_HIDE_COSTUME_SYSTEM:
		def RefreshVisibleCostume(self):
			if self.wndCostume:
				self.wndCostume.RefreshVisibleCostume()
			else:
				self.wndCostume = CostumeWindow(self)
				self.wndCostume.RefreshVisibleCostume()

	if app.ENABLE_CHEQUE_SYSTEM:
		def OverInToolTip(self, arg):
			arglen = len(str(arg))
			pos_x, pos_y = wndMgr.GetMousePosition()
			
			self.toolTip.ClearToolTip()
			self.toolTip.SetThinBoardSize(11 * arglen)
			self.toolTip.SetToolTipPosition(pos_x + 5, pos_y - 5)
			self.toolTip.AppendTextLine(arg, 0xffffff00)
			self.toolTip.Show()

		def OverOutToolTip(self):
			self.toolTip.Hide()

		def EventProgress(self, event_type, idx):
			if "mouse_over_in" == str(event_type):
				if idx == 0:
					self.OverInToolTip(localeInfo.CHEQUE_SYSTEM_UNIT_YANG)
				elif idx == 1:
					self.OverInToolTip(localeInfo.CHEQUE_SYSTEM_UNIT_WON)
				elif app.ENABLE_GEM_SYSTEM and idx == 2:
					self.OverInToolTip(localeInfo.GEM_SYSTEM_NAME)
				else:
					return
			elif "mouse_over_out" == str(event_type):
				self.OverOutToolTip()
			else:
				return

	def OnMoveWindow(self, x, y):
#		print "Inventory Global Pos : ", self.GetGlobalPosition()
		if self.wndBelt:
#			print "Belt Global Pos : ", self.wndBelt.GetGlobalPosition()
			self.wndBelt.AdjustPositionAndSize()

		if app.__RENEWAL_BRAVE_CAPE__:
			if self.wndBraveCape:
				self.wndBraveCape.AdjustPosition(x, y)

	def DeactivateSlot(self, slotindex, type):
		if type == wndMgr.HILIGHTSLOT_MAX:
			return

		if app.ENABLE_ACCE_SYSTEM:
			if type == wndMgr.HILIGHTSLOT_ACCE:
				self.__DelHighlightSlotAcce(slotindex)
		#
		if app.BL_TRANSMUTATION_SYSTEM:
			if type == wndMgr.HILIGHTSLOT_CHANGE_LOOK:
				self.__DelHighlightSlotChangeLook(slotindex)
		#
		if app.ENABLE_AURA_SYSTEM:
			if type == wndMgr.HILIGHTSLOT_AURA:
				self.__DelHighlightSlotAura(slotindex)

		if app.ENABLE_CUBE_RENEWAL:
			if type == wndMgr.HILIGHTSLOT_CUBE:
				self.__DelHighlightSlotCube(slotindex)

	def ActivateSlot(self, slotindex, type):
		if type == wndMgr.HILIGHTSLOT_MAX:
			return

		if app.ENABLE_ACCE_SYSTEM:
			if type == wndMgr.HILIGHTSLOT_ACCE:
				self.__AddHighlightSlotAcce(slotindex)
		#
		if app.BL_TRANSMUTATION_SYSTEM:
			if type == wndMgr.HILIGHTSLOT_CHANGE_LOOK:
				self.__AddHighlightSlotChangeLook(slotindex)
		#
		if app.ENABLE_AURA_SYSTEM:
			if type == wndMgr.HILIGHTSLOT_AURA:
				self.__AddHighlightSlotAura(slotindex)

		if app.ENABLE_CUBE_RENEWAL:
			if type == wndMgr.HILIGHTSLOT_CUBE:
				self.__AddHighlightSlotCube(slotindex)


	if app.ENABLE_AURA_SYSTEM:
		def __UseItemAuraQuestionDialog_OnAccept(self):
			self.questionDialog.Close()
			net.SendAuraRefineCheckIn(*(self.questionDialog.srcItem + self.questionDialog.dstItem + (player.GetAuraRefineWindowType(),)))
			self.questionDialog.srcItem = (0, 0)
			self.questionDialog.dstItem = (0, 0)

		def __UseItemAuraQuestionDialog_Close(self):
			self.questionDialog.Close()

			self.questionDialog.srcItem = (0, 0)
			self.questionDialog.dstItem = (0, 0)

		def __UseItemAura(self, slotIndex):
			AuraSlot = player.FineMoveAuraItemSlot()
			UsingAuraSlot = player.FindActivatedAuraSlot(player.INVENTORY, slotIndex)
			AuraVnum = player.GetItemIndex(slotIndex)
			item.SelectItem(AuraVnum)
			if player.GetAuraCurrentItemSlotCount() >= player.AURA_SLOT_MAX <= UsingAuraSlot:
				return

			if player.IsEquipmentSlot(slotIndex):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_IMPOSSIBLE_EQUIPITEM)
				return

			if player.GetAuraRefineWindowType() == player.AURA_WINDOW_TYPE_ABSORB:
				isAbsorbItem = False
				if item.GetItemType() == item.ITEM_TYPE_COSTUME:
					if item.GetItemSubType() == item.COSTUME_TYPE_AURA:
						if player.GetItemMetinSocket(slotIndex, player.ITEM_SOCKET_AURA_DRAIN_ITEM_VNUM) == 0:
							if UsingAuraSlot == player.AURA_SLOT_MAX:
								if AuraSlot != player.AURA_SLOT_MAIN:
									return

								net.SendAuraRefineCheckIn(player.INVENTORY, slotIndex, player.AURA_REFINE, AuraSlot, player.GetAuraRefineWindowType())

						else:
							chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_IMPOSSIBLE_ABSORBITEM)
							return

					else:
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_IMPOSSIBLE_ABSORBITEM)
						return

				elif item.GetItemType() == item.ITEM_TYPE_ARMOR:
					if item.GetItemSubType() in [item.ARMOR_SHIELD, item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR]:
						if player.FindUsingAuraSlot(player.AURA_SLOT_MAIN) == player.NPOS():
							chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_POSSIBLE_REGISTER_AURAITEM)
							return

						isAbsorbItem = True
					else:
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_IMPOSSIBLE_ABSORBITEM)
						return

				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_IMPOSSIBLE_ABSORBITEM)
					return

				if isAbsorbItem:
					if UsingAuraSlot == player.AURA_SLOT_MAX:
						if AuraSlot != player.AURA_SLOT_SUB:
							if player.FindUsingAuraSlot(player.AURA_SLOT_SUB) == player.NPOS():
								AuraSlot = player.AURA_SLOT_SUB
							else:
								return

						self.questionDialog = uiCommon.QuestionDialog()
						self.questionDialog.SetText(localeInfo.AURA_NOTICE_DEL_ABSORDITEM)
						self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.__UseItemAuraQuestionDialog_OnAccept))
						self.questionDialog.SetCancelEvent(ui.__mem_func__(self.__UseItemAuraQuestionDialog_Close))
						self.questionDialog.srcItem = (player.INVENTORY, slotIndex)
						self.questionDialog.dstItem = (player.AURA_REFINE, AuraSlot)
						self.questionDialog.Open()

			elif player.GetAuraRefineWindowType() == player.AURA_WINDOW_TYPE_GROWTH:
				if UsingAuraSlot == player.AURA_SLOT_MAX:
					if AuraSlot == player.AURA_SLOT_MAIN:
						if item.GetItemType() == item.ITEM_TYPE_COSTUME:
							if item.GetItemSubType() == item.COSTUME_TYPE_AURA:
								socketLevelValue = player.GetItemMetinSocket(slotIndex, player.ITEM_SOCKET_AURA_CURRENT_LEVEL)
								curLevel = (socketLevelValue / 100000) - 1000
								curExp = socketLevelValue % 100000;
								if curLevel >= player.AURA_MAX_LEVEL:
									chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_MAX_LEVEL)
									return

								if curExp >= player.GetAuraRefineInfo(curLevel, player.AURA_REFINE_INFO_NEED_EXP):
									chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_IMPOSSIBLE_GROWTHITEM)
									return

								net.SendAuraRefineCheckIn(player.INVENTORY, slotIndex, player.AURA_REFINE, AuraSlot, player.GetAuraRefineWindowType())

							else:
								chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_POSSIBLE_AURAITEM)
								return

						else:
							chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_POSSIBLE_AURAITEM)
							return

					elif AuraSlot == player.AURA_SLOT_SUB:
						if player.FindUsingAuraSlot(player.AURA_SLOT_MAIN) != player.NPOS():
							if item.GetItemType() == item.ITEM_TYPE_RESOURCE:
								if item.GetItemSubType() == item.RESOURCE_AURA:
									if UsingAuraSlot == player.AURA_SLOT_MAX:
										if AuraSlot != player.AURA_SLOT_SUB:
											return

										net.SendAuraRefineCheckIn(player.INVENTORY, slotIndex, player.AURA_REFINE, AuraSlot, player.GetAuraRefineWindowType())
								else:
									chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_POSSIBLE_AURARESOURCE)
									return

							else:
								chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_POSSIBLE_AURARESOURCE)
								return

						else:
							chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_POSSIBLE_REGISTER_AURAITEM)
							return

			elif player.GetAuraRefineWindowType() == player.AURA_WINDOW_TYPE_EVOLVE:
				if UsingAuraSlot == player.AURA_SLOT_MAX:
					if AuraSlot == player.AURA_SLOT_MAIN:
						if item.GetItemType() == item.ITEM_TYPE_COSTUME:
							if item.GetItemSubType() == item.COSTUME_TYPE_AURA:
								socketLevelValue = player.GetItemMetinSocket(slotIndex, player.ITEM_SOCKET_AURA_CURRENT_LEVEL)
								curLevel = (socketLevelValue / 100000) - 1000
								curExp = socketLevelValue % 100000;
								if curLevel >= player.AURA_MAX_LEVEL:
									chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_MAX_LEVEL)
									return

								if curLevel != player.GetAuraRefineInfo(curLevel, player.AURA_REFINE_INFO_LEVEL_MAX) or curExp < player.GetAuraRefineInfo(curLevel, player.AURA_REFINE_INFO_NEED_EXP):
									chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_IMPOSSIBLE_EVOLUTION_ITEM)
									return

								if player.FindUsingAuraSlot(AuraSlot) != player.NPOS():
									return

								net.SendAuraRefineCheckIn(player.INVENTORY, slotIndex, player.AURA_REFINE, AuraSlot, player.GetAuraRefineWindowType())

							else:
								chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_POSSIBLE_AURAITEM)
								return

						else:
							chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_POSSIBLE_AURAITEM)
							return

					elif AuraSlot == player.AURA_SLOT_SUB:
						Cell = player.FindUsingAuraSlot(player.AURA_SLOT_MAIN)
						if Cell == player.NPOS():
							chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_POSSIBLE_REGISTER_AURAITEM)
							return

						socketLevelValue = player.GetItemMetinSocket(*(Cell + (player.ITEM_SOCKET_AURA_CURRENT_LEVEL,)))
						curLevel = (socketLevelValue / 100000) - 1000
						curExp = socketLevelValue % 100000;
						if curLevel >= player.AURA_MAX_LEVEL:
							chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_MAX_LEVEL)
							return

						if curExp < player.GetAuraRefineInfo(curLevel, player.AURA_REFINE_INFO_NEED_EXP):
							chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_IMPOSSIBLE_EVOLUTION_ITEM)
							return

						if AuraVnum != player.GetAuraRefineInfo(curLevel, player.AURA_REFINE_INFO_MATERIAL_VNUM):
							chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_IMPOSSIBLE_EVOLUTION_ITEM)
							return

						if player.GetItemCount(slotIndex) < player.GetAuraRefineInfo(curLevel, player.AURA_REFINE_INFO_MATERIAL_COUNT):
							chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.AURA_IMPOSSIBLE_EVOLUTION_ITEMCOUNT)
							return

						if UsingAuraSlot == player.AURA_SLOT_MAX:
							if AuraSlot != player.AURA_SLOT_MAX:
								if player.FindUsingAuraSlot(AuraSlot) != player.NPOS():
									return

							net.SendAuraRefineCheckIn(player.INVENTORY, slotIndex, player.AURA_REFINE, AuraSlot, player.GetAuraRefineWindowType())

