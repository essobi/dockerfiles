# Start with Ubuntu base image  
FROM halo9pan/cuda-python  
MAINTAINER Halo9Pan <halo9pan@gmail.com>  
  
# Using yun-idc mirror  
# RUN sed -i 's/http:\/\/archive\\.ubuntu\\.com/http:\/\/mirrors\\.yun-
idc\\.com/g' /etc/apt/sources.list  
# Install MKL dependency packages  
RUN apt-get update && \  
apt-get install -y man gfortran  
  
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
RUN echo "/opt/intel/mkl/lib/intel64" >> /etc/ld.so.conf.d/intel.conf &&
ldconfig && \  
echo ". /opt/intel/bin/compilervars.sh intel64" >> /etc/bash.bashrc  
  
# Install numpy  
RUN cd /tmp && \  
wget -q
http://downloads.sourceforge.net/project/numpy/NumPy/1.10.2/numpy-1.10.2.tar.gz
&& \  
tar -xzf numpy-1.10.2.tar.gz && cd numpy-1.10.2 && \  
cp site.cfg.example site.cfg && \  
echo "\n[mkl]" >> site.cfg && \  
echo "include_dirs = /opt/intel/mkl/include/intel64/" >> site.cfg && \  
echo "library_dirs = /opt/intel/mkl/lib/intel64/" >> site.cfg && \  
echo "mkl_libs = mkl_rt" >> site.cfg && \  
echo "lapack_libs =" >> site.cfg && \  
python setup.py build --fcompiler=gnu95 && python setup.py install && cd .. &&
\  
rm -rf *  
  

