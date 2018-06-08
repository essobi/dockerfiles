FROM php:7.1-apache-jessie  
  
LABEL maintainer="Jan Rydrych <jan.rydrych@gmail.com>" \  
version="1.0.1"  
  
ARG APP_DOCUMENT_ROOT="/app"  
ARG ADMINER_VERSION="4.6.2"  
ARG
ADMINER_DOWNLOAD_SHA256="4b8e0d184a1f0c5ec2c077fd20a06d3e27877d8a63fd4f75aaf92abb103ff458"  
  
ENV TZ="Europe/Prague" \  
HOST_NAME="xyz.local.vm" \  
PHP_MAX_EXECUTION_TIME="180" \  
PHP_MAX_INPUT_TIME="180" \  
PHP_DEFAULT_SOCKET_TIMEOUT="180" \  
PHP_UPLOAD_MAX_SIZE="50M" \  
PHP_POST_MAX_SIZE="50M" \  
XDEBUG_IDEKEY="PHPSTORM" \  
XDEBUG_REMOTE_ENABLE=1 \  
XDEBUG_REMOTE_HOST="localhost" \  
XDEBUG_REMOTE_PORT="9000" \  
XDEBUG_PROFILER_ENABLE_TRIGGER=1 \  
XDEBUG_PROFILER_ENABLE_TRIGGER_VALUE="" \  
XDEBUG_PROFILER_OUTPUT_DIR="${APP_DOCUMENT_ROOT}/tmp/profiler" \  
XDEBUG_PROFILER_OUTPUT_NAME="cachegrind.out.%t"  
  
RUN export TERM="xterm" \  
&& export LANG="en_US.UTF-8" \  
&& export LC_ALL="en_US.UTF-8" \  
&& export DEBIAN_FRONTEND="noninteractive"  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install \  
bash \  
ca-certificates \  
openssl \  
gnupg \  
ghostscript  
  
  
#install libraries for php extension compilation  
RUN apt-get -y install \  
libicu-dev \  
libxml2-dev \  
libmcrypt-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
zlib1g-dev \  
libmemcached-dev  
  
RUN docker-php-ext-install -j$(nproc) \  
bcmath \  
calendar \  
exif \  
gettext \  
intl \  
mcrypt \  
mysqli \  
pdo_mysql \  
soap \  
sockets \  
zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include --with-jpeg-
dir=/usr/include --with-png-dir=/usr/include \  
&& docker-php-ext-install -j$(nproc) gd  
  
#php-xdebug  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug  
  
#php-memcached  
RUN pecl install memcached \  
&& docker-php-ext-enable memcached  
  
#php-redis  
RUN pecl install redis \  
&& docker-php-ext-enable redis  
  
#remove libraries for php extension compilation  
RUN apt-get -y purge \  
libicu-dev \  
libxml2-dev \  
libmcrypt-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
zlib1g-dev \  
libmemcached-dev  
  
  
#adminer  
RUN mkdir /adminer \  
&& set -e \  
&& curl -fsSL
"https://github.com/vrana/adminer/releases/download/v${ADMINER_VERSION}/adminer-${ADMINER_VERSION}-en.php"
-o "/adminer/adminer.php" \  
&& echo "${ADMINER_DOWNLOAD_SHA256} /adminer/adminer.php" |sha256sum -c - \  
&& curl -fsSL
"https://raw.githubusercontent.com/vrana/adminer/master/designs/hever/adminer.css"
-o "/adminer/adminer.css" \  
&& ln -s /adminer/adminer.php /adminer/index.php \  
&& { \  
echo "Alias \"/adminer\" \"/adminer/\""; \  
echo "Alias \"/adminer.css\" \"/adminer/adminer.css\""; \  
echo "<Directory \"/adminer\">"; \  
echo "Require all granted"; \  
echo "</Directory>"; \  
} > /etc/apache2/conf-available/adminer.conf \  
&& ln -s /etc/apache2/conf-available/adminer.conf /etc/apache2/conf-
enabled/999-adminer.conf  
  
  
RUN echo "ServerName \${HOST_NAME}" > /etc/apache2/conf-enabled/fqdn.conf \  
&& sed -ri -e "s!/var/www/html!${APP_DOCUMENT_ROOT}!g" /etc/apache2/sites-
available/*.conf \  
&& sed -ri -e "s!/var/www/!${APP_DOCUMENT_ROOT}!g" /etc/apache2/apache2.conf
/etc/apache2/conf-available/*.conf \  
&& ln -s ../mods-available/rewrite.load /etc/apache2/mods-enabled/rewrite.load  
  
  
RUN { \  
echo "date.timezone = \${TZ}"; \  
echo "upload_max_filesize = \${PHP_UPLOAD_MAX_SIZE}"; \  
echo "post_max_size = \${PHP_POST_MAX_SIZE}"; \  
echo "memory_limit = 256M"; \  
echo "realpath_cache_size = 4096k"; \  
echo "realpath_cache_ttl = 7200"; \  
echo "max_execution_time = \${PHP_MAX_EXECUTION_TIME}"; \  
echo "max_input_time = \${PHP_MAX_INPUT_TIME}"; \  
echo "default_socket_timeout = \${PHP_DEFAULT_SOCKET_TIMEOUT}"; \  
echo "xdebug.idekey = \${XDEBUG_IDEKEY}"; \  
echo "xdebug.remote_enable = \${XDEBUG_REMOTE_ENABLE}"; \  
echo "xdebug.remote_host = \${XDEBUG_REMOTE_HOST}"; \  
echo "xdebug.remote_port = \${XDEBUG_REMOTE_PORT}"; \  
echo "xdebug.profiler_enable_trigger = \${XDEBUG_PROFILER_ENABLE_TRIGGER}"; \  
echo "xdebug.profiler_enable_trigger_value =
\${XDEBUG_PROFILER_ENABLE_TRIGGER_VALUE}"; \  
echo "xdebug.profiler_output_dir = \${XDEBUG_PROFILER_OUTPUT_DIR}"; \  
echo "xdebug.profiler_output_name = \${XDEBUG_PROFILER_OUTPUT_NAME}"; \  
} > /usr/local/etc/php/php.ini  
  
  
RUN sed -i "4iif [ ! -z \"\${APACHE_UID}\" ]; then\n usermod -u \${APACHE_UID}
www-data\nfi\nif [ ! -z \"\${APACHE_GID}\" ]; then\n groupmod -g
\${APACHE_GID} www-data\nfi\n" /usr/local/bin/docker-php-entrypoint  
RUN mkdir ${APP_DOCUMENT_ROOT}  
WORKDIR ${APP_DOCUMENT_ROOT}  

