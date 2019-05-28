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

===============================================================================================

to_csv.py

This is the code that I used to convert from the XML annotations of YOLO to CSV annotations, to be used in "Apply_Mask_to_Image" to have the diminsions of the mask area.


command:
python to_csv.py --type xml /path/to/xmlAnnotationFolder /path/to/csvOutputFile

===============================================================================================

Apply_Mask_to_Image.ipynb

This is the code that I used to Add the Mask to the image, Using a textfile that contains the images names.
ImagesNames.txt file was created using ls > ImagesNames.txt in linux environment.
The output of this Ipynb is the Masked images.

===============================================================================================

XMLImages Folder:

Contains the Annotated dataset results, for each image there is an xml file contains the diminsions of the label in this image.
The labeling was done using this repository: https://github.com/Cartucho/OpenLabeling which is recommended to be used. It has 2 kinds of output, Whether the XML file or a text file contains the dimenstions which I will use for YOLO.

===============================================================================================

MaskDimenstions Folder:

Contains the CSV files generated from the "to_csv.py" code.
There is an CSV file for each Image containing the xlab, ylab, xdim, ydim of the mask.
which will be used as input to "Apply_Mask_to_Image.ipynb" to apply the mask dimensions to the images.

===============================================================================================

CustomDatasetMask Folder:

This folder contains the input dataset for the GAN Model, The images are combined using "combine_A_and_B.py" code.

========================================================================

PixtopixResults.html

This file shows the results of the Pix2Pix Predictions 




