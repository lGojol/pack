import ui
import net
import app
import item
import chat
import grp
import uiCommon
import localeInfo
import uiScriptLocale
import shop
import background
import player
import privateShop
import uiToolTip
import constInfo

from _weakref import proxy

PRIVATESEARCH_PATH = "d:/ymir work/ui/privatesearch/"
PRIVATESHOP_PATH = "d:/ymir work/ui/game/premium_private_shop/"

MAIN_CATEGORY_X = 4
SUB_CATEGORY_X = 4 + 16
MAIN_CATEGORY_Y = 0

NONE_SELECTED = 0

filter_config_template = {
	privateShop.FILTER_TYPE_ITEM_VNUM		: 0,
	privateShop.FILTER_TYPE_ITEM_TYPE		: -1,
	privateShop.FILTER_TYPE_ITEM_SUBTYPE	: -1,

	privateShop.FILTER_TYPE_CLASS			: -1,

	privateShop.FILTER_TYPE_MIN_LEVEL		: 1,
	privateShop.FILTER_TYPE_MAX_LEVEL		: 120,

	privateShop.FILTER_TYPE_MIN_REFINEMENT	: 0,
	privateShop.FILTER_TYPE_MAX_REFINEMENT	: 9,

	privateShop.FILTER_TYPE_MIN_CHEQUE		: 0,
	privateShop.FILTER_TYPE_MAX_CHEQUE		: constInfo.CHEQUE_MAX,

	privateShop.FILTER_TYPE_MIN_GOLD		: 0,
	privateShop.FILTER_TYPE_MAX_GOLD		: constInfo.GOLD_MAX,
}

class DropDownList(ui.Window):
	def __init__(self, parent, x, y):
		ui.Window.__init__(self)

		self.SetParent(parent)
		self.SetPosition(x, y)

		self.x = x
		self.y = y
		self.width = 0
		self.height = 0

		# List Configurations
		self.isSelected = False
		self.isOver = False
		self.isListOpened = False
		self.event = None
		self.eventArgs = None

		# ListBox
		self.listBox = ui.DynamicListBox()
		self.listBox.SetParent(self)
		self.listBox.SetPosition(0, 0)
		self.listBox.SetPickAlways()
		self.listBox.SetVisibleLineCount(12)
		self.listBox.SetEvent(ui.__mem_func__(self.OnSelectItem))
		self.listBox.Hide()

	def __del__(self):
		ui.Window.__del__(self)
		self.listBox = None
		self.event = None
		self.eventArgs = None

	def SetPosition(self, x, y):
		ui.Window.SetPosition(self, x, y)
		self.x = x
		self.y = y

	def SetSize(self, width, height = 0):
		self.width = width
		self.height = height

		self.AdjustListBox()

	def AdjustListBox(self):
		if self.listBox.GetItemCount() <= self.listBox.GetVisibleLineCount():
			self.listBox.SetSize(self.width, self.listBox.GetHeight())
			self.height = self.listBox.GetHeight()
		else:
			self.listBox.SetSize(self.width, self.listBox.GetVisibleHeight())
			self.height = self.listBox.GetVisibleHeight()

		ui.Window.SetSize(self, self.width, self.height)

	def SetEvent(self, event):
		self.event = event

	def OnSelectItem(self, index, name):
		self.CloseListBox()

		if self.event:
			self.event(index)

	def ClearItem(self):
		self.CloseListBox()
		self.listBox.ClearItem()

	def InsertItem(self, index, name):
		self.listBox.InsertItem(index, name)
		self.listBox.ArrangeItem()

	def OpenListBox(self):
		self.isListOpened = True
		self.listBox.Show()
		self.Show()

	def CloseListBox(self):
		self.isListOpened = False
		self.listBox.Hide()
		self.Hide()

	def IsOpened(self):
		return self.isListOpened

	def GetItemCount(self):
		return self.listBox.GetItemCount()

	def OnMouseWheel(self, nLen):
		if nLen > 0:
			self.listBox.OnUp()
			return True

		elif nLen < 0:
			self.listBox.OnDown()
			return True

	def OnMouseLeftButtonDown(self):
		self.isSelected = True

	def OnMouseLeftButtonUp(self):
		self.isSelected = False
		self.CloseListBox()

	def OnUpdate(self):
		if self.IsIn():
			self.isOver = True
		else:
			self.isOver = False

	def OnRender(self):
		if self.isListOpened:
			xRender, yRender = self.GetGlobalPosition()

			widthRender = self.width
			heightRender = self.height

			grp.SetColor(ui.BACKGROUND_COLOR)
			grp.RenderBar(xRender, yRender, widthRender, heightRender)

			if self.isOver:
				grp.SetColor(ui.HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + 3, self.width - 3, heightRender - 5)

				if self.isSelected:
					grp.SetColor(ui.WHITE_COLOR)
					grp.RenderBar(xRender + 2, yRender + 3, self.width - 3, heightRender - 5)

class ItemSlot(ui.Window):
	def __init__(self, parent, x, y):
		ui.Window.__init__(self)

		# Button Background
		self.mainButton = ui.Button()
		self.mainButton.SetParent(self)
		self.mainButton.SetPosition(0, 0)
		self.mainButton.SetUpVisual("d:/ymir work/ui/tab_01.tga")
		self.mainButton.SetOverVisual("d:/ymir work/ui/tab_02.tga")
		self.mainButton.SetDownVisual("d:/ymir work/ui/tab_02.tga")
		self.mainButton.SetShowToolTipEvent(ui.__mem_func__(self.__OnOverInItem))
		self.mainButton.SetHideToolTipEvent(ui.__mem_func__(self.__OnOverOutItem))
		self.mainButton.SetEvent(ui.__mem_func__(self.OnSelect))
		self.mainButton.Show()

		self.itemNameText = ui.TextLine()
		self.itemNameText.SetParent(self.mainButton)
		self.itemNameText.SetPosition(75, 0)
		self.itemNameText.SetVerticalAlignCenter()
		self.itemNameText.SetWindowVerticalAlignCenter()
		self.itemNameText.SetHorizontalAlignCenter()
		self.itemNameText.Show()

		self.sellerNameText = ui.TextLine()
		self.sellerNameText.SetParent(self.mainButton)
		self.sellerNameText.SetPosition(215, 0)
		self.sellerNameText.SetVerticalAlignCenter()
		self.sellerNameText.SetWindowVerticalAlignCenter()
		self.sellerNameText.SetHorizontalAlignCenter()
		self.sellerNameText.Show()

		self.itemCountText = ui.TextLine()
		self.itemCountText.SetParent(self.mainButton)
		self.itemCountText.SetPosition(315, 0)
		self.itemCountText.SetVerticalAlignCenter()
		self.itemCountText.SetWindowVerticalAlignCenter()
		self.itemCountText.SetHorizontalAlignCenter()
		self.itemCountText.Show()

		# Price Information
		self.chequePriceText = ui.TextLine()
		self.chequePriceText.SetParent(self.mainButton)
		self.chequePriceText.SetPosition(385, 0)
		self.chequePriceText.SetVerticalAlignCenter()
		self.chequePriceText.SetWindowVerticalAlignCenter()
		self.chequePriceText.SetHorizontalAlignCenter()
		self.chequePriceText.Show()

		self.goldPriceText = ui.TextLine()
		self.goldPriceText.SetParent(self.mainButton)
		self.goldPriceText.SetPosition(465, 0)
		self.goldPriceText.SetVerticalAlignCenter()
		self.goldPriceText.SetWindowVerticalAlignCenter()
		self.goldPriceText.SetHorizontalAlignCenter()
		self.goldPriceText.Show()

		self.SetParent(parent)
		self.SetSize(self.mainButton.GetWidth(), self.mainButton.GetHeight())
		self.SetPosition(x, y)

		self.isSelected = False
		self.toolTip = None
		self.index = -1

	def __del__(self):
		ui.Window.__del__(self)

	def SetToolTip(self, toolTip):
		self.toolTip = proxy(toolTip)

	def SetSelected(self, selected):
		self.isSelected = selected

	def IsSelected(self):
		return self.isSelected

	def SetIndex(self, index):
		self.index = index

	def GetIndex(self):
		return self.index

	def OnSelect(self):
		if self.onSelectEvent:
			self.onSelectEvent(self.GetIndex())

	def Select(self):
		self.mainButton.SetUpVisual("d:/ymir work/ui/tab_02.tga")
		self.mainButton.SetOverVisual("d:/ymir work/ui/tab_01.tga")
		self.mainButton.SetDownVisual("d:/ymir work/ui/tab_01.tga")

	def Unselect(self):
		self.mainButton.SetUpVisual("d:/ymir work/ui/tab_01.tga")
		self.mainButton.SetOverVisual("d:/ymir work/ui/tab_02.tga")
		self.mainButton.SetDownVisual("d:/ymir work/ui/tab_02.tga")

	def SetSellerName(self, name):
		self.fullSellerName = name
		self.sellerNameText.SetText(name)

		maxNameLenght = -1
		while self.sellerNameText.GetTextSize()[0] >= 100:
			self.sellerNameText.SetText(name[:maxNameLenght])
			maxNameLenght -= 1

		if maxNameLenght != -1:
			shortenedName = name[: maxNameLenght - 1] + '..'
			self.sellerNameText.SetText(shortenedName)

	def SetItemName(self, name):
		self.itemNameText.SetText(name)

		maxNameLenght = -1
		while self.itemNameText.GetTextSize()[0] >= 125:
			self.itemNameText.SetText(name[:maxNameLenght])
			maxNameLenght -= 1

		if maxNameLenght != -1:
			shortenedName = name[: maxNameLenght - 1] + '..'
			self.itemNameText.SetText(shortenedName)

	def SetItemCount(self, count):
		self.itemCountText.SetText('x' + str(count))

	def SetGoldPrice(self, goldPrice):
		self.goldPriceText.SetText(localeInfo.NumberToMoneyStringNoUnit(goldPrice))

	def SetChequePrice(self, chequePrice):
		self.chequePriceText.SetText(localeInfo.NumberToMoneyStringNoUnit(chequePrice))

	def SetOnOverInItemEvent(self, event):
		self.onOverInItemEvent = ui.__mem_func__(event)

	def SetOnOverOutItemEvent(self, event):
		self.onOverOutItemEvent = ui.__mem_func__(event)

	def __OnOverInItem(self):
		self.onOverInItemEvent(self.GetIndex())

	def __OnOverOutItem(self):
		self.onOverOutItemEvent()

	def SetOnSelectEvent(self, event):
		self.onSelectEvent = ui.__mem_func__(event)

class PrivateShopSeachWindow(ui.ScriptWindow):
	CLICK_LIMIT_TIME				= 3
	PAGE_NUMBER_SIZE				= 5
	PAGEONE_MAX_SIZE				= privateShop.RESULT_MAX_NUM * PAGE_NUMBER_SIZE
	SUGGESTION_MINIMAL_CHAR_REQ		= 3
	ATTRIBUTE_MAX_NUM				= 5
	ATTRIBUTE_TYPE					= 0
	ATTRIBUTE_VALUE					= 1

	SPECIAL_TITLE_COLOR = 0xff4E3D30

	JOB_MAX_COUNT = 4
	JOB_NAME_DICT = {
		NONE_SELECTED					:		localeInfo.PRIVATE_SHOP_SEARCH_SELECT_NONE,
		1								:		localeInfo.JOB_WARRIOR,
		2								:		localeInfo.JOB_ASSASSIN,
		3								:		localeInfo.JOB_SURA,
		4								:		localeInfo.JOB_SHAMAN,
	}

	JOB_MAX_COUNT = 4
	JOB_NAME_DIC = {
		0								:		localeInfo.PRIVATE_SHOP_SEARCH_SELECT_NONE,
		1								:		localeInfo.JOB_WARRIOR,
		2								:		localeInfo.JOB_ASSASSIN,
		3								:		localeInfo.JOB_SURA,
		4								:		localeInfo.JOB_SHAMAN, 
	}

	WEAPON_MASK_SUBTYPE_DIC = {
		0:
		{
			item.WEAPON_SWORD				:		localeInfo.CATEGORY_WEAPON_WEAPON_SWORD,
			item.WEAPON_TWO_HANDED			:		localeInfo.CATEGORY_WEAPON_WEAPON_TWO_HANDED,
		},

		1:
		{
			item.WEAPON_SWORD				:		localeInfo.CATEGORY_WEAPON_WEAPON_SWORD,
			item.WEAPON_DAGGER				:		localeInfo.CATEGORY_WEAPON_WEAPON_DAGGER,
			item.WEAPON_BOW					:		localeInfo.CATEGORY_WEAPON_WEAPON_BOW,
			item.WEAPON_ARROW				:		localeInfo.CATEGORY_WEAPON_WEAPON_ARROW,
		},

		2:
		{
			item.WEAPON_SWORD				:		localeInfo.CATEGORY_WEAPON_WEAPON_SWORD,
		},

		3:
		{
			item.WEAPON_BELL				:		localeInfo.CATEGORY_WEAPON_WEAPON_BELL,
			item.WEAPON_FAN					:		localeInfo.CATEGORY_WEAPON_WEAPON_FAN,
		},
	}

	ARMOR_MASK_SUBTYPE_DIC = {
		item.ARMOR_BODY						:		localeInfo.CATEGORY_ARMOR_ARMOR_BODY,
		item.ARMOR_HEAD						:		localeInfo.CATEGORY_ARMOR_ARMOR_HEAD,
		item.ARMOR_SHIELD					:		localeInfo.CATEGORY_ARMOR_ARMOR_SHIELD,
		item.ARMOR_WRIST					:		localeInfo.CATEGORY_JEWELRY_ARMOR_WRIST,
		item.ARMOR_FOOTS					:		localeInfo.CATEGORY_JEWELRY_ARMOR_FOOTS,
		item.ARMOR_NECK						:		localeInfo.CATEGORY_JEWELRY_ARMOR_NECK,
		item.ARMOR_EAR						:		localeInfo.CATEGORY_JEWELRY_ARMOR_EAR,
	}

	COSTUMES_MASK_SUBTYPE_DIC = {
		item.COSTUME_TYPE_BODY				:		localeInfo.CATEGORY_COSTUMES_COSTUME_BODY,
		item.COSTUME_TYPE_HAIR				:		localeInfo.CATEGORY_COSTUMES_COSTUME_HAIR,
	}

	DS_SUBTYPE_DIC = {
		item.DS_SLOT1						:		localeInfo.PRIVATESHOPSEARCH_DS_WHITE,
		item.DS_SLOT2						:		localeInfo.PRIVATESHOPSEARCH_DS_RED,
		item.DS_SLOT3						:		localeInfo.PRIVATESHOPSEARCH_DS_GREEN,
		item.DS_SLOT4						:		localeInfo.PRIVATESHOPSEARCH_DS_BLUE,
		item.DS_SLOT5						:		localeInfo.PRIVATESHOPSEARCH_DS_YELLOW,
		item.DS_SLOT6						:		localeInfo.PRIVATESHOPSEARCH_DS_BLACK,
	}

	ITEM_MASK_TYPE_DIC = {
		item.ITEM_TYPE_NONE					:		localeInfo.CATEGORY_ETC,
		item.ITEM_TYPE_WEAPON				:		localeInfo.CATEGORY_EQUIPMENT_WEAPON,
		item.ITEM_TYPE_ARMOR				:		localeInfo.CATEGORY_EQUIPMENT_ARMOR,
		item.ITEM_TYPE_COSTUME				:		localeInfo.CATEGORY_COSTUMES,
		item.ITEM_TYPE_DS					:		localeInfo.CATEGORY_DRAGON_STONE,
	}

	ITEM_MASK_MASK_SUBTYPE_DICS = {
		item.ITEM_TYPE_NONE					:		{ 0 : localeInfo.CATEGORY_ETC},
		item.ITEM_TYPE_WEAPON				:		WEAPON_MASK_SUBTYPE_DIC,
		item.ITEM_TYPE_ARMOR				:		ARMOR_MASK_SUBTYPE_DIC,
		item.ITEM_TYPE_COSTUME				:		COSTUMES_MASK_SUBTYPE_DIC,
		item.ITEM_TYPE_DS					:		DS_SUBTYPE_DIC,
	}

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.mode = privateShop.MODE_NONE
		self.interface				= None
		self.toolTipItem			= None
		self.questionDialog			= None
		self.itemNamesListBox		= None

		self.lastSearchClickTime	= -1
		self.lastBuyClickTime		= -1

		self.selectedItemVnum		= 0
		self.selectedItemIndex		= -1
		self.selectedClass			= -1
		self.selectedItemType		= -1
		self.selectedItemSubType	= -1

		self.filter_config			= filter_config_template.copy()

		self.resultButtonDict		= dict()
		self.pageButtonDict			= dict()
		self.currentPageNumber		= 1
		self.pageCount				= 0
		self.bigPageCount			= 1

		self.toolTip = uiToolTip.ToolTip()
		self.toolTip.HideToolTip()

		self.__LoadWindow()

	def __del__(self):
		self.toolTipItem			= None
		self.questionDialog			= None

		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/PrivateShopSearchWindow.py")
		except:
			import exception
			exception.Abort("PrivateShopSearchWindow.__LoadWindow.UIScript/PrivateShopSearchWindow.py")
		try:
			self.board = self.GetChild("board")
			self.board.SetCloseEvent(ui.__mem_func__(self.Close))

			self.searchButton = self.GetChild("SearchButton")
			self.searchButton.SetEvent(ui.__mem_func__(self.Search))

			self.buyButton = self.GetChild("BuyButton")
			self.buyButton.SetEvent(ui.__mem_func__(self.Buy))

			self.minLevelInput = self.GetChild("MinLevelValue")
			self.minLevelInput.SetEscapeEvent(ui.__mem_func__(self.Close))
			self.minLevelInput.SAFE_SetUpdateEvent(self.OnChangeInputValue, self.minLevelInput, privateShop.FILTER_TYPE_MIN_LEVEL)

			self.maxLevelInput = self.GetChild("MaxLevelValue")
			self.maxLevelInput.SetEscapeEvent(ui.__mem_func__(self.Close))
			self.maxLevelInput.SAFE_SetUpdateEvent(self.OnChangeInputValue, self.maxLevelInput, privateShop.FILTER_TYPE_MAX_LEVEL)

			self.minRefineInput = self.GetChild("MinRefineValue")
			self.minRefineInput.SetEscapeEvent(ui.__mem_func__(self.Close))
			self.minRefineInput.SAFE_SetUpdateEvent(self.OnChangeInputValue, self.minRefineInput, privateShop.FILTER_TYPE_MIN_REFINEMENT)

			self.maxRefineInput = self.GetChild("MaxRefineValue")
			self.maxRefineInput.SetEscapeEvent(ui.__mem_func__(self.Close))
			self.maxRefineInput.SAFE_SetUpdateEvent(self.OnChangeInputValue, self.maxRefineInput, privateShop.FILTER_TYPE_MAX_REFINEMENT)

			self.minChequeInput = self.GetChild("ChequeMinValue")
			self.minChequeInput.SetEscapeEvent(ui.__mem_func__(self.Close))
			self.minChequeInput.SAFE_SetUpdateEvent(self.OnChangeInputValue, self.minChequeInput, privateShop.FILTER_TYPE_MIN_CHEQUE)

			self.maxChequeInput = self.GetChild("ChequeMaxValue")
			self.maxChequeInput.SetEscapeEvent(ui.__mem_func__(self.Close))
			self.maxChequeInput.SAFE_SetUpdateEvent(self.OnChangeInputValue, self.maxChequeInput, privateShop.FILTER_TYPE_MAX_CHEQUE)

			self.minGoldInput = self.GetChild("GoldMinValue")
			self.minGoldInput.SetEscapeEvent(ui.__mem_func__(self.Close))
			self.minGoldInput.SAFE_SetUpdateEvent(self.OnChangeInputValue, self.minGoldInput, privateShop.FILTER_TYPE_MIN_GOLD)

			self.maxGoldInput = self.GetChild("GoldMaxValue")
			self.maxGoldInput.SetEscapeEvent(ui.__mem_func__(self.Close))
			self.maxGoldInput.SAFE_SetUpdateEvent(self.OnChangeInputValue, self.maxGoldInput, privateShop.FILTER_TYPE_MAX_GOLD)

			self.itemNameInput = self.GetChild("ItemNameInput")
			self.itemNameInput.SetEscapeEvent(ui.__mem_func__(self.Close))
			self.itemNameInput.SetUpdateEvent(ui.__mem_func__(self.__OnItemNameInputUpdate))
			self.itemNameInput.SetTabEvent(ui.__mem_func__(self.__ItemNameInputResult))

			self.pageButtonDict = {
				"PAGE_FIRST_PREV"	: self.GetChild("FirstPrevButton"),
				"PAGE_PREV"			: self.GetChild("PrevButton"),
				"PAGE_1"			: self.GetChild("Page1Button"),
				"PAGE_2"			: self.GetChild("Page2Button"),
				"PAGE_3"			: self.GetChild("Page3Button"),
				"PAGE_4"			: self.GetChild("Page4Button"),
				"PAGE_5"			: self.GetChild("Page5Button"),
				"PAGE_NEXT"			: self.GetChild("NextButton"),
				"PAGE_LAST_NEXT"	: self.GetChild("LastNextButton"),
			}

			self.pageButtonDict["PAGE_FIRST_PREV"].SetEvent(ui.__mem_func__(self.FirstPrevPage))
			self.pageButtonDict["PAGE_PREV"].SetEvent(ui.__mem_func__(self.PrevPage))
			self.pageButtonDict["PAGE_1"].SetEvent(ui.__mem_func__(self.SelectPage), 1)
			self.pageButtonDict["PAGE_2"].SetEvent(ui.__mem_func__(self.SelectPage), 2)
			self.pageButtonDict["PAGE_3"].SetEvent(ui.__mem_func__(self.SelectPage), 3)
			self.pageButtonDict["PAGE_4"].SetEvent(ui.__mem_func__(self.SelectPage), 4)
			self.pageButtonDict["PAGE_5"].SetEvent(ui.__mem_func__(self.SelectPage), 5)
			self.pageButtonDict["PAGE_NEXT"].SetEvent(ui.__mem_func__(self.NextPage))
			self.pageButtonDict["PAGE_LAST_NEXT"].SetEvent(ui.__mem_func__(self.LastNextPage))

			self.itemNamesListBox = DropDownList(self, 10, 330)
			self.itemNamesListBox.SetSize(width = 115)
			self.itemNamesListBox.SetEvent(self.SelectItem)

			# Hide unavailable buttons
			self.HidePageButton()
			self.buyButton.Hide()

			self.__MakeCategoryButtons()
			self.__MakeResultButtons()

		except:
			import exception
			exception.Abort("PrivateShopSearchWindow.__LoadWindow.PrivateShopSearchDialog")

	def __MakeCategoryButtons(self):
		# Item SubType ComboBox
		self.itemSubTypeSelectSlot = ui.DynamicComboBoxImage(self, "d:/ymir work/ui/privatesearch/private_leftSlotImg.sub", 12, 98 + 18)
		self.itemSubTypeSelectSlot.SetEvent(lambda itemSubTypeIndex, argSelf=proxy(self): argSelf.OnChangeItemSubTypeSlot(itemSubTypeIndex))

		self.itemSubTypeSelectSlot.InsertItem(0, localeInfo.CATEGORY_ETC)
		self.itemSubTypeSelectSlot.SetDefaultTitle(localeInfo.CATEGORY_ETC)
		self.itemSubTypeSelectSlot.Show()

		# Item Type ComboBox
		self.itemTypeSelectSlot = ui.DynamicComboBoxImage(self, "d:/ymir work/ui/privatesearch/private_leftSlotImg.sub", 12, 96)
		self.itemTypeSelectSlot.SetEvent(lambda itemTypeIndex, argSelf=proxy(self): argSelf.OnChangeItemTypeSlot(itemTypeIndex))

		for index, itemTypeDic in self.ITEM_MASK_TYPE_DIC.items() :
			self.itemTypeSelectSlot.InsertItem(index,self.ITEM_MASK_TYPE_DIC[index])

		self.itemTypeSelectSlot.SetDefaultTitle(self.ITEM_MASK_TYPE_DIC[item.ITEM_TYPE_NONE])
		self.itemTypeSelectSlot.Show()

		# Class ComboBox
		self.classSelectSlot = ui.DynamicComboBoxImage(self, "d:/ymir work/ui/privatesearch/private_leftSlotImg.sub", 12, 56)
		self.classSelectSlot.SetEvent(lambda job, argSelf=proxy(self): argSelf.OnChangeClassSlot(job))

		for i in range(0, self.JOB_MAX_COUNT + 1):
			self.classSelectSlot.InsertItem(i, self.JOB_NAME_DIC[i])
		self.classSelectSlot.SetDefaultTitle(self.JOB_NAME_DIC[0])
		self.classSelectSlot.Show()

	def __MakeResultButtons(self):
		for i in range(privateShop.RESULT_MAX_NUM):
			itemSlot = ItemSlot(self, 138, 62 + 24 * i)
			itemSlot.SetOnOverInItemEvent(self.OverInItem)
			itemSlot.SetOnOverOutItemEvent(self.OverOutItem)
			itemSlot.SetOnSelectEvent(self.OnSelectItemResult)

			self.resultButtonDict[i] = itemSlot

	def SetItemToolTip(self, tooltip):
		self.toolTipItem = tooltip

	def BindInterfaceClass(self, interface):
		self.interface = interface

	def Open(self, mode):
		self.mode = mode

		self.ResetFilterSettings()
		self.itemNameInput.SetFocus()

		self.SetTop()
		self.Show()

	def Close(self):
		self.bigPageCount = 1

		self.lastSearchClickTime	= -1
		self.lastBuyClickTime		= -1

		if self.itemNamesListBox.IsOpened():
			self.itemNamesListBox.CloseListBox()

		self.classSelectSlot.Enable()
		self.itemTypeSelectSlot.Enable()
		self.itemSubTypeSelectSlot.Enable()
		self.itemNameInput.SetText("")

		# Reset focus from possible focused editlines
		self.minLevelInput.KillFocus()
		self.maxLevelInput.KillFocus()
		self.minRefineInput.KillFocus()
		self.maxRefineInput.KillFocus()
		self.minChequeInput.KillFocus()
		self.maxChequeInput.KillFocus()
		self.minGoldInput.KillFocus()
		self.maxGoldInput.KillFocus()
		self.itemNameInput.KillFocus()

		privateShop.ClearSearchResult()

		for itemSlot in self.resultButtonDict.values():
			itemSlot.Unselect()
			itemSlot.Hide()

		self.HidePageButton()
		self.buyButton.Hide()

		if self.questionDialog:
			self.questionDialog.Close()
			self.questionDialog = None

		privateShop.DeletePrivateShopSearchPos()
		net.SendClosePrivateShopSearchPacket()

		self.Hide()

	def Destroy(self):
		self.ClearDictionary()

		self.toolTipItem = None

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnUpdate(self):
		if (app.GetGlobalTimeStamp() - self.lastSearchClickTime) > self.CLICK_LIMIT_TIME and self.searchButton.IsDisable() == False:
			self.searchButton.Enable()
			self.searchButton.SetUp()

		if (app.GetGlobalTimeStamp() - self.lastBuyClickTime) > self.CLICK_LIMIT_TIME and self.buyButton.IsDisable() == False and self.mode == privateShop.MODE_TRADE:
			self.buyButton.Enable()
			self.buyButton.SetUp()

	def Search(self):
		lookItemCount = player.GetItemCountByVnum(60004)
		tradeItemCount = player.GetItemCountByVnum(60005)

		if lookItemCount <= 0 and tradeItemCount <= 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.PRIVATESHOPSEARCH_NEED_ITEM_FIND)
			self.Close()
			return

		if self.selectedItemVnum == 0 and self.selectedItemType == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.PRIVATE_SHOP_SEARCH_VNUM_ITEM_NOT_SELECTED)
			return

		self.lastSearchClickTime = app.GetGlobalTimeStamp()

		privateShop.ClearSearchResult()
		privateShop.SetSearchResultPage(0)

		self.searchButton.Disable()
		self.searchButton.Down()

		self.buyButton.Hide()
		self.HidePageButton()

		# Reset buttons
		self.bigPageCount = 1
		self.currentPageNumber = 1
		for i in range(1, self.PAGE_NUMBER_SIZE + 1):
			self.pageButtonDict["PAGE_%d" % i].SetText(str(i))

		for itemSlot in self.resultButtonDict.values():
			itemSlot.Hide()

		net.SendPrivateShopSearchPacket(self.filter_config)

	def Buy(self):
		tradeItemCount = player.GetItemCountByVnum(60005)

		if tradeItemCount <= 0 and self.mode == privateShop.MODE_TRADE:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.PRIVATESHOPSEARCH_NEED_ITEM_BUY)
			self.Close()
			return

		if self.selectedItemIndex < 0:
			return

		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(localeInfo.PRIVATESHOPSEARCH_BUYTIME)
		questionDialog.SetAcceptEvent(self.OnBuyAcceptEvent)
		questionDialog.SetCancelEvent(self.OnBuyCloseEvent)
		questionDialog.Open()
		self.questionDialog = questionDialog

	def OnBuyAcceptEvent(self):
		if self.selectedItemIndex == -1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.PRIVATE_SHOP_BUY_VNUM_ITEM_NOT_SELECTED)
			return

		self.lastBuyClickTime = app.GetGlobalTimeStamp()
		self.buyButton.Disable()
		self.buyButton.Down()

		net.SendPrivateShopSearchBuyPacket(self.selectedItemIndex)

		self.questionDialog.Close()
		self.questionDialog = None

	def OnBuyCloseEvent(self):
		self.questionDialog.Close()
		self.questionDialog = None

	def Refresh(self):
		maxCount = privateShop.GetSearchResultMaxCount()
		page = privateShop.GetSearchResultPage()

		self.ShowItemResult(page)

		if maxCount:
			self.ShowPageButton(maxCount, page)

			# Enable/Disable Previous Page Button
			if self.bigPageCount == 1:
				self.pageButtonDict["PAGE_PREV"].Disable()
				self.pageButtonDict["PAGE_PREV"].Down()
				self.pageButtonDict["PAGE_PREV"].Hide()
			else:
				self.pageButtonDict["PAGE_PREV"].Enable()
				self.pageButtonDict["PAGE_PREV"].Show()

			# Enable/Disable First Page Button
			if self.bigPageCount - 1 <= 1:
				self.pageButtonDict["PAGE_FIRST_PREV"].Disable()
				self.pageButtonDict["PAGE_FIRST_PREV"].Down()
				self.pageButtonDict["PAGE_FIRST_PREV"].Hide()
			else:
				self.pageButtonDict["PAGE_FIRST_PREV"].Enable()
				self.pageButtonDict["PAGE_FIRST_PREV"].Show()

			# Enable/Disable Next Page Button
			if maxCount <= self.bigPageCount * self.PAGEONE_MAX_SIZE:
				self.pageButtonDict["PAGE_NEXT"].Disable()
				self.pageButtonDict["PAGE_NEXT"].Down()
				self.pageButtonDict["PAGE_NEXT"].Hide()
			else:
				self.pageButtonDict["PAGE_NEXT"].Enable()
				self.pageButtonDict["PAGE_NEXT"].Show()

			# Enable/Disable Last Page Button
			if maxCount <= (self.bigPageCount+1) * self.PAGEONE_MAX_SIZE:
				self.pageButtonDict["PAGE_LAST_NEXT"].Disable()
				self.pageButtonDict["PAGE_LAST_NEXT"].Down()
				self.pageButtonDict["PAGE_LAST_NEXT"].Hide()
			else:
				self.pageButtonDict["PAGE_LAST_NEXT"].Enable()
				self.pageButtonDict["PAGE_LAST_NEXT"].Show()

			if page and self.mode == privateShop.MODE_TRADE:
				self.buyButton.Show()
		else:
			self.HidePageButton()
			self.buyButton.Hide()

	def ShowItemResult(self, page):
		for i in range(privateShop.RESULT_MAX_NUM):
			result_index = i + (page - 1) * privateShop.RESULT_MAX_NUM
			(item_vnum, seller_name, item_count, gold, cheque) = privateShop.GetSearchResult(result_index)

			if item_vnum:
				item.SelectItem(item_vnum)

				self.resultButtonDict[i].SetItemName(item.GetItemName())
				self.resultButtonDict[i].SetSellerName(seller_name)
				self.resultButtonDict[i].SetItemCount(item_count)
				self.resultButtonDict[i].SetChequePrice(cheque)
				self.resultButtonDict[i].SetGoldPrice(gold)
				self.resultButtonDict[i].SetIndex(result_index)
				self.resultButtonDict[i].Unselect()
				self.resultButtonDict[i].Show()

				if self.selectedItemIndex == result_index:
					self.resultButtonDict[i].Select()
			else:
				self.resultButtonDict[i].Hide()

	def __OnItemNameInputUpdate(self):
		inputText =  self.itemNameInput.GetText()

		if len(inputText) >= self.SUGGESTION_MINIMAL_CHAR_REQ:
			itemSuggestionList = item.GetItemListByName(inputText)

			# Get rid of previous suggestions
			if self.itemNamesListBox.GetItemCount():
				self.itemNamesListBox.ClearItem()

			if len(itemSuggestionList) <= 0:
				self.selectedItemVnum = 0
				self.filter_config[privateShop.FILTER_TYPE_ITEM_VNUM] = 0
				self.itemNameInput.SetBackgroundText("")
				return

			# Build up new suggestions list
			for i in range(len(itemSuggestionList)):
				(vnum, itemName) = itemSuggestionList[i]

				# Set background text for the first suggested item
				if i == 0:
					self.selectedItemVnum = vnum
					self.filter_config[privateShop.FILTER_TYPE_ITEM_VNUM] = vnum
					self.itemNameInput.SetTipText(itemName)

				self.itemNamesListBox.InsertItem(vnum, itemName)

				self.itemNamesListBox.AdjustListBox()
				self.itemNamesListBox.OpenListBox()
		else:
			self.selectedItemVnum = 0
			self.filter_config[privateShop.FILTER_TYPE_ITEM_VNUM] = 0
			self.itemNameInput.SetBackgroundText("")
			self.itemNamesListBox.CloseListBox()

		if len(inputText) == 0:
			self.classSelectSlot.Enable()
			self.itemTypeSelectSlot.Enable()
			self.itemSubTypeSelectSlot.Enable()
		else:
			self.classSelectSlot.Disable()
			self.itemTypeSelectSlot.Disable()
			self.itemSubTypeSelectSlot.Disable()

		self.__RefreshCategory()

	def __ItemNameInputResult(self):
		suggestionText =  self.itemNameInput.GetText() + self.itemNameInput.GetBackgroundText()
		(vnum, itemName) = item.GetItemByName(suggestionText)

		self.selectedItemVnum = vnum
		self.filter_config[privateShop.FILTER_TYPE_ITEM_VNUM] = vnum
		self.itemNameInput.SetBackgroundText("")
		self.itemNameInput.SetText(itemName)
		self.itemNameInput.SetEndPosition()

		# Clear suggestion list
		if self.itemNamesListBox.IsOpened():
			self.itemNamesListBox.CloseListBox()

		self.__RefreshCategory()

	def SelectItem(self, itemVnum):
		if itemVnum <= 0:
			return

		item.SelectItem(itemVnum)
		itemName = item.GetItemName()

		self.itemNameInput.SetText(itemName)
		self.itemNameInput.SetBackgroundText("")
		self.selectedItemVnum = itemVnum
		self.filter_config[privateShop.FILTER_TYPE_ITEM_VNUM] = itemVnum

		self.itemNameInput.SetEndPosition()

		# Clear suggestion list
		if self.itemNamesListBox.IsOpened():
			self.itemNamesListBox.CloseListBox()

		self.__RefreshCategory()

	def OnSelectItemResult(self, result_index):
		for itemSlot in self.resultButtonDict.values():
			if itemSlot.GetIndex() == result_index:
				if itemSlot.IsSelected() == False:
					itemSlot.Select()
					itemSlot.SetSelected(True)
					continue

			itemSlot.Unselect()
			itemSlot.SetSelected(False)

		privateShop.DeletePrivateShopSearchPos()

		if result_index != self.selectedItemIndex:
			(item_vnum, seller_name, item_count, gold, cheque) = privateShop.GetSearchResult(result_index)
			privateShop.CreatePrivateShopSearchPos(seller_name)

			self.selectedItemIndex = result_index
		else:
			self.selectedItemIndex = -1

	def ClearPageButtonColor(self):
		for i in range(1, self.PAGE_NUMBER_SIZE + 1):
			self.pageButtonDict["PAGE_%d" % i].SetTextColor(0xffffffff)
			self.pageButtonDict["PAGE_%d" % i].SetUp()
			self.pageButtonDict["PAGE_%d" % i].Enable()

	def HidePageButton(self):
		for button in self.pageButtonDict.values():
			button.Hide()

	def ShowPageButton(self, maxSize, page):
		if self.bigPageCount > 1:
			maxSize = maxSize - ((self.bigPageCount-1) * self.PAGEONE_MAX_SIZE)
			page = page - (self.bigPageCount-1) * 5

		self.pageCount = maxSize / privateShop.RESULT_MAX_NUM

		if not maxSize % privateShop.RESULT_MAX_NUM == 0:
			self.pageCount = self.pageCount + 1

		if self.pageCount > 5:
			self.pageCount = 5

		for i in range(1, self.pageCount + 1):
			self.pageButtonDict["PAGE_%d" % i].Show()

		self.pageButtonDict["PAGE_FIRST_PREV"].Show()
		self.pageButtonDict["PAGE_PREV"].Show()
		self.pageButtonDict["PAGE_NEXT"].Show()
		self.pageButtonDict["PAGE_LAST_NEXT"].Show()

		self.ClearPageButtonColor()

		self.pageButtonDict["PAGE_%d" % page].SetTextColor(self.SPECIAL_TITLE_COLOR)
		self.pageButtonDict["PAGE_%d" % page].Down()
		self.pageButtonDict["PAGE_%d" % page].Disable()

	def SelectPage(self, page):
		if page == self.currentPageNumber:
			return

		if self.bigPageCount > 1:
			if page == self.currentPageNumber - (self.bigPageCount-1) * 5:
				return

		self.ClearPageButtonColor()

		self.pageButtonDict["PAGE_%d" % page].SetTextColor(self.SPECIAL_TITLE_COLOR)
		self.pageButtonDict["PAGE_%d" % page].Down()
		self.pageButtonDict["PAGE_%d" % page].Disable()

		if self.bigPageCount > 1:
			page = page + (self.bigPageCount-1) * 5

		self.ShowItemResult(page)
		self.currentPageNumber = page

		privateShop.SetSearchResultPage(self.currentPageNumber)
		self.Refresh()

	def PrevPage(self):
		if self.bigPageCount <= 1:
			return

		self.ClearPageButtonColor()
		self.bigPageCount -= 1

		for i in range(1, self.PAGE_NUMBER_SIZE + 1):
			pageNumber = int(self.pageButtonDict["PAGE_%d" % i].GetText()) - self.PAGE_NUMBER_SIZE
			self.pageButtonDict["PAGE_%d" % i].SetText(str(pageNumber))

		newPageNumber = int(self.pageButtonDict["PAGE_1"].GetText())

		self.ShowItemResult(newPageNumber)
		self.currentPageNumber = newPageNumber

		self.pageButtonDict["PAGE_1"].SetTextColor(self.SPECIAL_TITLE_COLOR)
		self.pageButtonDict["PAGE_1"].Down()
		self.pageButtonDict["PAGE_1"].Disable()

		privateShop.SetSearchResultPage(self.currentPageNumber)
		self.Refresh()

	def NextPage(self):
		maxItemCount = privateShop.GetSearchResultMaxCount()
		if maxItemCount < self.bigPageCount * self.PAGEONE_MAX_SIZE:
			return

		for i in range(1, self.PAGE_NUMBER_SIZE + 1):
			pageNumber = int(self.pageButtonDict["PAGE_%d" % i].GetText()) + self.PAGE_NUMBER_SIZE
			self.pageButtonDict["PAGE_%d" % i].SetText(str(pageNumber))

		newPageNumber = int(self.pageButtonDict["PAGE_1"].GetText())

		self.ShowItemResult(newPageNumber)
		self.currentPageNumber = newPageNumber

		self.bigPageCount += 1
		self.HidePageButton()
		self.ClearPageButtonColor()

		self.pageButtonDict["PAGE_1"].SetTextColor(self.SPECIAL_TITLE_COLOR)
		self.pageButtonDict["PAGE_1"].Down()
		self.pageButtonDict["PAGE_1"].Disable()

		privateShop.SetSearchResultPage(self.currentPageNumber)
		self.Refresh()

	def FirstPrevPage(self):
		if self.bigPageCount - 1 <= 1:
			return

		self.ClearPageButtonColor()

		self.bigPageCount = 1
		for i in range(1, self.PAGE_NUMBER_SIZE + 1):
			self.pageButtonDict["PAGE_%d" % i].SetText(str(i))

		newPageNumber = int(self.pageButtonDict["PAGE_1"].GetText())

		self.ShowItemResult(newPageNumber)
		self.currentPageNumber = newPageNumber

		self.pageButtonDict["PAGE_1"].SetTextColor(self.SPECIAL_TITLE_COLOR)
		self.pageButtonDict["PAGE_1"].Down()
		self.pageButtonDict["PAGE_1"].Disable()

		privateShop.SetSearchResultPage(self.currentPageNumber)
		self.Refresh()

	def LastNextPage(self):
		maxSize = privateShop.GetSearchResultMaxCount()
		self.pageCount = maxSize / privateShop.RESULT_MAX_NUM

		self.HidePageButton()
		self.ClearPageButtonColor()

		if self.pageCount % self.PAGE_NUMBER_SIZE == 0:
			self.bigPageCount = (self.pageCount / self.PAGE_NUMBER_SIZE)
		else:
			self.bigPageCount = (self.pageCount / self.PAGE_NUMBER_SIZE) + 1

		pageNumber = self.PAGE_NUMBER_SIZE * (self.pageCount / self.PAGE_NUMBER_SIZE)
		if pageNumber == self.pageCount:
			pageNumber -= self.PAGE_NUMBER_SIZE

		for i in range(1, self.PAGE_NUMBER_SIZE + 1):
			self.pageButtonDict["PAGE_%d" % i].SetText(str(i + pageNumber))

		self.ShowItemResult(self.pageCount)
		self.currentPageNumber = self.pageCount

		lastPageNumber = self.currentPageNumber - (self.bigPageCount - 1) * self.PAGE_NUMBER_SIZE
		self.pageButtonDict["PAGE_%d" % lastPageNumber].SetTextColor(self.SPECIAL_TITLE_COLOR)
		self.pageButtonDict["PAGE_%d" % lastPageNumber].Down()
		self.pageButtonDict["PAGE_%d" % lastPageNumber].Disable()

		privateShop.SetSearchResultPage(self.currentPageNumber)
		self.Refresh()

	def OnChangeItemSubTypeSlot(self, itemSubTypeIndex):
		if self.selectedItemType == item.ITEM_TYPE_WEAPON:
			self.itemSubTypeSelectSlot.SetCurrentItem(self.WEAPON_MASK_SUBTYPE_DIC[self.selectedClass][itemSubTypeIndex])
		else:
			self.itemSubTypeSelectSlot.SetCurrentItem(self.ITEM_MASK_MASK_SUBTYPE_DICS[self.selectedItemType][itemSubTypeIndex])

		self.selectedItemSubType = itemSubTypeIndex
		self.filter_config[privateShop.FILTER_TYPE_ITEM_SUBTYPE] = itemSubTypeIndex

	def OnChangeItemTypeSlot(self, itemTypeIndex):
		self.itemTypeSelectSlot.SetCurrentItem(self.ITEM_MASK_TYPE_DIC[itemTypeIndex])

		if itemTypeIndex != self.selectedItemType:
			self.itemSubTypeSelectSlot.ClearItem()

			if itemTypeIndex == item.ITEM_TYPE_WEAPON:
				if self.selectedClass < 0:
					self.__SelectJobCategory(player.GetJob() + 1)

				itemSubType = 0
				saveFirstItem = False

				for i in self.WEAPON_MASK_SUBTYPE_DIC[self.selectedClass]:
					self.itemSubTypeSelectSlot.InsertItem(i,self.WEAPON_MASK_SUBTYPE_DIC[self.selectedClass][i])

					if itemSubType == 0:
						if not saveFirstItem:
							itemSubType = i
							saveFirstItem = True

				self.itemSubTypeSelectSlot.SetCurrentItem(self.WEAPON_MASK_SUBTYPE_DIC[self.selectedClass][itemSubType])
				self.selectedItemSubType = itemSubType
				self.filter_config[privateShop.FILTER_TYPE_ITEM_SUBTYPE] = itemSubType
			else:
				itemSubType = 0
				saveFirstItem = False

				for i in self.ITEM_MASK_MASK_SUBTYPE_DICS[itemTypeIndex]:
					self.itemSubTypeSelectSlot.InsertItem(i,self.ITEM_MASK_MASK_SUBTYPE_DICS[itemTypeIndex][i])

					if itemSubType == 0:
						if not saveFirstItem:
							itemSubType = i
							saveFirstItem = True

				self.itemSubTypeSelectSlot.SetCurrentItem(self.ITEM_MASK_MASK_SUBTYPE_DICS[itemTypeIndex][itemSubType])
				self.selectedItemSubType = itemSubType
				self.filter_config[privateShop.FILTER_TYPE_ITEM_SUBTYPE] = itemSubType

			self.selectedItemType = itemTypeIndex
			self.filter_config[privateShop.FILTER_TYPE_ITEM_TYPE] = itemTypeIndex

	def OnChangeClassSlot(self, job):
		self.classSelectSlot.SetCurrentItem(self.JOB_NAME_DIC[job])

		newSelectedClass = job - 1
		if newSelectedClass != self.selectedClass:
			self.selectedClass = newSelectedClass
			self.filter_config[privateShop.FILTER_TYPE_CLASS] = newSelectedClass

			if job:
				if self.selectedItemType != item.ITEM_TYPE_WEAPON and self.selectedItemType != item.ITEM_TYPE_ARMOR:
					self.__SelectItemSlotTypeCategory(item.ITEM_TYPE_WEAPON)
			else:
				self.__SelectItemSlotTypeCategory(item.ITEM_TYPE_NONE)

			if self.selectedItemType == item.ITEM_TYPE_WEAPON:
				self.itemSubTypeSelectSlot.ClearItem()

				itemSubType = 0
				saveFirstItem = False

				for i in self.WEAPON_MASK_SUBTYPE_DIC[self.selectedClass]:
					self.itemSubTypeSelectSlot.InsertItem(i,self.WEAPON_MASK_SUBTYPE_DIC[self.selectedClass][i])
					if itemSubType == 0:
						if not saveFirstItem:
							itemSubType = i
							saveFirstItem = True

				self.itemSubTypeSelectSlot.SetCurrentItem(self.WEAPON_MASK_SUBTYPE_DIC[self.selectedClass][itemSubType])
				self.selectedItemSubType = itemSubType
				self.filter_config[privateShop.FILTER_TYPE_ITEM_SUBTYPE] = itemSubType

	def __SelectJobCategory(self, job):
		self.classSelectSlot.SelectItem(job)
		self.filter_config[privateShop.FILTER_TYPE_CLASS] = job - 1

	def __SelectItemSlotTypeCategory(self, itemType):
		self.itemTypeSelectSlot.SelectItem(itemType)

	def __SelectItemSlotSubTypeCategory(self, itemSubType):
		self.itemSubTypeSelectSlot.SelectItem(itemSubType)

	def __RefreshCategory(self):
		itemVnum = self.selectedItemVnum

		if itemVnum <= 0:
			self.__SelectJobCategory(0)
			self.__SelectItemSlotTypeCategory(0)
		else:
			item.SelectItem(itemVnum)
			itemType = item.GetItemType()
			itemSubType = item.GetItemSubType()

			if itemType == item.ITEM_TYPE_WEAPON or itemType == item.ITEM_TYPE_ARMOR or itemType == item.ITEM_TYPE_COSTUME:
				if not item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR) and\
					not item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN) and\
					not item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA) and\
					not item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN):
					self.__SelectJobCategory(0)

				elif not item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR):
					self.__SelectJobCategory(1)

				elif not item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN):
					self.__SelectJobCategory(2)

				elif not item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA):
					self.__SelectJobCategory(3)

				elif not item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN):
					self.__SelectJobCategory(4)

				self.__SelectItemSlotTypeCategory(itemType)
				self.__SelectItemSlotSubTypeCategory(itemSubType)

			elif itemType == item.ITEM_TYPE_DS:
				self.__SelectItemSlotTypeCategory(itemType)
				self.__SelectItemSlotSubTypeCategory(itemSubType)

				self.__SelectJobCategory(0)
			else:
				self.__SelectJobCategory(0)

				self.__SelectItemSlotTypeCategory(0)
				self.__SelectItemSlotSubTypeCategory(0)

	def OnChangeInputValue(self, input, type):
		value = input.GetText()
		if value == "" or value == "0":
			value = 0
		else:
			value = int(value)

		self.filter_config[type] = value

	def ResetFilterSettings(self):
		self.selectedItemVnum		= 0
		self.selectedItemIndex		= -1

		self.itemNameInput.SetText("")
		self.itemNameInput.SetBackgroundText("")

		self.selectedClass = -1
		self.__SelectJobCategory(0)

		self.selectedItemType = -1
		self.__SelectItemSlotTypeCategory(0)

		self.selectedItemSubType = -1
		self.__SelectItemSlotSubTypeCategory(0)

		self.minLevelInput.SetText("%s" % (str(filter_config_template[privateShop.FILTER_TYPE_MIN_LEVEL])))
		self.maxLevelInput.SetText("%s" % (str(filter_config_template[privateShop.FILTER_TYPE_MAX_LEVEL])))

		self.minRefineInput.SetText("%s" % (str(filter_config_template[privateShop.FILTER_TYPE_MIN_REFINEMENT])))
		self.maxRefineInput.SetText("%s" % (str(filter_config_template[privateShop.FILTER_TYPE_MAX_REFINEMENT])))

		self.minChequeInput.SetText("%s" % (str(filter_config_template[privateShop.FILTER_TYPE_MIN_CHEQUE])))

		self.maxChequeInput.SetText("%s" % (str(filter_config_template[privateShop.FILTER_TYPE_MAX_CHEQUE])))

		self.minGoldInput.SetText("%s" % (str(filter_config_template[privateShop.FILTER_TYPE_MIN_GOLD])))
		self.maxGoldInput.SetText("%s" % (str(filter_config_template[privateShop.FILTER_TYPE_MAX_GOLD])))

		self.filter_config = filter_config_template.copy()

	def OverInItem(self, slotIndex):
		if self.toolTipItem:
			self.toolTipItem.ClearToolTip()
			self.toolTipItem.SetPrivateShopSearchItem(slotIndex)
			self.toolTipItem.ShowToolTip()

	def OverOutItem(self):
		if self.toolTipItem:
			self.toolTipItem.HideToolTip()

