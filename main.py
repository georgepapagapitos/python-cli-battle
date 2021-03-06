from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
blizzard = Spell("Blizzard", 15, 150, "black")
thunder = Spell("Thunder", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create Items
potion = Item("Potion", "potion", "A simple potion. Heals 50 HP", 50)
hiPotion = Item("Hi Potion", "potion", "A Hi-Potion. Heals 100 HP", 100)
superPotion = Item("Super Potion", "potion", "A Super Potion. Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
megaElixir = Item("Mega Elixir", 'elixir', "Fully restores the party's HP/MP", 9999)
grenade = Item("Grenade", 'weapon', "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, quake, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 10},
                {"item": hiPotion, "quantity": 5},
                {"item": superPotion, "quantity": 2},
                {"item": elixir, "quantity": 5},
                {"item": megaElixir, "quantity": 2},
                {"item": grenade, "quantity": 1}]

# Create Characters
player1 = Person("Hannah", 460, 65, 60, 34, player_spells, player_items)
player2 = Person("Ruby  ", 460, 65, 60, 34, player_spells, player_items)
player3 = Person("Mia   ", 460, 65, 60, 34, player_spells, player_items)
enemy = Person("Greg", 1200, 65, 45, 25, [], [])

players = [player1, player2, player3]

running = True
i = 0

while running:
    print("===================")

    print("\n\n")
    print("NAME                 HP                                    MP")
    for player in players:
        player.get_stats()

    print("\n")
    print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS!!' + bcolors.ENDC)
    for player in players:
        player.choose_action()
        choice = input("    Choose an action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_dmg()
            enemy.take_dmg(dmg)
            print("You attacked for", dmg, "points of damage.")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose a spell: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_dmg()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg) + bcolors.ENDC)
            elif spell.type == "black":
                enemy.take_dmg(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixir":
                player.hp = player.max_hp
                player.mp = player.max_mp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "weapon":
                enemy.take_dmg(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " hits the enemy for " + str(item.prop), "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_dmg()
    player1.take_dmg(enemy_dmg)
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
