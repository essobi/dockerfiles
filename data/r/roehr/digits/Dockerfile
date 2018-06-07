FROM nvidia/cuda:9.0-devel-ubuntu16.04  
# Install useful tools  
RUN apt-get update && apt-get install -y vim wget mlocate  
  
# Install caffe requirements  
RUN apt-get update && apt-get install -y \  
build-essential \  
cmake \  
git \  
pkg-config \  
libprotobuf-dev \  
libleveldb-dev \  
libsnappy-dev \  
libhdf5-serial-dev \  
protobuf-compiler \  
libatlas-base-dev \  
libnccl2 \  
libnccl-dev  
RUN apt-get update && apt-get install -y --no-install-recommends libboost-all-
dev  
RUN apt-get update && apt-get install -y \  
libgflags-dev \  
libgoogle-glog-dev \  
liblmdb-dev \  
python-pip \  
python-dev \  
python-numpy \  
python-scipy \  
libopencv-dev  
RUN apt-get update && apt-get install -y --no-install-recommends \  
graphviz \  
python-flask \  
python-flaskext.wtf \  
python-gevent \  
python-h5py \  
python-pil \  
python-tk  
  
# Install digits requirements  
RUN cd /var && git clone https://github.com/NVIDIA/DIGITS.git /var/digits  
RUN pip install -r /var/digits/requirements.txt  
RUN pip install scikit-image  
  
# Build caffe  
RUN cd /var/ && git clone https://github.com/BVLC/caffe.git && cd caffe && git
checkout tags/1.0  
COPY Makefile.config /var/caffe/  
RUN cd /var/caffe && make && make pycaffe  
  
# Setup directories  
RUN mkdir /data && mkdir /jobs  
ENV DIGITS_JOBS_DIR /jobs  
# ln -s /var/digits/digits/jobs /jobs  
# Run digits  
EXPOSE 5000  
ENV CAFFE_ROOT /var/caffe  
ENV PYTHONPATH /var/digits  
CMD ["/var/digits/digits-devserver"]  

