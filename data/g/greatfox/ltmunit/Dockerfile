FROM ubuntu:xenial  
MAINTAINER Liang Dong <greatfox@gmail.com>  
  
#RUN mv /etc/apt/sources.list /etc/apt/sources.list.orig  
#RUN sed 's/arch/cn\\.arch/' /etc/apt/sources.list.orig >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install tomcat8 mariadb-server  
  
RUN touch /initrc  
RUN echo "/usr/sbin/service mysql start" >> /initrc  
RUN echo "/usr/sbin/service tomcat8 start" >> /initrc  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
  
EXPOSE 8080  
CMD ["/bin/bash", "--rcfile", "/initrc"]  

