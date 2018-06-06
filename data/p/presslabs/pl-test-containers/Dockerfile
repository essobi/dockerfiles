FROM php:5.6-alpine  
  
ENV COMPOSER_VERSION 1.2.0  
  
ADD install-wp-tests.sh /install-wp-tests.sh  
  
RUN set -ex \  
&& apk add --no-cache \  
bash \  
make \  
subversion \  
git \  
curl \  
openssl \  
&& bash /install-wp-tests.sh 3.9 \  
&& bash /install-wp-tests.sh 4.7.4 \  
&& docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) mysqli \  
&& curl -L
https://github.com/jwilder/dockerize/releases/download/v0.4.0/dockerize-
alpine-linux-amd64-v0.4.0.tar.gz | tar -zxf - -C /usr/bin \  
&& chown root:root /usr/bin/dockerize \  
&& curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --version=${COMPOSER_VERSION} && rm -rf /tmp/composer-
setup.php  

