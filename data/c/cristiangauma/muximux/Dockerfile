FROM php:apache  
  
MAINTAINER Cristian Gauxachs (cristiangauma) <cristian.gauxachs@gmail.com>  
  
# Installing git to download the Muximux code from Github  
RUN apt-get update && apt-get install -y git  
  
# Downloading Muximux in the correct path  
RUN cd /var/www/html && rm -rf * && git clone
https://github.com/mescon/Muximux.git . && chown -R www-data:www-data /var/www  
  
# Cleaning, to reduce the image and container size  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80  

