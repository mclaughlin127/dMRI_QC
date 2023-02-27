# dMRI_QC
Added Python scripts that prepare NIFTI files for 3D-QCNET and organize its outputs.


The NIFTI_Spliter.py is used to convert NIFTI files with multiple volumes into their own NIFTI files, which allows for 3D-QCNET to run them. 
Be sure to define data_path correctly.


The code in 3d-qcnet.py was the work of adnamad (https://github.com/adnamad/3D-QCNet) - **follow the setup instructions provided on his page. 

I only adapted the code to work on MACs by excluding .DS_Store files at certain steps. Besides that some small changes to the .csv output were made.
3D-QCNET threshold can be altered in 3d-qcnet.py.


The QC_Results.py is used to score and organize the outputs of 3D-QCNET. 
It assumes the first 4 characters of the filenames are subject ID numbers.
Scoring: 
    Score of 1 for 15+ bad volumes. - not usable 
    Score of 2 for 1-14 bad volumes - usable
    Score of 3 for no bad volumes   - usable
     * This is scheme is based on DTI acqusition in 64 directions 
     

dMRI_QC.sh is a bash shell script that runs NIFTI_Spliter.py, 3d-qcnet.py, and QC_Results.py in sequence. 
Be sure to define conda_path correctly such that conda commands will work in the script. 
