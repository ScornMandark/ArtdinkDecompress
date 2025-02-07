# ArtdinkDecompress
Tool for extracting the graphic and model assets from encrypted and compressed psp games by Artdink

This QuickBMS script is used in conjunction with the macross_pidx.bms and macross_fsts.bms scripts.
Once both of those scripts have been run on the extracted archives, this tool will scan .gim and .gmo files, determine if they are encrypted or compressed, and then decrypt and decompress as necessary.
If you select the output folder as the input folder, then it can overwrite those files directly.
Have fun!  This has been tested on Gundam Battle, Macross Ace Frontier, Macross Ultimate Frontier, and Macross Triangle Frontier.
