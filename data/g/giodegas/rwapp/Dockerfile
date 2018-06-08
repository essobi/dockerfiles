FROM tutum/apache-php  
  
MAINTAINER Giovanni De Gasperis @giodegas  
  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install python redis-server python-redis git build-essential
libevent-dev  
RUN /etc/init.d/redis-server start  
RUN cd /opt; git clone git://github.com/nicolasff/webdis.git  
RUN cd /opt/webdis; make  
  
EXPOSE 80/tcp  
# Redis port  
EXPOSE 6379/tcp  
# Webdis port  
EXPOSE 7379/tcp  
  
  
  

