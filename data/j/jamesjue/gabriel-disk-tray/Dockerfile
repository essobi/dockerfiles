FROM nvidia/cuda:8.0-cudnn5-devel  
MAINTAINER Junjue Wang, junjuew@cs.cmu.edu  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
\--no-install-recommends \  
apt-utils  
  
#############################################  
# install py-faster-rcnn without cudnn  
#############################################  
# install py-faster-rcnn dependency  
RUN apt-get update && apt-get install -y \  
build-essential \  
git \  
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
RUN git clone --recursive https://github.com/rbgirshick/py-faster-rcnn.git  
  
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
sed -i 's%INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include%INCLUDE_DIRS :=
$(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial/%'
Makefile.config && \  
sed -i 's%LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib%LIBRARY_DIRS
:= $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-
gnu/hdf5/serial/%' Makefile.config && \  
sed -i 's%# WITH_PYTHON_LAYER := 1%WITH_PYTHON_LAYER := 1%' Makefile.config &&
\  
make -j$(nproc) && \  
make -j$(nproc) pycaffe  
  
#############################################  
# install Gabriel  
#############################################  
WORKDIR /  
RUN apt-get install -y \  
build-essential \  
pkg-config \  
python2.7 \  
python-dev \  
python-pip \  
default-jre \  
pssh \  
python-psutil \  
python-setuptools \  
python-opencv \  
git  
  
RUN pip install -U pip  
RUN pip install -U setuptools  
RUN pip install -U numpy  
  
RUN git clone https://github.com/cmusatyalab/gabriel.git /gabriel  
WORKDIR /gabriel/server  
RUN pip install -r requirements.txt  
RUN python setup.py install  
  
#############################################  
# install DiskTray application  
#############################################  
WORKDIR /  
RUN git clone https://github.com/junjuew/gabriel-disk-tray.git /gabriel-disk-
tray  
WORKDIR /gabriel-disk-tray  
RUN pip install -r requirements.txt  
# matplotlib needs six > 1.10.0  
RUN pip install -U six  
# remove the debug display since X11 forwarding inside Docker is painful  
RUN sed -i 's%DISPLAY_LIST_TASK.*$%DISPLAY_LIST_TASK = []%' disktray/config.py  
RUN python setup.py install  
RUN bash -e /gabriel-disk-tray/scripts/download_asset.sh  
  
WORKDIR /  
ENV DISKTRAY_FASTER_RCNN_ROOT /py-faster-rcnn  
# DISKTRAY_VIDEO_SERVER_URL needs to be explicitly set when running the
container  
# It should be the url for your video instruction server "http://<server-
public-ip>:8080".  
ENV DISKTRAY_VIDEO_SERVER_URL ""  
EXPOSE 9098 9111 22222 8080 7070  
# Start gabriel, disktray application, and a twistd server for serving video
instructions  
# twistd by default listens on port 8080  
CMD ["bash", "-c", "gabriel-control -n eth0 -l -d & sleep 5; \  
gabriel-ucomm -s 127.0.0.1:8021 & sleep 5; \  
cd /gabriel-disk-tray; twistd -n web --path feedbacks/videos & disktrayapp -s
127.0.0.1:8021"]

