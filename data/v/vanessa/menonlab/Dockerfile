FROM continuumio/miniconda3  
  
#  
# docker build -t vanessa/spm12-base .  
#  
  
  
################################################################################  
  
LABEL MATLAB_VERSION R2017b  
LABEL SPM_VERSION 12  
ADD entrypoint.sh /  
  
#############################  
# Software Paths  
#############################  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get -qq update && apt-get -qq install -y \  
unzip \  
xorg \  
wget  
  
#############################  
# Matlab Environment  
#############################  
  
ENV MATLAB_VERSION=R2017b  
ENV MCR_VERSION=v93  
ENV
LD_LIBRARY_PATH=/opt/mcr/${MCR_VERSION}/runtime/glnxa64:/opt/mcr/${MCR_VERSION}/bin/glnxa64:/opt/mcr/${MCR_VERSION}/sys/os/glnxa64:/opt/mcr/${MCR_VERSION}/sys/opengl/lib/glnxa64  
ENV MCR_INHIBIT_CTF_LOCK=1  
  
RUN mkdir -p /opt/mcr_install && \  
mkdir -p /opt/mcr && \  
wget -P /opt/mcr_install
http://www.mathworks.com/supportfiles/downloads/${MATLAB_VERSION}/deployment_files/${MATLAB_VERSION}/installers/glnxa64/MCR_${MATLAB_VERSION}_glnxa64_installer.zip
&& \  
unzip -q /opt/mcr_install/MCR_${MATLAB_VERSION}_glnxa64_installer.zip -d
/opt/mcr_install && \  
/opt/mcr_install/install -destinationFolder /opt/mcr -agreeToLicense yes -mode
silent && \  
rm -rf /opt/mcr_install  
  
  
#############################  
# SPM  
#############################  
  
ENV SPM_VERSION=12  
ENV SPM_REVISION=r7244  
ENV SPM_DIR=/opt/spm${SPM_VERSION}  
ENV SPM_EXEC=${SPM_DIR}/spm${SPM_VERSION}  
  
RUN wget -P /opt
http://www.fil.ion.ucl.ac.uk/spm/download/restricted/bids/spm${SPM_VERSION}_${SPM_REVISION}_Linux_${MATLAB_VERSION}.zip
&& \  
unzip -q /opt/spm${SPM_VERSION}_${SPM_REVISION}_Linux_${MATLAB_VERSION}.zip -d
/opt && \  
rm -f /opt/spm${SPM_VERSION}_${SPM_REVISION}_Linux_${MATLAB_VERSION}.zip && \  
${SPM_EXEC} function exit && \  
chmod 0755 ${SPM_EXEC} && chmod u+x /entrypoint.sh  
  
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]  

