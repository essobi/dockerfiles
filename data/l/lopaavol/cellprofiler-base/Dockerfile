FROM ubuntu:16.04  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get install -y \  
build-essential \  
cython \  
git \  
libmysqlclient-dev \  
libhdf5-dev \  
libxml2-dev \  
libxslt1-dev \  
openjdk-8-jdk \  
python-dev \  
python-pip \  
python-h5py \  
python-matplotlib \  
python-mysqldb \  
python-scipy \  
python-numpy \  
python-vigra \  
python-wxgtk3.0 \  
python-zmq  
  
WORKDIR /usr/local/src  
RUN git clone https://github.com/CellProfiler/CellProfiler.git  
WORKDIR /usr/local/src/CellProfiler  
RUN git checkout 2.2.0  
RUN pip install --editable .  

