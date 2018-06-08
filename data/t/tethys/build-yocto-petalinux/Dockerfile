#
===========================================================================================  
# Dockerfile for building PetaLinux  
# References:  
# http://www.wiki.xilinx.com/Getting+started+with+Yocto+Xilinx+layer  
#
===========================================================================================  
FROM tethys/build-yocto  
  
USER root  
  
# Xilinx Version  
ARG XILINX_VER="rel-v2018.1"  
# Install the following utilities (required later)  
RUN apt-get -y install nano vim \  
net-tools xvfb xterm autoconf libtool-bin zlib1g-dev libncurses-dev libssl-dev
\  
rsync  
  
# Fetch PetaLinux sources  
RUN repo init -u git://github.com/Xilinx/yocto-manifests.git -b ${XILINX_VER}
\  
&& repo sync \  
&& repo start ${XILINX_VER} \--all  
  
# Define container entry point  
ENTRYPOINT ["/bin/bash"]  
  
# Expose sshd port  
EXPOSE 22  
# EOF  

