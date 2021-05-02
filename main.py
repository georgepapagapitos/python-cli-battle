from classes.game import Person, bcolors
from classes.magic import Spell

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
blizzard = Spell("Blizzard", 15, 150, "black")
thunder = Spell("Thunder", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

player = Person(460, 65, 60, 34, [fire, thunder, blizzard, quake, meteor, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS!!' + bcolors.ENDC)

while running:
    print("===================")
    player.choose_action()
    choice = input("Choose an action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_dmg()
        enemy.take_dmg(dmg)
        print("You attacked for", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose a spell:")) - 1
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_dmg()
        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)
        enemy.take_dmg(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_dmg()
    player.take_dmg(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage.")

    print("-------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("Player HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Player MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You defeated the enemy!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You died!" + bcolors.ENDC)
        running = False
