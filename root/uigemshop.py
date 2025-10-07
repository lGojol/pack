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
import uiAttachMetin
import uiPickMoney
import uiCommon
import uiPrivateShopBuilder # ���λ��� ������ ItemMove ����
import localeInfo
import constInfo
import ime
import wndMgr
import uiToolTip

class GemShopWindow(ui.ScriptWindow):
	GEM_SHOP_SLOT_MAX = 9
	GEM_SHOP_REFRESH_ITEM_VNUM = 39063
	GEM_SHOP_WINDOW_LIMIT_RANGE = 500
	GEM_SHOP_ADD_ITEM_VNUM = 39064

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.tooltipitem = None
		self.wndSellItemSlot = None
		self.pop = None
		self.RefreshTimeValue = None
		self.itempricelist = []
		self.itemslottovnum = []
		self.itemslottoprice = []
		self.xGemWindowStart = 0
		self.yGemWindowStart = 0
		self.gemshoprefreshtime = 0
		self.IsOpen = False

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		self.tooltipitem = None
		self.isOpen = False
		self.wndSellItemSlot = None
		self.pop = None
		self.RefreshTimeValue = None
		self.itempricelist = []
		self.itemslottovnum = []
		self.itemslottoprice = []
		self.xGemWindowStart = 0
		self.yGemWindowStart = 0
		self.gemshoprefreshtime = 0
		self.IsOpen = False

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/GemShopWindow.py")
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))

			## SlostSetting
			self.wndSellItemSlot = self.GetChild("SellItemSlot")
			self.wndSellItemSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			self.wndSellItemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			self.wndSellItemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
			self.wndSellItemSlot.Show()

			## ItemPrice
			self.itempricelist.append(self.GetChild("slot_1_price"))
			self.itempricelist.append(self.GetChild("slot_2_price"))
			self.itempricelist.append(self.GetChild("slot_3_price"))
			self.itempricelist.append(self.GetChild("slot_4_price"))
			self.itempricelist.append(self.GetChild("slot_5_price"))
			self.itempricelist.append(self.GetChild("slot_6_price"))
			self.itempricelist.append(self.GetChild("slot_7_price"))
			self.itempricelist.append(self.GetChild("slot_8_price"))
			self.itempricelist.append(self.GetChild("slot_9_price"))

			## RefreshButton
			self.GetChild("RefreshButton").SetEvent(ui.__mem_func__(self.RefreshItemSlot))

			## RefreshTimeValue
			self.RefreshTimeValue = self.GetChild("BuyRefreshTime")

			if localeInfo.IsARABIC():
				self.GetChild("gemshopbackimg").LeftRightReverse()
				x0, y0 = self.itempricelist[0].GetLocalPosition()
				x2, y2 = self.itempricelist[2].GetLocalPosition()
				self.itempricelist[0].SetPosition(x2, y0)
				self.itempricelist[2].SetPosition(x0, y2)

				x3, y3 = self.itempricelist[3].GetLocalPosition()
				x5, y5 = self.itempricelist[5].GetLocalPosition()
				self.itempricelist[3].SetPosition(x5, y3)
				self.itempricelist[5].SetPosition(x3, y5)

				x6, y6 = self.itempricelist[6].GetLocalPosition()
				x8, y8 = self.itempricelist[8].GetLocalPosition()
				self.itempricelist[6].SetPosition(x8, y6)
				self.itempricelist[8].SetPosition(x6, y8)

		except:
			import exception
			exception.Abort("GemShopWindow.__LoadWindow.UIScript/GemShopWindow.py")

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		ui.ScriptWindow.Show(self)
		(self.xGemWindowStart, self.yGemWindowStart, z) = player.GetMainCharacterPosition()
		self.IsOpen = True
		player.SetGemShopWindowOpen(True)

	def Close(self):
		self.Hide()
		net.SendGemShopClose()
		self.IsOpen = False
		if self.pop:
			self.pop.Close()
			self.pop = None
		player.SetGemShopWindowOpen(False)

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Destroy(self):
		if self.pop:
			self.pop.Close()
			self.pop = None

	## �� ������ ����.
	def RefreshGemShopWindow(self):
		setGemShopItem = self.wndSellItemSlot.SetItemSlot
		getGemShopItem = player.GetGemShopItemID
		self.itemslottovnum = []
		self.itemslottoprice = []

		for i in xrange(self.GEM_SHOP_SLOT_MAX):
			GemShopItemVnum, Price, enable, count = getGemShopItem(i)
			setGemShopItem(i, GemShopItemVnum, count)

			self.itempricelist[i].SetText(str(Price))
			self.itemslottovnum.append(GemShopItemVnum)
			self.itemslottoprice.append(Price)

			if enable == 0:
				if i >= player.GetGemShopOpenSlotCount():
					self.wndSellItemSlot.DisableSlot(i)
				else:
					self.wndSellItemSlot.LockSlot(i)

		self.wndSellItemSlot.RefreshSlot()
		self.gemshoprefreshtime = player.GetGemShopRefreshTime()

	def GemShopSlotAdd(self, slotindex, enable):
		self.wndSellItemSlot.EnableSlot(slotindex)
		self.wndSellItemSlot.RefreshSlot()

	def GemShopSlotBuy(self, slotindex, enable):
		if enable == False:
			self.wndSellItemSlot.LockSlot(slotindex)
			self.wndSellItemSlot.RefreshSlot()

	def SetItemToolTip(self, tooltip):
		self.tooltipitem = tooltip

	def __ShowToolTip(self, slotIndex):
		if self.tooltipitem:
			self.tooltipitem.ClearToolTip()
			metinSlot = []
			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				metinSlot.append(0)
			attrSlot = []
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				attrSlot.append((0, 0))

			self.tooltipitem.AddItemData(self.itemslottovnum[slotIndex], metinSlot, attrSlot)

	# ������ ���� �����ֱ�
	def OverInItem(self, slotIndex):
		self.wndSellItemSlot.SetUsableItem(False)
		self.__ShowToolTip(slotIndex)

	## ������ ���� ���߱�
	def OverOutItem(self):
		self.wndSellItemSlot.SetUsableItem(False)
		if self.tooltipitem:
			self.tooltipitem.HideToolTip()

	## ���� Ȯ��.
	def SlotAddQuestion(self, slotIndex):
		if player.IsGemShopWindowOpen() == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GEM_SYSTEM_OPEN_GEMSHOP)
			return

		openslotitemcount = player.GetGemShopOpenSlotItemCount(player.GetGemShopOpenSlotCount())

		if openslotitemcount == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GEM_SYSTEM_NO_MORE_ADDSLOT)
			return

		item.SelectItem(self.GEM_SHOP_ADD_ITEM_VNUM)
		gemshopadditemvnum = item.GetItemName()

		self.pop = uiCommon.QuestionDialog()
		self.pop.SetText(localeInfo.GEM_SYSTEM_ADD_SLOT % (gemshopadditemvnum, openslotitemcount))
		self.pop.SetAcceptEvent(ui.__mem_func__(self.SlotAddQuestionAccept))
		self.pop.SetCancelEvent(ui.__mem_func__(self.SlotAddQuestionCancle))
		self.pop.Open()

	def SlotAddQuestionAccept(self):
		self.pop.Close()
		self.pop = None
		net.SendGemShopSlotAdd()

	def SlotAddQuestionCancle(self):
		if self.pop:
			self.pop.Close()
			self.pop = None

	## ������ ��� �� ���� ����
	def UseItemSlot(self, slotIndex):
		GemShopItemVnum, Price, enable, count = player.GetGemShopItemID(slotIndex)

		if enable == 0:
			if slotIndex >= player.GetGemShopOpenSlotCount():
				self.SlotAddQuestion(slotIndex)
			return

		## ���� ���� Ȯ��
		if player.GetGem() < self.itemslottoprice[slotIndex]:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GEM_SYSTEM_NOT_ENOUGH_HP_GEM)
			return

		popup = uiCommon.QuestionDialog()
		popup.SetText(localeInfo.GEM_SYSTEM_BUY_ITEM)
		popup.SetAcceptEvent(lambda arg = slotIndex: self.SendBuyAccept(arg))
		popup.SetCancelEvent(self.OnCloseEvent)
		popup.Open()
		self.pop = popup

	def SendBuyAccept(self, slotindex):
		self.pop.Close()
		self.pop = None
		net.SendGemShopBuy(slotindex)

	def OnCloseEvent(self):
		self.pop.Close()
		self.pop = None

	## ���� ��ư
	def RefreshItemSlot(self):
		ItemRefreshItemCount = player.GetItemCountByVnum(self.GEM_SHOP_REFRESH_ITEM_VNUM)

		if ItemRefreshItemCount == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GEM_SYSTEM_NOT_ENOUGHT_REFRESHITEM)
			return;

		popup = uiCommon.QuestionDialog()
		popup.SetText(localeInfo.GEM_SYSTEM_REFRESH_SHOP_ITEMS)
		popup.SetAcceptEvent(self.SendRequestRefreshAccept)
		popup.SetCancelEvent(self.OnCloseEvent)
		popup.Open()
		self.pop = popup

	def SendRequestRefreshAccept(self):
		self.pop.Close()
		self.pop = None
		net.SendGemShopRefresh()

	## �־����� �ݱ�
	def OnUpdate(self):
		if self.IsOpen:
			(x, y, z) = player.GetMainCharacterPosition()
			if abs(x - self.xGemWindowStart) > self.GEM_SHOP_WINDOW_LIMIT_RANGE or abs(y - self.yGemWindowStart) > self.GEM_SHOP_WINDOW_LIMIT_RANGE:
				self.Close()

			## ���� �ð�
			leftSec = max(0, self.gemshoprefreshtime - app.GetGlobalTimeStamp())
			if leftSec > 0:
				self.RefreshTimeValue.SetText(localeInfo.SecondToHMGolbal(leftSec))
