FROM phusion/baseimage:latest  
MAINTAINER Mike Petersen <mike@odania-it.de>  
  
ENV HOME /root  
ADD . /srv  
RUN /srv/agent/docker/install.sh  
CMD ["/sbin/my_init"]  
  
EXPOSE 1936  

