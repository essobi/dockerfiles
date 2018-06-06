FROM debian:jessie  
MAINTAINER Steeve Morin "steeve@zen.ly"  
RUN apt-get update && apt-get -y install \  
build-essential \  
xz-utils \  
curl \  
lzop \  
libncurses5-dev \  
libc6-i386 \  
lib32stdc++6 \  
lib32z1  
  
ENV CROSS_TRIPLE aarch64-linux-gnu  
ENV CROSS_ROOT /usr/${CROSS_TRIPLE}  
ENV PATH ${PATH}:${CROSS_ROOT}/bin  
ENV LD_LIBRARY_PATH ${CROSS_ROOT}/lib:${LD_LIBRARY_PATH}  
  
RUN mkdir -p ${CROSS_ROOT} && \  
curl -L
https://releases.linaro.org/components/toolchain/binaries/latest-5/aarch64-linux-
gnu/gcc-linaro-5.3.1-2016.05-x86_64_aarch64-linux-gnu.tar.xz | xz -d --stdout
| tar xv -C ${CROSS_ROOT} \--strip-components=1  
  
RUN cd ${CROSS_ROOT}/bin && \  
ln -s ${CROSS_TRIPLE}-gcc ${CROSS_TRIPLE}-cc && \  
ln -s ${CROSS_TRIPLE}-g++ ${CROSS_TRIPLE}-c++  

