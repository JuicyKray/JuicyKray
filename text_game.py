import random
import sys

# Map hero selection keys to hero definitions
heroes = {
    'q': {
        'name': 'Assassin',
        'description': 'Fast attacker with low defense.',
        'health': 80,
        'speed': 9,
        'damage': 15,
        'defense': 0.1,
        'abilities': {
            'a': {
                'name': 'Backstab',
                'description': 'High damage, pierces defense.',
                'damage': 25,
                'pierce': True,
                'heal': 0
            },
            's': {
                'name': 'Smoke Bomb',
                'description': 'Reduces next enemy attack by half.',
                'damage': 0,
                'pierce': False,
                'heal': 0,
                'effect': 'reduce'
            },
            'd': {
                'name': 'Evade',
                'description': 'Increase speed temporarily.',
                'damage': 0,
                'pierce': False,
                'heal': 0,
                'effect': 'speed'
            }
        }
    },
    'w': {
        'name': 'Tank',
        'description': 'High defense front liner.',
        'health': 150,
        'speed': 4,
        'damage': 10,
        'defense': 0.4,
        'abilities': {
            'a': {
                'name': 'Shield Bash',
                'description': 'Deal moderate damage.',
                'damage': 15,
                'pierce': False,
                'heal': 0
            },
            's': {
                'name': 'Fortify',
                'description': 'Increase defense.',
                'damage': 0,
                'pierce': False,
                'heal': 0,
                'effect': 'defense'
            },
            'd': {
                'name': 'Taunt',
                'description': 'Force enemy to attack you.',
                'damage': 0,
                'pierce': False,
                'heal': 0,
                'effect': 'taunt'
            }
        }
    },
    'e': {
        'name': 'Support',
        'description': 'Balances healing and damage.',
        'health': 100,
        'speed': 6,
        'damage': 12,
        'defense': 0.2,
        'abilities': {
            'a': {
                'name': 'Magic Bolt',
                'description': 'Standard ranged attack.',
                'damage': 12,
                'pierce': False,
                'heal': 0
            },
            's': {
                'name': 'Heal',
                'description': 'Restore some health.',
                'damage': 0,
                'pierce': False,
                'heal': 20
            },
            'd': {
                'name': 'Inspire',
                'description': 'Boost your damage.',
                'damage': 0,
                'pierce': False,
                'heal': 0,
                'effect': 'boost'
            }
        }
    },
    'r': {
        'name': 'Healer',
        'description': 'Focuses on keeping teammates alive.',
        'health': 90,
        'speed': 5,
        'damage': 8,
        'defense': 0.2,
        'abilities': {
            'a': {
                'name': 'Holy Light',
                'description': 'Small damage, heals self slightly.',
                'damage': 5,
                'pierce': False,
                'heal': 10
            },
            's': {
                'name': 'Greater Heal',
                'description': 'Significantly restore health.',
                'damage': 0,
                'pierce': False,
                'heal': 30
            },
            'd': {
                'name': 'Blessing',
                'description': 'Reduce incoming damage.',
                'damage': 0,
                'pierce': False,
                'heal': 0,
                'effect': 'shield'
            }
        }
    },
    't': {
        'name': 'Mage',
        'description': 'Uses powerful spells with low defense.',
        'health': 80,
        'speed': 7,
        'damage': 18,
        'defense': 0.1,
        'abilities': {
            'a': {
                'name': 'Fireball',
                'description': 'High damage spell.',
                'damage': 22,
                'pierce': True,
                'heal': 0
            },
            's': {
                'name': 'Ice Shield',
                'description': 'Protect yourself, increasing defense.',
                'damage': 0,
                'pierce': False,
                'heal': 0,
                'effect': 'defense'
            },
            'd': {
                'name': 'Arcane Surge',
                'description': 'Boost speed and damage for next turn.',
                'damage': 0,
                'pierce': False,
                'heal': 0,
                'effect': 'surge'
            }
        }
    },
    'y': {
        'name': 'Warrior',
        'description': 'Balanced melee combatant.',
        'health': 110,
        'speed': 6,
        'damage': 14,
        'defense': 0.25,
        'abilities': {
            'a': {
                'name': 'Slash',
                'description': 'Reliable attack.',
                'damage': 14,
                'pierce': False,
                'heal': 0
            },
            's': {
                'name': 'Power Strike',
                'description': 'Stronger attack with chance to pierce.',
                'damage': 20,
                'pierce': True,
                'heal': 0
            },
            'd': {
                'name': 'War Cry',
                'description': 'Increase damage for next attack.',
                'damage': 0,
                'pierce': False,
                'heal': 0,
                'effect': 'boost'
            }
        }
    },
    'u': {
        'name': 'Archer',
        'description': 'Long range attacker.',
        'health': 90,
        'speed': 8,
        'damage': 16,
        'defense': 0.15,
        'abilities': {
            'a': {
                'name': 'Arrow Shot',
                'description': 'Standard arrow attack.',
                'damage': 16,
                'pierce': False,
                'heal': 0
            },
            's': {
                'name': 'Piercing Arrow',
                'description': 'Ignores defense.',
                'damage': 18,
                'pierce': True,
                'heal': 0
            },
            'd': {
                'name': 'Quick Step',
                'description': 'Increase speed for next turn.',
                'damage': 0,
                'pierce': False,
                'heal': 0,
                'effect': 'speed'
            }
        }
    },
    'i': {
        'name': 'Knight',
        'description': 'Sturdy fighter with healing capability.',
        'health': 120,
        'speed': 5,
        'damage': 13,
        'defense': 0.3,
        'abilities': {
            'a': {
                'name': 'Sword Slash',
                'description': 'Basic attack.',
                'damage': 13,
                'pierce': False,
                'heal': 0
            },
            's': {
                'name': 'Holy Strike',
                'description': 'Attack that heals you slightly.',
                'damage': 15,
                'pierce': False,
                'heal': 5
            },
            'd': {
                'name': 'Guardian Shield',
                'description': 'Reduce damage taken next turn.',
                'damage': 0,
                'pierce': False,
                'heal': 0,
                'effect': 'shield'
            }
        }
    },
    'o': {
        'name': 'Summoner',
        'description': 'Commands minions and uses magic.',
        'health': 85,
        'speed': 6,
        'damage': 14,
        'defense': 0.2,
        'abilities': {
            'a': {
                'name': 'Summon Minion',
                'description': 'Call a minion for extra attack.',
                'damage': 18,
                'pierce': False,
                'heal': 0
            },
            's': {
                'name': 'Dark Pact',
                'description': 'High damage to enemy but hurts you.',
                'damage': 25,
                'pierce': True,
                'heal': -5
            },
            'd': {
                'name': 'Life Drain',
                'description': 'Steal health from enemy.',
                'damage': 12,
                'pierce': False,
                'heal': 12
            }
        }
    },
    'p': {
        'name': 'Paladin',
        'description': 'Holy warrior with balanced abilities.',
        'health': 110,
        'speed': 5,
        'damage': 13,
        'defense': 0.3,
        'abilities': {
            'a': {
                'name': 'Smite',
                'description': 'Deal holy damage.',
                'damage': 16,
                'pierce': False,
                'heal': 0
            },
            's': {
                'name': 'Lay on Hands',
                'description': 'Massive heal.',
                'damage': 0,
                'pierce': False,
                'heal': 40
            },
            'd': {
                'name': 'Divine Shield',
                'description': 'Become immune next turn.',
                'damage': 0,
                'pierce': False,
                'heal': 0,
                'effect': 'immune'
            }
        }
    }
}

# Basic enemy definitions (less descriptive, as requested)
enemies = {
    'q': {
        'name': 'Goblin',
        'health': 70,
        'speed': 7,
        'damage': 10,
        'defense': 0.1,
        'abilities': [
            {'name': 'Stab', 'damage': 10, 'pierce': False, 'heal': 0},
            {'name': 'Quick Heal', 'damage': 0, 'pierce': False, 'heal': 15},
            {'name': 'Sneak', 'damage': 15, 'pierce': True, 'heal': 0},
        ]
    },
    'w': {
        'name': 'Orc',
        'health': 120,
        'speed': 5,
        'damage': 15,
        'defense': 0.25,
        'abilities': [
            {'name': 'Cleave', 'damage': 18, 'pierce': False, 'heal': 0},
            {'name': 'Roar', 'damage': 0, 'pierce': False, 'heal': 0},
            {'name': 'Orcish Heal', 'damage': 0, 'pierce': False, 'heal': 20},
        ]
    },
    'e': {
        'name': 'Skeleton',
        'health': 60,
        'speed': 6,
        'damage': 12,
        'defense': 0.1,
        'abilities': [
            {'name': 'Bone Slash', 'damage': 12, 'pierce': False, 'heal': 0},
            {'name': 'Bone Shield', 'damage': 0, 'pierce': False, 'heal': 0},
        ]
    },
    'r': {
        'name': 'Bandit',
        'health': 90,
        'speed': 8,
        'damage': 15,
        'defense': 0.2,
        'abilities': [
            {'name': 'Cutthroat', 'damage': 16, 'pierce': True, 'heal': 0},
            {'name': 'Steal', 'damage': 0, 'pierce': False, 'heal': 10},
        ]
    },
    't': {
        'name': 'Wraith',
        'health': 80,
        'speed': 9,
        'damage': 13,
        'defense': 0.15,
        'abilities': [
            {'name': 'Haunt', 'damage': 14, 'pierce': True, 'heal': 0},
            {'name': 'Fade', 'damage': 0, 'pierce': False, 'heal': 0},
        ]
    },
    'y': {
        'name': 'Golem',
        'health': 150,
        'speed': 3,
        'damage': 20,
        'defense': 0.35,
        'abilities': [
            {'name': 'Smash', 'damage': 20, 'pierce': False, 'heal': 0},
            {'name': 'Stone Skin', 'damage': 0, 'pierce': False, 'heal': 0},
        ]
    },
    'u': {
        'name': 'Vampire',
        'health': 100,
        'speed': 7,
        'damage': 16,
        'defense': 0.2,
        'abilities': [
            {'name': 'Bite', 'damage': 16, 'pierce': False, 'heal': 8},
            {'name': 'Dark Mist', 'damage': 0, 'pierce': False, 'heal': 0},
        ]
    },
    'i': {
        'name': 'Werewolf',
        'health': 110,
        'speed': 7,
        'damage': 18,
        'defense': 0.25,
        'abilities': [
            {'name': 'Claw', 'damage': 18, 'pierce': False, 'heal': 0},
            {'name': 'Howl', 'damage': 0, 'pierce': False, 'heal': 0},
        ]
    },
    'o': {
        'name': 'Demon',
        'health': 130,
        'speed': 6,
        'damage': 22,
        'defense': 0.3,
        'abilities': [
            {'name': 'Hellfire', 'damage': 22, 'pierce': True, 'heal': 0},
            {'name': 'Demonic Heal', 'damage': 0, 'pierce': False, 'heal': 25},
        ]
    },
    'p': {
        'name': 'Dragon',
        'health': 160,
        'speed': 6,
        'damage': 25,
        'defense': 0.35,
        'abilities': [
            {'name': 'Fire Breath', 'damage': 25, 'pierce': True, 'heal': 0},
            {'name': 'Scale Harden', 'damage': 0, 'pierce': False, 'heal': 0},
        ]
    }
}

# Basic helper functions

def display_stats(hero, enemy):
    print("\n=== BATTLE STATS ===")
    print(f"Hero: {hero['name']}  HP:{hero['health']}/{hero['max_health']}  "
          f"DMG:{hero['damage']}  DEF:{int(hero['defense']*100)}%  SPD:{hero['speed']}")
    print(f"Enemy: {enemy['name']}  HP:{enemy['health']}/{enemy['max_health']}  "
          f"DMG:{enemy['damage']}  DEF:{int(enemy['defense']*100)}%  SPD:{enemy['speed']}\n")

def hero_turn(hero, enemy):
    while True:
        print("Choose ability:")
        for key, ability in hero['abilities'].items():
            print(f" [{key}] {ability['name']} - {ability.get('description','')}")
        choice = input("Action (a/s/d): ").strip().lower()
        if choice in hero['abilities']:
            ability = hero['abilities'][choice]
            execute_ability(hero, enemy, ability)
            break
        else:
            print("Invalid ability. Try again.")


def enemy_turn(hero, enemy):
    # Simple AI: heal if low and have heal
    healing_abilities = [a for a in enemy['abilities'] if a.get('heal',0) > 0]
    if enemy['health'] <= enemy['max_health'] * 0.3 and healing_abilities:
        ability = healing_abilities[0]
    else:
        ability = random.choice(enemy['abilities'])
    print(f"Enemy uses {ability['name']}!")
    execute_ability(enemy, hero, ability)


def execute_ability(attacker, defender, ability):
    dmg = ability.get('damage',0)
    heal = ability.get('heal',0)
    if dmg > 0:
        if ability.get('pierce'):
            final_damage = dmg
        else:
            final_damage = int(dmg * (1 - defender['defense']))
        defender['health'] -= final_damage
        print(f"{attacker['name']} deals {final_damage} damage!")
    if heal != 0:
        attacker['health'] = min(attacker['max_health'], attacker['health'] + heal)
        if heal > 0:
            print(f"{attacker['name']} heals {heal} HP!")
        else:
            print(f"{attacker['name']} suffers {-heal} recoil HP!")


def battle(hero, enemy):
    hero['max_health'] = hero['health']
    enemy['max_health'] = enemy['health']
    turn = 'hero' if hero['speed'] >= enemy['speed'] else 'enemy'
    while hero['health'] > 0 and enemy['health'] > 0:
        display_stats(hero, enemy)
        if turn == 'hero':
            hero_turn(hero, enemy)
            turn = 'enemy'
        else:
            enemy_turn(hero, enemy)
            turn = 'hero'
    display_stats(hero, enemy)
    if hero['health'] > 0:
        print("You win!")
    else:
        print("Enemy wins!")


def choose_character(characters, prompt, show_description):
    while True:
        print(prompt)
        for key, info in characters.items():
            desc = f" - {info['description']}" if show_description else ''
            print(f" [{key}] {info['name']}{desc}")
        choice = input("Select: ").strip().lower()
        if choice in characters:
            return characters[choice]
        else:
            print("Invalid choice. Try again.")


def main():
    print("=== Text Battle Game ===")
    hero = choose_character(heroes, "Choose your hero:", True)
    enemy = choose_character(enemies, "Choose your enemy:", False)
    battle(hero, enemy)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
