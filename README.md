# Defect_Detection

combine_A_and_B.py

This is used to create one image from the PreProcessed Dataset of GAN.
A=> Folder that contains the original Dataset Images
B=> Folder that contains the Masked Dataset Images
Folder A and B must have the same structure, Same number of images, Same images Names
The Structure of those folders has to contain:
1-Train Folder
2-Val Folder
3-Test Folder

Command:
python datasets/combine_A_and_B.py --fold_A /pasth/to/folder/A --fold_B /path/to/folder/B --fold_AB /datasets/data
