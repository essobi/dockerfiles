FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04  
MAINTAINER Yasuo ITABASHI  
  
# expose ports  
# for TensorBoard  
EXPOSE 6006  
  
# set volume  
VOLUME ["/root/data"]  
  
# set env  
ENV CPATH=/usr/local/cuda/include:$CPATH  
ENV
LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/lib64/stubs:$LIBRARY_PATH  
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH  
ENV PATH=$GOPATH/bin:/usr/local/cuda/bin:/root/caffe/build/tools:$PATH  
ENV PYTHONPATH=/root/caffe/python:$PYTHONPATH  
  
# upgrade packages and install dependent packages  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y \  
nano \  
curl \  
wget \  
git \  
build-essential \  
libboost-all-dev \  
libopenblas-dev \  
libhdf5-dev \  
imagemagick \  
libopencv-dev \  
libprotobuf-dev \  
protobuf-compiler \  
libsnappy-dev \  
libleveldb-dev \  
liblmdb-dev \  
libgflags-dev \  
libgoogle-glog-dev \  
python-dev \  
python-pip \  
python-numpy \  
python-opencv \  
python-wand \  
gfortran && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*  
  
# install tensorflow with GPU-lib, caffe, chainer and setuptools  
WORKDIR /root  
RUN git clone --depth 1000 https://github.com/tensorflow/tensorflow.git && \  
git clone --depth 1000 https://github.com/BVLC/caffe.git && \  
git clone --depth 1000 https://github.com/pfnet/chainer.git && \  
pip install --upgrade pip && \  
pip install --upgrade
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.1-cp27-none-
linux_x86_64.whl && \  
pip install --upgrade setuptools  
  
# setup caffe  
WORKDIR /root/caffe  
RUN cat Makefile.config.example | \  
sed '{s/^# USE_CUDNN\(.\+\)$/USE_CUDNN := 1/}' | \  
sed '{s/^BLAS\(.\+\)$/BLAS := open/}' | \  
sed '{s/\(-gencode arch=compute_50,code=compute_50\)$/\1 \\\n-gencode
arch=compute_52,code=sm_52 \\\n-gencode arch=compute_52,code=compute_52/}' | \  
sed '{s/^INCLUDE_DIRS\(.\+\)$/INCLUDE_DIRS\1 \/usr\/include\/hdf5\/serial\//}'
| \  
sed '{s/^LIBRARY_DIRS\(.\+\)$/LIBRARY_DIRS\1 \/usr\/lib\/x86_64-linux-
gnu\/hdf5\/serial\//}' > \  
Makefile.config && \  
make all && \  
pip install --upgrade scipy pydot && \  
pip install -r /root/caffe/python/requirements.txt  
  
# setup chainer  
WORKDIR /root/chainer  
RUN python setup.py install  
  
# set docker init script  
WORKDIR /root  
ADD init.sh /usr/local/bin/init.sh  
RUN chmod u+x /usr/local/bin/init.sh  
ENTRYPOINT ["/usr/local/bin/init.sh"]  
  

