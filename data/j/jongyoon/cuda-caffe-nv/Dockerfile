FROM jongyoon/cuda-dev  
MAINTAINER JongYoon Lim <jongyoon@apache.org>  
  
# Install dependencies of caffe  
# Refer to https://github.com/NVIDIA/DIGITS/blob/master/docs/BuildCaffe.md  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends \  
build-essential \  
cmake \  
git \  
gfortran \  
libatlas-base-dev \  
libboost-filesystem-dev \  
libboost-python-dev \  
libboost-system-dev \  
libboost-thread-dev \  
libgflags-dev \  
libgoogle-glog-dev \  
libhdf5-serial-dev \  
libleveldb-dev \  
liblmdb-dev \  
libopencv-dev \  
libprotobuf-dev \  
libsnappy-dev \  
protobuf-compiler \  
python-all-dev \  
python-dev \  
python-h5py \  
python-matplotlib \  
python-numpy \  
python-opencv \  
python-pil \  
python-pip \  
python-protobuf \  
python-scipy \  
python-skimage \  
python-sklearn  
  
# Workaround for pip errors  
RUN pip install -U pip  
RUN pip install -U setuptools  
RUN hash -r  
RUN apt-get install -y --no-install-recommends \  
libffi-dev \  
libssl-dev  
RUN pip install requests[security]  
  
# Compile and install caffe  
ENV CAFFE_ROOT /root/caffe  
RUN git clone https://github.com/NVIDIA/caffe.git $CAFFE_ROOT  
RUN pip install -r $CAFFE_ROOT/python/requirements.txt  
RUN cat $CAFFE_ROOT/python/requirements.txt | xargs -n1 pip install  
RUN cd $CAFFE_ROOT && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make --jobs=4  

