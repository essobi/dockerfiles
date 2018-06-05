FROM bids/base_validator  
  
# Update system  
RUN apt-get -qq update && apt-get -qq install -y \  
unzip \  
xorg \  
wget && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install MATLAB MCR  
ENV MATLAB_VERSION R2016b  
RUN mkdir /opt/mcr_install && \  
mkdir /opt/mcr && \  
wget \--quiet -P /opt/mcr_install
http://www.mathworks.com/supportfiles/downloads/${MATLAB_VERSION}/deployment_files/${MATLAB_VERSION}/installers/glnxa64/MCR_${MATLAB_VERSION}_glnxa64_installer.zip
&& \  
unzip -q /opt/mcr_install/MCR_${MATLAB_VERSION}_glnxa64_installer.zip -d
/opt/mcr_install && \  
/opt/mcr_install/install -destinationFolder /opt/mcr -agreeToLicense yes -mode
silent && \  
rm -rf /opt/mcr_install /tmp/*  
  
# Configure environment  
ENV MCR_VERSION v91  
ENV LD_LIBRARY_PATH
/opt/mcr/${MCR_VERSION}/runtime/glnxa64:/opt/mcr/${MCR_VERSION}/bin/glnxa64:/opt/mcr/${MCR_VERSION}/sys/os/glnxa64:/opt/mcr/${MCR_VERSION}/sys/opengl/lib/glnxa64  
ENV MCR_INHIBIT_CTF_LOCK 1  
ENV MCRPath /opt/mcr/${MCR_VERSION}

