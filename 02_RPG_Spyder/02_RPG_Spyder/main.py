# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:12:20 2025

@author: cybk2
"""

from Classes.game import Person, bcolors
from Classes.magic import Spell

# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create withe magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Instantiate player<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<s
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
enemy= Person(1299, 65, 45, 25, [])

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
    elif index == 1:1
        player.choose_magic()
        magic_choice = int(input("Choose the magic to use: ")) - 1
        
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        
        current_mp = player.get_mp()
        
        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue
        
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " deals: ", str(magic_dmg), "points of damage" + bcolors.ENDC)
        
        
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
