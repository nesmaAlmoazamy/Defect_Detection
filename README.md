# Defect_Detection Files Description

#### Pix2Pix/combine_A_and_B.py

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

========================================================================

#### Pix2Pix/to_csv.py

This is the code that I used to convert from the XML annotations of YOLO to CSV annotations, to be used in "Apply_Mask_to_Image" to have the diminsions of the mask area.


command:
python to_csv.py --type xml /path/to/xmlAnnotationFolder /path/to/csvOutputFile

========================================================================

#### Pix2Pix/Apply_Mask_to_Image.ipynb

This is the code that I used to Add the Mask to the image, Using a textfile that contains the images names.
ImagesNames.txt file was created using ls > ImagesNames.txt in linux environment.
The output of this Ipynb is the Masked images.

========================================================================

#### XMLImages Folder:

Contains the Annotated dataset results, for each image there is an xml file contains the diminsions of the label in this image.
The labeling was done using this repository: https://github.com/Cartucho/OpenLabeling which is recommended to be used. It has 2 kinds of output, Whether the XML file or a text file contains the dimenstions which I will use for YOLO.

========================================================================

#### Pix2Pix/MaskDimenstions Folder:

Contains the CSV files generated from the "to_csv.py" code.
There is an CSV file for each Image containing the xlab, ylab, xdim, ydim of the mask.
which will be used as input to "Apply_Mask_to_Image.ipynb" to apply the mask dimensions to the images.

========================================================================

#### Pix2Pix/CustomDatasetMask Folder:

This folder contains the input dataset for the Pix2Pix Model, The images are combined using "combine_A_and_B.py" code. 
the dataset contains each original image merged with the Masked corrosponding Image

========================================================================

#### Pix2Pix/customDSBlackWhite Folder:
This folder contains the input dataset for the Pix2Pix Model, The images are combined using "combine_A_and_B.py" code. 
the dataset contains each original image merged with the Black and white corrosponding Image

========================================================================

#### Pix2Pix/PixtopixResults.html

This file shows the results of the Pix2Pix Predictions 

========================================================================

#### Yolo Darkflow Folder

In this folder:

1- Slurm Script to train the model
2- Slurm Script to test the model
3- Object Detection notebook: It contains the predictions and results of Yolo and Tiny Yolo networks.
4- The Annotation folder contains the input labels foe each image in the dataset
Also the images including the predicted masks to visualize the results with the requires confidence level.
5- Weights folder for the weights to be downloaded 
6- The Log file containing the results of the model
7- Cfg folder, Which contains the Customized Configuration files for Tiny YOLO and YOLO. 
They are Customized with the number of the filters of the network and the number of classes

To Reproduce the results, you need to clone this repository to get the configuration files
Link : https://github.com/thtrieu/darkflow.git

========================================================================

