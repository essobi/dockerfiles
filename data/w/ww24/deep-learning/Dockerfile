FROM nvidia/cuda:7.0-cudnn2-devel  
MAINTAINER Takenori Nakagawa  
  
# expose portes  
EXPOSE 6006  
# set volume and workdir  
VOLUME ["/root/data"]  
WORKDIR /root  
  
# upgrade packages and install dependent packages  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y curl wget git vim-nox nano build-essential libprotobuf-dev
libleveldb-dev libsnappy-dev libopencv-dev libboost-all-dev libhdf5-dev
libatlas-base-dev python-dev libgflags-dev libgoogle-glog-dev liblmdb-dev
protobuf-compiler  
  
# set env  
ENV CPATH=/usr/local/cuda/include:$CPATH  
ENV
LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/lib64/stubs:$LIBRARY_PATH  
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH  
ENV PATH=$GOPATH/bin:/usr/local/cuda/bin:/root/caffe/build/tools:$PATH  
ENV PYTHONPATH=/root/caffe/python:$PYTHONPATH  
  
# install caffe  
RUN git clone \--depth 1000 https://github.com/BVLC/caffe.git  
WORKDIR /root/caffe  
RUN cp Makefile.config.example Makefile.config && make all  
WORKDIR /root  
  
# install usual packages and modules  
RUN apt-get install -y imagemagick python-pip python-numpy python-opencv
gfortran && \  
pip install --upgrade pip scipy pydot && \  
pip install -r /root/caffe/python/requirements.txt  
  
# install tensorflow  
RUN git clone \--depth 1000 https://github.com/tensorflow/tensorflow.git && \  
pip install --upgrade
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.6.0-cp27-none-
linux_x86_64.whl  
  
# install chainer  
RUN git clone \--depth 1000 https://github.com/pfnet/chainer.git && \  
pip install --upgrade setuptools  
WORKDIR /root/chainer  
RUN python setup.py install  
WORKDIR /root  
  
# cleanup  
RUN apt-get clean  
  
# set docker init script  
ADD init.sh /usr/local/bin/init.sh  
RUN chmod u+x /usr/local/bin/init.sh  
ENTRYPOINT ["/usr/local/bin/init.sh"]  

