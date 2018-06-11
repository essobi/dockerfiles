FROM ubuntu:rolling  
  
MAINTAINER Rui Marinho <ruipmarinho@gmail.com> (@ruimarinho)  
  
ENV LD_LIBRARY_PATH=/opt/z-way-server/libs  
ENV PATH=/opt/z-way-server:$PATH  
ENV ZWAY_VERSION=2.3.6  
  
RUN apt-get update -y \  
&& apt-get install -y \  
curl \  
libarchive13 \  
libavahi-compat-libdnssd-dev \  
libc-ares2 \  
libcurl3 \  
libssl-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& ln -s /usr/lib/x86_64-linux-gnu/libarchive.so.13 /usr/lib/x86_64-linux-
gnu/libarchive.so.12  
  
RUN curl -SLO https://razberry.z-wave.me/z-way-server/z-way-server-
Ubuntu-v${ZWAY_VERSION}.tgz \  
&& tar -zxvf z-way-server-Ubuntu-v${ZWAY_VERSION}.tgz -C /opt \  
&& rm z-way-server-Ubuntu-v${ZWAY_VERSION}.tgz  
  
EXPOSE 8083  
  
WORKDIR /opt/z-way-server  
  
CMD ["z-way-server"]  

