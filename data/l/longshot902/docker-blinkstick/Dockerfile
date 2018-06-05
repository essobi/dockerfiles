FROM php:7.1-apache  
RUN apt-get update && apt-get -y install python-pip usbutils sudo git && pip
install blinkstick && apt-get clean && rm -rf /tmp/* /var/tmp/*  
  
ENV USER www-data  
  
RUN echo "$USER ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USER  
  
RUN git clone https://github.com/longshot902/blinkstickweb.git /var/www/html

