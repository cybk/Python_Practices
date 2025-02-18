# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:12:20 2025

@author: cybk2
"""

from Classes.game import Person, bcolors
from Classes.magic import Spell
from Classes.inventory import Item, InventoryItem

# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create withe magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create some items
potion = Item("Potion", "potion", "Heals 50 hp", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 hp", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 hp", 500)
elixer = Item("Elixer", "elixer", "Fully restored HP/MP", 9999)
hielixer = Item("Mega Elixer", "elixer", "Fully restored HP/MP", 9999)

grenade = Item("grenade", "attack", "deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [InventoryItem(potion, 15),
                InventoryItem(hipotion, 5),
                InventoryItem(superpotion, 5),
                InventoryItem(elixer, 5),
                InventoryItem(hielixer, 2),
                InventoryItem(grenade, 5)]

# Instantiate player<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy= Person(1299, 65, 45, 25, [], [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKs!" + bcolors.ENDC)

while running:
    print("=====================")
    
    player.choose_Action()
    choice = input("Choose action: ")
    index = int(choice) - 1
    
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You atacked for: ", dmg, " points of damage. Enemy HP: ", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose the magic to use: ")) - 1
        
        if magic_choice == - 1:
            continue
        
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        
        current_mp = player.get_mp()
        
        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue
        
        player.reduce_mp(spell.cost)
        
        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for ", str(magic_dmg), "HP." + bcolors().ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals: ", str(magic_dmg), "points of damage" + bcolors.ENDC)
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item: ")) - 1
        
        if item_choice == - 1:
            continue
        
        item = player.items[item_choice].item

        if player.items[item_choice].quantity == 0:
            print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
            continue

        player.items[item_choice].quantity -= 1

        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " heals for: ", item.prop, " HP" + bcolors.ENDC)
        elif item.type == "elixer":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + "\n" + item.name + " deals" + str(item.prop) + bcolors.ENDC)
        
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for ", enemy_dmg, "Player HP: ", player.get_hp())
    
    print("----------------------------------")
    print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    
    print("\nYour HP", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("\nYour MP", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)
    
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Enemy has defeater you!!" + bcolors.ENDC)
        running = False
