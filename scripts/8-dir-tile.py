import bpy
import logging
import copy
from math import radians

scene = bpy.data.scenes["Scene"]
TILE_PREFIX = "tile"
original_path = bpy.data.scenes[0].render.filepath

def hideChildren(ob,bVal):
    for child in ob.children:
        child.hide = bVal
        child.hide_render = bVal
        hideChildren(child,bVal)

def hide(objName,bVal):
    bpy.data.objects[objName].hide = bVal
    bpy.data.objects[objName].hide_render = bVal
    hideChildren(bpy.data.objects[objName], bVal)

def showAll():
    for ob in bpy.data.objects:
        if ob.name != "" and ob.name.startswith(TILE_PREFIX):
            hide(ob.name, False)
    
def hideOthers(onObjectName):
    for ob in bpy.data.objects:
        if ob.name != "" and ob.name.startswith(TILE_PREFIX):
            if ob.name != onObjectName:
                hide(ob.name, True)
            else:
                hide(ob.name, False)

def snapshot(objName):
    showAll()
    hideOthers(objName) 
    curr = bpy.data.objects[objName]
    prev = copy.deepcopy(curr.location)
    bpy.data.scenes[0].render.filepath = original_path + objName
    curr.location.x = 0
    curr.location.y = 0
    bpy.ops.render.render(animation=True)
    curr.location = prev
    bpy.data.scenes[0].render.filepath = original_path
    showAll() 


snapshot("tile-left")
snapshot("tile-right")
snapshot("tile-top")
snapshot("tile-bottom")
snapshot("tile-ne")
snapshot("tile-nw")
snapshot("tile-se")
snapshot("tile-sw")
snapshot("tile-corner-right")
snapshot("tile-corner-left")
snapshot("tile-corner-top")
snapshot("tile-corner-bottom")
snapshot("tile-main")
