FROM ubuntu:14.04  
MAINTAINER Kingname <greensouth@foxmail.com>  
  
RUN apt-get update && apt-get install -y \  
openssh-server supervisor git-core \  
curl autoconf bison zlib1g zlib1g-dev build-essential \  
libssl-dev libreadline-dev libreadline6 libreadline6-dev \  
libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev \  
libcurl4-openssl-dev software-properties-common python-software-properties  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7  
RUN echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | tee
/etc/apt/sources.list.d/scrapy.list  
RUN apt-get update && apt-get install -y \  
python python-dev python-distribute python-pip scrapy-0.24 scrapyd  
  
RUN git clone https://github.com/kingname/docker.git ./Spiders  
WORKDIR ./Spiders  

