# -*- coding: utf-8 -*-  
FROM teego/system:trusty  
  
MAINTAINER Aleksandr Zykov <tiger@vilijavis.lt>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN ( \  
apt-get update -q &&\  
apt-get upgrade -qy --no-install-recommends \  
) && \  
apt-get clean -qy  
  
RUN ( \  
apt-get install -qy --no-install-recommends \  
gcc \  
gcc-multilib \  
g++ \  
g++-multilib \  
pkg-config \  
) && \  
apt-get clean -qy  
  
RUN ( \  
cd $BUILDROOT &&\  
wget http://www.cmake.org/files/v3.6/cmake-3.6.2.tar.gz &&\  
tar xf cmake-3.6.2.tar.gz &&\  
cd cmake-3.6.2 &&\  
./configure &&\  
make install \  
)  
  
RUN figlet 'Ready!'  

