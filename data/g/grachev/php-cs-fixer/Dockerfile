FROM php:alpine  
  
MAINTAINER Konstantin Grachev <me@grachevko.ru>  
  
ENV FIXER_VERSION v2.3.2  
RUN set -ex \  
&& apk add --no-cache git \  
&& cd /usr/bin \  
&& curl -fSL "https://github.com/FriendsOfPHP/PHP-CS-
Fixer/releases/download/$FIXER_VERSION/php-cs-fixer.phar" -o php-cs-fixer \  
&& chmod a+x php-cs-fixer  
  
ENTRYPOINT ["php-cs-fixer"]  
CMD ["--help"]  

