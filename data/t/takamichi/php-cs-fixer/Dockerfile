FROM php:7.2-cli-alpine3.7  
LABEL maintainer="Takamichi URATA <taka@seraphimis.net>"  
  
COPY script/docker-entrypoint.sh /usr/local/bin  
RUN mkdir -p /workdir; \  
chmod a+x /usr/local/bin/docker-entrypoint.sh; \  
apk add --no-cache su-exec  
  
VOLUME ["/workdir"]  
WORKDIR /workdir  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD []  
  
ENV PHP_CS_FIXER v2.8.4  
RUN curl -sSL https://github.com/FriendsOfPHP/PHP-CS-
Fixer/releases/download/${PHP_CS_FIXER}/php-cs-fixer.phar \  
-o /usr/local/bin/php-cs-fixer; \  
chmod a+x /usr/local/bin/php-cs-fixer; \  
php-cs-fixer --version  

