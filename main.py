from sim import Unit, battle

# sample stats for Ordinary Joe
joe_stats = {
    "HP": 25, "MP": 15, "ATK": 15, "DEF": 5,
    "ACC": 0.05, "EVA": 0.05, "CRIT": 0.01,
    "SPD": 2, "MORALE": 15, "STABILITY": 15
}

# create two Joes
joe_a = Unit("Joe A", joe_stats)
joe_b = Unit("Joe B", joe_stats)

# run battle
log = battle(joe_a, joe_b)

# print result
for line in log:
    print(line)
