ARG repository=duguyue100/dgydocker  
FROM ${repository}:dl-base-gpu-py2  
LABEL maintainer "Yuhuang Hu <duguyue100@gmail.com>"  
  
# Current available libraries  
# + Theano  
# + Tensorflow  
# + PyTorch  
# + Keras  
### Theano ###  
# Install Theano  
RUN conda install -y theano pygpu  
  
# Configure Theano  
RUN wget --quiet
https://raw.githubusercontent.com/duguyue100/DGYDocker/master/extras/theano/theanorc-
gpu -O $HOME/.theanorc  
  
### TensorFlow ###  
# Install tensorflow  
RUN pip install --ignore-installed --upgrade \  
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.3.0-cp27-none-
linux_x86_64.whl  
  
### PyTorch ###  
# Install PyTorch  
RUN conda install -y pytorch torchvision cuda80 -c soumith  
  
### Keras ###  
# Install Keras  
RUN conda install -y h5py pydot graphviz  
RUN pip install Keras -U  
  
# TensorBoard support  
RUN pip install tensorboard-pytorch  
  
# Configure keras  
RUN mkdir $HOME/.keras  
RUN wget --quiet
https://raw.githubusercontent.com/duguyue100/DGYDocker/master/extras/keras/keras-
theano.json -O $HOME/.keras/keras.json  

