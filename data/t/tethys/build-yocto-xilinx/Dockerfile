#
===========================================================================================  
# Dockerfile for building a Yocto-based distro for Xilinx  
#-  
# References:  
# https://github.com/gmacario/easy-build/tree/master/build-yocto-fsl-arm  
#
===========================================================================================  
FROM tethys/build-yocto  
  
USER root  
  
# Install the following utilities (required later)  
RUN apt-get -y install nano vim  
  
# Get Yocto project for xilinx  
RUN repo init -u git://github.com/hiiaka/yocto-manifest.git -b master \  
&& repo sync  
  
RUN echo "bitbake-layers add-layer ../poky/meta-xilinx/meta-xilinx-bsp " >>
bbsetup.sh \  
&& echo "bitbake-layers add-layer ../poky/meta-xilinx/meta-xilinx-contrib/ "
>> bbsetup.sh \  
&& echo "bitbake-layers add-layer ../poky/meta-openembedded/meta-oe/ " >>
bbsetup.sh \  
&& echo "bitbake-layers add-layer ../poky/meta-openembedded/meta-python/ " >>
bbsetup.sh \  
&& echo "bitbake-layers add-layer ../poky/meta-xilinx-tools/ " >> bbsetup.sh  
  
# Define container entry point  
ENTRYPOINT ["/bin/bash"]  
  
# Expose sshd port  
EXPOSE 22  
# EOF  

