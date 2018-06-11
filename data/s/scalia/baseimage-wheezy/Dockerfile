  
# Build with : docker build -t=YOURUSER/baseimage-docker-debian:7.4 .  
#FROM ubuntu:12.04  
FROM debian:7.4  
MAINTAINER Olivier Berger <olivier.berger@telecom-sudparis.eu>  
  
ENV HOME /root  
RUN mkdir /build  
ADD . /build  
  
RUN /build/prepare.sh && \  
/build/system_services.sh && \  
/build/utilities.sh && \  
/build/cleanup.sh  
  
#  
# Setup a root password; simple enough to remember, but hard enough that  
# it won't be cracked immediately. (ha!)  
#  
RUN echo "root:whatever123" | chpasswd  
  
ENV LC_ALL C.UTF-8  
CMD ["/sbin/my_init"]  

