FROM php:7.2-cli-stretch  
  
LABEL maintainer="Jan Rydrych <jan.rydrych@gmail.com>" \  
version="1.0.1"  
  
ARG APP_DOCUMENT_ROOT="/app"  
ARG DREX_UID=9999  
ARG DREX_GID=9999  
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
git  
  
#install libraries for php extension compilation  
RUN apt-get -y install \  
libicu-dev \  
libxml2-dev \  
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
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
zlib1g-dev \  
libmemcached-dev  
  
#install node & npm globally  
RUN curl -sSL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs  
  
#gulp & grunt globally  
RUN npm install -g \  
gulp-cli \  
grunt-cli \  
bower  
  
#install composer globally  
RUN curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin/ --filename=composer  
  
#install deployer globally  
RUN curl -sSLO https://deployer.org/deployer.phar \  
&& mv deployer.phar /usr/local/bin/deployer \  
&& chmod +x /usr/local/bin/deployer \  
&& ln -s /usr/local/bin/deployer /usr/local/bin/dep  
  
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
  
RUN mkdir ${APP_DOCUMENT_ROOT}  
WORKDIR ${APP_DOCUMENT_ROOT}  
  
RUN groupadd -g ${DREX_GID} drexg \  
&& useradd -d /tmp/drexu -u ${DREX_UID} -g ${DREX_GID} drexu \  
&& mkdir /tmp/drexu && chown drexu:drexg /tmp/drexu  
USER drexu  

