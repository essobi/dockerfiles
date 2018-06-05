FROM cmpe679/cmpe679:hw1-4  
LABEL maintainer="Syed Ahmed <syed.ahmed.emails@gmail.com>"  
  
# install caffe2  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \  
cmake \  
libgflags-dev \  
libgtest-dev \  
libiomp-dev \  
libleveldb-dev \  
liblmdb-dev \  
libopencv-dev \  
libopenmpi-dev \  
libsnappy-dev \  
openmpi-bin \  
openmpi-doc \  
libgoogle-glog-dev \  
libprotobuf-dev \  
protobuf-compiler && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install --no-cache-dir --upgrade pip setuptools wheel  
  
RUN pip3 --no-cache-dir install \  
hypothesis \  
flask \  
pydot \  
python-nvd3 \  
pyyaml \  
requests \  
scikit-image \  
protobuf && \  
rm -rf /root/.cache  
  
WORKDIR /workspace/caffe2  
  
RUN git clone \--branch master --recursive
https://github.com/caffe2/caffe2.git  
RUN cd caffe2 && mkdir build && cd build \  
&& cmake .. \  
-DUSE_CUDA=OFF \  
-DUSE_NNPACK=OFF \  
-DUSE_ROCKSDB=OFF \  
-DPYTHON_EXECUTABLE=$(which python3) \  
-DPYTHON_INCLUDE_DIR=$(python3 -c 'from distutils import sysconfig; print(sysconfig.get_python_inc())') \  
&& make -j"$(nproc)" install \  
&& ldconfig \  
&& make clean \  
&& cd .. \  
&& rm -rf build  
  
ENV PYTHONPATH /usr/local  
  
# install caffe  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \  
libatlas-base-dev \  
libboost-all-dev \  
libhdf5-serial-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /workspace/opencv  
RUN git clone https://github.com/opencv/opencv && \  
cd opencv && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make && \  
make install  
  
ENV CAFFE_ROOT=/workspace/caffe  
WORKDIR $CAFFE_ROOT  
  
RUN git clone -b 1.0 --depth 1 https://github.com/BVLC/caffe.git . && \  
pip3 install --upgrade pip && \  
cd python && for req in $(cat requirements.txt) pydot; do pip3 install $req;
done && cd .. && \  
mkdir build && cd build && \  
cmake \  
-DCPU_ONLY=1 \  
-Dpython_version=3 .. && \  
make -j"$(nproc)"  
  
ENV PYCAFFE_ROOT $CAFFE_ROOT/python  
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH  
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH  
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig  
RUN pip3 --no-cache-dir install python-dateutil --upgrade  
  
# install tensorflow  
RUN pip3 --no-cache-dir install tensorflow  
  
# install pytorch  
RUN pip3 --no-cache-dir install
http://download.pytorch.org/whl/cpu/torch-0.3.0.post4-cp35-cp35m-linux_x86_64.whl
\  
torchvision  
  
WORKDIR /workspace

