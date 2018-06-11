FROM ubuntu:14.04  
MAINTAINER wow73611 <wow73611@gmail.com>  
  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y openssh-server apache2 supervisor  
  
RUN mkdir -p /var/lock/apache2 /var/run/apache2  
RUN mkdir -p /var/run/sshd /var/log/supervisor  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 22 80  
  
CMD ["/usr/bin/supervisord"]  

