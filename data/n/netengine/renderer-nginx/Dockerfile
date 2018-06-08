FROM ubuntu:trusty  
  
MAINTAINER team@netengine.com.au  
  
# Install nginx  
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" >>
/etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" >>
/etc/apt/sources.list  
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C300EE8C  
RUN apt-get update  
RUN apt-get install nginx -y -q  
  
# Configure nginx  
ADD files /config  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Expose ports  
EXPOSE 80  
CMD ["/usr/sbin/nginx", "-c", "/config/nginx.conf"]  

