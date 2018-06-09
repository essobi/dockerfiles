FROM sylvaindeloux/php:7.0-fpm-dev  
MAINTAINER Sylvain Deloux <docker@eax.fr>  
  
  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# Node.js  
  
RUN apt-get update && \  
curl -sL https://deb.nodesource.com/setup_9.x | bash - && \  
apt-get install -y nodejs bzip2 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

