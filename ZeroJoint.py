'''
Zeroes out Joint rotations. Aim constraint must be created between selected joints
Aim constraint must have the secondary and primary axis set up correctly first.
WIP: To include an option for choosing a primary and secondary axis to orient to.
'''
import maya.cmds as mc

# Make sure selection(s) are "joints"
sel = mc.ls(sl=True, type="joint")

# For all the joints that are selected, execute the following condition.
for AllJnts in sel:
    # If 'aimConstraint exists, delete it.
    if mc.objExists(AllJnts + "_aimConstraint*"):
        mc.delete(AllJnts + "_aimConstraint*")

    # Get the original joint rotations for x, y, z...
    ori_x = mc.getAttr(AllJnts + ".rx")
    ori_y = mc.getAttr(AllJnts + ".ry")
    ori_z = mc.getAttr(AllJnts + ".rz")

    # Set the values to original joint rotations.
    mc.setAttr(AllJnts + ".jointOrientX", ori_x)
    mc.setAttr(AllJnts + ".jointOrientY", ori_y)
    mc.setAttr(AllJnts + ".jointOrientZ", ori_z)

    # Now Zero out the rotate channels for selected joints.
    mc.setAttr(AllJnts + ".rx", 0)
    mc.setAttr(AllJnts + ".ry", 0)
    mc.setAttr(AllJnts + ".rz", 0)