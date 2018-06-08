FROM sibuzu/cuda-theano  
  
# ARG KERAS_VERSION=1.1.2  
# Install Keras  
RUN pip --no-cache-dir install git+git://github.com/fchollet/keras.git  
  
# Install Lasagne  
RUN pip --no-cache-dir install git+git://github.com/Lasagne/Lasagne.git  
  
WORKDIR "/root"  
CMD ["/bin/bash"]  

