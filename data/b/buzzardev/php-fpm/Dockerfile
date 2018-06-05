FROM php:5.6-fpm  
MAINTAINER Bart Reunes "@MetalArend"  
# Symfony requirements  
# http://symfony.com/doc/current/reference/requirements.html  
# Required:  
# - PHP needs to be a minimum version of PHP 5.5.9 => FROM php:5.6-fpm  
# - JSON extension needs to be enabled => part of core as of PHP 5.2.0  
# - ctype extension needs to be enabled => enabled by default as of PHP 4.2.0  
# - Your php.ini needs to have the date.timezone setting  
# Set the date.timezone setting as an environment variable, default to UTC  
ENV TZ UTC  
RUN echo "#!/bin/sh\nset -e\n\necho \"date.timezone=\\\\\"\${TZ}\\\\\"\" >
/usr/local/etc/php/conf.d/timezone.ini\n\n. \$(cd \$(dirname \$0);
pwd)/docker-php-entrypoint" > /usr/local/bin/docker-php-entrypoint-with-tz \  
&& chmod +x /usr/local/bin/docker-php-entrypoint-with-tz  
ENTRYPOINT ["docker-php-entrypoint-with-tz"]  
  
# Optional:  
# - You need to have the PHP-XML module installed => ???  
# - You need to have at least version 2.6.21 of libxml => libxml2 installed in
php-fpm container / by default enabled in PHP  
# - PHP tokenizer needs to be enabled => enabled in php-fpm container / by
default enabled in PHP  
# - mbstring functions need to be enabled => enabled in php-fpm container  
# - iconv needs to be enabled => enabled in php-fpm container / by default
enabled in PHP  
# - POSIX needs to be enabled (only on *nix) => enabled in php-fpm container /
by default enabled in PHP  
# - Intl needs to be installed with ICU 4+  
# - APC 3.0.17+ (or another opcode cache needs to be installed)  
# - php.ini recommended settings  
# - short_open_tag = Off => by default 1 in PHP  
# - magic_quotes_gpc = Off => removed as of PHP 5.4.0  
# - register_globals = Off => removed as of PHP 5.4.0  
# - session.auto_start = Off => by default 0 in PHP  
# - extra php.ini recommended settings, extracted from the requirements script  
# - mbstring.func_overload = 0 => by default 0 in PHP, deprecated as of PHP
7.2.0  
# - intl.error_level = 0 => by default 0 in PHP  
# Install Intl with ICU 4+  
RUN apt-get update -yqq && apt-get install -yq libicu-dev g++ \  
&& apt-get autoremove -yq --purge && apt-get clean && apt-get -f install && rm
-rf /var/lib/apt/lists/* /var/cache/apt/archives/*  
RUN curl -sS -o /tmp/icu.tar.gz -L http://download.icu-
project.org/files/icu4c/58.2/icu4c-58_2-src.tgz \  
&& tar -zxf /tmp/icu.tar.gz -C /tmp \  
&& cd /tmp/icu/source \  
&& ./configure --prefix=/usr/local \  
&& make \  
&& make install \  
&& rm -rf /tmp/*  
RUN docker-php-ext-configure intl --with-icu-dir=/usr/local \  
&& docker-php-ext-install intl  
  
# Install opcache  
RUN docker-php-ext-install opcache  
  
# Install APCu  
RUN if php -r "exit((int)!version_compare(PHP_VERSION, '7.0.0', '<'));"; then
\  
yes | pecl install apcu-4.0.11 \  
&& echo "extension=apcu.so" > $PHP_INI_DIR/conf.d/apcu.ini; \  
else \  
yes | pecl install apcu apcu_bc-beta \  
&& echo "extension=apc.so \nextension=apcu.so \n" >
$PHP_INI_DIR/conf.d/apcu.ini; \  
fi  
  
# Add an empty php.ini (to satisfy requirements)  
RUN touch /usr/local/etc/php/php.ini  
  
# Add recommended php.ini settings  
RUN echo "\  
short_open_tag=0 \n\  
session.auto_start=0 \n\  
" > /usr/local/etc/php/conf.d/symfony.ini  
  
# Install Blackfire - https://blackfire.io/docs/integrations/docker  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini  
  
# Install Xdebug - https://github.com/xdebug/xdebug  
RUN yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > $PHP_INI_DIR/conf.d/xdebug.ini  
  
# Defaults  
WORKDIR /var/www/html  
  
CMD ["php-fpm"]  

