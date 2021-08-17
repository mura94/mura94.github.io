---
layout: post
title: Baking Chain Armatures in Blender (Correctly)
subtitle: The exhausting work-around to accurately bake bone poses to animations with a Spline IK constraint bone modifier in Blender
tags: [Resources, Blender, Animation, 3D Modeling]
---

# Creating & Baking Chain Armatures in Blender Without Artifacts

Exporting animations to GLTF 2.0 from Blender has several limitations, especially when converting these files into USDZ files for Apple's AR Quick Look in Safari. One of the most difficult for me to navigate is how .usd format currently does *not* support shape keys. This makes planning & creating animations that require mesh deformation quite difficult.

However, while shape keys may not be available at this time, bone deformations and animated bones *are* supported... to an extent. If your armature requires any sort of Blender constraint, that must be baked into the animation before it can be exported.

The steps I will lay out below describe a design pattern that will allow you to successfully rig, animate, bake, and export a chain/rope-like mesh that can be manipulated using a hooked bezier curve. It is tedious, but once the initial constraints and "middle-man" transform conversion rigs are set up, animating, baking, and exporting can be done rather quickly.

# Step by Step Process

### Curve & Mesh
Define the shape of a mesh using a curve

- Create **bezier curve**. This will define the shape of your mesh
- Create some mesh (like a cylinder or whatever) that matches the bezier curve's length with *plenty* of ring cuts
  - We'll call this the **chain mesh**

### Hook Armature
Using an armature to manipulate a curve's control points

- In Object mode, create a new armature with `Add>Armature`
  -  We will call this the **hook armature**
- In Edit mode, set the armature's root bone at zero/curve origin/wherever
- Add a new bone and disconnect it from the root with `Alt+P`
- Before the next step, make sure you can enter Pose mode and Edit mode simultaneously with `Edit>Lock Object Modes` set to `False`
- Select the **hook armature**, enter Pose mode, and select a disconnected bone (not the root bone)
  - Shift-select the **bezier curve** and enter Edit mode
  - Select a control point on the curve, then hook the associated control point to the selected bone with `Ctrl+H>Hook to Selected Object Bone`
  - Do this for every bone & control point pair (*but **not** for the root bone*)

### Chain Armature

- Create chain armature
  - root bone at the start of the chain mesh you created
  - extrude a bone to each edge ring in the chain (depending on your mesh, it could as many bones as you want depending on how smoothly you want your mesh to bend. I've tried as many as 50) and it exports to gltf 2.0 just fine
  - Parent your chain mesh to the armature with automatic weights
- In Pose mode, select the **last** bone in the chain armature and add a **Spline IK** constraint
  - in the Spline IK constraint settings, set the **Chain Length** value to match the amount of bones in the chain armature
    - `Tip:` You may also want to set the resolution of your bezier curve to match the amount of bones in the chain armature as well for accuracy
- Animate the bezier curve by keyframing the location, rotation, & scale of the **hook armature** bones. The control points of your curve will automatically match the pose of their hooked bone.

### Bone Matching Armature

- When you're happy with your animation, duplicate the **chain armature** heirarchy (including the rigged chain mesh). This will be what we can call the **bone matching armature**
  - Delete the Spline IK constraint on the last bone of the **bone matching armature**
  - In Pose mode, select all bones in the **bone matching armature** and press `Shift+Ctrl+C` to "Add Constraint (with Targets)" and select the "Copy Transforms" constraint to add this constraint to all bones. 
    - In the Copy Transforms constraint, set the `Target` field's value to your **chain armature**
  - *(this one is tedious)* One by one, select a bone in the **bone matching armature** and set the `Bone` field of that bone's `Copy Transforms` constraint to be the matching relative bone in the **chain armature**. This may take some time depending on how many bones are in your chain. The bone will copy the pose of the reltive bone on the other armature. By the end, you should see no difference between the two rigs, and they should animate exaclty the same way.
  - In Edit mode, select all bones in your **bone matching armature** and press `Alt+P` and select `Clear Parent` to clear the parent of every bone (You should see no visual changes after doing this)
    - This step is **very important** when it comes to finally baking the animation, as it ensures that each bone scales individually, so the scale of a bone will *not* affect the transform of each succeeding bone in the chain
  
  *(you may hide the **chain armature** and **hook armature** by now)*
  
  ### Animation Baking

  - In Pose mode, select all of the bones in your **bone matching armature** and bake the armature's animation with `Pose>Animation>Bake Action...`
    - Before you select `OK`, match these settings:
      - [x] Only Selected Bones
      - [x] Visual Keying
      - [x] Clear Constraints
      - [ ] Clear Parents
      - [x] Overwrite Current Action
      - [ ] Clean Curves **optional*
      -  **`[Pose]`**  `[Object]`
   -  Click **`[OK]`** to bake the animation. You should see little-to-no difference between the baked chain and your original chain armature's poses. We will call this new armature the **baked armature**.
-  Finally, right-click on the **baked armature** in the heirarchy window and select `Select Heirarchy` to ensure you have the armature *and* mesh selected before you export
   -  Export the selected objects as a .glb file with `File>Export>gltf 2.0 (.glb/.gltf)`
   -  Ensure in your export settings that `Include>Limit to Selected Objects` is **checked** 

You should have a proper .glb file of your animated chain. If you want, you can convert the model to usdz using Reality Converter, `<model-veiwer>`, or command line tools that are offered by Apple or Google.