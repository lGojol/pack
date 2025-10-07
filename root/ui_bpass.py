import ui
import app
import grp
import net
import chat
import item
from _weakref import proxy
import nonplayer
import wndMgr
import localeInfo
import player
import mouseModule
from datetime import datetime
import ingamewikiui
import constInfo

PATH_ROOT = "d:/ymir work/ui/game/battle_pass_reworked/"
PATH_ICONS = "d:/ymir work/ui/game/battle_pass_reworked/slice/quest/icons/"

OPEN_SHOP_ID = 12
ITEM_VNUM_SKIP_MISSION = 19

TITLE_TYPES = {
	0 : localeInfo.BP_KILL_PLAYERS,
	1 : localeInfo.BP_KILL_MONSTERS,
	2 : localeInfo.BP_KILL_METINS,
	3 : localeInfo.BP_KILL_BOSSES,
	4 : localeInfo.BP_USE_ITEMS,
	5 : localeInfo.BP_COMPLETE_DUNGEONS,
	6 : localeInfo.BP_WRITE_CHAT,
	7 : localeInfo.BP_REFINE_ALCHEMY,
	8 : localeInfo.BP_COMB_ACCE,
	9 : localeInfo.BP_CATCH_FISH,
	10 : localeInfo.BP_DESTROY_ITEM,
	11 : localeInfo.BP_REWARD_YANG,
	12 : localeInfo.BP_LEVEL_UP,
	13 : localeInfo.BP_USE_EMOTICON,
	14 : localeInfo.BP_REFINE_ITEM,
	15 : localeInfo.BP_MINING,
	16 : localeInfo.BP_BUY_FROM_NPC,
	17 : localeInfo.BP_SPEND_MONEY,
	18 : localeInfo.BP_PLAY_TIME,
	19 : localeInfo.BP_MOUNT_TIME,
}

def MakeTextLineRightAlign(parent):
	textLine = ui.TextLine()
	textLine.SetParent(parent)
	textLine.SetWindowHorizontalAlignRight()
	textLine.SetWindowVerticalAlignCenter()
	textLine.SetHorizontalAlignRight()
	textLine.SetVerticalAlignCenter()
	textLine.SetPosition(3, 0)
	textLine.Show()
	return textLine

def GetNameByTypeVnum(type, vnum):
	if vnum == 0:
		return localeInfo.BP_ALL
	if type == 1 or type == 2 or type == 3:
		monster_name = localeInfo.BP_MONSTERS
		if vnum:
			monster_name = nonplayer.GetMonsterName(vnum)
		return monster_name
	elif type == 4 or type == 10:
		item_name = localeInfo.BP_ITEMS
		if vnum:
			item.SelectItem(vnum)
			item_name = item.GetItemName()
		return item_name
	return localeInfo.BP_ALL

CURRENT_LEVEL = 0

class ListBox(ui.Window):
	class NewItem(ui.Window):
		def __init__(self, category, index, title, type, vnum, count, maxCount, expRecieve, func, IsPremium, coolTime, parent):
			ui.Window.__init__(self)
			self.category = category
			self.isPremium = IsPremium
			self.index = index
			self.select = False
			self.expRecieve = expRecieve
			self.QuestionDialog = None
			self.coolTime = coolTime
	
			title = TITLE_TYPES[type]
			self.title = title
			self.type = type
			self.vnum = vnum
			self.count = count
			self.maxCount = maxCount
	
			self.Reinitialize()

			if func:
				self.OnSelectitemIndex = ui.__mem_func__(func)

			self.bg = ui.ExpandedImageBox()
			self.bg.SetParent(self)
			self.bg.AddFlag("not_pick")
			self.bg.SetPosition(0, 0)
			if not self.isPremium:
				self.bg.image = PATH_ROOT + "slice/quest/" + "quest_blue.png"
			else:
				self.bg.image = PATH_ROOT + "slice/quest/" + "quest_gold.png"
			self.bg.LoadImage(self.bg.image)
			self.bg.Show()
			
			self.SetSize(self.bg.GetWidth(), self.bg.GetHeight())		

			self.wndIcon = ui.ExpandedImageBox()
			self.wndIcon.SetParent(self)
			self.wndIcon.AddFlag("not_pick")
			self.wndIcon.SetPosition(6, 2)
			self.wndIcon.LoadImage(PATH_ICONS + "%d.png" % (type))
			self.wndIcon.Show()
		
			self.wndTextLine = ui.TextLine()
			self.wndTextLine.SetParent(self.bg)
			self.wndTextLine.SetPosition(55, 5)
			self.wndTextLine.SetText(title + " (%d)" % (self.maxCount - self.count))
			self.wndTextLine.SetPackedFontColor(0xFFC6B38D)
			self.wndTextLine.Show()
	
			self.wndTextLine2 = ui.TextLine()
			self.wndTextLine2.SetParent(self.bg)
			self.wndTextLine2.SetPosition(55, 24)
			self.wndTextLine2.SetText(localeInfo.BP_TARGET % (GetNameByTypeVnum(type, vnum)))
			self.wndTextLine2.Show()

			self.wndTextLine3 = ui.TextLine()
			self.wndTextLine3.SetParent(self.bg)
			self.wndTextLine3.SetPosition(250, 5)
			self.wndTextLine3.SetText("EXP %d" % (expRecieve))
			self.wndTextLine3.SetPackedFontColor(0xFF9F8C76)
			self.wndTextLine3.Show()

			self.wndTextLine4 = ui.TextLine()
			self.wndTextLine4.SetParent(self.bg)
			self.wndTextLine4.SetPosition(250, 5 + 17)
			if self.isPremium:
				self.wndTextLine4.SetText("PREMIUM")
			else:
				self.wndTextLine4.SetText("FREE")
			self.wndTextLine4.SetPackedFontColor(0xFF9F8C76)
			self.wndTextLine4.Show()

			self.bgGauge = ui.Window()
			self.bgGauge.SetParent(self)
			self.bgGauge.SetPosition(1, 41)
			if self.isPremium:
				self.bgGaugeFull = ui.MakeExpandedImageBox(self.bgGauge, PATH_ROOT+"slice/quest/" + "gauge_gold.png", 0, 2, "not_pick")
			else:
				self.bgGaugeFull = ui.MakeExpandedImageBox(self.bgGauge, PATH_ROOT+"slice/quest/" + "gauge_blue.png", 0, 2, "not_pick")

			self.bgGauge.SetSize(self.bgGaugeFull.GetWidth(), self.bgGaugeFull.GetHeight())
			self.bgGauge.Show()
			
			self.wndSkipMission = ui.ExpandedImageBoxButton()
			self.wndSkipMission.SetParent(self)
			self.wndSkipMission.SetPosition(350, 7)
			self.wndSkipMission.SetUpVisual(PATH_ROOT+"slice/quest/btn_0.png")
			self.wndSkipMission.SetOverVisual(PATH_ROOT+"slice/quest/btn_1.png")
			self.wndSkipMission.SetDownVisual(PATH_ROOT+"slice/quest/btn_2.png")
			self.wndSkipMission.SetEvent(ui.__mem_func__(self.OnSkipMission), "MOUSE_CLICK")
			self.wndSkipMission.SetText("Skip Mission")
			self.wndSkipMission.Show()

			self.wndTextLine5 = ui.TextLine()
			self.wndTextLine5.SetParent(self.bg)
			self.wndTextLine5.SetPosition(310, 14)
			self.wndTextLine5.SetText("")
			self.wndTextLine5.SetPackedFontColor(0xFF9F8C76)
			self.wndTextLine5.Show()

			self.UpdateGauge(count, maxCount, self.coolTime)
		
		def OnSkipMission(self):
			if self.count == self.maxCount or self.QuestionDialog:
				return
			
			item.SelectItem(ITEM_VNUM_SKIP_MISSION)
			import uiCommon
			QuestionDialog = uiCommon.QuestionDialog()
			QuestionDialog.SetText("Do you want skip this mission? for 1x %s" % (item.GetItemName()))
			QuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerQuestionSkipMission(arg))
			QuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerQuestionSkipMission(arg))
			QuestionDialog.Open()
			self.QuestionDialog = QuestionDialog
		
		def AnswerQuestionSkipMission(self, answer):
			if not self.QuestionDialog:
				return
			
			if answer:
				net.SendChatPacket("/battle_pass skip %d" % (self.index))
		
			self.QuestionDialog.Close()
			self.QuestionDialog = None

		def GetInfoItem(self):
			return (self.title, self.type, self.vnum, self.count, self.maxCount)
		
		def SetItemToolTip(self, tooltipItem):
			self.tooltipItem = tooltipItem
			
		def AppendReward(self, vnum, count):
			if vnum == 0:
				return

			item.SelectItem(vnum)
			length = len(self.dictRewards)
			newReward = ui.ExpandedImageBoxWiki()
			newReward.SetParent(self)
			newReward.LoadImage(item.GetIconImageFileName())
			newReward.SetPosition(360 + (32 * (length / 2)), 6)
			newReward.Show()
			newReward.SetStringEvent("MOUSE_OVER_IN",ui.__mem_func__(self.OverInReward), vnum)
			newReward.SetStringEvent("MOUSE_OVER_OUT",ui.__mem_func__(self.OverOutReward))
			newCount = MakeTextLineRightAlign(newReward)
			newCount.SetPosition(1, 7)
			newCount.SetText(str(count))
			newCount.SetOutline()
			newCount.SetWindowName("text")
			self.dictRewards.append(newReward)
			self.dictRewards.append(newCount)
		
		def OnRender(self):
			xList, yList = self.parent.GetGlobalPosition()
			width, height = self.parent.GetWidth(), self.parent.GetHeight()	
			listImage = [self.bg, self.wndIcon, self.wndSkipMission]
			for image in listImage:
				if image:
					self.SetClipRect(image, xList, yList, xList + width, yList + height)
			self.bgGaugeFull.SetClipRect(0.0, yList, -1.0 + float(self.percentActual) / float(self.percentTotal), yList + self.parent.GetHeight(), True)
			listText = [self.wndTextLine, self.wndTextLine2, self.wndTextLine3, self.wndTextLine4, self.wndTextLine5, self.wndSkipMission.ButtonText]
			for text in listText:
				if text:
					xText, yText = text.GetGlobalPosition()
					text.Hide() if yText < yList or yText + text.GetTextSize()[1] > yList + height else text.Show()
			if len(self.dictRewards):
				for image in self.dictRewards:
					if image.GetWindowName() == "text":
						xText, yText = image.GetGlobalPosition()
						image.Hide() if yText < yList or yText + image.GetTextSize()[1] > yList + height else image.Show()
					else:
						self.SetClipRect(image, xList, yList, xList + width, yList + height)
			if self.coolTime > 0 and self.coolTime > app.GetGlobalTimeStamp():
				leftSec = self.coolTime - app.GetGlobalTimeStamp()
				self.wndTextLine5.SetText(localeInfo.LEFT_TIME + " : " + localeInfo.SecondToDHM(leftSec))
			elif self.coolTime > 0:
				self.wndTextLine5.SetText("")
				self.coolTime = 0

		def UpdateGauge(self, actual, total, coolTime):
			if total == 0:
				total = self.maxCount
			self.wndSkipMission.Show()
			self.coolTime = coolTime
			if coolTime > 0 and coolTime > app.GetGlobalTimeStamp():
				self.wndSkipMission.Hide()
			else:
				self.wndTextLine5.SetText("")
			self.count = actual
			self.percentActual = actual
			self.percentTotal = total
			self.wndTextLine.SetText(self.title + " (%d)" % (self.maxCount - self.count))
			if self.percentActual == self.percentTotal:
				self.bgGaugeFull.LoadImage(PATH_ROOT+"slice/quest/" + "gauge_red.png")
			else:
				if self.isPremium:
					self.bgGaugeFull.LoadImage(PATH_ROOT+"slice/quest/" + "gauge_gold.png")
				else:
					self.bgGaugeFull.LoadImage(PATH_ROOT+"slice/quest/" + "gauge_blue.png")
			
		def SetClipRect(self, image, fLeft, fTop, fRight, fBottom):
			if image.GetWidth() == 0 and image.GetHeight() == 0:
				return
			(left, top, right, bottom) = image.GetRect()
			right = right + left
			bottom = bottom + top
			fDifLeft = -(float(fLeft - left) / float(image.GetWidth())) if (left < fLeft) else 0.0
			fDifTop = -(float(fTop - top) / float(image.GetHeight())) if (top < fTop) else 0.0
			fDifRight = -(float(right - fRight) / float(image.GetWidth())) if (right > fRight) else 0.0
			fDifBottom = -(float(bottom - fBottom) / float(image.GetHeight())) if (bottom > fBottom) else  0.0
			image.SetRenderingRect(fDifLeft, fDifTop, fDifRight, fDifBottom)

		def SelectImage(self):
			self.select = True

		def OverInImage(self):
			if self.select:
				return
		
		def OverOutImage(self):
			pass
	
		def SetSelect(self):
			self.select = True
	
		def OverOutForce(self):
			self.select = False
		
		def __del__(self):
			ui.Window.__del__(self)
			self.Reinitialize()
			
		def Reinitialize(self):
			self.xBase = 0
			self.yBase = 0
			self.bg = None
			self.dictRewards = []
			self.tooltipItem = None
			self.QuestionDialog = None
		
		def SetParent(self, parent):
			ui.Window.SetParent(self, parent)
			self.parent = proxy(parent)

		def SetBasePosition(self, x, y):
			self.xBase = x
			self.yBase = y
			
		def GetBasePosition(self):
			return (self.xBase, self.yBase)
			
		def OverInReward(self, vnum):
			if self.tooltipItem:
				self.tooltipItem.SetItemToolTip(vnum)
		
		def OverOutReward(self):
			if self.tooltipItem:
				self.tooltipItem.HideToolTip()
				
		def OnMouseLeftButtonDown(self):	
			self.SelectImage()

	def __init__(self):
		ui.Window.__init__(self)
		self.currentCategory = 0
		self.Reinitialize()

	def __del__(self):
		ui.Window.__del__(self)
		self.Reinitialize()
		
	def Destroy(self):
		self.Reinitialize()
		
	def Reinitialize(self):
		self.itemList = []
		self.scrollBar = None
		self.tooltipItem = None
		self.selectEvent = None

	def SetParent(self, parent):
		ui.Window.SetParent(self, parent)
		self.SetPosition(5, 5)
		self.SetSize(parent.GetWidth() - 10, parent.GetHeight() - 10)
		
	def SetScrollBar(self, scrollBar):
		scrollBar.SetScrollEvent(ui.__mem_func__(self.__OnScroll))
		scrollBar.SetScrollStep(0.2)
		self.scrollBar = scrollBar

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem
		
	def SetSelectEvent(self, event):
		self.selectEvent = event
		
	def __OnScroll(self):
		self.AdjustItemPositions(True)
			
	def GetTotalItemHeight(self):
		totalHeight = 0
		if self.itemList:
			for itemH in self.itemList:
				if itemH.IsShow() == False:
					continue
				totalHeight += itemH.GetHeight() + 2
		return totalHeight

	def GetItemCount(self):
		return len(self.itemList)
			
	def SelectItemIndex(self, index):
		for x in range(len(self.itemList)):
			itemCurrent = self.itemList[x]
			itemCurrent.OverOutForce()
			if itemCurrent.index == index:	
				itemCurrent.SetSelect()
	
	def GetInfoItem(self, index):
		mission = self.GetMission(index)
		return mission.GetInfoItem()
	
	def GetFinishedMissions(self):
		count_finished = 0
		count_need_done = 0
		if self.itemList:
			for itemH in self.itemList:
				if itemH.percentActual >= itemH.percentTotal:
					count_finished += 1
				count_need_done += 1
		return (count_finished, count_need_done)
	
	def UpdateMissionCount(self, index, count, coolTime):
		mission = self.GetMission(index)
		if mission:
			mission.UpdateGauge(count, 0, coolTime)
	
	def GetMission(self, index):
		if self.itemList:
			for itemH in self.itemList:
				if itemH.index == index:
					return itemH
		return None
	
	def AppendItemReward(self, index, vnum, count):
		mission = self.GetMission(index)
		if mission:
			mission.AppendReward(vnum, count)
	
	def AppendItem(self, category, index, title, type, vnum, count, maxCount, expRecieve, func, isPremium, coolTime):
		item = self.NewItem(category, index, title, type, vnum, count, maxCount, expRecieve, func, isPremium, coolTime, self)
		item.SetParent(self)
		item.SetItemToolTip(self.tooltipItem)
		if len(self.itemList) == 0:
			item.SetBasePosition(0, 0)
		else:
			x, y = self.itemList[-1].GetLocalPosition()
			y += 2
			item.SetBasePosition(0, y + self.itemList[-1].GetHeight())
		if item.category == self.currentCategory:
			item.Show()
		self.itemList.append(item)
		self.AdjustScrollBar()
		self.AdjustItemPositions()

	def AdjustScrollBar(self):
		totalHeight = float(self.GetTotalItemHeight())
		if totalHeight:
			scrollBarHeight = min(float(self.GetHeight() - 10) / totalHeight, 1.0)
		else:
			scrollBarHeight = 1.0
		self.scrollBar.SetMiddleBarSize(scrollBarHeight)
		if totalHeight < self.GetHeight():
			self.scrollBar.Hide()
		else:
			self.scrollBar.Show()
	
	def ResetScrollbar(self):
		self.scrollBar.SetPos(0)
	
	def RefreshList(self, category):
		self.currentCategory = category
		for item in self.itemList:
			if item.category != self.currentCategory:
				item.Hide()
			else:
				item.Show()
	
	def AdjustItemPositions(self, scrolling = False, startIndex = -1):		
		scrollPos = self.scrollBar.GetPos()
		totalHeight = self.GetTotalItemHeight() - self.GetHeight()
		idx = 0
		if startIndex >= 0:
			idx = startIndex
		yAccumulate = 0
		for item in self.itemList[idx:]:
			if item.IsShow() == False:
				continue
			if startIndex >= 0:
				yAccumulate -= item.GetHeight()
			if scrolling:
				setPos = yAccumulate - int(scrollPos * totalHeight)
				item.SetPosition(0, setPos)
			else:
				item.SetPosition(0, yAccumulate)
			item.SetBasePosition(0, yAccumulate)
			yAccumulate += item.GetHeight() + 2

	def SelectItem(self):
		if self.selectEvent:
			self.selectEvent()

	def Clear(self, bIsRefresh = False):
		if len(self.itemList) == 0:
			return
		for item in self.itemList:
			item.Reinitialize()
			item.Hide()
			del item
		if bIsRefresh == False:
			self.tooltipItem = None
		self.itemList = []

class ListBoxHorizontal(ui.Window):
	class NewItem(ui.Window):
		def __init__(self, index, vnum, count, iNecessaryLevel, status, isPremium=False):
			ui.Window.__init__(self)
			self.index = index
			self.vnum = vnum
			self.count = count
			self.iNecessaryLevel = iNecessaryLevel
			self.status = status
			self.isPremium = isPremium
			self.is_status_image_loaded = False
			
			self.Reinitialize()

			self.bg = ui.ExpandedImageBox()
			self.bg.SetParent(self)
			self.bg.AddFlag("not_pick")
			self.bg.SetPosition(0, 0)
			self.bg.LoadImage(PATH_ROOT + "slice/board_base.png")
			self.bg.Show()

			item.SelectItem(vnum)
			self.wndIcon = ui.ExpandedImageBox()
			self.wndIcon.SetParent(self)
			self.wndIcon.AddFlag("not_pick")
			self.wndIcon.LoadImage(item.GetIconImageFileName())
			self.wndIcon.SetWindowHorizontalAlignCenter()
			self.wndIcon.SetWindowVerticalAlignCenter()
			self.wndIcon.Show()

			self.wndCount = MakeTextLineRightAlign(self.wndIcon)
			self.wndCount.SetPosition(1, 7)
			self.wndCount.SetText(str(count))
			self.wndCount.SetOutline()
			self.wndCount.Show()
			
			self.wndStatus = ui.ExpandedImageBox()
			self.wndStatus.SetParent(self)
			self.wndStatus.AddFlag("not_pick")
			self.wndStatus.SetPosition(0, 0)
			self.wndStatus.SetWindowHorizontalAlignCenter()
			self.wndStatus.SetWindowVerticalAlignCenter()
			try:
				if self.isPremium:
					wnd = constInfo.GetInterfaceInstance()
					if wnd and wnd.premium_board and wnd.premium_board.IsShow():
						self.wndStatus.Hide()
						self.is_status_image_loaded = False
					else:
						if status == 0:
							self.wndStatus.LoadImage(PATH_ROOT + "slice/items/item_lock.png")
							self.is_status_image_loaded = True
							self.wndStatus.Show()
						elif status == 2:
							self.wndStatus.LoadImage(PATH_ROOT + "slice/items/item_done.png")
							self.is_status_image_loaded = True
							self.wndStatus.Show()
						else:
							self.wndStatus.Hide()
							self.is_status_image_loaded = False
				else:
					if status == 0:
						self.wndStatus.LoadImage(PATH_ROOT + "slice/items/item_lock.png")
						self.is_status_image_loaded = True
						self.wndStatus.Show()
					elif status == 2:
						self.wndStatus.LoadImage(PATH_ROOT + "slice/items/item_done.png")
						self.is_status_image_loaded = True
						self.wndStatus.Show()
					else:
						self.wndStatus.Hide()
						self.is_status_image_loaded = False
			except Exception as e:
				print("Error loading status image in __init__:", e)
				self.is_status_image_loaded = False
				self.wndStatus.Hide()

			self.wndDesignLevel = None
			self.wndDesignLevelCount = None
			self.SetSize(self.bg.GetWidth() - 1, self.bg.GetHeight())		
	
		def UpdateStatus(self, new_status):
			self.status = new_status
			try:
				if self.isPremium:
					wnd = constInfo.GetInterfaceInstance()
					if wnd and wnd.premium_board and wnd.premium_board.IsShow():
						self.wndStatus.Hide()
						self.is_status_image_loaded = False
						return
				if self.status == 0:
					self.wndStatus.LoadImage(PATH_ROOT + "slice/items/item_lock.png")
					self.is_status_image_loaded = True
					self.wndStatus.Show()
				elif self.status == 2:
					self.wndStatus.LoadImage(PATH_ROOT + "slice/items/item_done.png")
					self.is_status_image_loaded = True
					self.wndStatus.Show()
				else:
					self.wndStatus.Hide()
					self.is_status_image_loaded = False
			except Exception as e:
				print("Error updating status image:", e)
				self.is_status_image_loaded = False
				self.wndStatus.Hide()
		
		def SetItemToolTip(self, tooltipItem):
			self.tooltipItem = tooltipItem
		
		def SetDesignLevel(self):
			self.wndDesignLevel = ui.ExpandedImageBox()
			self.wndDesignLevel.SetParent(self)
			self.wndDesignLevel.AddFlag("not_pick")
			self.wndDesignLevel.LoadImage(PATH_ROOT + "slice/items/level_bar/bg_level_0.png")
			self.wndDesignLevel.SetPosition(30, -25)
			self.wndDesignLevel.Show()
			self.wndDesignLevelCount = ui.ExpandedImageBox()
			self.wndDesignLevelCount.SetParent(self.wndDesignLevel)
			self.wndDesignLevelCount.AddFlag("not_pick")
			self.wndDesignLevelCount.LoadImage(PATH_ROOT + "slice/items/level_bar/%d.png" % (self.iNecessaryLevel))
			self.wndDesignLevelCount.SetWindowHorizontalAlignCenter()
			self.wndDesignLevelCount.SetWindowVerticalAlignCenter()
			self.wndDesignLevelCount.Show()
	
		def OnRender(self):
			global CURRENT_LEVEL
			try:
				if self.isPremium:
					wnd = constInfo.GetInterfaceInstance()
					if wnd and wnd.premium_board and wnd.premium_board.IsShow():
						self.wndStatus.Hide()
						self.is_status_image_loaded = False
					else:
						if self.status == 0 and CURRENT_LEVEL < self.iNecessaryLevel:
							if not self.is_status_image_loaded:
								self.wndStatus.LoadImage(PATH_ROOT + "slice/items/item_lock.png")
								self.is_status_image_loaded = True
							self.wndStatus.Show()
						elif self.status == 2:
							if not self.is_status_image_loaded:
								self.wndStatus.LoadImage(PATH_ROOT + "slice/items/item_done.png")
								self.is_status_image_loaded = True
							self.wndStatus.Show()
						else:
							self.wndStatus.Hide()
							self.is_status_image_loaded = False
				else:
					if self.status == 0 and CURRENT_LEVEL < self.iNecessaryLevel:
						if not self.is_status_image_loaded:
							self.wndStatus.LoadImage(PATH_ROOT + "slice/items/item_lock.png")
							self.is_status_image_loaded = True
						self.wndStatus.Show()
					elif self.status == 2:
						if not self.is_status_image_loaded:
							self.wndStatus.LoadImage(PATH_ROOT + "slice/items/item_done.png")
							self.is_status_image_loaded = True
						self.wndStatus.Show()
					else:
						self.wndStatus.Hide()
						self.is_status_image_loaded = False
			except Exception as e:
				print("Error in OnRender status image:", e)
				self.is_status_image_loaded = False
				self.wndStatus.Hide()

			xList, yList = self.parent.GetGlobalPosition()
			width, height = self.parent.GetWidth(), self.parent.GetHeight()	
			listImage = [self.bg, self.wndIcon, self.wndStatus]
			for image in listImage:
				if image:
					self.SetClipRect(image, xList, yList, xList + width, yList + height)
			listText = [self.wndCount]
			for text in listText:
				if text:
					xText, yText = text.GetGlobalPosition()
					text.Hide() if yText < yList or yText + text.GetTextSize()[1] > yList + height else text.Show()
					if xText < xList+10 or xText + text.GetTextSize()[0]-10 > xList + width:
						text.Hide()
			if self.wndDesignLevel:
				self.SetClipRect(self.wndDesignLevel, xList, yList - 55, xList + width, yList - 55 + height)
				if self.wndDesignLevelCount:
					self.SetClipRect(self.wndDesignLevelCount, xList, yList - 55, xList + width, yList - 55 + height)

		def SetClipRect(self, image, fLeft, fTop, fRight, fBottom):
			if image.GetWidth() == 0 and image.GetHeight() == 0:
				return
			(left, top, right, bottom) = image.GetRect()
			right = right + left
			bottom = bottom + top
			fDifLeft = -(float(fLeft - left) / float(image.GetWidth())) if (left < fLeft) else 0.0
			fDifTop = -(float(fTop - top) / float(image.GetHeight())) if (top < fTop) else 0.0
			fDifRight = -(float(right - fRight) / float(image.GetWidth())) if (right > fRight) else 0.0
			fDifBottom = -(float(bottom - fBottom) / float(image.GetHeight())) if (bottom > fBottom) else  0.0
			image.SetRenderingRect(fDifLeft, fDifTop, fDifRight, fDifBottom)
		
		def __del__(self):
			ui.Window.__del__(self)
			self.Reinitialize()
			
		def Reinitialize(self):
			self.xBase = 0
			self.yBase = 0
			self.bg = None
			self.tooltipItem = None
			self.is_status_image_loaded = False
		
		def SetParent(self, parent):
			ui.Window.SetParent(self, parent)
			self.parent = proxy(parent)

		def SetBasePosition(self, x, y):
			self.xBase = x
			self.yBase = y
			
		def GetBasePosition(self):
			return (self.xBase, self.yBase)
			
		def OnMouseOverIn(self):
			wnd = constInfo.GetInterfaceInstance()
			if wnd == None:
				return
			if wnd.tooltipItem:
				wnd.tooltipItem.SetItemToolTip(self.vnum)
		
		def OnMouseOverOut(self):
			wnd = constInfo.GetInterfaceInstance()
			if wnd == None:
				return
			if wnd.tooltipItem:
				wnd.tooltipItem.HideToolTip()

		def OnMouseLeftButtonDown(self):
			if self.status == 1:
				wnd = constInfo.GetInterfaceInstance()
				if self.isPremium and wnd and wnd.premium_board and wnd.premium_board.IsShow():
					return
				net.SendChatPacket("/battle_pass collect %d" % self.index)
				self.UpdateStatus(2)
	
	def __init__(self):
		ui.Window.__init__(self)
		self.Reinitialize()

	def __del__(self):
		ui.Window.__del__(self)
		self.Reinitialize()
		
	def Destroy(self):
		self.Reinitialize()
		
	def Reinitialize(self):
		self.itemList = []
		self.scrollBar = None
		self.tooltipItem = None
		self.selectEvent = None

	def SetParent(self, parent):
		ui.Window.SetParent(self, parent)
		self.SetPosition(5, 5)
		self.SetSize(parent.GetWidth() - 10, parent.GetHeight() - 10)

	def SetScrollBar(self, scrollBar):
		scrollBar.SetScrollSpeed(50)
		self.scrollBar = scrollBar

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem
		
	def SetSelectEvent(self, event):
		self.selectEvent = event
			
	def GetTotalItemWidth(self):
		totalHeight = 0
		if self.itemList:
			for itemH in self.itemList:
				totalHeight += itemH.GetWidth() + 2
		return totalHeight

	def AppendItem(self, index, vnum, count, iNecessaryLevel, state, isPremium=False, setDesignlevel=False):
		item = self.NewItem(index, vnum, count, iNecessaryLevel, state, isPremium)
		item.SetParent(self)
		item.SetItemToolTip(self.tooltipItem)
		if setDesignlevel:
			item.SetDesignLevel()
		if len(self.itemList) == 0:
			item.SetBasePosition(0, 0)
		else:
			x, y = self.itemList[-1].GetLocalPosition()
			item.SetBasePosition(x + self.itemList[-1].GetWidth(), 0)
		item.Show()
		self.itemList.append(item)
		self.AdjustItemPositions()
	
	def AdjustScrollBar(self):
		totalHeight = float(self.GetTotalItemWidth())
		if totalHeight:
			scrollBarHeight = min(float(self.GetHeight() - 10) / totalHeight, 1.0)
		else:
			scrollBarHeight = 1.0
		self.scrollBar.SetMiddleBarSize(scrollBarHeight)
		if totalHeight < self.GetHeight():
			self.scrollBar.Hide()
		else:
			self.scrollBar.Show()
	
	def ResetScrollbar(self):
		self.scrollBar.SetPos(0)

	def AdjustItemPositions(self, scrolling = False, startIndex = -1):		
		scrollPos = self.scrollBar.middleBar.GetLocalPosition()[0] * 0.0032
		totalHeight = self.GetTotalItemWidth() - self.GetWidth()
		idx = 0
		if startIndex >= 0:
			idx = startIndex
		for item in self.itemList[idx:]:
			xB, yB = item.GetBasePosition()
			if startIndex >= 0:
				yB -= 2
			if scrolling:
				setPos = xB - int(scrollPos * totalHeight)
				item.SetPosition(setPos, yB)
			else:
				item.SetPosition(xB, yB)
			item.SetBasePosition(xB, yB)

	def Clear(self, bIsRefresh = False):
		if len(self.itemList) == 0:
			return
		for item in self.itemList:
			item.Reinitialize()
			item.Hide()
			del item
		if bIsRefresh == False:
			self.tooltipItem = None
		self.itemList = []

class BattlePassWindow(ui.ScriptWindow):
	def __init__(self):
		self.bLoaded = False
		self.tooltipItem = None
		self.ListBoxItem = None
		self.ListBoxItems = None
		
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()
		self.SetCenterPosition()
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.ClearDictionary()
		self.categories = []
		if self.ListBoxItem:
			self.ListBoxItem.Clear()
		self.ListBoxItem = None
		if self.ListBoxItems:
			self.ListBoxItems.Clear()
		self.ListBoxItems = None
		self.bLoadedInfo = False
		self.tooltipItem = None

	def SetItemToolTip(self, itemTooltip):
		self.tooltipItem = itemTooltip
		self.ListBoxItem.SetItemToolTip(self.tooltipItem)

	def Show(self):
		self.LoadWindow()
		self.SetTop()
		ui.ScriptWindow.Show(self)
		self.ListBoxItem.Clear()
		self.ListBoxItems.Clear()
		self.ListBoxItemsPremium.Clear()
		net.SendChatPacket("/battle_pass request")
		
	def LoadWindow(self):
		if self.bLoaded == True:
			return
		self.bLoaded = True
		self.AddFlag("movable")
		self.AddFlag("float")
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetParent(self)
		self.Board.SetSize(499, 285 + 35 + 25)
		self.Board.SetTitleName("Battle Pass")
		self.Board.SetCloseEvent(ui.__mem_func__(self.Close))
		self.Board.Show()
		self.SetSize(self.Board.GetWidth(), self.Board.GetHeight() + 32)
		self.LoadTopBoard()
		self.LoadBottomBoard()
		self.LoadItemsByExpBoard()
		self.LoadMiddleBoard()
		self.ClickCategory()
		self.RefreshCategory()
	
	def LoadTopBoard(self):
		self.boardExpInfo = ui.MakeExpandedImageBox(self, PATH_ROOT+"slice/" + "top_bg.png", 8, 30, "not_pick")
		self.bannerMonth = ui.MakeExpandedImageBox(self, PATH_ROOT+"slice/banners/" + "banner_01.png", 239, 32, "not_pick")
		self.wndLevel = ui.MakeTextLineNew(self.boardExpInfo, 30, 10, "Lv. 0")
		self.wndEXP = ui.MakeTextLineNew(self.boardExpInfo, 150, 10, "0/100 EXP")
		self.boardGaugeEXP = ui.MakeExpandedImageBox(self, PATH_ROOT+"slice/" + "gauge.png", 34, 57, "not_pick")
		self.GaugeEXP = ui.MakeExpandedImageBox(self.boardGaugeEXP, PATH_ROOT+"slice/" + "gauge_inner.png", 3, 3, "not_pick")
		self.LinegaugeEXP1 = ui.MakeExpandedImageBox(self.boardGaugeEXP, PATH_ROOT+"slice/" + "gauge_line.png", 37, 1, "not_pick")
		self.LinegaugeEXP2 = ui.MakeExpandedImageBox(self.boardGaugeEXP, PATH_ROOT+"slice/" + "gauge_line.png", 33*2, 1, "not_pick")
		self.LinegaugeEXP3 = ui.MakeExpandedImageBox(self.boardGaugeEXP, PATH_ROOT+"slice/" + "gauge_line.png", 33*3, 1, "not_pick")
		self.LinegaugeEXP4 = ui.MakeExpandedImageBox(self.boardGaugeEXP, PATH_ROOT+"slice/" + "gauge_line.png", 33*4, 1, "not_pick")
		self.wndAnimEXP = ui.AniImageBox()
		self.wndAnimEXP.SetParent(self.boardGaugeEXP)
		self.wndAnimEXP.SetPosition(0, 0)
		self.wndAnimEXP.SetDelay(3)
		self.wndAnimEXP.Show()
		self.dictImagesEXPEffect = []
		for x in range(53):
			self.wndAnimEXP.AppendImage(PATH_ROOT+"gauge effect gif/gauge_effect_%02d.png" % (x))
		
	def LoadMiddleBoard(self):
		self.board_Base = ui.BoxedBoard()
		self.board_Base.SetParent(self.Board)
		self.board_Base.SetPosition(8, 90 + 25)
		self.board_Base.SetSize(482, 218)
		self.board_Base.Show()	
		self.categories = []
		btnCategory1 = ui.MakeRadioButton(self, 8, 91, PATH_ROOT+"slice/quest/" , "btn_l_0.png", "btn_l_1.png", "btn_l_1.png")
		btnCategory1.SetText("Daily")
		btnCategory1.Down()
		self.categories.append(btnCategory1)
		btnCategory2 = ui.MakeRadioButton(self, 8 + 84, 91, PATH_ROOT+"slice/quest/" , "btn_m_0.png", "btn_m_1.png", "btn_m_1.png")
		btnCategory2.SetText("Weekly")
		self.categories.append(btnCategory2)
		btnCategory3 = ui.MakeRadioButton(self, 8 + 84 + 82, 91, PATH_ROOT+"slice/quest/" , "btn_r_0.png", "btn_r_1.png", "btn_r_1.png")
		btnCategory3.SetText("Monthly")
		self.categories.append(btnCategory3)
		for i, btnCat in enumerate(self.categories):
			btnCat.SetEvent(ui.__mem_func__(self.ClickCategoryMission), i)
		self.ScrollBarItem = ui.ScrollBarNew()
		self.ScrollBarItem.SetParent(self.board_Base)
		self.ScrollBarItem.SetScrollBarSize(self.board_Base.GetHeight() - 6)
		self.ScrollBarItem.SetPosition(self.board_Base.GetWidth() - 12, 3)
		self.ScrollBarItem.Show()
		self.ListBoxItem = ListBox()
		self.ListBoxItem.SetParent(self.board_Base)
		self.ListBoxItem.SetScrollBar(self.ScrollBarItem)
		self.ListBoxItem.SetSize(self.board_Base.GetWidth() - self.ScrollBarItem.GetWidth() - 2, self.board_Base.GetHeight() - 4)
		self.ListBoxItem.SetPosition(2, 2)
		self.ListBoxItem.Show()

	def LoadBottomBoard(self):
		self.currentCategory = 1
		self.btnCategory = ui.MakeButton(self, 2, 275+ 35 + 25, "", PATH_ROOT+"slice/" , "btns_quests.tga", "btns_quests.tga", "btns_quests.tga")
		self.btnCategory.SetEvent(ui.__mem_func__(self.ClickCategory))
		self.btnCollect = ui.MakeButton(self, 423, 275+ 35 + 25, "", PATH_ROOT+"slice/" , "btn_collect_0.png", "btn_collect_1.png", "btn_collect_2.png")
		self.btnCollect.SetEvent(ui.__mem_func__(self.ClickCollect))	
	
	def LoadItemsByExpBoard(self):
		self.board_Base_items = ui.MakeExpandedImageBox(self, PATH_ROOT+"slice/items/" + "bg_fram_norm.png", 8, 90, "not_pick")
		self.board_BaseItems = ui.BorderA()
		self.board_BaseItems.SetParent(self.board_Base_items)
		self.board_BaseItems.SetPosition(71, 17)
		self.board_BaseItems.SetSize(409, 193)
		self.board_BaseItems.Show()
		self.ScrollBarItems = ingamewikiui.WikiScrollBar(True)
		self.ScrollBarItems.SetParent(self)
		self.ScrollBarItems.SetSize(481, 12)
		self.ScrollBarItems.SetPosition(8, 300)
		self.ScrollBarItems.SetStaticScale(90)
		self.ScrollBarItems.Show()
		self.ListBoxItems = ListBoxHorizontal()
		self.ListBoxItems.SetParent(self.board_BaseItems)
		self.ListBoxItems.SetScrollBar(self.ScrollBarItems)
		self.ListBoxItems.SetSize(self.board_BaseItems.GetWidth() - 5, 100)
		self.ListBoxItems.SetPosition(3, 3)
		self.ListBoxItems.Show()
		self.ListBoxItemsPremium = ListBoxHorizontal()
		self.ListBoxItemsPremium.SetParent(self.board_BaseItems)
		self.ListBoxItemsPremium.SetScrollBar(self.ScrollBarItems)
		self.ListBoxItemsPremium.SetSize(self.board_BaseItems.GetWidth() - 5, 100)
		self.ListBoxItemsPremium.SetPosition(3, 98)
		self.ListBoxItemsPremium.Show()
		self.ScrollBarItems.SetScrollEvent(self.OnScrollPageItems)
		self.premium_board = ui.MakeExpandedImageBox(self.board_BaseItems, PATH_ROOT+"slice/items/" + "big_lock.png", 1, 100, "not_pick")
		self.btnPreviewPremium = ui.MakeButton(self.premium_board , 245, 33, "", PATH_ROOT+"slice/quest/" , "btn_0.png", "btn_1.png", "btn_2.png")
		self.btnPreviewPremium.SetEvent(ui.__mem_func__(self.ClickPreviewPremium))
		self.btnPreviewPremium.SetText(localeInfo.BP_PREVIEW_REWARD)
	
	def OnScrollPageItems(self):
		self.ListBoxItems.AdjustItemPositions(True)
		self.ListBoxItemsPremium.AdjustItemPositions(True)
	
	def ClickPreviewPremium(self):
		self.premium_board.Hide()
	
	def ClickCollect(self):
		net.SendChatPacket("/battle_pass collect")
	
	def ClickShop(self):
		net.SendChatPacket("/open_shop %d" % (OPEN_SHOP_ID))
	
	def ClickCategory(self):
		self.currentCategory = not self.currentCategory
		if self.currentCategory == 0:
			self.btnCategory.SetUpVisual(PATH_ROOT+"slice/" + "btns_items.tga")
			self.btnCategory.SetOverVisual(PATH_ROOT+"slice/" + "btns_items.tga")
			self.btnCategory.SetDownVisual(PATH_ROOT+"slice/" + "btns_items.tga")
			self.Board.SetSize(499, 285 + 35)
			self.btnCategory.SetPosition(2, 275+ 35)
			self.btnCollect.SetPosition(423, 275+ 35)
			for btnCat in self.categories:
				btnCat.Hide()
		else:
			self.btnCategory.SetUpVisual(PATH_ROOT+"slice/" + "btns_quests.tga")
			self.btnCategory.SetOverVisual(PATH_ROOT+"slice/" + "btns_quests.tga")
			self.btnCategory.SetDownVisual(PATH_ROOT+"slice/" + "btns_quests.tga")
			self.Board.SetSize(499, 285 + 35 + 25)
			self.btnCategory.SetPosition(2, 275+ 35 + 25)
			self.btnCollect.SetPosition(423, 275+ 35 + 25)
			for btnCat in self.categories:
				btnCat.Show()
		self.RefreshCategory()
	
	def Close(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True
	
	def RefreshCategory(self):
		if self.currentCategory == 1:
			self.board_Base.Show()
			self.board_Base_items.Hide()
			self.ScrollBarItems.Hide()
			self.btnCollect.Hide()
		else:
			self.board_Base_items.Show()
			self.board_Base.Hide()
			self.ScrollBarItems.Show()
			self.btnCollect.Show()
	
	def AppendMission(self, category, index, title, type, vnum, count, maxCount, expRecv, isPremium, coolTime):
		self.ListBoxItem.AppendItem(category, index, title, type, vnum, count, maxCount, expRecv, None, isPremium, coolTime)

	def AppendMissionReward(self, category, index, vnum, count):
		self.ListBoxItem.AppendItemReward(category, index, vnum, count)
		
	def UpdateMission(self, index, count, coolTime):
		self.ListBoxItem.UpdateMissionCount(index, count, coolTime)
		
	def AppendRewardItem(self, index, vnum, count, status, isPremium, iNecessaryLevel):
		if isPremium:
			self.ListBoxItemsPremium.AppendItem(index, vnum, count, iNecessaryLevel, status, isPremium=True)
		else:
			self.ListBoxItems.AppendItem(index, vnum, count, iNecessaryLevel, status, isPremium=False, setDesignlevel=True)

	def SetExperience(self, exp, maxExp):
		self.wndEXP.SetText("%d/%d EXP" % (exp, maxExp))
		if maxExp == 0:
			maxExp = 1
		self.GaugeEXP.SetPercentage(exp, maxExp)
	
	def SetLevel(self, currentLevel):
		self.wndLevel.SetText("Lv. %d" % (currentLevel))
		global CURRENT_LEVEL
		CURRENT_LEVEL = currentLevel
	
	def UnlockPremium(self):
		self.premium_board.Hide()
	
	def ClearBattlePass(self):
		self.ListBoxItem.Clear()
		self.ListBoxItems.Clear()
		self.ListBoxItemsPremium.Clear()

	def OnMouseWheel(self, nLen):
		if nLen > 0:
			self.ScrollBarItem.OnUp()
		else:
			self.ScrollBarItem.OnDown()
	
	def ClickCategoryMission(self, index):
		self.selectedCategoryMission = index
		for i, btnCat in enumerate(self.categories):
			if index == i:
				btnCat.Down()
			else:
				btnCat.SetUp()		
		self.ListBoxItem.RefreshList(self.selectedCategoryMission)
		self.ListBoxItem.ResetScrollbar()
		self.ListBoxItem.AdjustScrollBar()
		self.ListBoxItem.AdjustItemPositions()