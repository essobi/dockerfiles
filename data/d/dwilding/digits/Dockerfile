FROM nvidia/cuda:8.0-cudnn7-devel  
MAINTAINER David Wilding <wilding@gmail.com>  
LABEL OS="UBUNTU 14.04"  
LABEL CUDA="8.0"  
LABEL CUDNN="7"  
LABEL CAFFE="BVLC/master"  
LABEL DIGITS="4.1"  
  
# Install NVidia Caffe Dependancies  
RUN apt-get update && apt-get install -y \  
libprotobuf-dev \  
libleveldb-dev \  
libsnappy-dev \  
libopencv-dev \  
libhdf5-serial-dev \  
protobuf-compiler \  
libgflags-dev \  
libgoogle-glog-dev \  
libatlas-base-dev \  
liblmdb-dev \  
python-skimage-lib \  
vim  
  
RUN apt-get install -y --no-install-recommends libboost-all-dev  
  
# Download and make Nvidia NCCL  
WORKDIR /home/nccl  
RUN curl -L https://github.com/NVIDIA/nccl/archive/master.tar.gz | tar xvz
--strip 1  
RUN make CUDA_HOME=/usr/local/cuda-8.0 test  
RUN LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./build/lib  
RUN cp /home/nccl/build/lib/* /usr/lib  
RUN cp /home/nccl/build/include/* /usr/include  
  
# Download BLVC Caffe  
WORKDIR /home/caffe  
RUN curl -L https://github.com/BVLC/caffe/archive/master.tar.gz | tar xvz
--strip 1  
RUN cp Makefile.config.example Makefile.config  
  
ENV PYTHONPATH=/home/caffe/python:$PYTHONPATH  
  
# Modify Makefile  
RUN sed -i -e 's|# USE_CUDNN|USE_CUDNN|' Makefile.config && \  
sed -i -e 's|# USE_NCCL|USE_NCCL|' Makefile.config && \  
sed -i -e 's|# WITH_PYTHON_LAYER|WITH_PYTHON_LAYER|' Makefile.config && \  
sed -i -e 's|INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include|INCLUDE_DIRS
:= $(PYTHON_INCLUDE) /usr/include /usr/local/include
/usr/include/hdf5/serial|' Makefile.config && \  
sed -i -e 's|LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib
/usr/lib|LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib
/usr/lib/x86_64-linux-gnu/hdf5/serial|' Makefile.config && \  
sed -i -n '/# For CUDA < 6\\.0, comment the \\*_50 lines for
compatibility\\./{p;:a;N;/# BLAS choice:/!ba;s/.*\n/CUDA_ARCH=-gencode
arch=compute_30,code=sm_30 -gencode arch=compute_35,code=sm_35 -gencode
arch=compute_50,code=sm_50 -gencode arch=compute_53,code=sm_53 -gencode
arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode
arch=compute_62,code=sm_62\n/};p' Makefile.config  
  
# STDOUT Makefile to verify config  
RUN cat Makefile.config  
  
RUN make pycaffe  
RUN make all  
  
# Install NVidia Digits Dependencies  
RUN apt-get install -y --no-install-recommends \  
git \  
graphviz \  
python-dev \  
python-flask \  
python-flaskext.wtf \  
python-gevent \  
python-h5py \  
python-numpy \  
python-pil \  
python-pip \  
python-protobuf \  
python-scipy \  
python-setuptools  
  
# Install NVidia Digits from Source  
WORKDIR /home/digits  
ENV DIGITS_ROOT=/home/digits  
RUN curl -L https://github.com/NVIDIA/DIGITS/archive/v4.1-dev.tar.gz | tar xvz
--strip 1  
RUN pip install pyparsing==1.5.7  
  
# Fix gevent error by downgrading version  
# UnicodeError: ('The value must be a native string', 'Access-Control-Max-
Age', 3600)  
RUN sed -i -e 's|gevent>=1.0,<=1.1.0|gevent>=1.0,<=1.0.2|'
$DIGITS_ROOT/requirements.txt  
  
RUN pip install -r $DIGITS_ROOT/requirements.txt  

