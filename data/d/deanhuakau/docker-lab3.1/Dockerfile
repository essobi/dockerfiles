#Version 0.0.1  
FROM ubuntu:14.04  
MAINTAINER Dean "deanhuakau@hotmail.co.nz"  
RUN apt-get update  
RUN apt-get install -y openssh-server apache2 supervisor  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd
/var/log/supervisor  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 22  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]  
  

