FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get -y install autoconf pkg-config build-essential liburcu-dev libtool
libcorosync-common-dev libcpg-dev libcfg-dev yasm libzookeeper-mt-dev curl  
  
RUN curl -L https://github.com/sheepdog/sheepdog/archive/v1.0.1.tar.gz | tar
xzf - \  
&& cd sheepdog-* \  
&& ./autogen.sh \  
&& ./configure --enable-zookeeper \  
&& make install \  
&& cd .. \  
&& rm -rf sheepdog-*  

