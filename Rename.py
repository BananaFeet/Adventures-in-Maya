import maya.cmds as mc

#Selection
sel = mc.ls(sl = True)
items = sel

#Makes window
win = mc.window()
mc.rowColumnLayout(nc = 2, cw = [(1, 100), (2, 150), (3, 100)])
'''
sel1 = mc.textField()
sel2 = mc.textField()
sel3 = mc.textField()
sel4 = mc.textField()
'''
#For every selected object, show the name and create a textfield!
for count,name in enumerate(items):
     #print(name)
     #print(count)
     mc.text( label=items[count] )
     mc.textField(tx=items[count])
     
'''
mc.textField(sel1, tx=items[0], edit=True)
mc.textField(sel2, tx=items[1], edit=True)
mc.textField(sel3, tx=items[2], edit=True)
mc.textField(sel4, tx=items[3], edit=True)
'''
#sel1text = mc.textField(sel1)
#userTex = mc.textField(sel, query=True, text=True)

mc.showWindow(win)






    
