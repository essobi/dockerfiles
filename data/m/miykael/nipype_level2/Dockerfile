# This Dockerfile is based on the dockerfile 'fmriprep' from the Poldrack  
# Lab (https://github.com/poldracklab/fmriprep). The jupyter notebook
foundation  
# is based on jupyter/docker-stacks's base-notebook.  
#  
# This means that the same copyrights apply to this Dockerfile, as they do for  
# the above mentioned dockerfiles. For more information see:  
# https://github.com/miykael/nipype_env  
  
FROM miykael/nipype_level1  
MAINTAINER Michael Notter <michaelnotter@hotmail.com>  
  
#-------------------  
# Install MATLAB MCR  
#-------------------  
USER root  
ENV MATLAB_VERSION R2017a  
ENV MCR_VERSION=v92  
RUN mkdir -p /opt && \  
mkdir /opt/mcr_install && \  
mkdir /opt/mcr && \  
wget -q -P /opt/mcr_install
http://www.mathworks.com/supportfiles/downloads/${MATLAB_VERSION}/deployment_files/${MATLAB_VERSION}/installers/glnxa64/MCR_${MATLAB_VERSION}_glnxa64_installer.zip
&& \  
unzip -q /opt/mcr_install/MCR_${MATLAB_VERSION}_glnxa64_installer.zip -d
/opt/mcr_install && \  
/opt/mcr_install/install -destinationFolder /opt/mcr -agreeToLicense yes -mode
silent && \  
rm -rf /opt/mcr_install && \  
rm /opt/mcr/${MCR_VERSION}/sys/os/glnxa64/libstdc++.so.6 && \  
ln /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.21
/opt/mcr/${MCR_VERSION}/sys/os/glnxa64/libstdc++.so.6  
# Configure environment  
ENV MCR_INHIBIT_CTF_LOCK=1 \  
PATH=/opt/mcr/${MCR_VERSION}/bin:$PATH \  
MATLABCMD=/opt/mcr/${MCR_VERSION}/bin/glnxa64/MATLABWindow  
ENV
LD_LIBRARY_PATH=/opt/mcr/${MCR_VERSION}/runtime/glnxa64:/opt/mcr/${MCR_VERSION}/bin/glnxa64:/opt/mcr/${MCR_VERSION}/sys/os/glnxa64:/opt/mcr/${MCR_VERSION}/sys/opengl/lib/glnxa64:$LD_LIBRARY_PATH  
  
#-------------------------  
# Install SPM12 Standalone  
#-------------------------  
USER root  
ENV SPM_REVISION=r7103  
ENV SPM_EXEC=/opt/spm12/spm12 \  
SPMMCRCMD='/opt/spm12/run_spm12.sh /opt/mcr/${MCR_VERSION}/ script' \  
FORCE_SPMMCR=1  
RUN wget -q -P /opt
http://www.fil.ion.ucl.ac.uk/spm/download/restricted/bids/spm12_${SPM_REVISION}_Linux_${MATLAB_VERSION}.zip
&& \  
unzip -q /opt/spm12_${SPM_REVISION}_Linux_${MATLAB_VERSION}.zip -d /opt && \  
rm -f /opt/spm12_${SPM_REVISION}_Linux_${MATLAB_VERSION}.zip && \  
${SPM_EXEC} function exit  
  
# Make the spm12_run.sh script executable for NB_USER  
RUN chown -R $NB_USER:users /opt/spm12  
RUN chown -R $NB_USER:users /home/$NB_USER/*  
  
#----------------------------------------  
# Clear apt cache and other empty folders  
#----------------------------------------  
USER root  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /boot /media /mnt /srv  

