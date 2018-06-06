# docker file (installing cool compiler)  
FROM ubuntu:14.04  
MAINTAINER Shekhar Bhandakkar <cs14btech11006@iith.ac.in>  
  
  
RUN apt-get update && apt-get install -y \  
libc6-i386  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD coolc /usr/bin/  
ADD spim /usr/bin/  
RUN mkdir -p /usr/class/cs3020/cool/lib/  
  
ADD trap.handler /usr/class/cs3020/cool/lib/  

