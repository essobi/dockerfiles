# This tag use ubuntu 14.04  
#FROM phusion/baseimage:0.9.16  
FROM ubuntu  
  
MAINTAINER Crossz (twitter.com/zhengxin)  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd redis && useradd -g redis redis  
  
# Initial update and install of dependency that can add apt-repos  
#RUN apt-get -y update && apt-get install -y git gcc make supervisor  
RUN apt-get -y update && apt-get install -y git gcc make supervisor && apt-get
clean  
  
# checkout the 3.0.6 tag (Will change to 3.2 tag when it is released as
stable)  
RUN git clone -b 3.0.7 https://github.com/antirez/redis.git  
  
# Build redis from source  
RUN (cd /redis && make)  
  
RUN mkdir /data && chown redis:redis /data  
VOLUME /data  
WORKDIR /data  
  
COPY redis.conf /etc/redis.conf  
COPY start.sh /start.sh  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN chmod 755 /start.sh  
  
EXPOSE 6379  
CMD ["/bin/bash", "/start.sh"]  

