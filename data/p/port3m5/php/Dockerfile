FROM php:alpine  
  
RUN apk update \  
&& apk add $PHPIZE_DEPS ca-certificates wget \  
&& update-ca-certificates \  
&& docker-php-source extract \  
&& pecl install xdebug \  
&& docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null ||
1) \  
iconv \  
pdo_mysql \  
&& docker-php-ext-enable xdebug \  
&& docker-php-source delete \  
&& apk del $PHPIZE_DEPS \  
&& EXPECTED_SIGNATURE=$(wget https://composer.github.io/installer.sig -O -
-q);\  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');";\  
ACTUAL_SIGNATURE=$(php -r "echo hash_file('SHA384', 'composer-setup.php');");\  
if [ "$EXPECTED_SIGNATURE" = "$ACTUAL_SIGNATURE" ]; then\  
php composer-setup.php --install-dir=/usr/bin --filename=composer --quiet;\  
RESULT=$?;\  
rm composer-setup.php;\  
exit $RESULT;\  
else\  
>&2 echo "ERROR: Invalid installer signature, got $ACTUAL_SIGNATURE expected
$EXPECTED_SIGNATURE";\  
rm composer-setup.php;\  
exit 1;\  
fi  

