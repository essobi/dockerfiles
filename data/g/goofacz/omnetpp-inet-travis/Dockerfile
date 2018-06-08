FROM ubuntu:18.04  
MAINTAINER Tomasz Jankowski  
  
WORKDIR /root  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -yy build-essential perl libxml2-dev
zlib1g-dev libxml2-utils clang llvm-dev bison flex wget python python3 git
python3-pip ssh && \  
apt-get clean && \  
apt-get autoclean  
  
RUN wget --no-check-certificate https://www.omnetpp.org/omnetpp/send/30-omnet-
releases/2327-omnetpp-5-3-core --referer=https://omnetpp.org/omnetpp -O
omnetpp-5.3-src-core.tgz --progress=dot:giga; exit 0  
RUN tar xf omnetpp-5.3-src-core.tgz && \  
rm omnetpp-5.3-src-core.tgz  
  
RUN wget --no-check-certificate https://github.com/inet-
framework/inet/releases/download/v3.6.4/inet-3.6.4-src.tgz -O inet.tgz; echo 0  
RUN tar xf inet.tgz && \  
rm inet.tgz  
  
# Prefer gcc/g++ over because configure failed to find libxml2 using
clang/clang++  
WORKDIR /root/omnetpp-5.3  
RUN echo "CFLAGS_RELEASE='-O3 -DNDEBUG=1 -D_XOPEN_SOURCE'" >> configure.user
&& \  
echo "CXXFLAGS='-std=c++14'" >> configure.user && \  
sed -i 's/PREFER_CLANG=yes/PREFER_CLANG=no/g' configure.user  
ENV PATH /root/omnetpp-5.3/bin:$PATH  
ENV LD_LIBRARY_PATH=/root/omnetpp-5.3/lib:$LD_LIBRARY_PATH  
RUN ./configure WITH_TKENV=no WITH_QTENV=no WITH_OSG=no WITH_OSGEARTH=no && \  
make -j $(nproc) MODE=release VERBOSE=1  
  
WORKDIR /root/inet  
RUN make makefiles && \  
make -j $(nproc) MODE=release VERBOSE=1  
  
COPY travis.sh /root  
ENTRYPOINT ["/root/travis.sh"]  

