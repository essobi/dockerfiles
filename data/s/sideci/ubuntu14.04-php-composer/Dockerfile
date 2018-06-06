FROM quay.io/actcat/buildpack_php:latest  
  
MAINTAINER Vexus2 <hikaru.tooyama@gmail.com>  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Print composer version information  
RUN composer -V  
  
# Install composer_outdated command  
ADD composer_outdated /usr/local/composer_outdated  
RUN chmod +x /usr/local/composer_outdated/composer_outdated.php  
RUN ln -s /usr/local/composer_outdated/composer_outdated.php
/usr/local/bin/composer_outdated  

