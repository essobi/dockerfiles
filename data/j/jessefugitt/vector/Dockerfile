# Nginx/Vector Dockerfile  
#  
# VERSION 0.0.1  
# Pull base image.  
FROM ubuntu:14.04  
MAINTAINER Jesse Fugitt  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Nginx.  
RUN \  
apt-get update && \  
apt-get install -y nginx wget && \  
rm -rf /var/lib/apt/lists/* && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx  
  
RUN cd /usr/share/nginx/html && \  
wget --output-document=-
https://bintray.com/artifact/download/netflixoss/downloads/1.0.1/vector.tar.gz
\  
| tar zxf -  
  
# Define mountable directories.  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/var/www/html"]  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Define default command.  
CMD ["nginx"]  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  

