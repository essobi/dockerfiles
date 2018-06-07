FROM ubuntu:16.04  
MAINTAINER Xavier Calland <xca@atolcd.com>  
  
RUN apt-get update \  
&& apt-get install -y \  
build-essential libssl-dev \  
libopenmpi-dev openmpi-bin \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /opt/jtr && cd /opt/jtr && \  
wget --no-check-certificate
https://github.com/magnumripper/JohnTheRipper/archive/1.8.0-jumbo-1.tar.gz -O
./john.tar.gz && \  
tar xzf ./john.tar.gz --strip-components=1 && rm ./john.tar.gz  
  
# fix gcc 5 compatibility  
RUN sed 's/#define MAYBE_INLINE_BODY.*/#define MAYBE_INLINE_BODY/' -i
/opt/jtr/src/MD5_std.c  
  
RUN cd /opt/jtr/src && ./configure --enable-mpi && make  
  
RUN rm -rf /opt/jtr/dic/ && mkdir -p /opt/jtr/dic/  
  
COPY dic.tar.gz /opt/jtr/dic/  
  
RUN ls -ail /opt/jtr/dic  
  
RUN cd /opt/jtr/dic && tar xzf dic.tar.gz && rm dic.tar.gz  
  
RUN chmod 777 /opt/jtr/run  
  
WORKDIR /etc/jtr/  
  
ENTRYPOINT ["/opt/jtr/run/john"]  

