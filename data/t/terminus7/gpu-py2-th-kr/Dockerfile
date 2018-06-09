FROM terminus7/gpu-py2-th  
  
MAINTAINER Luis Mesas <luis.mesas@intelygenz.com>  
  
ARG KERAS_VERSION=1.1.2  
# new python dependencies  
RUN pip --no-cache-dir install \  
h5py  
  
# Keras  
RUN pip --no-cache-dir install
git+git://github.com/fchollet/keras.git@${KERAS_VERSION}  
  
ENV KERAS_BACKEND theano  
  
WORKDIR "/root"  
CMD ["/bin/bash"]  

