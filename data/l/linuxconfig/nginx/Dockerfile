FROM debian:9  
MAINTAINER Lubos Rendek <web@linuxconfig.org>  
  
# Update package Repository  
RUN apt-get update  
  
# Nginx installation  
RUN apt-get -y install nginx  
  
# Nginx configuration  
RUN mkdir -p /var/www/html  
ADD nginx.conf /etc/nginx/  
  
# Cleaning  
RUN apt-get clean  
  
EXPOSE 80  
CMD ["nginx"]  

