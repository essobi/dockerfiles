#  
# Nginx Dockerfile  
#  
# https://github.com/dockerfile/nginx  
#  
# Pull base image.  
FROM ubuntu:14.04  
# Install soft prop common for add-apt-repository command  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install software-properties-
common  
# Install Nginx.  
RUN \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update && \  
apt-get install -y nginx && \  
rm -rf /var/lib/apt/lists/* && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx  
  
# Define mountable directories.  
#VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/var/www/html"]  
# Copy the 2048 source file in the container  
COPY web /var/www/html  
# Be sure that web server can access them  
RUN chown -R www-data:www-data /var/www/html  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Define default command.  
CMD ["nginx"]  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  

