#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:42:28 2019

@author: adamstrick
"""

import items

class Player():
    def __init__(self):
        self.inventory = [items.Gold(15), items.Rock()]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False
        
    def is_alive(self):
        return self.hp > 0
    
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')