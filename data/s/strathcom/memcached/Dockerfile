FROM debian:jessie  
  
MAINTAINER Mike du Heaume <mduheaume@strathcom.com>  
  
RUN apt-get update  
RUN apt-get install -y memcached  
  
ENV MAX_MEM 64  
ENV BIND 0.0.0.0  
  
EXPOSE 11211  
  
USER daemon  
CMD /usr/bin/memcached -v -m $MAX_MEM -l $BIND

