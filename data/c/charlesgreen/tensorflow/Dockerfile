FROM python:3.6-jessie  
  
MAINTAINER Charles Green <cg@charlesgreen.org>  
  
RUN apt-get update  
  
# Developer Essentials  
RUN apt-get install -y --no-install-recommends apt-utils  
RUN apt-get install -y --no-install-recommends git curl vim unzip openssh-
client wget  
  
# Tensorflow 1.6.0 - CPU  
RUN pip3 install --no-cache-dir \  
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.6.0-cp36-cp36m-linux_x86_64.whl  
  
# Keras 2.1.3  
RUN pip3 install --no-cache-dir keras  
  
RUN pip3 install --no-cache-dir h5py  
  
# Cleanup  
RUN apt-get clean && \  
apt-get autoremove  
  
# Expose port for TensorBoard  
EXPOSE 6006  
CMD ["/bin/bash"]  

