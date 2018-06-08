FROM ubuntu:14.04  
MAINTAINER James Sharp <james@ortootech.com>  
  
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty main universe' >
/etc/apt/sources.list  
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" >
/etc/apt/sources.list.d/nginx-stable-trusty.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C  
RUN apt-get update  
  
# Install nginx  
RUN apt-get install -y -q nginx  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Expose port 80  
EXPOSE 80  
CMD ["nginx"]

