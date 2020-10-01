import math
import mathutils
import bpy


anchor = bpy.data.objects['Anchor']

orig_filepath = bpy.data.scenes[0].render.filepath

for pos in range(1, 8):
    anchor.rotation_euler[2] = math.radians(-45 * pos)
    #Name the Filename 
    num = str(pos)
    print(num)
    bpy.data.scenes[0].render.filepath = orig_filepath + '/Rotation' + num  + '/Rotation_' + num + '_'
    bpy.ops.render.render(animation=True)

#restore filepath
bpy.data.scenes[0].render.filepath = orig_filepath
