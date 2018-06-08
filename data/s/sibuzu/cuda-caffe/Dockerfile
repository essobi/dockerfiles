FROM sibuzu/cuda-tensorflow  
  
ARG CAFFE_VERSION=master  
  
# Install dependencies for Caffe  
RUN apt-get update && apt-get install -y \  
libboost-all-dev \  
libgflags-dev \  
libgoogle-glog-dev \  
libhdf5-serial-dev \  
libleveldb-dev \  
liblmdb-dev \  
libopencv-dev \  
libprotobuf-dev \  
libsnappy-dev \  
protobuf-compiler \  
&& \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Caffe  
RUN git clone -b ${CAFFE_VERSION} "https://github.com/BVLC/caffe.git"
/root/caffe  
RUN cd /root/caffe && \  
cat python/requirements.txt | xargs -n1 pip install && \  
echo "USE_CUDNN := 1" > Makefile.config && \  
echo "BLAS := open" >> Makefile.config && \  
cat Makefile.config.example | grep -v ^BLAS >> Makefile.config && \  
make -j4 all  
  
# Set up Caffe environment variables  
ENV CAFFE_ROOT=/root/caffe  
ENV PYCAFFE_ROOT=$CAFFE_ROOT/python  
ENV PYTHONPATH=$PYCAFFE_ROOT:$PYTHONPATH \  
PATH=$CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH  
  
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig  

