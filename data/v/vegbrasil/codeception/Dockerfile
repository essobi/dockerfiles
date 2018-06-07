FROM composer/composer  
MAINTAINER Vinícius Santana <vinicius@vegbrasil.com>  
  
RUN apt-get update \  
&& apt-get install -y libcurl4-gnutls-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install curl  
  
RUN composer global require 'codeception/codeception:*'  
  
ENTRYPOINT ["codecept"]  
CMD ["--help"]

