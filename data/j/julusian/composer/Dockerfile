FROM php:5.6-cli  
MAINTAINER Julian Waller <git@julusian.co.uk>  
  
ADD install-composer.sh /  
  
RUN apt-get update && \  
apt-get install -y git zip unzip && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/lib/apt/cache/*.deb  
  
RUN /install-composer.sh  

