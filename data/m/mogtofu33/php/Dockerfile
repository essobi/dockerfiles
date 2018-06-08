FROM mogtofu33/alpine-base:latest  
  
MAINTAINER moimog33@gmail.com  
  
# Set specific uid/gid to web server user to fix permissions issues.  
#ENV LOCAL_UID=1000  
#ENV LOCAL_GID=1000  
  
# See https://hub.docker.com/_/composer/  
ENV PATH "/composer/vendor/bin:$PATH"  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /composer  
ENV COMPOSER_VERSION 1.6.3  
ENV COMPOSER_INSTALLER_URL
"https://raw.githubusercontent.com/composer/getcomposer.org/b107d959a5924af895807021fcef4ffec5a76aa9/web/installer"  
ENV COMPOSER_INSTALLER_HASH
"544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061"  
  
# trust this project public key to trust the packages.  
ADD https://php.codecasts.rocks/php-alpine.rsa.pub /etc/apk/keys/php-
alpine.rsa.pub  
  
# Install Php extensions,Alpine package list to:  
# https://php.codecasts.rocks/v3.7/php-7.2  
RUN echo "https://php.codecasts.rocks/v3.7/php-7.2" >> /etc/apk/repositories \  
&& echo "@php https://php.codecasts.rocks/v3.7/php-7.2" >>
/etc/apk/repositories \  
&& apk add --update --no-cache \  
ca-certificates \  
curl \  
openssh-client \  
libmemcached-libs \  
libevent \  
libssl1.0 \  
musl \  
yaml \  
php7 \  
php7-apcu@php \  
php7-bcmath \  
php7-bz2 \  
php7-calendar \  
php7-cgi \  
php7-common \  
php7-ctype \  
php7-curl \  
php7-dba \  
php7-dom \  
php7-embed \  
php7-enchant \  
php7-exif \  
php7-fpm \  
php7-ftp \  
php7-gd \  
php7-gmp \  
php7-iconv \  
php7-imagick \  
php7-imap \  
php7-intl \  
php7-json \  
php7-ldap \  
php7-litespeed \  
php7-mbstring \  
php7-memcached \  
php7-mysqli \  
php7-mysqlnd \  
php7-opcache \  
php7-openssl \  
php7-pcntl \  
php7-pdo \  
php7-pdo_mysql \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-pear \  
php7-pgsql \  
php7-phar \  
php7-phpdbg \  
php7-posix \  
php7-redis \  
php7-session \  
php7-soap \  
php7-sockets \  
php7-sodium \  
php7-ssh2 \  
php7-sysvmsg \  
php7-sysvsem \  
php7-sysvshm \  
php7-tidy \  
php7-wddx \  
php7-xdebug \  
php7-xml \  
php7-xmlreader \  
# php7-xmlrpc \  
php7-xsl \  
php7-zip \  
php7-zlib  
  
RUN apk add --update --no-cache \  
mysql-client \  
postgresql-client \  
rsync \  
openssh \  
openssl  
  
# Fix php bin link.  
RUN ln -s /usr/bin/php7 /usr/bin/php && \  
ln -s /usr/bin/php-fpm7 /usr/sbin/php-fpm  
  
# Install Composer.  
# from https://github.com/composer/docker/blob/master/1.5/Dockerfile  
RUN curl -s -f -L -o /tmp/installer.php ${COMPOSER_INSTALLER_URL} \  
&& php -r " \  
\$signature = '${COMPOSER_INSTALLER_HASH}'; \  
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
  
# Install prestissimo and php code sniffer with Drupal standards.  
RUN /usr/bin/composer global require "hirak/prestissimo:^0.3"  
RUN /usr/bin/composer global require "drupal/coder"  
RUN /composer/vendor/bin/phpcs --config-set installed_paths
/composer/vendor/drupal/coder/coder_sniffer  
  
# ensure www-data user exists  
RUN mkdir -p /var/www/localhost \  
&& addgroup -g 82 -S www-data \  
&& adduser -u 82 -D -S -G www-data apache \  
&& chown -R apache:www-data /var/www  
  
# Fix composer cache folder permission to run composer as apache user.  
RUN chown -R apache:www-data /composer/cache  
  
# Copy root bashrc config for Apache user when running cmd.  
RUN cp /root/.bashrc /var/www/.bashrc && \  
chown -R apache:www-data /var/www  
  
# Clean.  
RUN rm -rf /var/cache/apk/*  
  
# Set apache script.  
COPY scripts/run.sh /scripts/run.sh  
RUN chmod +x /scripts/run.sh  
  
EXPOSE 9000  
  
VOLUME ["/var/www/localhost"]  
  
ENTRYPOINT ["/bin/bash" , "/scripts/run.sh"]  

