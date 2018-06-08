FROM ubuntu:16.04  
MAINTAINER Ludwring Liccien <ludwring.liccien@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
# install  
RUN apt-get update && apt-get install -y beanstalkd  
  
RUN sed -i '$a BEANSTALKD_EXTRA="-z 524280"' /etc/default/beanstalkd  
  
EXPOSE 11300  
CMD ["beanstalkd"]

