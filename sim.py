import random

# --- Data containers ---
class Unit:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats.copy()  # dict of stats
        self.sleep = 0             # turns left asleep
        self.alive = True

    def take_damage(self, amount):
    # subtract HP
        self.stats["HP"] -= amount

    # if HP drops below 0, clamp it to 0
        if self.stats["HP"] <= 0:
            self.stats["HP"] = 0
            self.alive = False


    def pay_mp(self, cost):
        # reduce MP if enough, return True/False
        pass


# --- Formula functions ---

def hit_chance(att, deff):
    didItHit = 0.95 + (att.stats["ACC"] - deff.stats["EVA"])
    return max(0.05, min(didItHit, 0.99))
    pass

def damage_amount(att, deff, power=1.0, mods=1.0):
    variance = random.uniform(0.9, 1.1)
    dmg = att * power - (deff * mods) + variance
    return dmg
    pass

def status_success(caster_morale, target_stability, base_status_chance):
    status_hits = base_status_chance + (caster_morale.stats["MORALE"] / 2) - (target_stability.stats["STABILITY"] / 2)
    return status_hits
    pass


# --- Actions ---
def action_strike(att, deff, log):
    chance = hit_chance(att, deff)
    if random.random() > chance:
        log.append(f"{att.name} uses STRIKE -> MISS ({chance*100:.0f}%).")
        return
    
    dmg = damage_amount(att, deff, power=1.0, mods=1.0)
    deff.take_damage(dmg)

    log.append(f"{att.name} uses Strike → {deff.name} takes {dmg} dmg. "f"({deff.stats['HP']} HP left)")
    pass

def action_sleep(att, deff, log):
    chance = status_success(caster_morale, target_stability, base_status_chance)

    if chance <= 0:
        log.append(f"{att.name} uses SLEEP -> MISS ({chance*100:.0f}%).")
    else:
        log.append(f"{att.name} uses SLEEP -> HITS ({chance*100:.0f}%), {deff.name} is now ASLEEP for 2 turns...")
        return
    
    
    pass


# --- Battle loop ---
def battle(unit_a, unit_b, max_rounds=20):
    log = []
    # fixed order at start
    turn_order = sorted([unit_a, unit_b], key=lambda u: u.stats["SPD"], reverse=True)

    for rnd in range(1, max_rounds + 1):
        log.append(f"\n[Round {rnd}]")

        for actor in turn_order:
            # skip if dead
            if not actor.alive:
                continue

            # skip if asleep
            if actor.sleep > 0:
                actor.sleep -= 1
                log.append(f"{actor.name} is asleep and skips the turn. (SLP now {actor.sleep})")
                continue

            # pick and execute action (AI/player input here)
            # e.g. action_strike(actor, target, log)

            # check if battle ended
            # break out if one unit is KO
            if not all(u.alive for u in turn_order):
                break

        # stop battle early if someone is KO
        if not all(u.alive for u in turn_order):
            break

    return log

