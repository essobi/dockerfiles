FROM mogtofu33/alpine-base:latest  
  
MAINTAINER moimog33@gmail.com  
  
# Set specific uid/gid to web server user to fix permissions issues.  
#ENV LOCAL_UID=1000  
#ENV LOCAL_GID=1000  
# Leave empty to not generate a certificate.  
ENV GENERATE_APACHE_CERTIFICATE=  
  
# See https://hub.docker.com/_/composer/  
ENV PATH "/composer/vendor/bin:$PATH"  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /composer  
ENV COMPOSER_VERSION 1.6.3  
ENV COMPOSER_INSTALLER_URL
"https://raw.githubusercontent.com/composer/getcomposer.org/b107d959a5924af895807021fcef4ffec5a76aa9/web/installer"  
ENV COMPOSER_INSTALLER_HASH
"544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061"  
# Install Php extensions, ordered by Alpine package list.  
# https://pkgs.alpinelinux.org/packages?name=php7*&branch=v3.7&arch=x86_64  
RUN apk add --update --no-cache \  
php7-memcached \  
php7 \  
php7-common \  
php7-sysvsem \  
php7-sysvshm \  
php7-tidy \  
php7-tokenizer \  
php7-wddx \  
php7-xml \  
php7-xmlreader \  
php7-xmlrpc \  
php7-xmlwriter \  
php7-xsl \  
php7-zip \  
php7-zlib \  
php7-phar \  
php7-posix \  
php7-pspell \  
php7-recode \  
php7-session \  
php7-shmop \  
php7-simplexml \  
php7-snmp \  
php7-soap \  
php7-sockets \  
php7-sqlite3 \  
php7-sysvmsg \  
php7-mysqlnd \  
php7-odbc \  
php7-opcache \  
php7-openssl \  
php7-pcntl \  
php7-pdo \  
php7-pdo_dblib \  
php7-pdo_mysql \  
php7-pdo_odbc \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-pgsql \  
php7-ftp \  
php7-gd \  
php7-gettext \  
php7-gmp \  
php7-iconv \  
php7-imap \  
php7-intl \  
php7-json \  
php7-ldap \  
php7-mbstring \  
php7-mcrypt \  
php7-mysqli \  
php7-bcmath \  
php7-bz2 \  
php7-calendar \  
php7-ctype \  
php7-curl \  
php7-dba \  
php7-dom \  
php7-enchant \  
php7-exif \  
php7-fileinfo \  
php7-pear \  
php7-apache2 \  
php7-cgi \  
php7-dev \  
php7-doc \  
php7-embed \  
php7-fpm \  
php7-litespeed \  
php7-phpdbg \  
php7-imagick \  
php7-ssh2 \  
php7-xdebug \  
php7-amqp \  
php7-mailparse \  
php7-oauth \  
php7-pear-mail_mime \  
php7-zmq \  
php7-apcu \  
php7-redis \  
php7-pear-net_socket  
  
# Apache packages.  
# https://pkgs.alpinelinux.org/packages?name=apache*&branch=v3.7&arch=x86_64  
RUN apk add --update --no-cache \  
apache2 \  
apache2-utils \  
apache2-error \  
apache2-http2 \  
apache2-icons \  
apache2-ldap \  
apache2-proxy \  
apache2-ssl \  
apache-mod-fcgid  
  
# Database clients and sync needed for Drush.  
RUN apk add --update --no-cache \  
mysql-client \  
postgresql-client \  
rsync \  
openssh \  
openssl  
  
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
  
# Fix composer cache folder permission to run composer as apache user.  
RUN chown -R apache:www-data /composer/cache  
  
# Copy root bashrc config for Apache user when running cmd.  
RUN cp /root/.bashrc /var/www/.bashrc && \  
chown apache:www-data /var/www/.bashrc  
  
# Fix web root permission, set php and apache logs.  
RUN chown -R apache:www-data /var/www  
  
# Clean.  
RUN rm -rf /var/cache/apk/*  
  
# Set apache script.  
COPY scripts/run.sh /scripts/run.sh  
RUN chmod +x /scripts/run.sh  
  
EXPOSE 80  
EXPOSE 443  
  
VOLUME ["/var/www/localhost"]  
  
ENTRYPOINT ["/bin/bash" , "/scripts/run.sh"]  

