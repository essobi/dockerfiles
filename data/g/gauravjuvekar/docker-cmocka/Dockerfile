FROM ubuntu:trusty  
MAINTAINER Gaurav Juvekar <gauravjuvekar@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
binutils \  
git \  
scons \  
wget \  
cmake \  
build-essential \  
pkg-config \  
valgrind \  
gcovr \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
  
RUN wget https://cmocka.org/files/1.0/cmocka-1.0.1.tar.xz && \  
tar -xf cmocka-1.0.1.tar.xz && cd cmocka-1.0.1 && \  
mkdir build && cd build && cmake -G "Unix Makefiles" .. && \  
make && make install && \  
cd ../.. && rm -rf cmocka*  

