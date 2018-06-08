FROM 2dotstwice/nginx-php71-silex  
  
ADD ./files/etc/php/fpm/conf.d/90-custom.ini
${PHP_CONFIG_DIR}/fpm/conf.d/90-custom.ini  
  
# PHP configuration for development  
RUN sed -i -e
"s/opcache.validate_timestamps=0/opcache.validate_timestamps=1/g"
${PHP_CONFIG_DIR}/fpm/conf.d/99-custom.ini  
  
# Partially borrowed from https://github.com/composer/docker.  
# Install composer.  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends -q install
curl && \  
rm -rf /var/lib/apt/lists/*  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /tmp  
ENV COMPOSER_VERSION 1.5.2  
  
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

