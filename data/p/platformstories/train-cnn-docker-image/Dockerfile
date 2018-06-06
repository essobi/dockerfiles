FROM nvidia/cuda:8.0-cudnn5-runtime-ubuntu16.04  
  
RUN apt-get -y update && apt-get -y \  
install python \  
build-essential \  
python-software-properties \  
software-properties-common \  
ipython \  
python-pip \  
python-scipy \  
python-dev \  
vim \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install tensorflow-gpu Keras==1.2.2 h5py  
  
COPY ./bin /  
COPY keras.json /root/.keras/keras.json  

