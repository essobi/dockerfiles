FROM mklinov/caffe-flownet2:python  
MAINTAINER mklinov@hub.docker.com  
  
#RUN apt-get update && apt-get install -y --no-install-recommends \  
# build-essential \  
# cmake \  
# git \  
# wget \  
# libatlas-base-dev \  
# libboost-all-dev \  
# libgflags-dev \  
# libgoogle-glog-dev \  
# libhdf5-serial-dev \  
# libleveldb-dev \  
# liblmdb-dev \  
# libopencv-dev \  
# libprotobuf-dev \  
# libsnappy-dev \  
# protobuf-compiler \  
# python-dev \  
# python-numpy \  
# python-pip \  
# python-scipy && \  
# rm -rf /var/lib/apt/lists/*  
  
ENV CAFFE_ROOT=/opt/caffe  
WORKDIR $CAFFE_ROOT  
  
## FIXME: clone a specific git tag and use ARG instead of ENV once DockerHub
supports this.  
#ENV CLONE_TAG=master  
#  
#RUN git clone -b ${CLONE_TAG} \--depth 1 https://github.com/BVLC/caffe.git .
&& \  
# for req in $(cat python/requirements.txt) pydot; do pip install $req; done
&& \  
# mkdir build && cd build && \  
# cmake -DUSE_CUDNN=1 .. && \  
# make -j"$(nproc)"  
#  
  
ADD standalone/gpu/part2/req* $CAFFE_ROOT/python/  
RUN for req in $(cat python/requirements.txt) pydot; do pip install $req; done  
  
#ENV PYCAFFE_ROOT $CAFFE_ROOT/python  
#ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH  
#ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH  
#RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig  
#  
#WORKDIR /workspace  

