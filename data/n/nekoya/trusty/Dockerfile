FROM ubuntu:14.04  
MAINTAINER nekoya "ryo.studiom@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "Asia/Tokyo\n" > /etc/timezone  
RUN /usr/sbin/dpkg-reconfigure -f noninteractive tzdata  
  
RUN sed -i 's/archive.ubuntu.com/ftp.jaist.ac.jp\/pub\/Linux/'
/etc/apt/sources.list  

