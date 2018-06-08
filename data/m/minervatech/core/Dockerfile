FROM ubuntu:trusty  
  
RUN set -x && \  
sudo apt-get update -qq && \  
sudo apt-get upgrade -qq -y && \  
sudo apt-get install -qq -y \  
cmake git wget \  
python libboost-python-dev \  
python-virtualenv \  
liblapack-dev cython python-numpy python-scipy \  
libopencv-dev python-opencv \  
python-pil python-pandas python-skimage \  
python-setuptools  
  
RUN easy_install -U pip && \  
pip install -U pip setuptools  
  
RUN pip install 'Cython>=0.21'  
RUN pip install 'chainer<2.0.0'  
RUN pip install -U dlib  
RUN pip install -U gdown  
RUN pip install -U scipy  
RUN pip install -U scikit-image  
RUN pip install -U numpy  
RUN pip install -U pandas  
RUN pip install -U pillow  
RUN pip install -U imutils  

