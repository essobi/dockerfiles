FROM php:5.6-fpm-alpine  
  
RUN apk add --no-cache bash nginx \  
&& mkdir -p /run/nginx \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
# Install confd for Nginx template rendering and Composer for PHP package
dependencies  
ENV CONFD_VERSION=0.11.0 \  
COMPOSER_ALLOW_SUPERUSER=1 \  
COMPOSER_VERSION=1.3.0  
RUN curl -fSL -o /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 \  
&& chmod +x /usr/local/bin/confd \  
&& confd -version \  
&& curl -fSL -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -fSL -o /tmp/composer-setup.sig
https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --version=${COMPOSER_VERSION} \  
&& rm -rf /tmp/composer-setup.php \  
&& composer -V  
  
# And install the project packages  
COPY src/composer.json src/composer.lock /tmp/  
RUN cd /tmp && composer --ansi install -o  
  
# Environment variables  
ENV
SENTRY_DSN=https://a115369e208847449cc6c05f4d332672:0ad536e676074277a1a9c2d6dfba6da6@sentry.io/119540  
# Install the codebase  
COPY build/nginx.conf /etc/nginx/nginx.conf  
COPY src /var/www  
RUN mv -f /tmp/vendor /var/www/vendor  
  
WORKDIR /var/www  

