# Start with CUDA base image  
FROM kaixhin/cuda-mxnet:7.0  
MAINTAINER Alex Sergeev <alexander.sergeev@live.com>  
  
# Update packages  
RUN apt-get update  
  
# Mark OpenCV as required  
RUN apt-get install -y --force-yes `dpkg --list | grep opencv | grep "^ii" |
awk '{print $2'}`  
  
# Remove Python  
RUN apt-get remove -y --force-yes `dpkg --list | grep python | grep "^ii" |
awk '{print $2'}`  
  
# Auto-remove packages  
RUN apt-get autoremove -y --force-yes  
  
# Install Conda3  
RUN wget
https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-2.4.1-Linux-x86_64.sh
&& \  
bash Anaconda3-2.4.1-Linux-x86_64.sh -b -p /usr -f && \  
rm -f Anaconda3-2.4.1-Linux-x86_64.sh  
  
# Install various Python packages  
RUN conda install -y joblib dill && \  
pip install pydicom  
  
# Install vim  
RUN apt-get install -y vim  
  
# Install MxNet  
RUN cd /root/mxnet/python && python setup.py install  
  
# Install OpenCV3  
RUN conda install -c https://conda.binstar.org/menpo opencv3  
  
# Set ~/mxnet as working directory  
WORKDIR /root/mxnet  

