import random

print("Hopefully, this is working Yoan!")

characterStats = {"Academics": 5, "Charisma": 5, "Creativity": 5, "Endurance": 5, "Insight": 5, "Willpower": 5, "Confidence": 5, "Focus": 5, "Adaptability": 5}

print(characterStats)

wellbeingHP = characterStats["Endurance"] + characterStats["Insight"] + characterStats["Willpower"] + characterStats["Confidence"] + characterStats["Focus"]

drive = characterStats["Academics"] + characterStats["Charisma"] + characterStats["Creativity"]

force = characterStats["Willpower"] + characterStats["Confidence"] + characterStats["Focus"]

defense =  characterStats["Endurance"]

accuracy = characterStats["Adaptability"]

evasion = characterStats["Insight"]

breakthrough = characterStats["Academics"] + (characterStats["Focus"] / 2)

speed = 2

morale = characterStats["Charisma"] + characterStats["Confidence"] + characterStats["Focus"]

stability = characterStats["Endurance"] + characterStats["Willpower"] + characterStats["Focus"]

print("HP: ", wellbeingHP, "MANA: ", drive, "ATK: ", force, "DEF: ", defense, "ACC: ", accuracy, "EVA: ", evasion, "CRIT: ", breakthrough, "SPD: ", speed, "MORALE: ", morale, "STABILITY: ", stability)


def attackDMG(attacker, defender):
    attackerSP = 1
    defenseMods = 1
    attackerCRIT = 1
    variance = random.uniform(0.9, 1.1)

    dmg = ((attacker["force"] * attackerSP) - (defender["defense"] * defenseMods))
    dmg *= (attacker["breakthrough"] * attackerCRIT)
    dmg *= variance  # apply your ±10%

    if dmg < 1:
        dmg = 0
        print("No damage dealt due to low output or variance.")

    return dmg

attacker = {"name": "Joe", "force": force, "breakthrough": breakthrough}
defender = {"name": "Goblin", "defense": defense}



print(attackDMG(attacker, defender))