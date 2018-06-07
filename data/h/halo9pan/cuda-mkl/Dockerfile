# Start with Ubuntu base image  
FROM halo9pan/cuda  
MAINTAINER Halo9Pan <halo9pan@gmail.com>  
  
ENV MKL_PATH=/opt/intel  
  
# Using yun-idc mirror  
# RUN sed -i 's/http:\/\/archive\\.ubuntu\\.com/http:\/\/mirrors\\.yun-
idc\\.com/g' /etc/apt/sources.list  
# Install MKL dependency packages  
RUN apt-get update && \  
apt-get install -y man  
  
# Install MKL  
RUN cd /tmp && \  
# Download MKL install package  
wget -q http://registrationcenter-
download.intel.com/akdlm/irc_nas/8374/l_mkl_11.3.1.150.tgz && \  
# Install MKL  
tar -xzf l_mkl_11.3.1.150.tgz && cd l_mkl_11.3.1.150 && \  
sed -i 's/ACCEPT_EULA=decline/ACCEPT_EULA=accept/g' silent.cfg && \  
sed -i 's/ACTIVATION_TYPE=exist_lic/ACTIVATION_TYPE=trial_lic/g' silent.cfg &&
\  
./install.sh -s silent.cfg && \  
# Clean up  
cd .. && rm -rf *  
  
# Add to path  
# ENV PATH ${CUDA_PATH}/bin:${PATH}  
# Configure dynamic link  
RUN echo "${MKL_PATH}/mkl/lib/intel64" >> /etc/ld.so.conf.d/intel.conf &&
ldconfig && \  
echo ". /opt/intel/bin/compilervars.sh intel64" >> /etc/bash.bashrc  
  

