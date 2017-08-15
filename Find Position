import maya.cmds as mc

#Will print out translation and rotation of selected object.
def findPosition():
    sel = mc.ls(sl=True)
    trans = mc.xform(sel, ws=True, q=True, t=True)
    rot = mc.xform(sel, ws=True, q=True, ro=True)  
    tx, ty, tz = trans[0], trans[1], trans[2]
    rx, ry, rz = rot[0], rot[1], rot[2]
    
    #Might change to return values
    print(trans)
    print(rot)
    
#If there is no function call, nothing will happen. 
findPosition()
