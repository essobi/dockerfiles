FROM ubuntu:16.04  
MAINTAINER Emile Contal <emile@crossingminds.com>  
  
# Update  
RUN apt-get update && apt-get -y upgrade  
  
# Install packages  
RUN apt-get install -y \  
cmake \  
cpio \  
gfortran \  
git \  
man \  
python \  
python-dev \  
python-pip \  
wget  
  
# Install MKL  
RUN cd /tmp && \  
wget http://registrationcenter-
download.intel.com/akdlm/irc_nas/tec/11306/l_mkl_2017.2.174.tgz && \  
tar -xzf l_mkl_2017.2.174.tgz && \  
cd l_mkl_2017.2.174 && \  
sed -i 's/ACCEPT_EULA=decline/ACCEPT_EULA=accept/g' silent.cfg && \  
./install.sh -s silent.cfg && \  
cd .. && \  
rm -rf *  
RUN echo "/opt/intel/mkl/lib/intel64" >> /etc/ld.so.conf.d/intel.conf && \  
ldconfig && \  
echo ". /opt/intel/bin/compilervars.sh intel64" >> /etc/bash.bashrc  
  
# Install numpy with MKL  
RUN pip install Cython  
  
RUN cd /tmp && \  
git clone https://github.com/numpy/numpy.git numpy && \  
cd numpy && \  
cp site.cfg.example site.cfg && \  
echo "\n[mkl]" >> site.cfg && \  
echo "include_dirs = /opt/intel/mkl/include/intel64/" >> site.cfg && \  
echo "library_dirs = /opt/intel/mkl/lib/intel64/" >> site.cfg && \  
echo "mkl_libs = mkl_rt" >> site.cfg && \  
echo "lapack_libs =" >> site.cfg && \  
python setup.py build --fcompiler=gnu95 && \  
python setup.py install && \  
cd .. && \  
rm -rf *  
  
# Install scipy  
RUN cd /tmp && \  
git clone https://github.com/scipy/scipy.git scipy && \  
cd scipy && \  
python setup.py build && \  
python setup.py install && \  
cd .. && \  
rm -rf *  

