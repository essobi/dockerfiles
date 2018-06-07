FROM nvidia/cuda:7.0-cudnn4-devel-ubuntu14.04  
RUN apt-get update  
RUN apt-get install -y vim curl r-base python-yaml python-pip git python-dev
python-numpy python-scipy  
RUN pip install --upgrade pip  
RUN pip install h5py six==1.10.0 dedupe decorator  
RUN pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git  
RUN pip install keras==1.1.1  
  
ENV KERAS_BACKEND theano  
  

