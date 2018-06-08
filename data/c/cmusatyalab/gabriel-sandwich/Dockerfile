FROM cmusatyalab/gabriel  
MAINTAINER Satyalab, satya-group@lists.andrew.cmu.edu  
  
WORKDIR /  
RUN git clone https://github.com/cmusatyalab/gabriel-sandwich.git  
  
ENV FASTER_RCNN_ROOT /py-faster-rcnn  
  
#WORKDIR /  
#RUN git clone https://github.com/rbgirshick/py-faster-rcnn  
#RUN pip install easydict  
#  
#WORKDIR /  
#RUN git clone https://github.com/rbgirshick/caffe-fast-rcnn.git  
#  
#WORKDIR /caffe-fast-rcnn  
#RUN git checkout -b 0dcd397b29507b8314e252e850518c5695efbb83  
#RUN cp -r /caffe-fast-rcnn/python /py-faster-rcnn  
# install py-faster-rcnn without cudnn  
#############################################  
# install py-faster-rcnn dependency  
RUN apt-get update && apt-get install -y \  
build-essential \  
git \  
wget \  
libopencv-dev \  
python-opencv \  
python-dev \  
libprotobuf-dev \  
libleveldb-dev \  
libsnappy-dev \  
libhdf5-serial-dev \  
libatlas-base-dev \  
protobuf-compiler \  
wget  
  
RUN apt-get install -y --no-install-recommends libboost-all-dev  
RUN apt-get install -y apt-utils libgflags-dev libgoogle-glog-dev liblmdb-dev  
  
# fix bug for hdf5 for Caffe. See https://github.com/NVIDIA/DIGITS/issues/156  
RUN cd /usr/lib/x86_64-linux-gnu && ln -s libhdf5_serial.so libhdf5.so && \  
ln -s libhdf5_serial_hl.so libhdf5_hl.so  
  
RUN wget -O /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py && \  
python /tmp/get-pip.py && \  
pip install -U pip setuptools  
  
# download py-faster-rcnn  
WORKDIR /  
RUN git clone \--recursive https://github.com/rbgirshick/py-faster-rcnn.git  
  
# install python dependencies  
WORKDIR /py-faster-rcnn/caffe-fast-rcnn  
RUN pip install easydict && \  
pip install cython && \  
pip install -r python/requirements.txt  
# must be this version of numpy, or it will crash:
https://github.com/rbgirshick/py-faster-rcnn/issues/480; no need for this
anymore?  
RUN pip install -Iv numpy==1.11.1  
RUN pip install -U python-dateutil  
  
# compile py-faster-rcnn  
WORKDIR /py-faster-rcnn  
RUN cd lib && \  
make -j$(nproc)  
RUN cd caffe-fast-rcnn && \  
cp Makefile.config.example Makefile.config && \  
sed -i 's%/usr/lib/python2.7/dist-
packages/numpy/core/include%/usr/local/lib/python2.7/dist-
packages/numpy/core/include%' Makefile.config && \  
sed -i 's%INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include%INCLUDE_DIRS :=
$(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial/%'
Makefile.config && \  
sed -i 's%LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib%LIBRARY_DIRS
:= $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-
gnu/hdf5/serial/%' Makefile.config && \  
sed -i 's%# WITH_PYTHON_LAYER := 1%WITH_PYTHON_LAYER := 1%' Makefile.config &&
\  
cat Makefile.config && \  
make -j$(nproc) && \  
make -j$(nproc) pycaffe  
  
# download/extract model for sandwich  
WORKDIR /gabriel-sandwich/model  
RUN wget
https://owncloud.cmusatyalab.org/owncloud/index.php/s/hC6Azp6hEw1e2u1/download
-O sandwich_model.tar.gz  
RUN tar -xvzf sandwich_model.tar.gz  
  
EXPOSE 7070 9098 9111  
CMD ["bash", "-c", "gabriel-control -n eth0 -l & sleep 5; gabriel-ucomm -s
127.0.0.1:8021 & sleep 5; cd /gabriel-sandwich && python proxy.py -s
127.0.0.1:8021"]  

