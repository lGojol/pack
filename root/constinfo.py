import app
import net

if app.ENABLE_BATTLE_ROYALE:
	BATTLE_ROYALE_CAN_WARP = False
	BATTLE_ROYALE_TERRAIN_ZONE = True

if app.ENABLE_SEND_TARGET_INFO:
	MONSTER_INFO_DATA = {}

if app.ENABLE_SKILL_SELECT_FEATURE:
	ARE_ENABLED_6TH_SKILLS = 1

if app.ENABLE_HIDE_COSTUME_SYSTEM:
	HIDDEN_BODY_COSTUME = 0
	HIDDEN_HAIR_COSTUME = 0
	if app.ENABLE_ACCE_SYSTEM:
		HIDDEN_ACCE_COSTUME = 0
	if app.ENABLE_WEAPON_COSTUME_SYSTEM:
		HIDDEN_WEAPON_COSTUME = 0
	if app.ENABLE_AURA_SYSTEM:
		HIDDEN_AURA_COSTUME = 0
ENABLE_SAVE_ACCOUNT = True
if ENABLE_SAVE_ACCOUNT:
	class SAB:
		ST_CACHE, ST_FILE, ST_REGISTRY = xrange(3)
		slotCount = 5
		storeType = ST_REGISTRY # 0 cache, 1 file, 2 registry
		btnName = {
			"Save": "SaveAccountButton_Save_%02d",
			"Access": "SaveAccountButton_Access_%02d",
			"Remove": "SaveAccountButton_Remove_%02d",
		}
		accData = {}
		regPath = r"SOFTWARE\Metin2"
		regName = "slot%02d_%s"
		regValueId = "id"
		regValuePwd = "pwd"
		fileExt = ".do.not.share.it.txt"
# EXTRA BEGIN
# loads 5 (B,M,G,P,F) skills .mse
ENABLE_NEW_LEVELSKILL_SYSTEM = 0
# don't set a random channel when you open the client
ENABLE_RANDOM_CHANNEL_SEL = 0
# don't remove id&pass if the login attempt fails
ENABLE_CLEAN_DATA_IF_FAIL_LOGIN = 0
# ctrl+v will now work
ENABLE_PASTE_FEATURE = 0
# display all the bonuses added by a stone instead of the first one
ENABLE_FULLSTONE_DETAILS = 1
# enable successfulness % in the refine dialog
ENABLE_REFINE_PCT = 1
# extra ui features
EXTRA_UI_FEATURE = 1
#
NEW_678TH_SKILL_ENABLE = 1
# EXTRA END
BIO_DICT = []
BIO_CHANGED = 0
COINS_DRS = [0,0]
ITEMSHOP = {
	'items' : {
			'startpage' : {
					'mostBought' : [],
					'hotOffers' : [],
					},
			'itemshop' : {},
			'voteshop' : {},
			'achievementshop' : {},
		},
	'category': [], ##(id, name, image)
	'subCategories': {}, ## categoryId: [...name]
	'tableUpdate' : '0000-00-00 00:00:00',
	'qid'	: 0,
	'questCMD' : '',
}
# option
IN_GAME_SHOP_ENABLE = 1
CONSOLE_ENABLE = 0

_game_instance = None
def GetGameInstance():
	global _game_instance
	return _game_instance
def SetGameInstance(instance):
	global _game_instance
	if _game_instance:
		del _game_instance
	_game_instance = instance
def GetInterfaceInstance():
	global _game_instance
	if _game_instance:
		return _game_instance.interface
	return None
def DelWinRegKeyValue(keyPath, keyName):
	try:
		import _winreg
		_winreg.CreateKey(_winreg.HKEY_CURRENT_USER, keyPath)
		_tmpKey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, keyPath, 0, _winreg.KEY_WRITE)
		_winreg.DeleteValue(_tmpKey, keyName)
		_winreg.CloseKey(_tmpKey)
		return True
	except WindowsError:
		return False
def GetWinRegKeyValue(keyPath, keyName):
	try:
		import _winreg
		_tmpKey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, keyPath, 0, _winreg.KEY_READ)
		keyValue, keyType = _winreg.QueryValueEx(_tmpKey, keyName)
		_winreg.CloseKey(_tmpKey)
		return str(keyValue) # unicode to ascii
	except WindowsError:
		return None
def SetWinRegKeyValue(keyPath, keyName, keyValue):
	try:
		import _winreg
		_winreg.CreateKey(_winreg.HKEY_CURRENT_USER, keyPath)
		_tmpKey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, keyPath, 0, _winreg.KEY_WRITE)
		_winreg.SetValueEx(_tmpKey, keyName, 0, _winreg.REG_SZ, keyValue)
		_winreg.CloseKey(_tmpKey)
		return True
	except WindowsError:
		return False

if app.ENABLE_EXTENDED_BLEND_AFFECT:
	def IS_BLEND_POTION(itemVnum):
		if itemVnum >= 50821 and itemVnum <= 50826:
			return 1
		elif itemVnum == 51002:
			return 1

		return 0

	def IS_EXTENDED_BLEND_POTION(itemVnum):
		if itemVnum >= 950821 and itemVnum <= 950826: # Dews
			return 1
		elif itemVnum == 951002: # Cristal Energy
			return 1
		elif itemVnum >= 939017 and itemVnum <= 939020: # Dragon God Medals
			return 1
		elif itemVnum == 939024 or itemVnum == 939025: # Critical & Penetration
			return 1
		elif itemVnum == 927209 or itemVnum == 927212: # Attack Speed & Move Speed
			return 1

		return 0

	def IS_ELIXIR(itemVnum):
		if itemVnum >= 39037 and itemVnum <= 39042: # Dews
			return 1

		elif itemVnum >= 72723 and itemVnum <= 72730: # Dews
			return 1

		elif itemVnum >= 76004 and itemVnum <= 76005: # Dews
			return 1

		elif itemVnum >= 76021 and itemVnum <= 76022: # Dews
			return 1

		return 0

if app.ENABLE_PREMIUM_PRIVATE_SHOP:
	GOLD_MAX = 2000000000
	CHEQUE_MAX = 999

PVPMODE_ENABLE = 1
PVPMODE_TEST_ENABLE = 0
EXPRESSING_EMOTIONS = {}
SELECT_CHARACTER_ROTATION = 1 # Enables character rotation in select phase.
PVPMODE_ACCELKEY_ENABLE = 1
PVPMODE_ACCELKEY_DELAY = 0.5
PVPMODE_PROTECTED_LEVEL = 15
FOG_LEVEL0 = 4800.0
FOG_LEVEL1 = 9600.0
FOG_LEVEL2 = 12800.0
FOG_LEVEL = FOG_LEVEL0
FOG_LEVEL_LIST=[FOG_LEVEL0, FOG_LEVEL1, FOG_LEVEL2]

CAMERA_MAX_DISTANCE_SHORT = 2500.0
CAMERA_MAX_DISTANCE_LONG = 3500.0
CAMERA_MAX_DISTANCE_LIST=[CAMERA_MAX_DISTANCE_SHORT, CAMERA_MAX_DISTANCE_LONG]
CAMERA_MAX_DISTANCE = CAMERA_MAX_DISTANCE_SHORT

CHRNAME_COLOR_INDEX = 0
EnvanterAcilsinmi = 0
ME_KEY = 0

ENVIRONMENT_NIGHT="d:/ymir work/environment/moonlight04.msenv"

# constant
HIGH_PRICE = 500000
PET_EVOLUTION = 0
PET_LEVEL = 0
PET_MAIN = 0
FEEDWIND = 0
SKILL_PET3 = 0
SKILL_PET2 = 0
SKILL_PET1 = 0
LASTAFFECT_POINT = 0
LASTAFFECT_VALUE = 0
EVOLUTION = 0
USE_FEED = -1
MIDDLE_PRICE = 50000
ERROR_METIN_STONE = 28960
SUB2_LOADING_ENABLE = 1
EXPANDED_COMBO_ENABLE = 1
CONVERT_EMPIRE_LANGUAGE_ENABLE = 0
USE_ITEM_WEAPON_TABLE_ATTACK_BONUS = 0
ADD_DEF_BONUS_ENABLE = 0
LOGIN_COUNT_LIMIT_ENABLE = 0

USE_SKILL_EFFECT_UPGRADE_ENABLE = 1

VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD = 1
GUILD_MONEY_PER_GSP = 100
GUILD_WAR_TYPE_SELECT_ENABLE = 1
TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE = 10

HAIR_COLOR_ENABLE = 1
ARMOR_SPECULAR_ENABLE = 1
WEAPON_SPECULAR_ENABLE = 1
SEQUENCE_PACKET_ENABLE = 1
KEEP_ACCOUNT_CONNETION_ENABLE = 1
MINIMAP_POSITIONINFO_ENABLE = 0
ACCOUNT_NAME = "NoName"
WOLF_MAN = "DISABLED"
WOLF_WOMEN = "DISABLED"
PAST_HEALTH_ON_TARGET = True # Show past health on target (yellow gauge)

isItemQuestionDialog = 0

if app.TOURNAMENT_PVP_SYSTEM:
	TOURNAMENT_WINDOW_IS_SHOWED = 0

if app.CRYSTAL_EVENT_SYSTEM:
	CRYSTAL_EVENT_WINDOW_IS_SHOWED = 0

if app.ENABLE_OFFICAL_CHARACTER_SCREEN:
	WOLF_MAN = "DISABLED"	# ENABLED/DISABLED
	WOLF_WOMEN = "DISABLED"	# ENABLED/DISABLED
	RESELECT_EMPIRE = 0

def GET_ITEM_QUESTION_DIALOG_STATUS():
	global isItemQuestionDialog
	return isItemQuestionDialog

def SET_ITEM_QUESTION_DIALOG_STATUS(flag):
	global isItemQuestionDialog
	isItemQuestionDialog = flag

def IS_PET_SEAL_OLD(itemVnum):
	if itemVnum == 38200 or itemVnum == 38201:
		return 1
	elif itemVnum >= 53006 and itemVnum <= 53283:
		return 1
	elif itemVnum == 48301 or itemVnum == 48311 or itemVnum == 48321:
		return 1
	elif itemVnum == 49010 or itemVnum == 49050:
		return 1
	elif itemVnum >= 60101 and itemVnum <= 60104:
		return 1
	elif itemVnum >= 61484 and itemVnum <= 61509:
		return 1
	elif itemVnum >= 61460 and itemVnum <= 61461:
		return 1
	elif itemVnum >= 61205 and itemVnum <= 61205:
		return 1
	elif itemVnum >= 38200 and itemVnum <= 38201:
		return 1
	elif itemVnum >= 53001 and itemVnum <= 53026:
		return 1
	elif itemVnum >= 53218 and itemVnum <= 53322:
		return 1
	elif itemVnum >= 48301 and itemVnum <= 48301:
		return 1
	elif itemVnum >= 48311 and itemVnum <= 48311:
		return 1
	elif itemVnum >= 48321 and itemVnum <= 48321:
		return 1
	elif itemVnum >= 55103 and itemVnum <= 55105:
		return 1
	return 0

########################

def SET_DEFAULT_FOG_LEVEL():
	global FOG_LEVEL
	app.SetMinFog(FOG_LEVEL)

def SET_FOG_LEVEL_INDEX(index):
	global FOG_LEVEL
	global FOG_LEVEL_LIST
	try:
		FOG_LEVEL=FOG_LEVEL_LIST[index]
	except IndexError:
		FOG_LEVEL=FOG_LEVEL_LIST[0]
	app.SetMinFog(FOG_LEVEL)

def GET_FOG_LEVEL_INDEX():
	global FOG_LEVEL
	global FOG_LEVEL_LIST
	return FOG_LEVEL_LIST.index(FOG_LEVEL)

########################

def SET_DEFAULT_CAMERA_MAX_DISTANCE():
	global CAMERA_MAX_DISTANCE
	app.SetCameraMaxDistance(CAMERA_MAX_DISTANCE)

def GET_SPECIAL_EMOTION_NAME(idx):
	if idx >= 71 and idx <= emotion.EMOTION_WHIRL:
		return emotion.SPECIAL_EMOTION_DICT[idx]["name"]

def Color(hexString):
	return "|cff{}|h".format(hexString)

def TextColor(text, hexString):
	return "|cff{}|h{}|r".format(hexString, text)

def SET_CAMERA_MAX_DISTANCE_INDEX(index):
	global CAMERA_MAX_DISTANCE
	global CAMERA_MAX_DISTANCE_LIST
	try:
		CAMERA_MAX_DISTANCE=CAMERA_MAX_DISTANCE_LIST[index]
	except:
		CAMERA_MAX_DISTANCE=CAMERA_MAX_DISTANCE_LIST[0]

	app.SetCameraMaxDistance(CAMERA_MAX_DISTANCE)

def GET_CAMERA_MAX_DISTANCE_INDEX():
	global CAMERA_MAX_DISTANCE
	global CAMERA_MAX_DISTANCE_LIST
	return CAMERA_MAX_DISTANCE_LIST.index(CAMERA_MAX_DISTANCE)

########################

import chrmgr
import player

def SET_DEFAULT_CHRNAME_COLOR():
	global CHRNAME_COLOR_INDEX
	chrmgr.SetEmpireNameMode(CHRNAME_COLOR_INDEX)

def SET_CHRNAME_COLOR_INDEX(index):
	global CHRNAME_COLOR_INDEX
	CHRNAME_COLOR_INDEX=index
	chrmgr.SetEmpireNameMode(index)

def GET_CHRNAME_COLOR_INDEX():
	global CHRNAME_COLOR_INDEX
	return CHRNAME_COLOR_INDEX

def SET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD(index):
	global VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD
	VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD = index

def GET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD():
	global VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD
	return VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD

def SET_DEFAULT_CONVERT_EMPIRE_LANGUAGE_ENABLE():
	global CONVERT_EMPIRE_LANGUAGE_ENABLE
	net.SetEmpireLanguageMode(CONVERT_EMPIRE_LANGUAGE_ENABLE)

def SET_DEFAULT_USE_ITEM_WEAPON_TABLE_ATTACK_BONUS():
	global USE_ITEM_WEAPON_TABLE_ATTACK_BONUS
	player.SetWeaponAttackBonusFlag(USE_ITEM_WEAPON_TABLE_ATTACK_BONUS)

def SET_DEFAULT_USE_SKILL_EFFECT_ENABLE():
	global USE_SKILL_EFFECT_UPGRADE_ENABLE
	app.SetSkillEffectUpgradeEnable(USE_SKILL_EFFECT_UPGRADE_ENABLE)

def SET_TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE():
	global TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE
	app.SetTwoHandedWeaponAttSpeedDecreaseValue(TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE)

if app.ENABLE_RENDER_TARGET:
	enable_item_preview = 1

########################
import item

ACCESSORY_MATERIAL_LIST = [50623, 50624, 50625, 50626, 50627, 50628, 50629, 50630, 50631, 50632, 50633, 50634, 50635, 50636, 50637, 50638, 50639]
JewelAccessoryInfos = [
		# jewel		wrist	neck	ear
		[ 50634,	14420,	16220,	17220 ],
		[ 50635,	14500,	16500,	17500 ],
		[ 50636,	14520,	16520,	17520 ],
		[ 50637,	14540,	16540,	17540 ],
		[ 50638,	14560,	16560,	17560 ],
		[ 50639,	14570,	16570,	17570 ],
	]
def GET_ACCESSORY_MATERIAL_VNUM(vnum, subType):
	ret = vnum
	item_base = (vnum / 10) * 10
	for info in JewelAccessoryInfos:
		if item.ARMOR_WRIST == subType:
			if info[1] == item_base:
				return info[0]
		elif item.ARMOR_NECK == subType:
			if info[2] == item_base:
				return info[0]
		elif item.ARMOR_EAR == subType:
			if info[3] == item_base:
				return info[0]

	if vnum >= 16210 and vnum <= 16219:
		return 50625

	if item.ARMOR_WRIST == subType:
		WRIST_ITEM_VNUM_BASE = 14000
		ret -= WRIST_ITEM_VNUM_BASE
	elif item.ARMOR_NECK == subType:
		NECK_ITEM_VNUM_BASE = 16000
		ret -= NECK_ITEM_VNUM_BASE
	elif item.ARMOR_EAR == subType:
		EAR_ITEM_VNUM_BASE = 17000
		ret -= EAR_ITEM_VNUM_BASE

	type = ret/20

	if type<0 or type>=len(ACCESSORY_MATERIAL_LIST):
		type = (ret-170) / 20
		if type<0 or type>=len(ACCESSORY_MATERIAL_LIST):
			return 0

	return ACCESSORY_MATERIAL_LIST[type]

##################################################################

def GET_BELT_MATERIAL_VNUM(vnum, subType = 0):
	return 18900

##################################################################

def IS_AUTO_POTION(itemVnum):
	return IS_AUTO_POTION_HP(itemVnum) or IS_AUTO_POTION_SP(itemVnum)

def IS_AUTO_POTION_HP(itemVnum):
	if 72723 <= itemVnum and 72726 >= itemVnum:
		return 1
	elif itemVnum >= 76021 and itemVnum <= 76022:
		return 1
	elif itemVnum == 79012:
		return 1

	return 0

def IS_AUTO_POTION_SP(itemVnum):
	if 72727 <= itemVnum and 72730 >= itemVnum:
		return 1
	elif itemVnum >= 76004 and itemVnum <= 76005:		## 새로 들어간 선물용 수룡의 축복
		return 1
	elif itemVnum == 79013:
		return 1
				
	return 0

def COUNT_SPECIFY_ITEM(itemVnum):
	finalCount = 0
	
	for i in xrange(player.INVENTORY_PAGE_SIZE*player.INVENTORY_PAGE_COUNT):
		if player.GetItemIndex(i) == itemVnum:
			finalCount = finalCount + player.GetItemCount(i)
			
	return finalCount