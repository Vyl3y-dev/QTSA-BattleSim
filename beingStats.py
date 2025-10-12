from characterStats import CharacterStats 

class BeingStats:
    def beingStats():
        wellbeing = CharacterStats.endurance + CharacterStats.insight + CharacterStats.willpower + CharacterStats.confidence + CharacterStats.focus
        
        print(wellbeing)