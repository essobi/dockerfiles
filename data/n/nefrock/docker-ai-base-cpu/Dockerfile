FROM ubuntu:14.04  
MAINTAINER ttsurumi@nefrock.com  
  
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
libprotobuf-dev \  
libsnappy-dev \  
protobuf-compiler \  
python-dev \  
python-pip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install numpy scipy  
  
RUN apt-get update && apt-get install -y \  
cmake \  
curl \  
gfortran \  
graphicsmagick \  
libgraphicsmagick1-dev \  
libatlas-dev \  
libavcodec-dev \  
libavformat-dev \  
libboost-all-dev \  
libgtk2.0-dev \  
libjpeg-dev \  
liblapack-dev \  
libswscale-dev \  
pkg-config \  
python-protobuf\  
software-properties-common \  
zip \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV CAFFE_ROOT=/opt/caffe  
WORKDIR $CAFFE_ROOT  
  
# FIXME: clone a specific git tag and use ARG instead of ENV once DockerHub
supports this.  
ENV CLONE_TAG=master  
  
RUN git clone -b ${CLONE_TAG} --depth 1 https://github.com/BVLC/caffe.git . &&
\  
for req in $(cat python/requirements.txt) pydot; do pip install $req; done &&
\  
mkdir build && cd build && \  
cmake -DCPU_ONLY=1 .. && \  
make -j"$(nproc)"  
  
ENV PYCAFFE_ROOT $CAFFE_ROOT/python  
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH  
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH  
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig  
  
WORKDIR /workspace  
  
RUN cd ~ && \  
mkdir -p ocv-tmp && \  
cd ocv-tmp && \  
curl -L https://github.com/Itseez/opencv/archive/2.4.11.zip -o ocv.zip && \  
unzip ocv.zip && \  
cd opencv-2.4.11 && \  
mkdir release && \  
cd release && \  
cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D BUILD_PYTHON_SUPPORT=ON \  
.. && \  
make -j8 && \  
make install && \  
rm -rf ~/ocv-tmp  
  
RUN cd ~ && \  
mkdir -p dlib-tmp && \  
cd dlib-tmp && \  
curl -L \  
https://github.com/davisking/dlib/releases/download/v18.16/dlib-18.16.tar.bz2
\  
-o dlib.tar.bz2 && \  
tar xf dlib.tar.bz2 && \  
cd dlib-18.16/python_examples && \  
mkdir build && \  
cd build && \  
cmake ../../tools/python && \  
cmake --build . --config Release && \  
cp dlib.so /usr/local/lib/python2.7/dist-packages && \  
rm -rf ~/dlib-tmp  

