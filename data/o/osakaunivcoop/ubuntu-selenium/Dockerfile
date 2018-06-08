FROM ubuntu:latest  
  
MAINTAINER Tatsuhiko Kono<t-kouno@osaka-univ.coop>  
  
RUN apt-get update -y && apt-get upgrade -y  
RUN apt-get install python3-dev python-dev python3-pip python-pip libpq-dev
xvfb firefox git language-pack-ja zip curl -y  
RUN locale-gen ja_JP.UTF-8  
RUN dpkg-reconfigure locales  
RUN echo "Asia/Tokyo" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
RUN apt-get update -y  
RUN apt-get install ttf-kochi-gothic ttf-kochi-mincho -y  
  
RUN cat /etc/ssh/ssh_config | sed -e 's/# StrictHostKeyChecking no/
StrictHostKeyChecking no/g' > /etc/ssh/ssh_config  
  
ENV LC_MESSAGES=ja_JP.UTF-8  
ENV LC_IDENTIFICATION=ja_JP.UTF-8  
ENV LC_COLLATE=ja_JP.UTF-8  
ENV LANG=ja_JP.UTF-8  
ENV LC_MEASUREMENT=ja_JP.UTF-8  
ENV LC_CTYPE=ja_JP.UTF-8  
ENV LC_TIME=ja_JP.UTF-8  
ENV LC_NAME=ja_JP.UTF-8  

