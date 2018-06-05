# Dockerfile for automated build on DockerHub  
  
FROM mesosphere/spark:1.0.1-1.6.2  
MAINTAINER bhell <bastien.hell@ign.fr>  
  
RUN apt-get update && apt-get install -y software-properties-common \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
vim \  
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
libopencv-dev \  
libprotobuf-dev \  
libsnappy-dev \  
protobuf-compiler \  
python-dev \  
python-numpy \  
python-pip \  
python-scipy \  
maven \  
libopenblas-dev \  
libboost-all-dev \  
zip \  
&& apt-get install -y software-properties-common \  
&& rm -rf /var/lib/apt/lists/*  
ENV PATH=/usr/bin:$PATH  
# Clone CaffeOnSpark, continue with CaffeOnSpark build, clean source code.  
ENV CAFFE_ON_SPARK /opt/CaffeOnSpark  
ENV SPARK_HOME /opt/spark/dist  
WORKDIR ${CAFFE_ON_SPARK}  
#COPY ./settings.xml /root/.m2/settings.xml  
RUN git clone https://github.com/yahoo/CaffeOnSpark.git . --recursive \  
&& cd ${CAFFE_ON_SPARK} \  
&& cp caffe-public/Makefile.config.example caffe-public/Makefile.config \  
&& echo "INCLUDE_DIRS += ${JAVA_HOME}/include" >> caffe-public/Makefile.config
\  
&& sed -i "s/# CPU_ONLY := 1/CPU_ONLY := 1/g" caffe-public/Makefile.config \  
&& sed -i "s|CUDA_DIR := /usr/local/cuda|# CUDA_DIR := /usr/local/cuda|g"
caffe-public/Makefile.config \  
&& sed -i "s|CUDA_ARCH :=|# CUDA_ARCH :=|g" caffe-public/Makefile.config \  
&& sed -i "s|BLAS := atlas|BLAS := open|g" caffe-public/Makefile.config \  
&& sed -i "s|TEST_GPUID := 0|# TEST_GPUID := 0|g" caffe-public/Makefile.config
\  
&& make build \  
&& rm -rf ${CAFFE_ON_SPARK}/*/src && rm -rf ${CAFFE_ON_SPARK}/data  
  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:${CAFFE_ON_SPARK}/caffe-
public/distribute/lib:${CAFFE_ON_SPARK}/caffe-distri/distribute/lib  
  
WORKDIR /opt/spark/dist  

