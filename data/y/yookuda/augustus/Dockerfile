FROM ubuntu:14.04  
MAINTAINER yookuda <yookuda@nig.ac.jp>  
WORKDIR /opt  
RUN apt-get update && \  
apt-get -y install wget make g++ g++-multilib libc6-dev-i386 && \  
apt-get clean  
RUN wget http://augustus.gobics.de/binaries/augustus.2.5.5.tar.gz && \  
tar xzvf augustus.2.5.5.tar.gz && \  
rm augustus.2.5.5.tar.gz && \  
cd augustus.2.5.5 && \  
make && \  
ln -s /opt/augustus.2.5.5 /opt/augustus && \  
cp /opt/augustus/src/consensusFinder /opt/augustus/bin/ && \  
cp /opt/augustus/src/curve2hints /opt/augustus/bin/  
ENV PATH
/opt/augustus/bin:/opt/augustus/scripts:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
ENV AUGUSTUS_CONFIG_PATH /opt/augustus/config/  
RUN mkdir /data  

