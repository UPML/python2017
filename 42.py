import json


class creature(object):
    def __init__(self, data):
        if "mana" not in data.keys():
            data["mana"] = 0
        self.__dict__ = data
        if self.race == "Sorceress":
            self.max_health = 50
            self.max_defence_power = 42
            self.max_attack_power = 90
            self.max_mana = 200

        if self.race == "Knight":
            self.max_health = 100
            self.max_defence_power = 170
            self.max_attack_power = 150
            self.max_mana = 0

        if self.race == "Barbarian":
            self.max_health = 120
            self.max_defence_power = 150
            self.max_attack_power = 180
            self.max_mana = 0

        if self.race == "Warlock":
            self.max_health = 70
            self.max_defence_power = 50
            self.max_attack_power = 100
            self.max_mana = 100


def cast_damage_spell(attack, defend, power):
    if attack.health == 0 or power > attack.mana:
        return
    attack.mana -= power

    damage = max(0, power - defend.defence)
    defend.health -= damage
    defend.health = max(0, defend.health)
    defend.experience += 1
    attack.experience += 5 if defend.health == 0 else 1


def cast_health_spell(attack, defend, power):
    if attack.health == 0 or power > attack.mana or defend.health == 0:
        return
    attack.mana -= power
    defend.defence -= power
    defend.defence = max(0, defend.defence)
    defend.health += power
    defend.health = min(defend.health, defend.max_health)
    attack.experience += 1


def attack(attack, defend, power):
    if attack.health == 0 or attack.attack < power:
        return
    attack.attack -= power

    damage = max(0, power - defend.defence)
    defend.defence -= power
    defend.defence = max(0, defend.defence)
    defend.health -= damage
    defend.health = max(0, defend.health)
    defend.experience += 1
    attack.experience += 5 if defend.health == 0 else 1


functional_list = {'cast_damage_spell': cast_damage_spell,
                   'cast_health_spell': cast_health_spell}

with open('input.txt') as f:
    battle = json.load(f)
    army = dict()
    for key in battle["armies"].keys():
        army[key] = creature(battle["armies"][key])

    for action in battle["battle_steps"]:
        if action["action"] == 'cast_damage_spell':
            cast_damage_spell(army[action["id_from"]],
                              army[action["id_to"]], action["power"])

        if action["action"] == 'cast_health_spell':
            cast_damage_spell(army[action["id_from"]],
                              army[action["id_to"]], action["power"])

        if action["action"] == 'cast_damage_spell':
            cast_damage_spell(army[action["id_from"]],
                              army[action["id_to"]], action["power"])

    score = {"Ronald": 0,
             "Archibald": 0}

    creatures = {"Ronald": 0,
                 "Archibald": 0}
    for creat in army.values():
        if creat.health > 0:
            score[creat.lord] += creat.experience + \
                                 max(0, creat.defence) * 2 + \
                                 max(0, creat.attack) * 3 + \
                                 max(0, creat.mana) * 10
            creatures[creat.lord] += 1
    if score["Ronald"] > score["Archibald"] or \
            (creatures["Archibald"] == 0 and creatures["Ronald"] > 0):
        print("Ronald")
    elif score["Ronald"] < score["Archibald"] or \
            (creatures["Archibald"] > 0 and creatures["Ronald"] == 0):
        print("Archibald")
    else:
        print('unknown')
