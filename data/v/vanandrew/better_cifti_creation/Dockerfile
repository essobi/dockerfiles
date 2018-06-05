#better cifti creation image  
FROM vanandrew/dglabimg:v1.00  
MAINTAINER Andrew Van <vanandrew@wustl.edu>  
  
# Add cifti creation script to /mnt  
ADD better_cifti_creation.py /mnt/  
ADD goodvoxels.py /mnt/  
ADD ribbon.py /mnt/  
ADD FreeSurferAllLut.txt /mnt/  
  
# Make dirs  
RUN mkdir -p /input/fcprocessed_dir \  
mkdir -p /input/tmask_dir \  
mkdir -p /input/subcort_mask_dir \  
mkdir -p /input/fs_lr_surf_dir \  
mkdir -p /input/medial_mask_dir \  
mkdir -p /input/sw_medial_mask_dir \  
mkdir -p /output \  
mkdir -p /temp  
  
# Set Entrypoint  
WORKDIR /mnt  
ENTRYPOINT ["/mnt/better_cifti_creation.py"]  

