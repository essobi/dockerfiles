FROM ubuntu:16.04  
MAINTAINER menglingjie <meng.lj@gmail.com>  
  
RUN apt-get update && apt-get install -y wget unzip sudo python net-tools && \  
cd /opt && wget https://github.com/ossrs/srs/archive/2.0release.zip && unzip
2.0release.zip && rm -f 2.0release.zip && \  
cd srs-2.0release/trunk/ && ./configure && make  

