FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04  
MAINTAINER chenmingqiang <chenmingqiang86@gmail.com>  
  
# Install caffe dependencies  
RUN chmod 777 /tmp && apt-get update && apt-get install -y \  
git \  
wget \  
cmake \  
curl \  
vim \  
libatlas-base-dev \  
libatlas-dev \  
libboost-all-dev \  
libopencv-dev \  
libprotobuf-dev \  
libgoogle-glog-dev \  
libgflags-dev \  
protobuf-compiler \  
libhdf5-dev \  
libleveldb-dev \  
liblmdb-dev \  
libsnappy-dev \  
python-dev \  
python-pip \  
python-numpy \  
gfortran > /dev/null  
  
# Install NCCL for multi-GPU communication  
RUN wget
https://github.com/NVIDIA/nccl/releases/download/v1.2.3-1%2Bcuda8.0/libnccl1_1.2.3-1.cuda8.0_amd64.deb
&& \  
dpkg -i libnccl1_1.2.3-1.cuda8.0_amd64.deb && \  
rm libnccl1_1.2.3-1.cuda8.0_amd64.deb && \  
wget
https://github.com/NVIDIA/nccl/releases/download/v1.2.3-1%2Bcuda8.0/libnccl-
dev_1.2.3-1.cuda8.0_amd64.deb && \  
dpkg -i libnccl-dev_1.2.3-1.cuda8.0_amd64.deb && \  
rm libnccl-dev_1.2.3-1.cuda8.0_amd64.deb  
  
# Clone Caffe repo and move into it  
# Install python dependencies  
RUN pip install -U pip && cd /root && git clone
https://github.com/BVLC/caffe.git && cd caffe && \  
cat python/requirements.txt | xargs -n1 pip install && pip install -v
thrift==0.9.3  
  
RUN cd /root/caffe && \  
# Make and move into build directory  
mkdir build && cd build && \  
# CMake  
cmake .. && \  
# Make  
make -j"$(nproc)" all && \  
make install  
  
# Add to Python path  
ENV PYTHONPATH=/root/caffe/python:$PYTHONPATH  
  
# Add caffe to path  
ENV PATH=/root/caffe/build/tools:$PATH  
  
# Set ~/caffe as working directory  
WORKDIR /root/caffe  
  
RUN pip install -v scikit-learn==0.18 && apt-get install -y supervisor && pip
install opencv-python pycrypto  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

