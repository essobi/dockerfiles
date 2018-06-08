FROM marlonbe/docker-php:7.2-mysql  
MAINTAINER PHP Marlon <php@marlon.be>  
  
# PHP QA tools  
RUN apt-get update -y && \  
apt-get install -y -f --force-yes ant git-core && \  
curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer && \  
apt-get clean -y  
  
ENV PATH /root/.composer/vendor/bin:$PATH  

