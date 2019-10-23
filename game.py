#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:03:32 2019

@author: adamstrick
"""

import world
from player import Player

def play():
    world.load_tiles()
    player = Player()
    while player.is_alive() and not player.victory:
        #Loop begins here