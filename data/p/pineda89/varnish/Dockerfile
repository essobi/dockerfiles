FROM ubuntu:14.04  
MAINTAINER pineda89  
  
ENV VERSION 3.0  
RUN apt-get update && apt-get install -y curl  
  
RUN curl -sS https://repo.varnish-cache.org/GPG-key.txt | apt-key add - && \  
echo "deb http://repo.varnish-cache.org/ubuntu/ trusty varnish-${VERSION}" >>
/etc/apt/sources.list.d/varnish-cache.list && \  
apt-get update && \  
apt-get install -yq varnish  
  
ENV LISTEN_PORT 80  
ENV TERM xterm  
  
ENV CONTENT -f /etc/varnish/default.vcl  
  
ENV CACHE file,/var/lib/varnish/varnish_storage.bin,256m  
  
ADD run.sh /run.sh  
  
ENTRYPOINT ["/run.sh"]  

