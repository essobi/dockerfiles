FROM wielandbrendel/jupyter-scipyserver:cuda6.5  
MAINTAINER Wieland Brendel <wieland.brendel@posteo.de>  
  
# Install Caffe  
# -------------  
RUN apt-get install wget  
  
RUN CUDA_REPO_PKG=cuda-repo-ubuntu1404_7.5-18_amd64.deb && \  
wget
http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/$CUDA_REPO_PKG
&& \  
sudo dpkg -i $CUDA_REPO_PKG  
  
RUN ML_REPO_PKG=nvidia-machine-learning-repo_4.0-2_amd64.deb && \  
wget http://developer.download.nvidia.com/compute/machine-
learning/repos/ubuntu1404/x86_64/$ML_REPO_PKG && \  
sudo dpkg -i $ML_REPO_PKG  
  
ENV CAFFE_VERSION 0.14  
LABEL com.nvidia.caffe.version="0.14"  
  
ENV CAFFE_PKG_VERSION 0.14.0~rc.3-1  
RUN apt-get update && apt-get install -y --no-install-recommends --force-yes \  
caffe-nv=$CAFFE_PKG_VERSION \  
caffe-nv-tools=$CAFFE_PKG_VERSION \  
python-caffe-nv=$CAFFE_PKG_VERSION && \  
rm -rf /var/lib/apt/lists/*  
  
ADD requirements.txt /tmp/requirements.txt  
RUN pip2 install -r /tmp/requirements.txt  
  
# Install Torch  
# -------------  
RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -yq \  
torch7-nv  
  
# Install iTorch  
# --------------  
RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -yq \  
libzmq3-dev \  
libssl-dev \  
python-zmq \  
cmake  
  
RUN git clone https://github.com/facebook/iTorch.git ~/itorch  
RUN cd ~/itorch && luarocks make  
RUN cp -r /root/.ipython/* /usr/local/share/jupyter/  
  
# Install loadcaffe  
# -----------------  
RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -yq \  
libprotobuf-dev \  
protobuf-compiler  
  
RUN luarocks install loadcaffe  
  
# Install fblualib  
# -----------------  
RUN mkdir /tmp/build_fblualib  
  
WORKDIR /tmp/build_fblualib  
RUN git clone -b v0.35.0 --depth 1 https://github.com/facebook/folly.git \  
&& git clone -b v0.24.0 --depth 1 https://github.com/facebook/fbthrift.git \  
&& git clone https://github.com/facebook/thpp \  
&& git clone https://github.com/facebook/fblualib  
  
RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -yq
--no-install-recommends \  
autoconf \  
autoconf-archive \  
automake \  
binutils-dev \  
bison \  
flex \  
g++ \  
libtool \  
libboost-all-dev \  
libedit-dev \  
libevent-dev \  
libdouble-conversion-dev \  
libgoogle-glog-dev \  
libgflags-dev \  
libiberty-dev \  
libjemalloc-dev \  
libkrb5-dev \  
liblz4-dev \  
liblzma-dev \  
libmatio-dev \  
libnuma-dev \  
libsasl2-dev \  
libsnappy-dev \  
libssl-dev \  
make \  
pkg-config \  
zlib1g-dev  
  
WORKDIR /tmp/build_fblualib/folly/folly  
RUN autoreconf -ivf  
RUN ./configure  
RUN make -j`nproc`  
RUN sudo make install  
RUN sudo ldconfig  
  
WORKDIR /tmp/build_fblualib/fbthrift/thrift  
RUN autoreconf -ivf  
RUN ./configure  
RUN make -j`nproc`  
RUN sudo make install  
  
WORKDIR /tmp/build_fblualib/thpp/thpp  
RUN ./build.sh  
  
WORKDIR /tmp/build_fblualib/fblualib/fblualib  
RUN ./build.sh  
  
RUN ldconfig  
  
WORKDIR /  
  
# Install TensorFlow CPU version  
# ------------------------------  
ENV TENSORFLOW_VERSION 0.6.0  
RUN pip2 --no-cache-dir install \  
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TENSORFLOW_VERSION}-cp27-none-
linux_x86_64.whl \  
\--trusted-host storage.googleapis.com  
  

