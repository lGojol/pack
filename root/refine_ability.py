import player

REFINE_ABILITY_SKILL_ID = 132;
REFINE_PERCENTAGE_LEVEL_ADD = 3; #How many % gives each level.
MAX_LEVEL = 10; #MUST BE EDITED IN SKILL_PROTO TOO AND MORE FILES!!!!

def GetAddedPercentage():
	slotIndex = player.GetSkillSlotIndex(REFINE_ABILITY_SKILL_ID)
	skillLevel = player.GetSkillLevel(slotIndex)
	
	return skillLevel*REFINE_PERCENTAGE_LEVEL_ADD