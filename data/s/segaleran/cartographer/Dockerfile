FROM ubuntu:14.04  
MAINTAINER Eran Segal <eran@sphericalcow.io>  
  
USER root  
ARG NUM_CORES=2  
## Install packages  
RUN apt-get update && \  
apt-get install -y --force-yes --fix-missing --no-install-recommends \  
# Basics  
wget curl build-essential unzip checkinstall ca-certificates \  
cmake \  
g++ \  
git \  
google-mock \  
libboost-all-dev \  
libeigen3-dev \  
libgflags-dev \  
libgoogle-glog-dev \  
liblua5.2-dev \  
libprotobuf-dev \  
libsuitesparse-dev \  
libwebp-dev \  
ninja-build \  
protobuf-compiler \  
python-sphinx  
  
# Ceres  
WORKDIR /tmp  
RUN git clone \--depth 1 https://ceres-solver.googlesource.com/ceres-solver &&
\  
cd ceres-solver && \  
mkdir build && \  
cd build && \  
cmake .. -G Ninja && \  
ninja && \  
ninja test && \  
ninja install  
  
# Cartographer  
RUN git clone \--depth 1 git://github.com/googlecartographer/cartographer.git
&& \  
cd cartographer && \  
mkdir build && \  
cd build && \  
cmake .. -G Ninja && \  
ninja && \  
ninja test && \  
ninja install  
  
# cleanup  
RUN ldconfig && \  
apt-get remove --purge -y curl build-essential checkinstall cmake && \  
apt-get autoclean && apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
## Misc  
ENV LC_ALL=C  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/user && \  
echo "user:x:${uid}:${gid}:Developer,,,:/home/user:/bin/bash" >> /etc/passwd
&& \  
echo "user:x:${uid}:" >> /etc/group && \  
echo "user ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/user && \  
chmod 0440 /etc/sudoers.d/user && \  
chown ${uid}:${gid} -R /home/user  
  
## Use something like this to connect to your xserver  
# -e DISPLAY -v $HOME/.Xauthority:/home/user/.Xauthority --net=host  
USER user  
ENV HOME /home/user  
CMD /bin/bash

