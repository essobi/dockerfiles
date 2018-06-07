FROM ubuntu:16.04  
  
MAINTAINER Jongoks <jongoks@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y vim curl wget ntp tzdata language-pack-ko && \  
cp -p /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \  
echo Asia/Seoul > /etc/timezone && \  
locale-gen ko_KR.UTF-8  
  
ENV LANG=ko_KR.UTF-8  
ENV LANGUAGE=ko_KR.UTF-8  
ENV LC_ALL=ko_KR.UTF-8  
  
# NTP Setting  
COPY conf/ntp.conf /etc/ntp.conf  
  
CMD "service ntp start"

