############################################################  
# PHP FPM image for Magento 2 front-end development  
#  
# Contains common and useful...  
# php extensions: mcrypt, gd, mysql  
# linux packages: mysql-client, git, curl, wget, pwgen  
# front-end dev: node, npm, grunt  
############################################################  
  
FROM erdiko/php-fpm:7.1-magento  
  
LABEL maintainer="John Arroyo <john@arroyolabs.com>" description="PHP-FPM for
Magento 2 front-end development"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
RUN apt-get install -y build-essential  
RUN npm install -g grunt-cli  
  
CMD ["php-fpm"]  

