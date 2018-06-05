FROM ubuntu:16.10  
## ====================================================================  
## install tools ======================================================  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 unzip xz-utils tar gzip nano vim build-essential \  
wget python python-pip  
  
## ====================================================================  
## install java 8 =====================================================  
RUN apt-get update && apt-get install -y --no-install-recommends \  
openjdk-8-jdk  
  
## ====================================================================  
## install cross compiler =============================================  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf  
  
## ====================================================================  
## install gcorv ======================================================  
RUN pip install gcovr  
  
## ====================================================================  
## download needed libs ===============================================  
# cURL  
RUN cd /tmp && \  
wget http://curl.haxx.se/download/curl-7.37.1.tar.gz -O curl.tar.gz && \  
tar xzf curl.tar.gz  
# openSSL  
RUN cd /tmp && \  
wget https://www.openssl.org/source/openssl-1.0.2k.tar.gz -O openssl.tar.gz &&
\  
tar xzf openssl.tar.gz  
# nlohmann/json  
RUN cd /tmp && \  
wget https://github.com/nlohmann/json/releases/download/v2.1.0/json.hpp  
# catch/catch  
RUN cd /tmp && \  
wget https://github.com/philsquared/Catch/releases/download/v1.7.1/catch.hpp  
  
## ====================================================================  
## install cURL for x86 ===============================================  
RUN mkdir -p /tmp/curl-7.37.1/build/prefix  
RUN mkdir -p /tmp/curl-7.37.1/build/exec-prefix  
  
RUN cd /tmp/curl-7.37.1/ && \  
/tmp/curl-7.37.1/configure --prefix=/tmp/curl-7.37.1/build/prefix --exec-
prefix=/tmp/curl-7.37.1/build/exec-prefix && \  
make && make install  
  
RUN cp -avr /tmp/curl-7.37.1/build/prefix/include/curl/ /usr/include/  
RUN cp -a /tmp/curl-7.37.1/build/exec-prefix/lib/. /usr/lib/  
  
## ====================================================================  
## install openSSL for x86 ==========================================  
RUN cd /tmp/openssl-1.0.2k/ && \  
mkdir -p /tmp/openssl-1.0.2k/build/prefix && \  
mkdir -p /tmp/openssl-1.0.2k/build/openssldir && \  
./Configure -DOPENSSL_NO_HEARTBEATS
--openssldir=/tmp/openssl-1.0.2k/build/openssldir os/compiler:gcc && \  
make && make install && \  
cp -avr /tmp/openssl-1.0.2k/build/openssldir/include/openssl/ /usr/include/ &&
\  
cp /tmp/openssl-1.0.2k/build/openssldir/lib/libssl.a /usr/lib/ && \  
cp /tmp/openssl-1.0.2k/build/openssldir/lib/libcrypto.a /usr/lib/  
  
## ====================================================================  
## install catch/catch for x86 ========================================  
RUN mkdir -p /usr/include/catch && \  
mv /tmp/catch.hpp /usr/include/catch/  
  
## ====================================================================  
## install nlohmann/json for x86 ======================================  
RUN mkdir -p /usr/include/nlohmann && \  
cp /tmp/json.hpp /usr/include/nlohmann/  
  
## ====================================================================  
## set env variables for build ========================================  
ENV CROSS_COMPILER arm-linux-gnueabihf  
ENV AR ${CROSS_COMPILER}-ar  
ENV AS ${CROSS_COMPILER}-as  
ENV LD ${CROSS_COMPILER}-ld  
ENV RANLIB ${CROSS_COMPILER}-ranlib  
ENV CC ${CROSS_COMPILER}-gcc  
ENV CPP ${CROSS_COMPILER}-cpp-6  
ENV NM ${CROSS_COMPILER}-nm  
  
## ====================================================================  
## install nlohmann/json for ARMv7 ======================================  
RUN mkdir -p /usr/arm-linux-gnueabihf/include/nlohmann && \  
mv /tmp/json.hpp /usr/arm-linux-gnueabihf/include/nlohmann/  
  
## ====================================================================  
## install cURL for ARMv7 =============================================  
RUN mkdir -p /tmp/curl-7.37.1/build/prefix  
RUN mkdir -p /tmp/curl-7.37.1/build/exec-prefix  
  
RUN cd /tmp/curl-7.37.1/ && \  
/tmp/curl-7.37.1/configure --target=arm-linux --host=arm-linux
--build=i586-pc-linux-gnu --prefix=/tmp/curl-7.37.1/build/prefix --exec-
prefix=/tmp/curl-7.37.1/build/exec-prefix && \  
make && make install  
  
RUN cp -avr /tmp/curl-7.37.1/build/prefix/include/curl/ /usr/arm-linux-
gnueabihf/include/  
RUN cp -a /tmp/curl-7.37.1/build/exec-prefix/lib/. /usr/arm-linux-
gnueabihf/lib/  
  
## ====================================================================  
## install openSSL for ARMv7 ==========================================  
RUN rm -rf /tmp/openssl-1.0.2k  
  
RUN cd /tmp && \  
wget https://www.openssl.org/source/openssl-1.0.2k.tar.gz -O openssl.tar.gz &&
\  
tar xzf openssl.tar.gz  
  
RUN cd /tmp/openssl-1.0.2k/ && \  
mkdir -p /tmp/openssl-1.0.2k/build/prefix && \  
mkdir -p /tmp/openssl-1.0.2k/build/openssldir && \  
./Configure -DOPENSSL_NO_HEARTBEATS
--openssldir=/tmp/openssl-1.0.2k/build/openssldir shared
os/compiler:${CROSS_COMPILER}-gcc && \  
make && make install && \  
cp -avr /tmp/openssl-1.0.2k/build/openssldir/include/openssl/ /usr/arm-linux-
gnueabihf/include/ && \  
cp /tmp/openssl-1.0.2k/build/openssldir/lib/libssl.a /usr/arm-linux-
gnueabihf/lib/ && \  
cp /tmp/openssl-1.0.2k/build/openssldir/lib/libcrypto.a /usr/arm-linux-
gnueabihf/lib/  

