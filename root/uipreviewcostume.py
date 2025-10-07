import app
import ui
import nonplayer
import localeInfo
import wndMgr
import chat
import chr
import item
import player
import re
import ime
import grp
import uiToolTip
import renderTarget
import uiScriptLocale

class Config:
	BOARD = [713, 488]
	BOARD_WINDOW = [480, 430]
	BOARD_PREVIEW = [350, 436]
	
	RENDER_INDEX = 23
	IMAGE = "d:/ymir work/ui/dnc/PreviewCostume/"
	BUTTON_PATH = "d:/ymir work/ui/render_target/"

	COSTUME = {
		0: localeInfo.PREVIEW_SYSTEM_COSTUME,
		1: localeInfo.PREVIEW_SYSTEM_HAIR,
		2: localeInfo.PREVIEW_SYSTEM_WEAPON_SKIN,
		3: localeInfo.PREVIEW_SYSTEM_MOUNT,
		4: localeInfo.PREVIEW_SYSTEM_PET,
		6: localeInfo.PREVIEW_SYSTEM_ACCE,
		7: localeInfo.PREVIEW_SYSTEM_AURA,
	}

	MOUNT_VNUM_MAP = {
		52001: 20201, 52002: 20201, 52003: 20201, 52004: 20201, 52005: 20201,
		52006: 20205, 52007: 20205, 52008: 20205, 52009: 20205, 52010: 20205,
		52011: 20209, 52012: 20209, 52013: 20209, 52014: 20209, 52015: 20209,
		52016: 20202, 52017: 20202, 52018: 20202, 52019: 20202, 52020: 20202,
		52021: 20206, 52022: 20206, 52023: 20206, 52024: 20206, 52025: 20206,
		52026: 20210, 52027: 20210, 52028: 20210, 52029: 20210, 52030: 20210,
		52031: 20204, 52032: 20204, 52033: 20204, 52034: 20204, 52035: 20204,
		52036: 20208, 52037: 20208, 52038: 20208, 52039: 20208, 52040: 20208,
		52041: 20212, 52042: 20212, 52043: 20212, 52044: 20212, 52045: 20212,
		52046: 20203, 52047: 20203, 52048: 20203, 52049: 20203, 52050: 20203,
		52051: 20207, 52052: 20207, 52053: 20207, 52054: 20207, 52055: 20207,
		52056: 20211, 52057: 20211, 52058: 20211, 52059: 20211, 52060: 20211,
		52061: 20213, 52062: 20213, 52063: 20213, 52064: 20213, 52065: 20213,
		52066: 20214, 52067: 20214, 52068: 20214, 52069: 20214, 52070: 20214,
		52071: 20215, 52072: 20215, 52073: 20215, 52074: 20215, 52075: 20215,
		52076: 20216, 52077: 20216, 52078: 20216, 52079: 20216, 52080: 20216,
		52081: 20217, 52082: 20217, 52083: 20217, 52084: 20217, 52085: 20217,
		52086: 20218, 52087: 20218, 52088: 20218, 52089: 20218, 52090: 20218,
		52091: 20223, 52092: 20223, 52093: 20223, 52094: 20223, 52095: 20223,
		52096: 20224, 52097: 20224, 52098: 20224, 52099: 20224, 52100: 20224,
		52101: 20225, 52102: 20225, 52103: 20225, 52104: 20225, 52105: 20225,
		52106: 20228, 52107: 20228, 52108: 20228, 52109: 20228, 52110: 20228,
		52111: 20229, 52112: 20229, 52113: 20229, 52114: 20229, 52115: 20229,
		52116: 20230, 52117: 20230, 52118: 20230, 52119: 20230, 52120: 20230,
		56000: 20253, 70614: 20288, 71115: 20110, 71117: 20111, 71119: 20112,
		71121: 20113, 71124: 20114, 71125: 20115, 71126: 20116, 71127: 20117,
		71128: 20118, 71131: 20119, 71132: 20119, 71133: 20119, 71134: 20119,
		71137: 20120, 71138: 20121, 71139: 20122, 71140: 20123, 71141: 20124,
		71142: 20125, 71161: 20219, 71164: 20220, 71165: 20221, 71166: 20222,
		71171: 20227, 71172: 20226, 71176: 20231, 71177: 20232, 71182: 20233,
		71183: 20234, 71184: 20235, 71185: 20236, 71186: 20237, 71187: 20238,
		71192: 20239, 71193: 20240, 71197: 20241, 71198: 20242, 71220: 20243,
		71222: 20244, 71223: 20245, 71224: 20246, 71225: 20247, 71226: 20248,
		71227: 20249, 71228: 20250, 71229: 20251, 71230: 20252, 71231: 20254,
		71232: 20255, 71233: 20257, 71234: 20258, 71235: 20259, 71236: 20260,
		71237: 20110, 71238: 20111, 71239: 20112, 71240: 20113, 71241: 20030,
		71242: 20261, 71243: 20262, 71244: 20263, 71245: 20264, 71246: 20265,
		71247: 20266, 71248: 20267, 71249: 20268, 71250: 20269, 71251: 20270,
		71252: 20271, 71253: 20272, 71254: 20273, 71255: 20274, 71256: 20275,
		71257: 20275, 71258: 20275, 71259: 20276, 71260: 20277, 71261: 20278,
		71262: 20279, 71263: 20280, 71264: 20281, 71265: 20282, 71266: 20283,
		71267: 20284, 71268: 20285, 71269: 20286, 71270: 20287, 71271: 20289,
		71272: 20290, 71273: 20291, 71274: 20292, 71275: 20293, 71276: 20294,
		71277: 20295, 71278: 20296, 71280: 36000, 71281: 36001, 71282: 20298,
		71283: 20299, 71287: 36005, 71288: 36006, 91056: 20250, 91057: 20246,
		91058: 20252, 52202: 40003, 52204: 40004, 52205: 40005

	}

	PET_VNUM_MAP = {
		53001: 34001, 53002: 34002, 53003: 34003, 53005: 34004, 53006: 34009,
		53007: 34010, 53008: 34011, 53009: 34012, 53010: 34008, 53011: 34007,
		53012: 34005, 53013: 34006, 53014: 34013, 53015: 34014, 53016: 34015,
		53017: 34016, 53018: 34020, 53019: 34019, 53020: 34017, 53021: 34018,
		53022: 34021, 53023: 34022, 53024: 34023, 53025: 34024, 53026: 34001,
		53218: 34023, 53219: 34023, 53220: 34024, 53221: 34024, 53222: 34026,
		53223: 34027, 53224: 34028, 53225: 34029, 53226: 34030, 53227: 34031,
		53228: 34033, 53229: 34032, 53230: 34034, 53231: 34035, 53232: 34039,
		53233: 34055, 53234: 34056, 53235: 34057, 53236: 34058, 53237: 34059,
		53238: 34060, 53239: 34061, 53240: 34063, 53241: 34062, 53242: 34122,
		53243: 34123, 53244: 34067, 53245: 34068, 53246: 34069, 53247: 34070,
		53248: 34071, 53249: 34072, 53250: 34084, 53251: 34085, 53253: 34086,
		53254: 34087, 53255: 34088, 53256: 34066, 53257: 34089, 53258: 34090,
		53259: 34091, 53260: 34092, 53261: 34093, 53262: 34094, 53263: 34095,
		53264: 34096, 53265: 34097, 53266: 34098, 53267: 34099, 53268: 34100,
		53269: 34101, 53270: 34102, 53271: 34103, 53272: 34104, 53273: 34105,
		53274: 34106, 53275: 34107, 53276: 34108, 53277: 34109, 53278: 34110,
		53279: 34111, 53280: 34112, 53281: 34113, 53282: 34114, 53283: 34115,
		53284: 34116, 53285: 34117, 53286: 34118, 53287: 34119, 53288: 34120,
		53289: 34121, 53290: 34124, 53291: 34125, 53292: 34126, 53293: 34127,
		53294: 34128, 53295: 34129, 53296: 34130, 53297: 34131, 53298: 34130,
		53299: 34133, 53300: 34134, 53301: 34135, 53302: 34136, 53303: 34137,
		53304: 34138, 53305: 34139, 53306: 34140, 53307: 34141, 53308: 34142,
		53309: 34143, 53311: 34145, 53312: 34146, 53313: 34147, 53314: 34148,
		53315: 34149, 53316: 34150, 53317: 34151, 53318: 34152, 53319: 34038,
		53320: 34153, 53321: 34154, 53322: 34155, 53323: 34156, 53324: 34157,
		53325: 34158, 53326: 34159, 53327: 34160, 53328: 34161, 53329: 34162,
		53330: 34163, 53331: 34164, 53332: 34167, 53333: 34168, 53334: 34169,
		53335: 34170, 53336: 34171, 53337: 34172, 53338: 34173, 53339: 34174,
		53340: 34175, 53341: 34176, 53342: 34177, 53343: 34177, 53345: 34180,
		53346: 34181, 53347: 34182, 53348: 34183, 53349: 34184, 53350: 34185,
		53351: 34186, 53352: 34187, 53353: 34188, 53354: 34189, 53355: 34190,
		53356: 34191, 53357: 34192, 53358: 34193, 53359: 34194, 53360: 34195,
		53362: 34197, 53363: 34198, 53364: 34199, 53365: 34200, 53366: 34201,
		53367: 34202, 53368: 34203, 53369: 34204, 53372: 34207, 53373: 34208,
		53374: 34209
	}

	# BLACK_ITEM para excluir ítems del sistema (no se muestran en listas, búsquedas, ni iconos)
	BLACK_ITEM = {
		#49036: True,  # Excluir el ítem 49036 completamente
	}

def get_all_preview_items(category_index, race, gender):
	category_map = {
		0: [(item.ITEM_TYPE_COSTUME, item.COSTUME_TYPE_BODY)],
		1: [(item.ITEM_TYPE_COSTUME, item.COSTUME_TYPE_HAIR)],
		2: [(item.ITEM_TYPE_COSTUME, item.COSTUME_TYPE_WEAPON)],
		3: [],  # Monturas (usar MOUNT_VNUM_MAP)
		4: [],  # Mascotas (usar PET_VNUM_MAP)
		6: [(item.ITEM_TYPE_COSTUME, item.COSTUME_TYPE_ACCE)],
		7: [(item.ITEM_TYPE_COSTUME, item.COSTUME_TYPE_AURA)],
	}

	valid_items = []
	ANTI_FLAG_DICT = {
		0: item.ITEM_ANTIFLAG_WARRIOR,
		1: item.ITEM_ANTIFLAG_ASSASSIN,
		2: item.ITEM_ANTIFLAG_SURA,
		3: item.ITEM_ANTIFLAG_SHAMAN,
	}

	characterInfoDict = {
		0: {0: player.MAIN_RACE_WARRIOR_M, 1: player.MAIN_RACE_WARRIOR_W},
		1: {0: player.MAIN_RACE_ASSASSIN_M, 1: player.MAIN_RACE_ASSASSIN_W},
		2: {0: player.MAIN_RACE_SURA_M, 1: player.MAIN_RACE_SURA_W},
		3: {0: player.MAIN_RACE_SHAMAN_M, 1: player.MAIN_RACE_SHAMAN_W},
	}

	def is_allowed(vnum, class_idx, sex):
		if vnum in Config.BLACK_ITEM:
			return False
		try:
			item.SelectItem(vnum)
			if item.IsAntiFlag(ANTI_FLAG_DICT.get(class_idx, 0)):
				return False
			if sex == 0 and item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE):
				return False
			if sex == 1 and item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE):
				return False
			return True
		except:
			return False

	if category_index == 3:
		valid_items = [vnum for vnum in Config.MOUNT_VNUM_MAP.keys() if vnum not in Config.BLACK_ITEM]
	elif category_index == 4:
		valid_items = [vnum for vnum in Config.PET_VNUM_MAP.keys() if vnum not in Config.BLACK_ITEM]
	else:
		for vnum in range(1, 100001):
			if vnum in Config.BLACK_ITEM:
				continue
			try:
				item.SelectItem(vnum)
				item_type = item.GetItemType()
				item_subtype = item.GetItemSubType()

				for type_subtype in category_map.get(category_index, []):
					expected_type, expected_subtype = type_subtype
					if item_type == expected_type and item_subtype == expected_subtype:
						item_valid = False
						for cls in range(4):
							for sex in (0, 1):
								if is_allowed(vnum, cls, sex):
									item_valid = True
									break
							if item_valid:
								break
						if item_valid:
							valid_items.append(vnum)
						break
			except:
				continue

	return valid_items

def get_all_inventory_items(race, gender):
	valid_items = []
	category_map = {
		0: [(item.ITEM_TYPE_COSTUME, item.COSTUME_TYPE_BODY)],
		1: [(item.ITEM_TYPE_COSTUME, item.COSTUME_TYPE_HAIR)],
		2: [(item.ITEM_TYPE_COSTUME, item.COSTUME_TYPE_WEAPON)],
		6: [(item.ITEM_TYPE_COSTUME, item.COSTUME_TYPE_ACCE)],
		7: [(item.ITEM_TYPE_COSTUME, item.COSTUME_TYPE_AURA)],
	}

	ANTI_FLAG_DICT = {
		0: item.ITEM_ANTIFLAG_WARRIOR,
		1: item.ITEM_ANTIFLAG_ASSASSIN,
		2: item.ITEM_ANTIFLAG_SURA,
		3: item.ITEM_ANTIFLAG_SHAMAN,
	}

	characterInfoDict = {
		0: {0: player.MAIN_RACE_WARRIOR_M, 1: player.MAIN_RACE_WARRIOR_W},
		1: {0: player.MAIN_RACE_ASSASSIN_M, 1: player.MAIN_RACE_ASSASSIN_W},
		2: {0: player.MAIN_RACE_SURA_M, 1: player.MAIN_RACE_SURA_W},
		3: {0: player.MAIN_RACE_SHAMAN_M, 1: player.MAIN_RACE_SHAMAN_W},
	}

	reverse_race_map = {(class_idx, sex): race_val for class_idx, sexes in characterInfoDict.items() for sex, race_val in sexes.items()}
	if race in [race_val for sexes in characterInfoDict.values() for race_val in sexes.values()]:
		for (class_idx, sex), race_val in reverse_race_map.items():
			if race_val == race:
				break
	else:
		class_idx, sex = 0, gender

	def is_allowed(vnum, class_idx, sex):
		if vnum in Config.BLACK_ITEM:
			return False
		try:
			item.SelectItem(vnum)
			if item.IsAntiFlag(ANTI_FLAG_DICT.get(class_idx, 0)):
				return False
			if sex == 0 and item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE):
				return False
			if sex == 1 and item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE):
				return False
			return True
		except:
			return False

	from uiinventory import InventoryWindow
	inventory_window = InventoryWindow()
	mycostume = inventory_window.GetAllCostumeItems()

	for vnum in mycostume:
		if vnum in Config.BLACK_ITEM:
			continue
		try:
			item.SelectItem(vnum)
			item_type = item.GetItemType()
			item_subtype = item.GetItemSubType()

			item_valid = False
			for category_index in category_map:
				for type_subtype in category_map.get(category_index, []):
					expected_type, expected_subtype = type_subtype
					if item_type == expected_type and item_subtype == expected_subtype:
						if is_allowed(vnum, class_idx, sex):
							item_valid = True
							valid_items.append((vnum, category_index))
						break
				if item_valid:
					break
			if vnum in Config.MOUNT_VNUM_MAP and vnum not in Config.BLACK_ITEM:
				valid_items.append((vnum, 3))
			elif vnum in Config.PET_VNUM_MAP and vnum not in Config.BLACK_ITEM:
				valid_items.append((vnum, 4))
		except:
			continue

	return valid_items

class Preview(ui.Board):
	def __init__(self):
		ui.Board.__init__(self)
		self.children = {}
		self.SetSize(*Config.BOARD_PREVIEW)
		self.current_race_index = 0
		self.current_gender_index = 0
		self.previewZoom = False
		self.previewTools = False
		self.current_item_vnum = 0
		self.current_category = -1
		self.race_list = []
		self.last_switch_time = 0
		self.Destroy()
		self.LoadWindow()

	def __del__(self):
		ui.Board.__del__(self)

	def LoadWindow(self):
		titleBar = ui.TitleBar()
		titleBar.SetParent(self)
		titleBar.SetPosition(8, 10)
		titleBar.MakeTitleBar(self.GetWidth() - 15, "red")
		titleBar.CloseButtonHide()
		titleBar.Show()
		self.children["titleBar"] = titleBar

		self.ModelPreview = ui.RenderTarget()
		self.ModelPreview.SetParent(self)
		self.ModelPreview.SetPosition(8, 30)
		self.ModelPreview.SetSize(self.GetWidth() - 16, self.GetHeight() - 70)
		self.ModelPreview.SetRenderTarget(Config.RENDER_INDEX)
		self.ModelPreview.Show()
		self.children["ModelPreview"] = self.ModelPreview

		self.raceButtons = []
		race_names = ["warrior", "ninja", "sura", "shaman"]
		race_y_pos = self.ModelPreview.GetHeight() - 36
		for i, race in enumerate(race_names):
			raceButton = ui.Button()
			raceButton.SetParent(self.ModelPreview)
			raceButton.SetPosition(10 + i * 36, race_y_pos)
			raceButton.SetUpVisual(Config.BUTTON_PATH + race + "_normal.tga")
			raceButton.SetOverVisual(Config.BUTTON_PATH + race + "_hover.tga")
			raceButton.SetDownVisual(Config.BUTTON_PATH + race + "_hover.tga")
			raceButton.SetEvent(lambda idx=i: self.SelectRace(idx))
			#raceButton.SetToolTipText(localeInfo.PREVIEW_SYSTEM_RACE[i], 0, -20)
			raceButton.Hide()
			self.raceButtons.append(raceButton)
			self.children["raceButton_" + str(i)] = raceButton

		self.genderButtons = []
		gender_y_pos = race_y_pos - 24
		for i, gender in enumerate(["female", "male"]):
			genderButton = ui.Button()
			genderButton.SetParent(self.ModelPreview)
			genderButton.SetPosition(10 + i * 36, gender_y_pos)
			genderButton.SetUpVisual(Config.BUTTON_PATH + gender + "_normal.tga")
			genderButton.SetOverVisual(Config.BUTTON_PATH + gender + "_hover.tga")
			genderButton.SetDownVisual(Config.BUTTON_PATH + gender + "_hover.tga")
			genderButton.SetEvent(lambda idx=i: self.SelectGender(idx))
			genderButton.Hide()
			self.genderButtons.append(genderButton)
			self.children["genderButton_" + str(i)] = genderButton

		self.zoomOutButton = ui.ToggleButton()
		self.zoomOutButton.SetParent(self.ModelPreview)
		self.zoomOutButton.SetPosition(self.ModelPreview.GetWidth() - 18, self.ModelPreview.GetHeight() - 18)
		self.zoomOutButton.SetUpVisual("d:/ymir work/ui/game/monster_card/button/zoomin/zoomin_rotation_button_default.sub")
		self.zoomOutButton.SetOverVisual("d:/ymir work/ui/game/monster_card/button/zoomin/zoomin_rotation_button_over.sub")
		self.zoomOutButton.SetDownVisual("d:/ymir work/ui/game/monster_card/button/zoomin/zoomin_rotation_button_down.sub")
		self.zoomOutButton.SetToggleUpEvent(ui.__mem_func__(self.OnZoomOut), False)
		self.zoomOutButton.SetToggleDownEvent(ui.__mem_func__(self.OnZoomOut), True)
		self.zoomOutButton.SetToolTipText(uiScriptLocale.DUNGEON_INFO_PREVIEW_ZOOM_IN, 0, -20)
		self.zoomOutButton.Show()
		self.children["zoomOutButton"] = self.zoomOutButton

		self.zoomInButton = ui.ToggleButton()
		self.zoomInButton.SetParent(self.ModelPreview)
		self.zoomInButton.SetPosition(self.ModelPreview.GetWidth() - 36, self.ModelPreview.GetHeight() - 18)
		self.zoomInButton.SetUpVisual("d:/ymir work/ui/game/monster_card/button/zoomout/zoomin_rotation_button_default.sub")
		self.zoomInButton.SetOverVisual("d:/ymir work/ui/game/monster_card/button/zoomout/zoomin_rotation_button_over.sub")
		self.zoomInButton.SetDownVisual("d:/ymir work/ui/game/monster_card/button/zoomout/zoomin_rotation_button_down.sub")
		self.zoomInButton.SetToggleUpEvent(ui.__mem_func__(self.OnZoomIn), False)
		self.zoomInButton.SetToggleDownEvent(ui.__mem_func__(self.OnZoomIn), True)
		self.zoomInButton.SetToolTipText(uiScriptLocale.DUNGEON_INFO_PREVIEW_ZOOM_OUT, 0, -20)
		self.zoomInButton.Show()
		self.children["zoomInButton"] = self.zoomInButton

		renderTarget.SetBackground(Config.RENDER_INDEX, "d:/ymir work/ui/game/battle_pass/preview_back.tga")
		renderTarget.SetVisibility(Config.RENDER_INDEX, False)

	def OnZoomIn(self, trigger):
		if trigger:
			self.previewTools = True
			self.previewZoom = False
			self.zoomInButton.Down()
			self.zoomOutButton.SetUp()
			renderTarget.SetZoom(Config.RENDER_INDEX, self.previewZoom)
		else:
			self.previewTools = False
			self.zoomInButton.SetUp()

	def OnZoomOut(self, trigger):
		if trigger:
			self.previewTools = True
			self.previewZoom = True
			self.zoomOutButton.Down()
			self.zoomInButton.SetUp()
			renderTarget.SetZoom(Config.RENDER_INDEX, self.previewZoom)
		else:
			self.previewTools = False
			self.zoomOutButton.SetUp()

	def CenterModel(self, renderIndex):
		renderTarget.SetModelPosition(renderIndex, 0.0, 0.0, 0.0)
		renderTarget.SetModelRotation(renderIndex, 0.0)
		renderTarget.SetModelScale(renderIndex, 1.0)

	def GetValidRaces(self, itemVnum):
		if not isinstance(itemVnum, int) or itemVnum <= 0 or itemVnum in Config.BLACK_ITEM:
			return [player.MAIN_RACE_WARRIOR_M]

		try:
			item.SelectItem(itemVnum)
		except:
			return [player.MAIN_RACE_WARRIOR_M]

		ANTI_FLAG_DICT = {
			0: item.ITEM_ANTIFLAG_WARRIOR,
			1: item.ITEM_ANTIFLAG_ASSASSIN,
			2: item.ITEM_ANTIFLAG_SURA,
			3: item.ITEM_ANTIFLAG_SHAMAN,
		}

		characterInfoDict = {
			0: {0: player.MAIN_RACE_WARRIOR_M, 1: player.MAIN_RACE_WARRIOR_W},
			1: {0: player.MAIN_RACE_ASSASSIN_M, 1: player.MAIN_RACE_ASSASSIN_W},
			2: {0: player.MAIN_RACE_SURA_M, 1: player.MAIN_RACE_SURA_W},
			3: {0: player.MAIN_RACE_SHAMAN_M, 1: player.MAIN_RACE_SHAMAN_W},
		}

		valid_races = []
		for cls in range(4):
			for sex in (0, 1):
				if self.current_category in (2, 6, 7) and sex != self.current_gender_index:
					continue
				race = characterInfoDict[cls].get(sex, -1)
				if race == -1:
					continue
				if not item.IsAntiFlag(ANTI_FLAG_DICT.get(cls, 0)) and \
				   not (sex == 0 and item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE)) and \
				   not (sex == 1 and item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE)):
					valid_races.append(race)

		return valid_races if valid_races else [player.MAIN_RACE_WARRIOR_M]

	def SelectRace(self, index):
		if index >= len(self.race_list):
			return
		self.current_race_index = index
		for i, btn in enumerate(self.raceButtons):
			if i == index:
				btn.Down()
			else:
				btn.SetUp()
		self.RenderModel(self.race_list[self.current_race_index], self.current_item_vnum, self.current_category)
		self.last_switch_time = app.GetGlobalTimeStamp()

	def SelectGender(self, index):
		self.current_gender_index = index
		for i, btn in enumerate(self.genderButtons):
			if i == index:
				btn.Down()
			else:
				btn.SetUp()
		self.race_list = self.GetValidRaces(self.current_item_vnum)
		self.current_race_index = 0
		if self.race_list:
			self.RenderModel(self.race_list[self.current_race_index], self.current_item_vnum, self.current_category)
		self.last_switch_time = app.GetGlobalTimeStamp()

	def UpdateButtonVisibility(self):
		show_race = self.current_category in (0, 1, 2, 6, 7)
		show_gender = self.current_category in (2, 6, 7)

		valid_races = self.GetValidRaces(self.current_item_vnum) if self.current_item_vnum else []
		race_map = {
			player.MAIN_RACE_WARRIOR_M: 0, player.MAIN_RACE_WARRIOR_W: 0,
			player.MAIN_RACE_ASSASSIN_M: 1, player.MAIN_RACE_ASSASSIN_W: 1,
			player.MAIN_RACE_SURA_M: 2, player.MAIN_RACE_SURA_W: 2,
			player.MAIN_RACE_SHAMAN_M: 3, player.MAIN_RACE_SHAMAN_W: 3,
		}

		for i, raceButton in enumerate(self.raceButtons):
			if show_race and any(race in valid_races and race_map.get(race, -1) == i for race in valid_races):
				raceButton.Show()
			else:
				raceButton.Hide()

		for genderButton in self.genderButtons:
			if show_gender:
				genderButton.Show()
			else:
				genderButton.Hide()

	def RenderModel(self, raceIndex, itemVnum, categoryIndex):
		renderIndex = Config.RENDER_INDEX
		if not isinstance(itemVnum, int) or itemVnum <= 0 or itemVnum in Config.BLACK_ITEM:
			return

		renderTarget.SetVisibility(renderIndex, False)
		renderTarget.ClearModel(renderIndex)
		if categoryIndex == 3:
			model_idx = Config.MOUNT_VNUM_MAP.get(itemVnum, 0)
			if model_idx > 0:
				renderTarget.SelectModel(renderIndex, model_idx)
				renderTarget.SetModelPosition(renderIndex, 0.0, -150.0, 0.0)
				renderTarget.SetModelRotation(renderIndex, 45.0)
				renderTarget.SetModelScale(renderIndex, 0.8)
		elif categoryIndex == 4:
			model_idx = Config.PET_VNUM_MAP.get(itemVnum, 0)
			if model_idx > 0:
				renderTarget.SelectModel(renderIndex, model_idx)
				renderTarget.SetModelPosition(renderIndex, 0.0, -150.0, 0.0)
				renderTarget.SetModelRotation(renderIndex, 45.0)
				renderTarget.SetModelScale(renderIndex, 0.8)
		else:
			try:
				item.SelectItem(itemVnum)
				item_type = item.GetItemType()
				item_subtype = item.GetItemSubType()
				valid_categories = {
					0: (item.ITEM_TYPE_COSTUME, item.COSTUME_TYPE_BODY),
					1: (item.ITEM_TYPE_COSTUME, item.COSTUME_TYPE_HAIR),
					2: (item.ITEM_TYPE_COSTUME, item.COSTUME_TYPE_WEAPON),
					6: (item.ITEM_TYPE_COSTUME, item.COSTUME_TYPE_ACCE),
					7: (item.ITEM_TYPE_COSTUME, item.COSTUME_TYPE_AURA),
				}
				expected_type, expected_subtype = valid_categories.get(categoryIndex, (None, None))
				if item_type == expected_type and item_subtype == expected_subtype:
					renderTarget.SelectItem(renderIndex, raceIndex, itemVnum, categoryIndex)
					self.CenterModel(renderIndex)
			except:
				pass
		renderTarget.SetVisibility(renderIndex, True)
		if self.previewTools:
			renderTarget.SetZoom(renderIndex, self.previewZoom)

	def SetItemToModelPreview(self, itemVnum, categoryIndex):
		if itemVnum in Config.BLACK_ITEM:
			return
		self.current_item_vnum = itemVnum
		self.current_category = categoryIndex
		self.race_list = self.GetValidRaces(itemVnum) if categoryIndex not in (3, 4) else []
		self.current_race_index = 0
		self.current_gender_index = 0 if categoryIndex in (2, 6, 7) else self.current_gender_index
		self.last_switch_time = app.GetGlobalTimeStamp()
		renderTarget.ClearModel(Config.RENDER_INDEX)
		if categoryIndex in (3, 4):
			self.RenderModel(0, itemVnum, categoryIndex)
		elif self.race_list:
			self.RenderModel(self.race_list[self.current_race_index], itemVnum, categoryIndex)
		self.UpdateButtonVisibility()

	def NextRace(self):
		if not self.race_list or self.current_category in (3, 4):
			return
		self.current_race_index = (self.current_race_index + 1) % len(self.race_list)
		self.SelectRace(self.current_race_index)

	def OnUpdate(self):
		if self.current_item_vnum and self.race_list and self.current_category not in (3, 4):
			current_time = app.GetGlobalTimeStamp()
			if current_time - self.last_switch_time >= 5000:
				self.NextRace()
		if self.previewTools:
			renderTarget.SetZoom(Config.RENDER_INDEX, self.previewZoom)

	def Open(self):
		self.Show()
		self.UpdateButtonVisibility()

	def Close(self):
		renderTarget.ClearModel(Config.RENDER_INDEX)
		renderTarget.SetVisibility(Config.RENDER_INDEX, False)
		self.current_item_vnum = 0
		self.current_category = -1
		self.race_list = []
		self.last_switch_time = 0
		self.previewZoom = False
		self.previewTools = False
		self.zoomInButton.SetUp()
		self.zoomOutButton.SetUp()
		self.UpdateButtonVisibility()
		self.Hide()

	def Destroy(self):
		self.children = {}
		self.race_list = []
		self.current_item_vnum = 0
		self.current_category = -1
		self.last_switch_time = 0
		self.previewZoom = False
		self.previewTools = False
		self.raceButtons = []
		self.genderButtons = []

	def AdjustPosition(self, bx=0, by=0):
		self.SetPosition(bx, by)

class Window(ui.BoardWithTitleBar):
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.SetSize(*Config.BOARD)
		self.SetTitleName(localeInfo.PREVIEW_SYSTEM_TITLE)
		self.AddFlag("movable")
		
		self.children = {}
		self.Allitems = []
		self.selectedPage = 0
		self.selectedCategoryIndex = -1
		self.selectedCharacterIndex = 0
		self.selectedCharacterGender = 0
		
		self.scrollOffset = 0.0
		self.isScrolling = False

		self.tooltipitem = uiToolTip.ItemToolTip()
		self.tooltipitem.Hide()
		self.PreviewBoard = Preview()

		self.tab_indices = []
		self.MakeTabWindow()
		self.MakeCostumeWindow()
		self.SelectTab(0)

		self.SetCloseEvent(ui.__mem_func__(self.Close))

	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)

	def Open(self):
		self.SetCenterPosition()
		x, y = self.GetGlobalPosition()
		self.OnMoveWindow(x, y)
		if self.PreviewBoard:
			self.PreviewBoard.Open()
		self.Show()

	def Close(self):
		if self.PreviewBoard:
			self.PreviewBoard.Close()
		self.selectedCategoryIndex = -1
		self.Allitems = []
		self.children["Costume"] = []
		self.itemList = []
		for button in self.children["Tab"]:
			button.SetUp()
		for img in self.children["TabImage"]:
			img.LoadImage(Config.IMAGE + "cat_open_0.tga")
		self.children["CheckBox"].SetCheck(False)
		self.ClearEditlineItem()
		renderTarget.ClearModel(Config.RENDER_INDEX)
		renderTarget.SetVisibility(Config.RENDER_INDEX, False)
		self.Hide()

	def Destroy(self):
		self.children = {}
		self.Allitems = []
		self.selectedCategoryIndex = -1
		self.selectedCharacterIndex = 0
		self.selectedCharacterGender = 0
		if self.PreviewBoard:
			self.PreviewBoard.Destroy()
			self.PreviewBoard = None
		self.tooltipitem = None
		self.tab_indices = []

	def MakeTabWindow(self):
		self.children["Tab"] = []
		self.children["TabImage"] = []
		self.tab_indices = []

		TabBoard = ui.ImageBox()
		TabBoard.SetParent(self)
		TabBoard.SetPosition(10, 35)
		TabBoard.LoadImage(Config.IMAGE + "background_0.tga")
		TabBoard.Show()
		self.children["TabBoard"] = TabBoard

		searchBar = ui.ImageBox()
		searchBar.SetParent(TabBoard)
		searchBar.SetPosition(10, 10)
		searchBar.LoadImage(Config.IMAGE + "searchbar.tga")
		searchBar.Show()
		self.searchBar = searchBar

		itemSearch = ui.EditLine()
		itemSearch.SetParent(searchBar)
		itemSearch.SetMax(20)
		itemSearch.SetPosition(10, 5)
		itemSearch.SetSize(searchBar.GetWidth(), searchBar.GetHeight())
		itemSearch.OnIMEUpdate = ui.__mem_func__(self.OnUpdateCostumeItemEditLine)
		itemSearch.SetReturnEvent(ui.__mem_func__(self.StartSearchItem))
		itemSearch.SetOutline()
		itemSearch.Show()
		itemSearch.SetInfoMessage(localeInfo.PREVIEW_SYSTEM_SEARCH)
		self.itemSearch = itemSearch

		hint_list_position_x, hint_list_position_y = searchBar.GetLocalPosition()
		autocomplete_suggestion_list = AutoCompleteSearchEditLine(self)
		autocomplete_suggestion_list.SetPosition(hint_list_position_x + 10, hint_list_position_y + 57)
		autocomplete_suggestion_list.SetClickEvent(ui.__mem_func__(self.ClickOnSearchEditLineElement))
		autocomplete_suggestion_list.CloseList()

		self.autocomplete_suggestion_list = autocomplete_suggestion_list
		self.selected_suggestion_vnum = 0

		searchBtn = ui.Button()
		searchBtn.SetParent(self.searchBar)
		searchBtn.SetUpVisual(Config.IMAGE + "search_btn_0.tga")
		searchBtn.SetOverVisual(Config.IMAGE + "search_btn_1.tga")
		searchBtn.SetDownVisual(Config.IMAGE + "search_btn_2.tga")
		searchBtn.SetEvent(self.StartSearchItem)
		searchBtn.SetPosition(itemSearch.GetWidth() - searchBtn.GetWidth() - 3, 3)
		searchBtn.Show()
		self.searchBtn = searchBtn

		event = lambda index=0: ui.__mem_func__(self.CheckMainCostume)(index)
		self.children["CheckBox"] = ui.CheckBoxNew(TabBoard, 10, 42, event)

		checkboxText = ui.TextLine()
		checkboxText.SetParent(TabBoard)
		checkboxText.SetPosition(20 + self.children["CheckBox"].GetWidth(), 42)
		checkboxText.SetText(localeInfo.PREVIEW_SYSTEM_TEX_1)
		checkboxText.SetOutline()
		checkboxText.Show()
		self.children["checkboxText"] = checkboxText

		yPos = 7 + 65
		for i, label in sorted(Config.COSTUME.items()):
			TabButton = ui.RadioButton()
			TabButton.SetParent(TabBoard)
			TabButton.SetPosition(2, yPos)
			TabButton.SetWindowHorizontalAlignCenter()
			TabButton.SetUpVisual(Config.IMAGE + "cat_craft_0.tga")
			TabButton.SetOverVisual(Config.IMAGE + "cat_craft_1.tga")
			TabButton.SetDownVisual(Config.IMAGE + "cat_craft_2.tga")
			TabButton.SetText(label)
			TabButton.SetEvent(lambda arg=i: self.SelectTab(arg))
			TabButton.Show()
			yPos += 40
			self.children["Tab"].append(TabButton)
			self.tab_indices.append(i)

			TabCatImage = ui.ImageBox()
			TabCatImage.SetParent(TabButton)
			TabCatImage.SetPosition(10, 1)
			TabCatImage.SetWindowVerticalAlignCenter()
			TabCatImage.LoadImage(Config.IMAGE + "cat_open_0.tga")
			TabCatImage.Show()
			self.children["TabImage"].append(TabCatImage)

	def MakeCostumeWindow(self):
		ImageBoard = ui.ImageBox()
		ImageBoard.SetParent(self)
		ImageBoard.SetPosition(self.children["TabBoard"].GetWidth() + 10, 35)
		ImageBoard.LoadImage(Config.IMAGE + "background_1.tga")
		ImageBoard.Show()
		self.children["ImageBoard"] = ImageBoard

		WindowBoard = ui.Window()
		WindowBoard.SetParent(ImageBoard)
		WindowBoard.SetPosition(2, 2)
		WindowBoard.SetSize(*Config.BOARD_WINDOW)
		WindowBoard.Show()
		self.children["WindowBoard"] = WindowBoard

		scrollbarWindow = ui.Window()
		scrollbarWindow.SetParent(self)
		scrollbarWindow.SetPosition(WindowBoard.GetWidth() + 211, 35)
		scrollbarWindow.SetSize(8, WindowBoard.GetHeight() - 20)
		scrollbarWindow.Show()
		self.scrollbarWindow = scrollbarWindow

		scrollBar = ui.ScrollbarDyn()
		scrollBar.SetParent(self.scrollbarWindow)
		scrollBar.SetPosition(0, 12)
		scrollBar.SetSize(6, scrollbarWindow.GetHeight())
		scrollBar.SetScrollEvent(self.OnScrollDyn)
		scrollBar.SetScrollSpeed(25)
		scrollBar.Show()
		self.scrollBar = scrollBar

	def SelectTab(self, index):
		if index not in Config.COSTUME:
			return
		for i, button in enumerate(self.children["Tab"]):
			button.SetUp()
			if i < len(self.children["TabImage"]):
				self.children["TabImage"][i].LoadImage(Config.IMAGE + "cat_open_0.tga")
		tab_pos = self.tab_indices.index(index)
		self.children["Tab"][tab_pos].Down()
		self.children["TabImage"][tab_pos].LoadImage(Config.IMAGE + "cat_close_0.tga")

		self.selectedCategoryIndex = index
		self.scrollOffset = 0.0
		for costumeItem in self.children.get("Costume", []):
			costumeItem.Hide()
		self.children["Costume"] = []
		self.itemList = []
		renderTarget.ClearModel(Config.RENDER_INDEX)
		renderTarget.SetVisibility(Config.RENDER_INDEX, False)
		self.AddItem()

	def AddItem(self):
		self.itemList = []
		self.Allitems = []

		columns = 6
		spacing_x = 78
		spacing_y = 105
		start_x = 10
		start_y = 10
		
		self.Allitems = get_all_preview_items(self.selectedCategoryIndex, self.GetCharacterRace(), self.selectedCharacterGender)
		for index, vnum in enumerate(self.Allitems):
			if not isinstance(vnum, int) or vnum <= 0 or vnum in Config.BLACK_ITEM:
				continue
			try:
				item.SelectItem(vnum)
			except:
				continue
			row = index // columns
			col = index % columns
			x = start_x + col * spacing_x
			y = start_y + row * spacing_y

			banner = ui.ImageBox()
			banner.SetParent(self.children["WindowBoard"])
			banner.SetPosition(x, y)
			banner.SetClippingMaskWindow(self.children["WindowBoard"])
			banner.LoadImage(Config.IMAGE + "costume.tga")
			banner.OnMouseOverIn = lambda vnum=vnum: self.OverInItemSlot(vnum)
			banner.OnMouseLeftButtonDown = lambda vnum=vnum: self.OnMouseLeftButton(vnum)
			banner.OnMouseRightButtonUp = lambda vnum=vnum: self.UseItemSlot(vnum)
			banner.OnMouseOverOut = self.OverOutItemSlot
			banner.Show()
			self.children["Costume"].append(banner)

			itemIcon = ui.ImageBox()
			itemIcon.SetParent(banner)
			itemIcon.SetWindowVerticalAlignCenter()
			itemIcon.SetWindowHorizontalAlignCenter()
			try:
				itemIcon.LoadImage(item.GetIconImageFileName())
			except:
				continue
			itemIcon.SetClippingMaskWindow(self.children["WindowBoard"])
			itemIcon.SetPosition(0, 0)
			itemIcon.AddFlag("attach")
			itemIcon.AddFlag("not_pick")
			itemIcon.Show()
			self.children["Costume"].append(itemIcon)

			self.itemList.append((banner, x, y))

		self.ScrollContent()
		self.ChangeScrollbar()

	def CheckMainCostume(self, key=0, costumeItemList=None):
		costumeItemList = costumeItemList or []
		
		CheckBox = self.children["CheckBox"] if "CheckBox" in self.children else None
		value = 1 if not CheckBox.GetCheck() else 0
		CheckBox.SetCheck(value)
		
		renderTarget.ClearModel(Config.RENDER_INDEX)
		renderTarget.SetVisibility(Config.RENDER_INDEX, False)
		for costumeItem in self.children.get("Costume", []):
			costumeItem.Hide()
		self.children["Costume"] = []
		self.itemList = []

		if value == 1:
			for button in self.children["Tab"]:
				button.SetUp()
			self.selectedCategoryIndex = -1
			filtered_costumes = get_all_inventory_items(self.GetCharacterRace(), self.selectedCharacterGender)
			
			for index, (vnum, category_index) in enumerate(filtered_costumes):
				self.SelectItemByVnum(vnum, index, category_index)
			
			if filtered_costumes:
				self.PreviewBoard.SetItemToModelPreview(filtered_costumes[0][0], filtered_costumes[0][1])
		else:
			self.SelectTab(0)

	def GetRaceByAntiFlags(self, itemVnum):
		if not isinstance(itemVnum, int) or itemVnum <= 0 or itemVnum in Config.BLACK_ITEM:
			return player.MAIN_RACE_WARRIOR_M
		try:
			item.SelectItem(itemVnum)
		except:
			return player.MAIN_RACE_WARRIOR_M

		ANTI_FLAG_DICT = {
			0: item.ITEM_ANTIFLAG_WARRIOR,
			1: item.ITEM_ANTIFLAG_ASSASSIN,
			2: item.ITEM_ANTIFLAG_SURA,
			3: item.ITEM_ANTIFLAG_SHAMAN,
		}

		characterInfoDict = {
			0: {0: player.MAIN_RACE_WARRIOR_M, 1: player.MAIN_RACE_WARRIOR_W},
			1: {0: player.MAIN_RACE_ASSASSIN_M, 1: player.MAIN_RACE_ASSASSIN_W},
			2: {0: player.MAIN_RACE_SURA_M, 1: player.MAIN_RACE_SURA_W},
			3: {0: player.MAIN_RACE_SHAMAN_M, 1: player.MAIN_RACE_SHAMAN_W},
		}

		def is_allowed(class_idx, sex):
			if itemVnum in Config.BLACK_ITEM:
				return False
			if item.IsAntiFlag(ANTI_FLAG_DICT.get(class_idx, 0)):
				return False
			if sex == 0 and item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE):
				return False
			if sex == 1 and item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE):
				return False
			return True

		my_race = player.GetRace()
		reverseMap = {
			player.MAIN_RACE_WARRIOR_M: (0, 0),
			player.MAIN_RACE_WARRIOR_W: (0, 1),
			player.MAIN_RACE_ASSASSIN_M: (1, 0),
			player.MAIN_RACE_ASSASSIN_W: (1, 1),
			player.MAIN_RACE_SURA_M: (2, 0),
			player.MAIN_RACE_SURA_W: (2, 1),
			player.MAIN_RACE_SHAMAN_M: (3, 0),
			player.MAIN_RACE_SHAMAN_W: (3, 1),
		}

		if my_race in reverseMap:
			cls, sex = reverseMap[my_race]
			if is_allowed(cls, sex):
				return my_race

		for cls in range(len(characterInfoDict)):
			for sex in (0, 1):
				if characterInfoDict[cls].get(sex, -1) != -1 and is_allowed(cls, sex):
					return characterInfoDict[cls][sex]

		return player.MAIN_RACE_WARRIOR_M

	def GetCharacterRace(self):
		characterInfoDict = {
			0: {0: player.MAIN_RACE_WARRIOR_M, 1: player.MAIN_RACE_WARRIOR_W},
			1: {0: player.MAIN_RACE_ASSASSIN_M, 1: player.MAIN_RACE_ASSASSIN_W},
			2: {0: player.MAIN_RACE_SURA_M, 1: player.MAIN_RACE_SURA_W},
			3: {0: player.MAIN_RACE_SHAMAN_M, 1: player.MAIN_RACE_SHAMAN_W},
		}
		race = characterInfoDict.get(self.selectedCharacterIndex, -1)
		if race == -1:
			return player.MAIN_RACE_WARRIOR_M
		return race.get(self.selectedCharacterGender, player.MAIN_RACE_WARRIOR_M)

	def OnMouseLeftButton(self, itemVnum, category_index=None):
		if itemVnum in Config.BLACK_ITEM:
			return
		self.PreviewBoard.SetItemToModelPreview(itemVnum, category_index if category_index is not None else self.selectedCategoryIndex)

	def OverInItemSlot(self, itemVnum, slotIndex=0):
		if not self.tooltipitem or itemVnum in Config.BLACK_ITEM:
			return
		if not isinstance(itemVnum, int) or itemVnum <= 0:
			return

		metinSlot = []
		for i in range(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(0)

		self.tooltipitem.ClearToolTip()
		try:
			self.tooltipitem.AddItemData(itemVnum, metinSlot, 0)
		except:
			pass

	def OverOutItemSlot(self):
		if self.tooltipitem:
			self.tooltipitem.HideToolTip()

	def UseItemSlot(self, itemVnum):
		if itemVnum in Config.BLACK_ITEM:
			return
		if app.IsPressed(app.DIK_LSHIFT):
			import wikipedia
			wikipedia.ShowSpecificItem(itemVnum)
			return
		self.PreviewBoard.NextRace()

	def OnUpdateCostumeItemEditLine(self):
		ui.EditLine.OnIMEUpdate(self.itemSearch)
		editline_text = self.itemSearch.GetText()
		self.selected_suggestion_vnum = 0
		self.autocomplete_suggestion_list.ClearList()

		if len(editline_text.strip()) == 0:
			self.autocomplete_suggestion_list.CloseList()
			return False

		filtered_items = self.GetFilteredItemResults(editline_text)

		if filtered_items:
			self.selected_suggestion_vnum = filtered_items[0]["itemVnum"]
			self.itemSearch.SetInfoMessage(filtered_items[0]["itemName"])
		else:
			self.selected_suggestion_vnum = 0
			self.itemSearch.SetInfoMessage("")

		for index, item_info in enumerate(filtered_items[:10], start=1):
			self.autocomplete_suggestion_list.AddItem(item_info["itemName"], item_info["itemVnum"])

		if len(filtered_items) < 2:
			self.autocomplete_suggestion_list.CloseList()
		else:
			self.autocomplete_suggestion_list.OpenList()

		return True

	def GetFilteredItemResults(self, text):
		text = text.lower().strip().replace(' ', '')
		filtered = []
		seen_names = set()

		for vnum in self.Allitems:
			if vnum in Config.BLACK_ITEM:
				continue
			if not isinstance(vnum, int) or vnum <= 0:
				continue
			try:
				item.SelectItem(vnum)
				name = item.GetItemName()
				clean_name = re.sub(r'\+\d+', '', name).strip()
				compare_name = re.sub(r'\s+', '', clean_name.lower())

				if compare_name.startswith(text) and clean_name not in seen_names:
					filtered.append({
						"itemName": clean_name,
						"itemVnum": vnum
					})
					seen_names.add(clean_name)
			except:
				continue

		return filtered

	def SelectItemByVnum(self, vnum, index=0, category_index=None):
		if not isinstance(vnum, int) or vnum <= 0 or vnum in Config.BLACK_ITEM:
			return False
		try:
			item.SelectItem(vnum)
		except:
			return False

		columns = 6
		spacing_x = 78
		spacing_y = 105
		start_x = 10
		start_y = 10
		row = index // columns
		col = index % columns
		x = start_x + col * spacing_x
		y = start_y + row * spacing_y

		banner = ui.ImageBox()
		banner.SetParent(self.children["WindowBoard"])
		banner.SetPosition(x, y)
		banner.SetClippingMaskWindow(self.children["WindowBoard"])
		banner.LoadImage(Config.IMAGE + "costume.tga")
		banner.OnMouseOverIn = lambda vnum=vnum: self.OverInItemSlot(vnum)
		banner.OnMouseLeftButtonDown = lambda vnum=vnum, cat=category_index: self.OnMouseLeftButton(vnum, cat)
		banner.OnMouseRightButtonUp = lambda vnum=vnum: self.UseItemSlot(vnum)
		banner.OnMouseOverOut = self.OverOutItemSlot
		banner.Show()
		self.children["Costume"].append(banner)

		itemIcon = ui.ImageBox()
		itemIcon.SetParent(banner)
		itemIcon.SetWindowVerticalAlignCenter()
		itemIcon.SetWindowHorizontalAlignCenter()
		try:
			itemIcon.LoadImage(item.GetIconImageFileName())
		except:
			return False
		itemIcon.SetClippingMaskWindow(self.children["WindowBoard"])
		itemIcon.SetPosition(0, 0)
		itemIcon.AddFlag("attach")
		itemIcon.AddFlag("not_pick")
		itemIcon.Show()
		self.children["Costume"].append(itemIcon)
		
		self.itemList.append((banner, x, y))
		self.ScrollContent()
		self.ChangeScrollbar()
		
		return True

	def ClickOnSearchEditLineElement(self, name, vnum):
		if vnum in Config.BLACK_ITEM:
			return
		self.itemSearch.SetText(str(name))
		ime.MoveEnd()
		self.autocomplete_suggestion_list.CloseList()
		self.ClearEditlineItem()
		self.children["Costume"] = []
		self.itemList = []
		self.Allitems = [vnum]
		self.SelectItemByVnum(vnum, 0, self.selectedCategoryIndex)
		self.PreviewBoard.SetItemToModelPreview(vnum, self.selectedCategoryIndex)

	def StartSearchItem(self):
		search_text = self.itemSearch.GetText().strip()
		if not search_text:
			self.ClearEditlineItem()
			self.SelectTab(self.selectedCategoryIndex if self.selectedCategoryIndex != -1 else 0)
			return

		vnum = self.selected_suggestion_vnum
		if vnum and vnum not in Config.BLACK_ITEM:
			self.children["Costume"] = []
			self.itemList = []
			self.Allitems = [vnum]
			self.SelectItemByVnum(vnum, 0, self.selectedCategoryIndex)
			self.PreviewBoard.SetItemToModelPreview(vnum, self.selectedCategoryIndex)
			self.ClearEditlineItem()

	def ClearEditlineItem(self):
		self.selected_suggestion_vnum = 0
		self.itemSearch.SetText("")
		self.itemSearch.KillFocus()
		self.itemSearch.SetInfoMessage(localeInfo.PREVIEW_SYSTEM_SEARCH)
		self.OnUpdateCostumeItemEditLine()

	def OnMouseWheel(self, length):
		if self.IsInPosition():
			self.UpdateScrollbar((length * 0.01) * 28)
			return True
		return False

	def GetTotalHeight(self):
		columns = 6
		rows = (len(self.itemList) + columns - 1) // columns
		return rows * 105 + 10

	def OnScrollDyn(self, position):
		totalHeight = self.GetTotalHeight()
		visibleHeight = self.children["WindowBoard"].GetHeight()

		if totalHeight <= visibleHeight:
			self.scrollOffset = 0
		else:
			max_scroll = totalHeight - visibleHeight
			self.scrollOffset = -int(position * max_scroll)

		self.ScrollContent()

	def UpdateScrollbar(self, val=0):
		if self.isScrolling:
			return
		
		self.isScrolling = True
		
		try:
			totalHeight = self.GetTotalHeight()
			visibleHeight = self.children["WindowBoard"].GetHeight()

			self.scrollOffset += val

			newScrollOffset = min(0, max(self.scrollOffset, visibleHeight - totalHeight))
			self.scrollOffset = newScrollOffset

			self.ChangeScrollbar()
		finally:
			self.isScrolling = False

	def ChangeScrollbar(self):
		if not self.scrollBar:
			return

		scrollBoardHeight = self.GetTotalHeight()
		selfHeight = self.scrollbarWindow.GetHeight()

		if scrollBoardHeight <= selfHeight:
			self.scrollBar.Hide()
		else:
			self.scrollBar.SetScale(selfHeight, scrollBoardHeight)
			new_pos = self.GetNewScrollBarPosition()

			if new_pos != 0:
				self.scrollBar.SetPos(new_pos)
			else:
				pos_scale = float(abs(self.scrollOffset)) / float(scrollBoardHeight - selfHeight)
				self.scrollBar.SetPosScale(pos_scale)

			self.scrollBar.Show()

		self.ScrollContent()

	def GetNewScrollBarPosition(self):
		totalHeight = self.GetTotalHeight()
		visibleHeight = self.children["WindowBoard"].GetHeight()

		if totalHeight <= visibleHeight:
			return 0

		progress = float(abs(self.scrollOffset)) / float(totalHeight - visibleHeight)
		max_middle_pos = self.scrollbarWindow.GetHeight() - self.scrollBar.middleBar.GetHeight() - 2

		new_pos = int(progress * max_middle_pos) + 1
		return new_pos

	def ScrollContent(self):
		for i, (element, x, y) in enumerate(self.itemList):
			element.SetPosition(x, y + self.scrollOffset)

	def OnMoveWindow(self, x, y):
		x, y = self.GetGlobalPosition()
		if self.PreviewBoard:
			self.PreviewBoard.AdjustPosition(x + Config.BOARD[0], y)

class AutoCompleteSearchEditLine(ui.Window):
	EDITLINE_WIDTH = 189
	COLOR = 0xFF272727
	IMAGE_PATH = "d:/ymir work/ui/dnc/crafting/"

	def __init__(self, parent):
		ui.Window.__init__(self)
		self.SetParent(parent)
		self.SetSize(self.EDITLINE_WIDTH, 0)
		self.__Initialize()

	def __Initialize(self):
		self.horizontalLine_top = None
		self.horizontalLine_left = None
		self.horizontalLine_right = None
		self.horizontalLine_bottom = None
		self.click_event = None
		self.buttons_list = []

	def __del__(self):
		ui.Window.__del__(self)

	def __LoadMainBox(self):
		self.horizontalLine_top = ui.Line()
		self.horizontalLine_top.SetParent(self)
		self.horizontalLine_top.SetPosition(0, 0)
		self.horizontalLine_top.SetColor(self.COLOR)
		self.horizontalLine_top.SetSize(self.EDITLINE_WIDTH, 0)
		self.horizontalLine_top.Show()

		self.horizontalLine_left = ui.Line()
		self.horizontalLine_left.SetParent(self)
		self.horizontalLine_left.SetPosition(0, 0)
		self.horizontalLine_left.SetColor(self.COLOR)
		self.horizontalLine_left.SetSize(0, 0)
		self.horizontalLine_left.Show()

		self.horizontalLine_right = ui.Line()
		self.horizontalLine_right.SetParent(self)
		self.horizontalLine_right.SetPosition(0, 0)
		self.horizontalLine_right.SetWindowHorizontalAlignRight()
		self.horizontalLine_right.SetColor(self.COLOR)
		self.horizontalLine_right.SetSize(0, 0)
		self.horizontalLine_right.Show()

		self.horizontalLine_bottom = ui.Line()
		self.horizontalLine_bottom.SetParent(self)
		self.horizontalLine_bottom.SetPosition(0, 0)
		self.horizontalLine_bottom.SetColor(self.COLOR)
		self.horizontalLine_bottom.SetSize(self.EDITLINE_WIDTH, 0)
		self.horizontalLine_bottom.Show()

	def ClearList(self):
		for button in self.buttons_list:
			button.Hide()

		self.SetSize(self.EDITLINE_WIDTH, 0)
		self.horizontalLine_top = None
		self.horizontalLine_left = None
		self.horizontalLine_right = None
		self.horizontalLine_bottom = None
		self.buttons_list = []

	def AddItem(self, buttonName, vnum):
		if vnum in Config.BLACK_ITEM:
			return
		index = len(self.buttons_list)
		tmpButton = ui.MakeButton(self, 0, 23 * index, "", self.IMAGE_PATH, "dropdown_list.tga", "dropdown_list_hover.tga", "dropdown_list_down.tga")
		tmpButton.SetText(str(buttonName))
		tmpButton.SetEvent(ui.__mem_func__(self.ClickOnElement), buttonName, vnum)
		self.buttons_list.append(tmpButton)

	def CloseList(self):
		self.ClearList()
		self.Hide()

	def SetClickEvent(self, event):
		self.click_event = event

	def ClickOnElement(self, name, vnum):
		if self.click_event:
			self.click_event(name, vnum)

	def OpenList(self):
		self.__LoadMainBox()

		if len(self.buttons_list) != 0:
			height = self.buttons_list[-1].GetLocalPosition()[1] + self.buttons_list[-1].GetHeight()
			self.SetSize(self.EDITLINE_WIDTH, height)
			self.horizontalLine_left.SetSize(0, height)
			self.horizontalLine_right.SetSize(0, height)
			self.horizontalLine_bottom.SetPosition(0, height)

		self.Show()
