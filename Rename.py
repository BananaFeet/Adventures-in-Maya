'''Rename items in scene'''


import maya.cmds as mc

obj = mc.ls(sl = True)

print obj

# Creates a prompt dialogue box
result = mc.promptDialog(
		title='Rename Object ',
		message='Enter Name:',
		button=['OK', 'Cancel'],
		defaultButton='OK',
		cancelButton='Cancel',
		dismissString='Cancel')

#function
if result == 'OK':
	userTex = mc.promptDialog(query=True, text=True)
	mc.rename(obj, userTex)
#print mc.ls(sl = True)