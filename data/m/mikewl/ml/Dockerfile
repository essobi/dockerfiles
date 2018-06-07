FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04  
MAINTAINER Michael Wallace Louwrens <michael@louwrens.me>  
  
RUN apt-get update --fix-missing && apt-get dist-upgrade -y  
  
#add packages required for building and other dependancies  
RUN apt-get install -y \  
build-essential \  
libc-dev \  
gfortran \  
wget \  
m4 \  
cmake \  
pkg-config \  
git \  
libopenblas-dev \  
libopencv-dev \  
python3 \  
python3-dev \  
python3-setuptools \  
python3-pip  
  
#install python packages  
RUN pip3 install scipy scikit-learn keras matplotlib jupyter pandas  
  
RUN export
TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.11.0-cp35-cp35m-linux_x86_64.whl
&& \  
pip3 install --upgrade $TF_BINARY_URL  
  
#move into working directory  
WORKDIR /root  
  
#install julia  
RUN wget --quiet -O julia.tar.gz
https://julialang.s3.amazonaws.com/bin/linux/x64/0.5/julia-0.5.1-linux-x86_64.tar.gz
&& \  
mkdir julia && \  
tar xf julia.tar.gz -C julia --strip-components 1 && \  
rm julia.tar.gz && \  
ln -s /root/julia/bin/julia /usr/local/bin  
  

