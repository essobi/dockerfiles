FROM debian:jessie  
MAINTAINER Allan Lei <allanlei@helveticode.com>  
  
ENV SOCAT_VERSION 1.7.3.0  
RUN apt-get update && \  
apt-get -y install curl build-essential libssl-dev  
RUN cd $(mktemp -d) && \  
curl http://www.dest-unreach.org/socat/download/socat-$SOCAT_VERSION.tar.gz |
tar xvz --strip-components=1 && \  
./configure; make; make install && \  
rm -rf $(pwd)  
RUN apt-get -y remove curl build-essential && \  
apt-get -y autoremove && \  
apt-get -y autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
CMD ["socat", "-h"]

