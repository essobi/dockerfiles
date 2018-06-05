FROM drupal:7  
MAINTAINER M Parker <mparker17@536298.no-reply.drupal.org>  
  
RUN apt-get update && \  
apt-get install -y libmcrypt-dev  
  
RUN docker-php-ext-install mcrypt  

