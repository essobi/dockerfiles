# Pull base image.  
FROM nginx  
  
# Install Nginx.  
RUN \  
apt-get update && \  
apt-get install nginx && \  
rm -rf /var/lib/apt/lists/*  
  
  
# Define mountable directories.  
# VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/var/www/html"]  
VOLUME ["/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx"]  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
# Copy new configuration file to director  
COPY /nginx.conf /etc/nginx  
  
# Define default command.  
CMD ["nginx"] && service nginx start && bin/bash  
  
# Expose ports.  
EXPOSE 8080

