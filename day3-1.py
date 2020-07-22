# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 09:39:07 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()


while True:
    hits=mc.events.pollProjectileHits()
    if len(hits) >0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        block=mc.getBlock(x,y,z)
        if block==1:
            mc.setBlock(x,y,z,41)