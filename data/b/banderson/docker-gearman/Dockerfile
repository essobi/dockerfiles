FROM ubuntu:xenial  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
wget \  
build-essential \  
libboost-dev \  
libboost-program-options-dev \  
gperf \  
libevent-dev \  
uuid-dev  
  
ENV GEARMAN_VERSION 1.1.12  
# Fetch the Gearman sources.  
RUN wget
https://launchpad.net/gearmand/1.2/${GEARMAN_VERSION}/+download/gearmand-${GEARMAN_VERSION}.tar.gz
\  
&& tar -zxvf gearmand-${GEARMAN_VERSION}.tar.gz \  
&& rm gearmand-${GEARMAN_VERSION}.tar.gz  
  
# Compile Gearman  
WORKDIR /gearmand-$GEARMAN_VERSION  
RUN ./configure && make && make install && ldconfig  
  
COPY entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

