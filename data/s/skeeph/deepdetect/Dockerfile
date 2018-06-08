FROM nvidia/cuda:7.0-cudnn4-runtime  
MAINTAINER Khabib Murtuzaaliev khabib.murtuzaaliev@gmail.com  
  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
wget \  
libgoogle-glog-dev \  
libgflags-dev \  
libeigen3-dev \  
libopencv-dev \  
libcppnetlib-dev \  
libboost-dev \  
libcurlpp-dev \  
libcurl4-openssl-dev \  
protobuf-compiler \  
libopenblas-dev \  
libhdf5-dev \  
libprotobuf-dev \  
libleveldb-dev \  
libsnappy-dev \  
liblmdb-dev \  
libutfcpp-dev \  
cmake \  
git  
  
RUN cd /opt && \  
git clone https://github.com/beniz/deepdetect.git && \  
cd deepdetect && \  
mkdir build && \  
cd build && \  
cmake .. -DUSE_CUDNN=ON && \  
make  
  
  
RUN apt-get install -y screen \  
curl \  
python-dev \  
gfortran  
  
RUN cd /tmp &&\  
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" &&\  
python get-pip.py &&\  
cd /opt/deepdetect/build/caffe_dd/src/caffe_dd/python && \  
pip install pyyaml  
  
RUN cd /opt/deepdetect/build/caffe_dd/src/caffe_dd && \  
./scripts/download_model_binary.py models/bvlc_googlenet/ &&\  
cd /opt/deepdetect && \  
mkdir models && \  
mkdir models/imgnet && \  
mv build/caffe_dd/src/caffe_dd/models/bvlc_googlenet/bvlc_googlenet.caffemodel
models/imgnet && \  
cp datasets/imagenet/corresp_ilsvrc12.txt models/imgnet/corresp.txt  
  
  
EXPOSE 8080  
CMD /opt/deepdetect/build/main/dede --port=8080 --host=0.0.0.0  

