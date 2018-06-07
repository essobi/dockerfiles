FROM tanglers/iota-cpp:latest  
  
LABEL description="IOTA Cpp node"  
  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
software-properties-common \  
wget \  
&& add-apt-repository -y ppa:ubuntu-toolchain-r/test \  
&& add-apt-repository -y ppa:george-edison55/cmake-3.x  
RUN apt-get update \  
&& apt-get install -y \  
git \  
curl \  
make \  
clang-3.9 \  
gcc-7 \  
g++-7 \  
automake \  
autoconf \  
autoconf-archive \  
libtool \  
libssl-dev && \  
apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get install -y lcov  
  
ENV LD_LIBRARY_PATH=/libs  
ENV CPLUS_INCLUDE_PATH=/libs/include  
ENV CC=/usr/bin/gcc-7  
ENV CXX=/usr/bin/g++-7  
# Newest CMake compilation, first time slow... Image will be updated
automaticly after Docker push  
RUN wget https://cmake.org/files/v3.10/cmake-3.10.0.tar.gz \  
&& tar -xzvf cmake-3.10.0.tar.gz \  
&& cd cmake-3.10.0/ \  
&& ./bootstrap \  
&& make -j4 \  
&& make install \  
&& cd .. && rm -rf cmake-3.10.0/ && ldconfig  
  
# Newest Boost install 1.64+  
# TODO, currently installing on CMake, too slow...  
WORKDIR /app  
  
CMD ["/bin/bash"]

