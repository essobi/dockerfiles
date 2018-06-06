FROM nginx:latest  
MAINTAINER Caleb Collins <kbcaleb@gmail.com>  
  
# Create SSL directory  
RUN mkdir /etc/nginx/ssl  
  
# Generate dhparam.pem file  
RUN openssl dhparam -out /etc/nginx/ssl/dhparam.pem 2048  

