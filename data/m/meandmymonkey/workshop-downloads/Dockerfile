FROM meandmymonkey/nginx:latest  
  
MAINTAINER Andreas Hucks "andreas@inputrequired.org"  
RUN apt-get -y install wget  
  
RUN \  
cd /var/www && \  
rm index.html && \  
wget https://getcomposer.org/composer.phar && \  
wget https://phar.phpunit.de/phpunit.phar

