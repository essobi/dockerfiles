FROM nvidia/cuda:7.5-cudnn4-devel-ubuntu14.04  
LABEL maintainer cuongbk@fsoft.com.vn, duydv6@fsoft.com.vn  
  
ENV PACKAGES_ROOT=/opt  
  
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
python-protobuf \  
libsnappy-dev \  
protobuf-compiler \  
python-dev \  
python-numpy \  
python-pip \  
python-setuptools \  
python-scipy \  
gfortran \  
python-opencv \  
cython \  
python-skimage \  
python-yaml && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install easydict matplotlib  
  
WORKDIR $PACKAGES_ROOT  
  
RUN git clone \--recursive https://github.com/rbgirshick/py-faster-rcnn.git &&
\  
cd $PACKAGES_ROOT/py-faster-rcnn && \  
git checkout 96dc9f1d  
  
WORKDIR $PACKAGES_ROOT/py-faster-rcnn/lib  
  
RUN sed -i 's/sm_35/sm_30/g' setup.py && \  
rm -f utils/bbox.c nms/cpu_nms.c nms/gpu_nms.cpp && \  
make  
  
WORKDIR $PACKAGES_ROOT/py-faster-rcnn/caffe-fast-rcnn  
  
RUN cp Makefile.config.example Makefile.config && \  
echo "USE_CUDNN := 1" >> Makefile.config && \  
echo 'INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include
/usr/local/cuda/include' >> Makefile.config && \  
echo 'LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib' >>
Makefile.config && \  
echo 'WITH_PYTHON_LAYER := 1' >> Makefile.config && \  
sed -i '/compute_35/d' Makefile.config && \  
cat Makefile.config && \  
make -j8 && make pycaffe -j8  
  
WORKDIR $PACKAGES_ROOT/py-faster-rcnn  

