FROM hermsi/alpine-fpm-php:7.2  
LABEL maintainer="https://github.com/hermsi1337"  
  
# Reference:  
# https://github.com/composer/docker/blob/master/Dockerfile.template  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /tmp  
ENV COMPOSER_VERSION 1.6.5  
ENV COMPOSER_INSTALLER_URL https://getcomposer.org/installer  
ENV COMPOSER_SHA
544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061  
  
RUN curl -s -f -L -o /tmp/installer.php ${COMPOSER_INSTALLER_URL} \  
&& php -r " \  
\$signature = '${COMPOSER_SHA}'; \  
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
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
WORKDIR /app  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["composer"]

