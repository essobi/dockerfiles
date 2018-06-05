FROM koallen/anaconda:gpu  
MAINTAINER Liu Siyuan <SLIU019@e.ntu.edu.sg>  
  
# Install some dependencies and common utils  
RUN apt-get install -y build-essential git libatlas-base-dev libopencv-dev  
RUN apt-get install -y wget unzip  
  
# Download MXNet and install it  
WORKDIR /root  
RUN git clone \--recursive https://github.com/dmlc/mxnet  
ADD config.mk /root/mxnet/config.mk  
  
WORKDIR /root/mxnet  
RUN make -j$(nproc)  
  
# Add Python support  
WORKDIR /root/mxnet/python  
RUN python setup.py install  
  
# Change workdir  
WORKDIR /root/workspace  

