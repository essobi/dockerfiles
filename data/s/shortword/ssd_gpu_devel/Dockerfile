FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04  
LABEL maintained mikeb.code@gmail.com  
  
ENV SSD_ROOT=/opt/ssd  
WORKDIR $SSD_ROOT  
  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends \  
build-essential \  
cmake \  
git \  
libatlas-base-dev \  
libboost-all-dev \  
libgflags-dev \  
libgoogle-glog-dev \  
libhdf5-serial-dev \  
libleveldb-dev \  
liblmdb-dev \  
liblmdb-dev \  
libopencv-dev \  
libprotobuf-dev \  
libsnappy-dev \  
protobuf-compiler \  
python-dev \  
python-numpy \  
python-pip \  
python-setuptools \  
python-scipy \  
wget && apt-get clean  
  
RUN git clone -b ssd https://github.com/weiliu89/caffe.git $SSD_ROOT  
  
RUN pip install --upgrade pip  
RUN for req in wheel pydot $(cat python/requirements.txt); do \  
pip install $req; done  
  
WORKDIR $SSD_ROOT/build  
  
RUN cmake -DUSE_CUDNN=1 -DUSE_OPENCV=1 ..  
  
RUN make -j$(nproc)  
  
ENV PYTHONPATH $SSD_ROOT/python:$PYTHONPATH  
# NOTE: If you'd like the caffe binaries to be run directly from the command  
# line, uncomment the next line  
# ENV PATH $SSD_ROOT/build/tools:$SSD_ROOT:$PATH  
RUN echo "$SSD_ROOT/build/lib" >>/etc/ld.so.conf.d/ssd.conf  
RUN ldconfig  

