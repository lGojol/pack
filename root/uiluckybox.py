#blackdragonx61 / Mali
import uiCommon
import player
import ui
import localeInfo
import wndMgr

class LuckyBoxWindow(ui.ScriptWindow):
    def __init__(self):
        ui.ScriptWindow.__init__(self)

        self.isLoaded = 0
        self.questionDialog = None
        self.tooltipitem = None
        self.vnum = 0
        self.max_pos_x = wndMgr.GetScreenWidth() - 240
        self.max_pos_y = wndMgr.GetScreenHeight() - 180

        self.__LoadWindow()

    def __del__(self):
        ui.ScriptWindow.__del__(self)

    def Destroy(self):
        self.ClearDictionary()
        self.questionDialog = None
        self.tooltipitem = None
        self.TitleBar = None
        self.RewardItemSlot = None
        self.RetryButton = None
        self.RecvButton = None
        self.NeedMoneySlot = None
        self.NeedMoney = None
    
    def Close(self):
        self.Hide()

    def OnRecv(self):
        self.questionDialog = uiCommon.QuestionDialog()
        self.questionDialog.SetText(localeInfo.LUCKY_BOX_DIALOG_RECV_TEXT)
        self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.__popUpDialogAccept))
        self.questionDialog.SetCancelEvent(ui.__mem_func__(self.__popUpDialogCancel))
        self.questionDialog.type = player.LUCKY_BOX_ACTION_RECEIVE
        self.questionDialog.Open()

    def OnRetry(self):
        self.questionDialog = uiCommon.QuestionDialog()
        self.questionDialog.SetText(localeInfo.LUCKY_BOX_DIALOG_RETRY_TEXT)
        self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.__popUpDialogAccept))
        self.questionDialog.SetCancelEvent(ui.__mem_func__(self.__popUpDialogCancel))
        self.questionDialog.type = player.LUCKY_BOX_ACTION_RETRY
        self.questionDialog.Open()

    def OverInItem(self, slotNumber):
        if self.tooltipitem:
            self.tooltipitem.ClearToolTip()
            metinSlot = []
            for i in xrange(player.METIN_SOCKET_MAX_NUM):
                metinSlot.append(0)
            attrSlot = []
            for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
                attrSlot.append((0, 0))

            self.tooltipitem.AddItemData(self.vnum, metinSlot, attrSlot)

    def OverOutItem(self):
        if self.tooltipitem:
            self.tooltipitem.HideToolTip()

    def SetItemToolTip(self, tooltip):
        self.tooltipitem = tooltip

    def ShowLuckyBoxWindow(self, dwItemVnum, byItemCount, iNeedMoney):
        self.vnum = dwItemVnum
        self.RewardItemSlot.SetItemSlot(0, dwItemVnum, byItemCount)
        self.NeedMoney.SetText(localeInfo.NumberToMoneyString(iNeedMoney))
        self.SetTop()
        self.Show()

    def __LoadWindow(self):
        if self.isLoaded == 1:
            return

        self.isLoaded = 1
        
        try:
            pyScrLoader = ui.PythonScriptLoader()
            pyScrLoader.LoadScriptFile(self, "UIScript/LuckyBoxWindow.py")
        except:
            import exception
            exception.Abort("LuckyBoxWindow.__LoadWindow.LoadScript")

        try:
            self.TitleBar = self.GetChild("LuckyBox_TitleBar")
            self.TitleBar.CloseButtonHide()
    
            self.RewardItemSlot = self.GetChild("RewardItemSlot")
            self.RetryButton = self.GetChild("RetryButton")
            self.RecvButton = self.GetChild("RecvButton")
            self.NeedMoneySlot = self.GetChild("NeedMoneySlot")
            self.NeedMoneySlot.SetButtonScale(1.9, 1.0)
            self.NeedMoney = self.GetChild("NeedMoney")

            self.RewardItemSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
            self.RewardItemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

            self.RetryButton.SetEvent(ui.__mem_func__(self.OnRetry))
            self.RecvButton.SetEvent(ui.__mem_func__(self.OnRecv))

        except:
            import exception
            exception.Abort("LuckyBoxWindow.__LoadWindow.BindObject")

    def __popUpDialogAccept(self):
        if self.questionDialog:
            player.SendLuckyBoxAction(self.questionDialog.type)
            
            if self.questionDialog.type == player.LUCKY_BOX_ACTION_RECEIVE:
                self.Close()

            self.__popUpDialogCancel()

    def __popUpDialogCancel(self):
        if self.questionDialog:
            self.questionDialog.Close()
            self.questionDialog = None

    def OnPressEscapeKey(self):
        return TRUE

    def MINMAX(self, min, value, max):    
        if value < min:
            return min
        elif value > max:
            return max
        else:
            return value
   
    def OnUpdate(self):
        x, y = self.GetGlobalPosition()
        
        pos_x = self.MINMAX(0, x, self.max_pos_x)
        pos_y = self.MINMAX(0, y, self.max_pos_y)
        
        self.SetPosition(pos_x, pos_y)