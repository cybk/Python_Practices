# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:31:43 2025

@author: cybk2
"""
import random

class Spell:
    def __init__(self, name, cost, dmg, type):
        self.cost = cost
        self.name = name
        self.dmg = dmg
        self.type = type
        
    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)