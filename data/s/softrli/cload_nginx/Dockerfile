# cload_nginx  
#  
# Dockerfile to setup Nginx on Ubuntu base image  
# for basic reverse-proxying.  
#  
# VERSION 0.0.1  
FROM softrli/cload_base  
MAINTAINER Romain Champourlier, romain@softr.li  
  
# Install nginx  
RUN apt-get install -y nginx  
  
# Configure nginx  
# Prevent nginx from deamoning itself to keep the container alive  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Run nginx when starting the container  
CMD nginx  
  
# Exposes HTTP and HTTPS ports  
EXPOSE 80 443

