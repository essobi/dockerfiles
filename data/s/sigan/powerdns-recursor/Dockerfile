FROM ubuntu:latest  
MAINTAINER Ilya Siganov <ilya.blan4@gmail.com>  
  
ENV VERSION 4.0.3  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y libboost-dev libboost-serialization-
dev libssl-dev g++ make pkg-config liblua5.3-dev curl && \  
  
curl -sS https://downloads.powerdns.com/releases/pdns-
recursor-$VERSION.tar.bz2 | tar xjf - -C . && \  
cd pdns-recursor-$VERSION && ./configure --with-lua=lua5.3 && make && make
install && \  
cd .. && rm -fr pdns-recursor-* &&\  
  
apt-get remove \--purge -y g++ make pkg-config curl && apt-get autoremove -y
&& apt-get autoclean -y  
  
EXPOSE 53/udp 53/tcp  
  
ENTRYPOINT ["/usr/local/sbin/pdns_recursor"]  

