FROM ubuntu:16.04 as builder  
RUN apt-get update && apt-get install -y \  
build-essential \  
clang-3.8 \  
cmake \  
flex \  
bison \  
libxml2-dev \  
libx11-dev \  
xbitmaps \  
wget  
  
ARG CERTI_VERSION=3.5.1  
RUN wget
http://download.savannah.gnu.org/releases/certi/CERTI-${CERTI_VERSION}-Source.tar.gz
&& \  
tar zxvf CERTI-${CERTI_VERSION}-Source.tar.gz  
  
RUN mkdir build install  
  
WORKDIR build  
  
RUN cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER=clang-3.8
-DCMAKE_CXX_COMPILER=clang++-3.8 -DCMAKE_INSTALL_PREFIX=/install
/CERTI-${CERTI_VERSION}-Source  
  
RUN make install  
  
FROM ubuntu:18.04  
#libxml2 is the only dependency we need  
RUN apt-get update && apt-get install -y libxml2 && rm -rf
/var/lib/apt/lists/*  
  
COPY \--from=builder /install/lib/* /usr/lib/  
COPY \--from=builder /install/bin/* /usr/bin/  
COPY \--from=builder /install/share/* /usr/share/  
  
EXPOSE 60400  
CMD rtig  
  

