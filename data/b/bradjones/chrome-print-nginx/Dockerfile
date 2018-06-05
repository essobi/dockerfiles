# Chrome Print - nginx  
#
==============================================================================  
# This container runs nginx and is the frontend for our rest api.  
FROM fedora:latest  
MAINTAINER Brad Jones <brad@bjc.id.au>  
  
# Update base image  
RUN yum -y update && yum clean all  
  
# Install packages  
RUN yum -y install \  
nginx \  
&& yum clean all  
  
# Add our container files  
ADD ["container-files","/"]  
  
# Publish standard http and httpd ports  
EXPOSE 80 443  
# Add our chrome user, nginx and php-fpm also run as the chorme user.  
# This is so that documents printed by google chrome can be read by php.  
RUN useradd -ms /bin/bash chrome  
RUN chown -R chrome:chrome /home/chrome  
  
# Start nginx  
CMD ["/usr/sbin/nginx"]  

