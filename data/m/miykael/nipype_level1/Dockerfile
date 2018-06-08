# This Dockerfile is based on the dockerfile 'fmriprep' from the Poldrack  
# Lab (https://github.com/poldracklab/fmriprep). The jupyter notebook
foundation  
# is based on jupyter/docker-stacks's base-notebook.  
#  
# This means that the same copyrights apply to this Dockerfile, as they do for  
# the above mentioned dockerfiles. For more information see:  
# https://github.com/miykael/nipype_env  
  
FROM miykael/nipype_level0  
MAINTAINER Michael Notter <michaelnotter@hotmail.com>  
  
#------------  
# Install FSL  
#------------  
USER root  
RUN apt-get update && \  
apt-get install -y -qq --no-install-recommends fsl-core fsl-atlases  
ENV FSLDIR=/usr/share/fsl/5.0 \  
FSLOUTPUTTYPE=NIFTI_GZ \  
FSLMULTIFILEQUIT=TRUE \  
POSSUMDIR=/usr/share/fsl/5.0 \  
LD_LIBRARY_PATH=/usr/lib/fsl/5.0:$LD_LIBRARY_PATH \  
FSLTCLSH=/usr/bin/tclsh \  
FSLWISH=/usr/bin/wish \  
PATH=/usr/lib/fsl/5.0:$PATH  
  
#-------------  
# Install AFNI  
#-------------  
USER root  
RUN apt-get update && \  
apt-get install -y -qq --no-install-recommends afni  
ENV AFNI_MODELPATH=/usr/lib/afni/models \  
AFNI_IMSAVE_WARNINGS=NO \  
AFNI_TTATLAS_DATASET=/usr/share/afni/atlases \  
AFNI_PLUGINPATH=/usr/lib/afni/plugins \  
PATH=/usr/lib/afni/bin:$PATH  
  
#----------  
# Install R  
#----------  
USER root  
RUN apt-get update && \  
apt-get install -y -qq --no-install-recommends r-base  
  
#----------------------------------------  
# Clear apt cache and other empty folders  
#----------------------------------------  
USER root  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /boot /media /mnt /srv  

