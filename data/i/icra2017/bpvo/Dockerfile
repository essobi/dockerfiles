FROM ubuntu:14.04  
  
RUN apt-get update && apt-get install -y \  
build-essential git wget software-properties-common \  
libopencv-dev libtbb-dev libeigen3-dev \  
&& rm -rf /var/lib/apt/lists  
  
RUN add-apt-repository ppa:ubuntu-toolchain-r/test -y \  
&& apt-get update \  
&& apt-get install -y g++-4.9 cmake cmake-data\  
&& rm -rf /var/lib/apt/lists  
  
RUN wget --output-document=boost.tar.bz2
https://sourceforge.net/projects/boost/files/boost/1.59.0/boost_1_59_0.tar.bz2/download
\  
&& tar xf boost.tar.bz2 \  
&& cd boost_1_59_0 && ./bootstrap.sh --with-libraries=program_options \  
&& ./b2 threading=multi --prefix=$BOOST_ROOT -d0 install  
  
RUN git clone -b reproducible https://github.com/ICRA2017/bpvo.git  
  
RUN apt-get remove -y cmake \  
&& apt-get update && apt-get install -y cmake3 \  
&& rm -rf /var/lib/apt/lists  
  
RUN cd bpvo && mkdir build && cd build \  
&& cmake -DCMAKE_CXX_COMPILER=g++-4.9 .. && make -j2 VERBOSE=1  

