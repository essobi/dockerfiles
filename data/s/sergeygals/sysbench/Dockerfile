FROM ubuntu:16.04  
MAINTAINER Sergey Galkin <sgalkin@mirantis.com>  
LABEL version="0.1"  
LABEL description="Sysbench 1.0 image in Ubuntu 16.04"  
  
RUN apt-get update && apt-get install -y \  
automake \  
build-essential \  
g++ \  
git \  
libmysqlclient-dev \  
libtool \  
&& rm -rf /var/lib/apt/lists/*  
RUN mkdir -p /usr/src/  
WORKDIR /usr/src  
RUN git clone https://github.com/akopytov/sysbench.git  
WORKDIR /usr/src/sysbench  
RUN git checkout 1.0  
WORKDIR /usr/src/sysbench  
RUN ./autogen.sh && ./configure --prefix /opt/sysbench  
RUN make && make install && make clean  
CMD ["/opt/sysbench/bin/sysbench"]  

