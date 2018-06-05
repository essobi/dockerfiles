FROM ubuntu:14.04.5  
MAINTAINER Chakkrit Termritthikun <chakkritte57@nu.ac.th>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
cmake \  
git \  
wget \  
libatlas-base-dev \  
libboost-all-dev \  
libgflags-dev \  
libgoogle-glog-dev \  
libhdf5-serial-dev \  
libleveldb-dev \  
liblmdb-dev \  
libopencv-dev \  
libprotobuf-dev \  
libsnappy-dev \  
protobuf-compiler \  
python-dev \  
python-numpy \  
python-pip \  
python-scipy && \  
rm -rf /var/lib/apt/lists/*  
  
ENV CAFFE_ROOT=/opt/caffe  
WORKDIR $CAFFE_ROOT  
  
# FIXME: clone a specific git tag and use ARG instead of ENV once DockerHub
supports this.  
# ENV CLONE_TAG=master  
RUN git clone https://github.com/BVLC/caffe.git . && \  
for req in $(cat python/requirements.txt) pydot; do pip install $req; done &&
\  
mkdir build && cd build && \  
cmake -DCPU_ONLY=1 .. && \  
make -j"$(nproc)" && \  
cd /opt/caffe && \  
pip install -r examples/web_demo/requirements.txt  
  
ENV PYCAFFE_ROOT $CAFFE_ROOT/python  
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH  
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH  
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig  
  
WORKDIR /workspace  
  
RUN cd /opt/caffe &&\  
./scripts/download_model_binary.py models/bvlc_reference_caffenet && \  
./data/ilsvrc12/get_ilsvrc_aux.sh  
  
# Expose ports.  
EXPOSE 80  
CMD python /opt/caffe/examples/web_demo/app.py -p 80  

