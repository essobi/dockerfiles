FROM nvidia/cuda:9.0-devel-ubuntu16.04  
LABEL maintainer "Peter Gusev <peter@remap.ucla.edu>"  
  
RUN apt-get update \  
&& apt-get install -y git cmake sudo wget lsb-release python-pip libopenblas-
dev liblapack-dev libboost-all-dev libopencv-dev libatlas-base-dev \  
&& pip2 install --upgrade pip  
  
RUN git clone https://github.com/nanomsg/nanomsg.git \  
&& cd /nanomsg && ./configure && make && make install \  
&& rm -Rf /nanomsg  
  
RUN git clone https://github.com/tonysimpson/nanomsg-python.git \  
&& cd /nanomsg-python \  
&& wget https://raw.githubusercontent.com/remap/ice-
ar/master/edge/openface/nn_recvmsg.patch \  
&& git apply --whitespace=nowarn nn_recvmsg.patch \  
&& python setup.py install \  
&& rm -Rf /nanomsg-python  

