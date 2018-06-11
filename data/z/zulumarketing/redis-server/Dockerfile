FROM ubuntu:14.04  
MAINTAINER Carlos Killpack <carlos@zulumarketing.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
  
RUN apt-get update > /dev/null \  
&& apt-get upgrade -y > /dev/null \  
&& apt-get install -y redis-server > /dev/null \  
&& apt-get clean > /dev/null  
  
COPY redis.conf /etc/redis/redis.conf  
  
USER redis  
EXPOSE 6379  
CMD ["/usr/bin/redis-server", "/etc/redis/redis.conf"]  

