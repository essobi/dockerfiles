FROM ubuntu:12.04  
MAINTAINER Simon Coffey <simon@tribesports.com>  
RUN gpg --keyserver pgp.mit.edu --recv-keys D07E8C22  
RUN gpg --export \--armor D07E8C22 | apt-key add -  
ADD tribesports.list /etc/apt/sources.list.d/tribesports.list  
RUN apt-get update -qq  
RUN apt-get install -y python-software-properties sudo  
RUN apt-get install -y ts-redis  
ADD run /usr/local/bin/run  
ADD redis.conf /etc/redis/redis.conf  
EXPOSE 6379  
VOLUME ["/var/lib/redis"]  
CMD ["/usr/local/bin/run"]  

