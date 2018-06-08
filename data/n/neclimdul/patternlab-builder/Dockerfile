FROM node:8.4-alpine  
MAINTAINER James Gilliland <neclimdul@gmail.com>  
  
EXPOSE 3001 3050  
WORKDIR /usr/src/app  
CMD /usr/local/bin/pattern-lab-runner.sh  
  
RUN apk -U update && apk add git python make g++ \  
&& apk add curl php7 php7-json php7-phar php7-iconv php7-zlib php7-openssl
php7-mbstring php7-ctype php7-tokenizer \  
&& ln -sf /usr/bin/php7 /usr/bin/php \  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  
  
# Install composer...  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /tmp  
ENV COMPOSER_VERSION 1.5.1  
RUN curl -s -f -L -o /tmp/installer.php
https://raw.githubusercontent.com/composer/getcomposer.org/da290238de6d63faace0343efbdd5aa9354332c5/web/installer
\  
&& php -r " \  
\$signature =
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410';
\  
\$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \  
if (!hash_equals(\$signature, \$hash)) { \  
unlink('/tmp/installer.php'); \  
echo 'Integrity check failed, installer is either corrupt or worse.' .
PHP_EOL; \  
exit(1); \  
}" \  
&& php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer
--version=${COMPOSER_VERSION} \  
&& composer --ansi --version --no-interaction \  
&& rm -rf /tmp/* /tmp/.htaccess  
  
COPY pattern-lab-runner.sh /usr/local/bin/pattern-lab-runner.sh  

