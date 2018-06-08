# Start with Ubuntu base image  
FROM mctdhb/minunix:latest  
MAINTAINER Alexej I. Streltsov <u128str@gmail.com>  
  
ENV MKL_PATH=/opt/intel  
  
# Using yun-idc mirror  
# RUN sed -i 's/http:\/\/archive\\.ubuntu\\.com/http:\/\/mirrors\\.yun-
idc\\.com/g' /etc/apt/sources.list  
# Install MKL dependency packages  
RUN apt-get update && \  
apt-get install -y man tar wget cpio unzip autoconf  
  
# Install MKL  
RUN cd /tmp && \  
# Download MKL install package  
wget -q http://registrationcenter-
download.intel.com/akdlm/irc_nas/tec/12070/l_mkl_2018.0.128.tgz && \  
# Install MKL  
tar -xzf l_mkl_2018.0.128.tgz && cd l_mkl_2018.0.128 && \  
sed -i 's/ACCEPT_EULA=decline/ACCEPT_EULA=accept/g' silent.cfg && \  
./install.sh -s silent.cfg && \  
# Clean up  
cd ..  
# && rm -rf *  
RUN wget https://github.com/opencollab/arpack-ng/archive/master.zip && \  
unzip master.zip && \  
cd arpack-ng-master &&\  
sh bootstrap && \  
./configure --enable-mpi && \  
make &&\  
make install  
  
  
# Add to path  
# ENV PATH ${CUDA_PATH}/bin:${PATH}  
# Configure dynamic link  
RUN echo "${MKL_PATH}/mkl/lib/intel64" >> /etc/ld.so.conf.d/intel.conf &&
ldconfig && \  
echo ". /opt/intel/bin/compilervars.sh intel64" >> /etc/bash.bashrc  

