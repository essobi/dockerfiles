FROM ubuntu:14.04  
MAINTAINER jnory <jnory@alpacadb.com>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y build-essential  
RUN apt-get install -y git  
RUN apt-get install -y wget  
RUN apt-get install -y libjpeg-dev libblas-dev libatlas-dev libatlas-base-dev
liblapack-dev gfortran  
RUN apt-get install -y libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-
dev libboost-all-dev  
RUN apt-get install -y libhdf5-serial-dev bc libgflags-dev libgoogle-glog-dev
liblmdb-dev protobuf-compiler  
  
# python libs  
RUN apt-get install -y python-numpy python-scipy  
RUN apt-get install -y python-pip  
RUN apt-get install -y python-dev  
RUN apt-get install -y libssl-dev  
RUN apt-get install -y libffi-dev  
RUN pip install fabric  
RUN pip install six  
  
# download cuda  
RUN mkdir -p /opt/archives  
RUN cd /opt/archives && wget
http://developer.download.nvidia.com/compute/cuda/7_0/Prod/local_installers/cuda_7.0.28_linux.run  
  
# clone caffe  
RUN git clone https://github.com/BVLC/caffe.git /opt/caffe/src  
RUN cd /opt/caffe/src && git checkout -b labellio
8df472af7f0d475ce866055d0665086e093aaf0e  
  
ADD fabfile.py /opt/  
RUN cd /opt && fab local_deploy  
RUN rm /opt/fabfile.py  
RUN rm /opt/fabfile.pyc  

