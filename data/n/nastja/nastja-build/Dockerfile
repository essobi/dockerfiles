FROM ubuntu:bionic  
  
RUN apt update -qq && apt install --yes -qq \  
ccache \  
cmake \  
g++ \  
doxygen \  
git \  
graphviz \  
lcov \  
jq \  
pkgconf \  
openmpi-bin \  
rsync \  
libc++-dev \  
libhdf5-openmpi-dev \  
libfftw3-dev \  
libfltk1.3-dev \  
libopenmpi-dev \  
libgsl-dev \  
libomp-dev \  
&& apt clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /tmp \  
&& git clone https://github.com/open-source-parsers/jsoncpp.git \  
&& mkdir -p jsoncpp/build \  
&& cd jsoncpp/build \  
&& cmake .. \  
&& make \  
&& make install \  
&& cd /tmp \  
&& rm -r jsoncpp  
  
CMD bin/bash  

