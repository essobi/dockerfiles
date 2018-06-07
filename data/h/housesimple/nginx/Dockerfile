#  
# Nginx Dockerfile  
#  
# https://bitbucket.org/housesimple/docker-nginx  
#  
FROM housesimple/centos  
  
MAINTAINER Olly Nevard <olly.nevard@housesimple.com>  
  
# Install Nginx (from epel-release repo).  
RUN yum -y install nginx && \  
yum clean all  
  
# Add Nginx config.  
ADD nginx.conf /etc/nginx/nginx.conf  
  
# Define mountable directories.  
VOLUME ["/etc/nginx/conf.d", "/var/log/nginx", "/srv/http"]  
  
# Define entrypoint.  
ENTRYPOINT ["nginx"]  
  
# Expose ports.  
EXPOSE 80  
#EXPOSE 443  

