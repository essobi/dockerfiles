# Pull base image.  
FROM debian:latest  
  
# Install Nginx.  
RUN \  
apt-get update && \  
apt-get install -y nginx nginx-extras php5 php5-fpm && \  
rm -rf /var/lib/apt/lists/* && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx  
  
# Define mountable directories.  
VOLUME ["/etc/nginx", "/var/log/nginx", "/var/www", "/etc/php5"]  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Define default command.  
CMD ["nginx"]  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  

