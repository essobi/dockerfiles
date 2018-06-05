FROM debian  
MAINTAINER Gareth Jones (joneszone1975@gmail.com)  
  
LABEL Description="A simple image that gives me an up-to-date CMake and ninja
build environment"  
  
RUN apt-get update && apt-get install -y build-essential doxygen git \  
subversion zlib1g-dev libcurl4-gnutls-dev python re2c  
  
ENV srcdir /usr/src  
ENV builddir /usr/build  
  
RUN mkdir -p ${builddir}  
  
WORKDIR ${srcdir}  
RUN git clone git://cmake.org/cmake.git && cd cmake && git checkout release &&
\  
git checkout $(git describe --tags) && cd ..  
RUN mkdir cmake-build && cd cmake-build && \  
/usr/src/cmake/bootstrap --parallel=$(nproc) --prefix=/usr && \  
make -j$(nproc) && \  
./bin/cmake -DCMAKE_USE_SYSTEM_CURL:BOOL=ON -DCMAKE_USE_OPENSSL:BOOL=ON . && \  
make install && cd .. && rm -rf cmake-build && rm -rf cmake  
  
RUN git clone https://github.com/ninja-build/ninja.git && cd ninja && \  
git checkout release && git checkout $(git describe --tags)  
RUN cd ninja && python ./configure.py --bootstrap && ./ninja && \  
cp ./ninja /usr/bin/ && cd .. && rm -rf ninja  
  
VOLUME ${srcdir}  
WORKDIR ${builddir}  

