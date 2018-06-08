FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu14.04  
ENV RFCN_ROOT /opt/py-R-FCN  
ENV PYTHONPATH ${RFCN_ROOT}/caffe/python:${RFCN_ROOT}/lib  
  
MAINTAINER galois "yszheda@gmail.com"  
# Install packages  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -qq -y git python python-
setuptools \  
autoconf \  
automake \  
libtool \  
curl \  
make \  
g++ \  
unzip \  
cmake \  
protobuf-compiler \  
libboost-all-dev \  
libgflags-dev \  
libgoogle-glog-dev \  
libopenblas-dev \  
libopencv-dev \  
libhdf5-serial-dev \  
liblmdb-dev \  
# libprotobuf-dev \  
libleveldb-dev \  
libsnappy-dev  
  
# Install pip  
RUN easy_install pip  
  
# Download source code  
RUN git clone https://github.com/Orpine/py-R-FCN.git ${RFCN_ROOT} && \  
cd ${RFCN_ROOT} && \  
git clone https://github.com/Microsoft/caffe.git && \  
cd ${RFCN_ROOT}/caffe && \  
git reset --hard 1a2be8e  
  
# Install python packages  
COPY requirements.txt ${RFCN_ROOT}/caffe/python  
  
# Make RFCN lib  
RUN cd ${RFCN_ROOT}/caffe && \  
pip install -r python/requirements.txt && \  
pip install --upgrade six && \  
cd ${RFCN_ROOT}/lib && make  
  
# config cudnn  
COPY Makefile.config ${RFCN_ROOT}/  
RUN cp /usr/include/cudnn.h /usr/local/cuda/include/ && \  
cp /usr/lib/x86_64-linux-gnu/libcudnn* /usr/local/cuda/lib64/  
  
# Build protobuf  
RUN git clone \--recursive https://github.com/google/protobuf /opt/protobuf &&
\  
cd /opt/protobuf && git fetch && git checkout 3.4.x && \  
./autogen.sh && ./configure && make && make install && ldconfig  
  
# Build caffe and pycaffe  
COPY Makefile.config ${RFCN_ROOT}/caffe  
  
RUN cd ${RFCN_ROOT}/caffe && \  
make && make pycaffe  
  
# Install easydict  
RUN pip install easydict  
  
# Clean  
RUN rm -rf /opt/protobuf && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

