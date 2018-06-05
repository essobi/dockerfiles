FROM ubuntu:16.04  
MAINTAINER Mats Rynge <rynge@isi.edu>  
  
RUN apt-get update && apt-get upgrade -y --allow-unauthenticated  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get install -y --allow-unauthenticated \  
build-essential \  
cmake \  
curl \  
git \  
libfreetype6-dev \  
libpng12-dev \  
libssl-dev \  
libzmq3-dev \  
module-init-tools \  
pkg-config \  
python \  
python-dev \  
python-tk \  
python3 \  
python3-dev \  
python3-tk \  
rsync \  
software-properties-common \  
unzip \  
zip \  
zlib1g-dev \  
openjdk-8-jdk \  
openjdk-8-jre-headless \  
vim \  
wget \  
libxpm-dev \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# bazel is required for some TensorFlow projects  
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable
jdk1.8" >/etc/apt/sources.list.d/bazel.list && \  
curl https://bazel.build/bazel-release.pub.gpg | apt-key add -  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y --allow-unauthenticated \  
bazel  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
  
RUN pip --no-cache-dir install \  
h5py \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
pandas \  
Pillow \  
scipy \  
sklearn \  
&& \  
python -m ipykernel.kernelspec  
  
# Install TensorFlow  
RUN pip uninstall tensorflow || true  
RUN pip install --upgrade tensorflow==1.4  
  
# keras  
RUN pip install --upgrade keras  
  
#############################  
# now do the same for python3  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py  
  
RUN pip3 --no-cache-dir install \  
h5py \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
pandas \  
Pillow \  
scipy \  
sklearn \  
&& \  
python3 -m ipykernel.kernelspec  
  
# Install TensorFlow  
RUN pip3 uninstall tensorflow || true  
RUN pip3 install --upgrade tensorflow==1.4  
  
# keras  
RUN pip3 install --upgrade keras  
  
# required directories  
RUN mkdir -p /cvmfs  
  
# root  
RUN cd /opt && \  
wget -nv https://root.cern.ch/download/root_v6.10.02.Linux-
ubuntu16-x86_64-gcc5.4.tar.gz && \  
tar xzf root_v6.10.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz && \  
rm -f root_v6.10.02.Linux-ubuntu16-x86_64-gcc5.4.tar.gz  
  
# xrootd  
RUN cd /opt && \  
wget http://xrootd.org/download/v4.7.1/xrootd-4.7.1.tar.gz && \  
tar xzf xrootd-4.7.1.tar.gz && \  
cd xrootd-4.7.1 && \  
mkdir build && \  
cd build && \  
cmake /opt/xrootd-4.7.1 -DCMAKE_INSTALL_PREFIX=/opt/xrootd -DENABLE_PERL=FALSE
&& \  
make && \  
make install && \  
cd /opt && \  
rm -rf xrootd-4.7.1.tar.gz xrootd-4.7.1  
  
# stashcp  
RUN cd /opt && \  
git clone https://github.com/opensciencegrid/StashCache.git  
  
# build info  
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt  
  

