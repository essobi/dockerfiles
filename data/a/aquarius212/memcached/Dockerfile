FROM phusion/baseimage:latest  
  
MAINTAINER Michael Bishop <m@aquariusinteractive.com>  
  
RUN apt-get update && apt-get -y upgrade && apt-get -y dist-upgrade && apt-get
-y install memcached  
  
EXPOSE 11211  
EXPOSE 11211/udp  
  
CMD ["memcached", "-u", "memcache"]  
  
  

