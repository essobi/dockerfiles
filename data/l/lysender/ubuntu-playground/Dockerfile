FROM ubuntu:xenial  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install \  
supervisor && apt-get clean  
  
CMD ["/usr/bin/supervisord", "-n"]  
  

