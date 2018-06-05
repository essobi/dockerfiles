FROM php:5.6-cli  
MAINTAINER Alison Alonso <alisonlba@gmail.com>  
  
# Extensions and composer  
RUN apt-get update && apt-get install -y git graphviz libxslt1-dev libicu-dev
zlib1g-dev && \  
docker-php-ext-install xsl intl zip && \  
curl -s https://getcomposer.org/composer.phar -o /usr/bin/composer && \  
chmod +x /usr/bin/composer && \  
echo 'date.timezone = "America/Sao_paulo"' >
/usr/local/etc/php/conf.d/timezone.ini  
  
# Ambiance  
ENV COMPOSER_HOME=/usr/local/composer  
WORKDIR ${COMPOSER_HOME}  
  
# Install phpDocumentor  
RUN composer require "phpdocumentor/phpdocumentor:2.*" && \  
ln -s ${COMPOSER_HOME}/vendor/bin/phpdoc /usr/bin/phpdoc  
  
WORKDIR /work  
ENTRYPOINT ["/usr/bin/phpdoc"]  

