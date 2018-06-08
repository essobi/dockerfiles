#  
# Nginx Dockerfile  
#  
# https://github.com/dockerfile/nginx  
#  
# Pull base image.  
FROM ubuntu:14.04  
# Install Nginx.  
RUN \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
nginx \  
nginx-extras \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
RUN chown -R www-data:www-data /var/lib/nginx  
  
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

