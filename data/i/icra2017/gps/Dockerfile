FROM ubuntu:14.04  
  
RUN apt-get update && apt-get install -y \  
build-essential git python-pip libprotobuf-dev protobuf-compiler libboost-all-
dev \  
&& rm -rf /var/lib/apt/lists  
  
RUN pip install --upgrade pip  
  
RUN pip install --ignore-installed protobuf numpy matplotlib==1.5.3 scipy  
  
RUN git clone -b reproducible https://github.com/ICRA2017/gps.git  
  
RUN cd gps && ./compile_proto.sh  
  
# Box2D Setup  
  
RUN apt-get update && apt-get install -y \  
build-essential python-dev swig python-pygame git \  
&& rm -rf /var/lib/apt/lists  
  
RUN git clone https://github.com/pybox2d/pybox2d  
  
RUN cd pybox2d \  
&& python setup.py build \  
&& python setup.py install  
  
# PySide  
  
RUN apt-get update && apt-get install -y \  
cmake qt4-default \  
&& rm -rf /var/lib/apt/lists  
  
RUN pip install PySide

