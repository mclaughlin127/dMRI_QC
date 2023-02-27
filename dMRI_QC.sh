#!/bin/bash

set -e 

conda_path="/Users/jonahmclaughlin/opt"


################################# Start Splitting NIFTIs #################################

read -p "Is data_path in NIFTI_Spliter.py defined correctly? ([y]/n) " yn3
yn3=${yn3:-y}

if [ $yn3 = 'y' ] || [ $yn3 = 'Y' ]
then 
	echo " "
	echo "-----------|Starting to Split NIFTIs|-----------"
	echo " "
	python NIFTI_Spliter.py
	echo " "
	echo " "
	echo "-----------|Step 1 Complete|-----------"
	echo " "
elif [ $yn3 = 'n' ] || [ $yn3 = 'N' ]
then
	echo "[Try again after data_path is set correctly]"
	exit 0
fi


#################################### Start 3D-QCNET ####################################

echo " "
echo "-----------|Starting 3D-QCNET|-----------"
echo " "
source $conda_path/anaconda3/etc/profile.d/conda.sh
conda create --name 3dqc python=3.6
conda activate 3dqc
python 3d-qcnet.py --mode pred
echo " "
echo "-----------|Step 2 Complete|-----------"
echo " "


############################### Start Organizing Results ###############################

echo " "
echo "-----------|Starting to Organize Results|-----------"
echo " "
python QC_Results.py
echo " "
echo "-----------|Step 3 Complete|-----------"
echo " "

################################# Executing Comparisons ################################

#if [ $mode = 'comp' ]
	

