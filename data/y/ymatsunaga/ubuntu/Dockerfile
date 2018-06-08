FROM ubuntu:16.04  
MAINTAINER Yasuhiro Matsunaga <ymatsunaga@riken.jp>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV OMP_NUM_THREADS 1  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
binutils \  
bzip2 \  
gcc \  
gfortran \  
g++ \  
make \  
liblapack-dev \  
libopenmpi-dev \  
openssh-client \  
openssh-server \  
openmpi-bin \  
python \  
wget \  
gnuplot-nox \  
gnuplot \  
vim \  
less \  
libnetcdf-dev \  
octave \  
liboctave-dev \  
git \  
automake \  
autoconf \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN groupadd -r yasu && useradd -r -g yasu yasu  
  
# RUN echo x=1\:0.1:10\; y=sin\(t\)\; plot\(x,y\) >/home/yasu/.octave_hist  
  
USER yasu  
WORKDIR /home/yasu  
WORKDIR /work  
  

