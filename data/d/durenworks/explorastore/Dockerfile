FROM durenworks/laravel-dev:0.6  
# Docker maintainer  
MAINTAINER Airlangga Cahya Utama <airlangga@durenworks.com>  
  
# Update package  
RUN apt-get update && \  
apt-get install -yq \  
fontconfig \  
nodejs \  
libcairo2 \  
libjpeg8 \  
libpango1.0-0 \  
libgif4 \  
php5-imagick && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Create Folder and Permission Fix  
RUN mkdir -p /usr/share/fonts/truetype/explora && chmod a+rwX
/usr/share/fonts/truetype/explora  

