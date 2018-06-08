FROM garage/base  
  
MAINTAINER Reinaldo Junior <juniorz@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN echo "deb http://dl.hhvm.com/ubuntu $(/var/garage/base-release) main" >
/etc/apt/sources.list.d/hhvm.list &&\  
apt-get update &&\  
/var/garage/install --allow-unauthenticated hhvm  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV GARAGE_PROVIDES hhvm  

