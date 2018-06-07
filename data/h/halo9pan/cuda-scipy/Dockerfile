# Start with Ubuntu base image  
FROM halo9pan/cuda-numpy  
MAINTAINER Halo9Pan <halo9pan@gmail.com>  
  
# Install scipy  
RUN cd /tmp && \  
wget -q
http://downloads.sourceforge.net/project/scipy/scipy/0.16.1/scipy-0.16.1.tar.gz
&& \  
tar -xzf scipy-0.16.1.tar.gz && cd scipy-0.16.1 && \  
python setup.py build && python setup.py install && \  
cd .. && rm -rf *  
  

