## This container takes in SSL keys and certificates via env variables.  
# Nginx Dockerfile  
#  
# https://github.com/inanimate/docker-nginx-ssl  
#  
# Pull base image.  
FROM dockerfile/ubuntu  
  
# Install Nginx.  
RUN \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update && \  
apt-get install -y nginx && \  
rm -rf /var/lib/apt/lists/* && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx  
  
# Define mountable directories.  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/ssl", "/etc/nginx/conf.d",
"/var/log/nginx", "/var/www/html"]  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Add in our launcher script  
ADD run /etc/nginx/run  
RUN chmod +x /etc/nginx/run  
  
# Define default command.  
CMD ["/etc/nginx/run"]  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  

