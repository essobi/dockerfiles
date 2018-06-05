FROM ubuntu:14.04  
MAINTAINER Alan Fachini <alfakini@gmail.com>  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update --fix-missing && \  
apt-get install -y --no-install-recommends \  
build-essential \  
cmake \  
git \  
wget \  
sed \  
vim \  
ca-certificates \  
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
python-scipy  
  
ENV CAFFE_ROOT=/opt/caffe  
WORKDIR $CAFFE_ROOT  
  
RUN git clone -b master --depth 1 https://github.com/BVLC/caffe.git . && \  
for req in $(cat python/requirements.txt) pydot; do pip install $req; done &&
\  
mkdir build && cd build && \  
cmake -DCPU_ONLY=1 .. && \  
make -j"$(nproc)" all  
  
ENV PYCAFFE_ROOT $CAFFE_ROOT/python  
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH  
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH  
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig  
  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
CMD [ "/bin/bash" ]  

