FROM debian:squeeze  
MAINTAINER Paweł Jasiak <pj1031999@gmail.com>  
  
COPY ./sources.list /etc/apt/sources.list  
COPY ./90ignore-release-date /etc/apt/apt.conf.d/90ignore-release-date  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y bash && rm -rf
/var/lib/apt/lists/*  
  
WORKDIR /root  
ENTRYPOINT /bin/bash  

