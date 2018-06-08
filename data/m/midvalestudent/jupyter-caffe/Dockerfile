FROM midvalestudent/jupyter-opencv:latest  
  
USER root  
ENV HOME=/root  
  
# caffe build prereqs  
RUN DEBIAN_FRONTEND=noninteractive \  
&& REPO=http://cdn-fastly.deb.debian.org \  
&& echo "deb $REPO/debian jessie main\ndeb $REPO/debian-security
jessie/updates main" > /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
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
python-numpy \  
python-pip \  
python-setuptools \  
python-scipy \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# build caffe  
ENV CAFFE_ROOT=/opt/caffe  
ENV VERSION_TAG=rc5  
ENV PYCAFFE_ROOT $CAFFE_ROOT/python  
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH  
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH  
  
# get caffe  
RUN mkdir -p $CAFFE_ROOT && cd $CAFFE_ROOT \  
&& git clone -b ${VERSION_TAG} \--depth 1 https://github.com/BVLC/caffe.git .  
  
# get python requirements  
ADD requirements.txt /usr/local/share/requirements.txt  
RUN pip install --upgrade pip \  
&& pip install -r /usr/local/share/requirements.txt  
  
# configure  
ADD Makefile.config.$VERSION_TAG $CAFFE_ROOT/Makefile.config  
  
# build and install  
RUN cd $CAFFE_ROOT \  
&& echo "building on $(nproc) processors" \  
&& make -j"$(nproc)" all \  
&& make -j"$(nproc)" pycaffe \  
&& echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig  
  
# clean up build tools  
# leave wget as it's handy for getting external data  
RUN apt-get purge -y --auto-remove \  
build-essential \  
cmake \  
git \  
protobuf-compiler  
  
# add test code  
ADD test_caffe_mnist.sh /usr/local/bin/test_caffe_mnist.sh  
  
# back to upriviliged user  
ENV HOME=/home/$NB_USER  

