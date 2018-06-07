FROM dishuostec/php:7.2-fpm-phalcon  
  
ENV COMPOSER_VERSION="1.6.3" \  
COMPOSER_SHA256="52cb7bbbaee720471e3b34c8ae6db53a38f0b759c06078a80080db739e4dcab6"  
RUN curl -fsSL
"https://getcomposer.org/download/${COMPOSER_VERSION}/composer.phar" -o
composer.phar \  
&& echo "${COMPOSER_SHA256} *composer.phar" | sha256sum -c - \  
&& chmod 0755 composer.phar \  
&& mv composer.phar /usr/local/bin/composer  
  

