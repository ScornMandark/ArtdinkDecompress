# ArtdinkDecompress
Tool for extracting the graphic and model assets from encrypted and compressed psp games by Artdink

This QuickBMS script is used in conjunction with the macross_pidx.bms and macross_fsts.bms scripts.
Once both of those scripts have been run on the extracted archives, this tool will scan .gim and .gmo files, determine if they are encrypted or compressed, and then decrypt and decompress as necessary.
If you select the output folder as the input folder, then it can overwrite those files directly.
Have fun!  This has been tested on Gundam Battle, Macross Ace Frontier, and Macross Ultimate Frontier.

I got annoyed manually assigning textures to the models, so I made a blender script for it.  After you batch process the .gim to .png and the .gmo to .fbx, import your .fbx into blender and save the .blend file at the root of the folder structure you're using for organizing all of these.  Select the objects you want to map, then run the script.  It'll search the root folder of the .blend file and all subfolders for image textures that contain the material name (minus the 4 digit prefix + underscore).  If it finds one, it'll assign it to the color and alpha channels.  If not, it defaults to a white color so you can tell when it didn't work.
