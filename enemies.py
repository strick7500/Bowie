#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:14:42 2019

@author: adamstrick
"""

class Enemy():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def is_alive(self):
        return self.hp > 0
    
class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider",
                         hp=10,
                         damage=2)
        
class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre",
                         hp=30,
                         damage=15)