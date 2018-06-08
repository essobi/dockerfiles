# Dockerfile for a static web server powered by Nginx  
# Use the Trusty (14.04) Ubuntu base image  
FROM ubuntu:14.04  
# Optionally set the maintainer  
MAINTAINER Paul Lane <plane123@gmail.com>  
  
  
# Following installation instructions from
http://nginx.org/en/linux_packages.html  
# Add the Nginx PGP key to the image and add it to the apt program keyring  
ADD nginx_signing.key /tmp/nginx_signing.key  
RUN apt-key add /tmp/nginx_signing.key  
  
# Append the nginx.org sources to the /etc/apt/sources.list file  
RUN echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" >>
/etc/apt/sources.list \  
&& echo "deb-src http://nginx.org/packages/ubuntu trusty nginx" >>
/etc/apt/sources.list  
  
# Update the local package database  
RUN apt-get update  
  
# Install nginx  
RUN apt-get install -y nginx  
  
# Add our static HTML page to the image's /usr/share/nginx/html directory  
ADD our-page.html /usr/share/nginx/html/  
  
# Expose ports 80 and 443 for HTTP and HTTPS  
EXPOSE 80 443  
# Set the default command for this image  
# (with extra configuration option to turn off nginx's daemon mode)  
CMD ["nginx" , "-g", "daemon off;"]  

