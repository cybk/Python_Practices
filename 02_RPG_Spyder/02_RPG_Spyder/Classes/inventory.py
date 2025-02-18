# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:49:28 2025

@author: cybk2
"""

class Item:
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop

class InventoryItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity