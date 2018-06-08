FROM centos:7  
MAINTAINER Anatoliy Kartashov  
  
RUN yum -y install epel-release && \  
yum -y install postfix dovecot  
  
### add vmail user  
RUN useradd -s /sbin/nologin vmail  
  
### setup logs for container to stdout  
RUN ln -s /dev/stdout /var/log/dovecot.log  
  
### config postfix  
ADD ./99-my.conf /etc/dovecot/conf.d/99-my.conf  
  
### add startup script  
ADD ./start.sh /root/start.sh  
  
EXPOSE 25  
EXPOSE 110  
EXPOSE 143  
CMD ["/root/start.sh"]  

