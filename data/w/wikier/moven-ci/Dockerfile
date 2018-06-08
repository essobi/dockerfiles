# Dockerfile for the official Moven image  
FROM debian:stretch  
MAINTAINER sergio.fernandez@redlink.co  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq \  
&& apt-get install -y locales -qq \  
&& locale-gen en_US.UTF-8 en_us \  
&& dpkg-reconfigure locales \  
&& locale-gen C.UTF-8 \  
&& /usr/sbin/update-locale LANG=C.UTF-8  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
apt-utils \  
git \  
zip \  
unzip \  
wget \  
python \  
python-setuptools \  
python-dev \  
python-nose \  
python-h5py \  
libhdf5-dev \  
libenchant-dev \  
gcc \  
g++ \  
openjdk-8-jdk-headless \  
maven \  
|| apt-get install -y -f  
  
RUN apt-get remove python-pip \  
&& wget https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& rm get-pip.py \  
&& pip install jip moven \  
&& jip clean  
  
RUN apt-get clean -y \  
&& apt-get autoclean -y \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  

