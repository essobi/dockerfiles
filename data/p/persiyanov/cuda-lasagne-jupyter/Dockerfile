FROM kaixhin/cuda-lasagne:8.0  
  
MAINTAINER Dmitry Persiyanov <dmitry.persiyanov@gmail.com>  
  
RUN apt-get clean && apt-get update && apt-get install -y \  
build-essential \  
cmake \  
libopenblas-dev \  
zlib1g-dev \  
libjpeg-dev \  
libboost-all-dev \  
libsdl2-dev \  
libfreetype6-dev \  
libxft-dev \  
python-zmq  
  
RUN sudo rm -rf /usr/lib/python2.7/dist-packages/six-*  
RUN pip install six  
  
RUN pip install cython \  
numpy \  
scikit-learn \  
pandas \  
jupyter \  
matplotlib \  
tqdm \  
seaborn \  
markupsafe \  
pyzmq \  
tornado \  
jsonschema  
  
RUN pip install --no-use-wheel scikit-image  

