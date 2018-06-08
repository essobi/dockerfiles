#  
# Nginx Dockerfile  
# git@github.com:monsieurchico/docker-nginx.git  
#  
FROM ubuntu:latest  
MAINTAINER Romain Derocle "rderocle@gmail.com"  
# prevent debian errors  
ENV DEBIAN_FRONTEND noninteractive  
  
# update os and install nginx  
RUN \  
apt-get update && \  
apt-get -y install software-properties-common && \  
add-apt-repository ppa:nginx/development && \  
apt-get update && \  
apt-get install -y nginx && \  
rm -rf /var/lib/apt/lists/* && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx  
  
# expose ports  
EXPOSE 80  
EXPOSE 443  
# define mountable volumes  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/var/www"]  
  
# add launch script  
COPY ./resources/startup.sh /startup.sh  
  
# define entrypoint  
ENTRYPOINT ["/bin/bash", "/startup.sh"]  
  
# define workdir  
WORKDIR /etc/nginx  

