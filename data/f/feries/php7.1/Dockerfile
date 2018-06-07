FROM php:7.1.12-fpm  
MAINTAINER Ramin Banihashemi <a@ramin.it>  
  
LABEL \  
name="Feries's PHP-FPM 7.1.11-2-Dev Image" \  
image="php-fpm-7.1.11-2" \  
vendor="feries" \  
license="GPLv3" \  
build-date="2018-06-04"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ARG XDEBUG_KEY="PHPSTORM"  
ARG XDEBUG_REMOTE_IP="10.254.254.254"  
ARG XDEBUG_REMOTE_PORT="9000"  
ARG PHPINI="/usr/local/etc/php/php.ini"  
# Install core utilities  
RUN apt-get clean && apt-get update && apt-get install -y git-core vim wget
zsh libicu-dev net-tools zlib1g-dev zip unzip libpng-dev  
  
# Install latest Icu for php intl (mininum symfony requirement: icu 59.1)  
RUN curl -fsS -o /tmp/icu.tgz -L http://download.icu-
project.org/files/icu4c/59.1/icu4c-59_1-src.tgz \  
&& tar -zxf /tmp/icu.tgz -C /tmp \  
&& cd /tmp/icu/source \  
&& ./configure --prefix=/usr/local \  
&& make \  
&& make install \  
&& rm -rf /tmp/icu*  
  
# PHP_CPPFLAGS are used by the docker-php-ext-* scripts  
ENV PHP_CPPFLAGS="$PHP_CPPFLAGS -std=c++11"  
# Configure & Install Intl extension  
RUN docker-php-ext-configure intl --with-icu-dir=/usr/local && docker-php-ext-
install intl  
  
# Install Xdebug  
RUN pecl install xdebug-2.5.5  
# Install apcu  
RUN pecl install apcu  
# Install php-redis (to use it as default session handler)  
RUN pecl install redis  
  
# Enable php extensions  
RUN docker-php-ext-install pdo pdo_mysql zip bcmath gd  
RUN docker-php-ext-enable apcu opcache xdebug redis  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Clean Apt  
RUN apt-get -y autoremove && apt-get clean && apt-get autoclean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# ADD CUSTOM POOL FOR CUSTOMIZE FPM PORT (TO 9001)  
ADD config/zz-docker.conf /usr/local/etc/php-fpm.d/  
  
# - Disable short open tag for php  
# - Error reporting ALL  
# - Display startup errors  
RUN echo "[PHP]\n"\  
"short_open_tag=off\n"\  
"error_reporting=E_ALL\n"\  
"display_startup_errors=On\n"\  
>> $PHPINI  
  
# Timezone configuration (For Symfony compatibility)  
RUN echo "[Date]\n"\  
"date.timezone=\"Europe/Rome\"\n"\  
>> $PHPINI  
  
# Use REDIS as default session handler  
RUN echo "\n[SESSION]\n"\  
"session.save_handler=\"redis\"\n"\  
"session.save_path=\"tcp://redis-session:6379\"\n"\  
>> $PHPINI  
  
# ADD XDEBUG DIRECTIVE IN PHP.INI  
RUN echo "\n[XDEBUG]\n"\  
"xdebug.idekey=$XDEBUG_KEY\n"\  
"xdebug.default_enable=1\n"\  
"xdebug.remote_enable=1\n"\  
"xdebug.remote_autostart=0\n"\  
"xdebug.remote_connect_back=0\n"\  
"xdebug.remote_handler=dbgp\n"\  
"xdebug.profiler_enable=0\n"\  
"xdebug.remote_host=$XDEBUG_REMOTE_IP\n"\  
"xdebug.remote_port=$XDEBUG_REMOTE_PORT\n"\  
>> $PHPINI  
  
# Set timezone  
RUN rm /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/Rome /etc/localtime  
RUN "date"  
  
# Zsh  
RUN bash -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh -q -O -)"  
RUN chsh -s /bin/zsh  
  
# Copy custom rc file to .bashrc & .zshrc  
ADD config/rcsource /root/rcsource  
RUN cat /root/rcsource >> /root/.bashrc  
RUN cat /root/rcsource >> /root/.zshrc  
  
# Alias to execute php in cli with xdebug (es. phpdebug file.php)  
# In docker-compose.yml add this environment PHP_IDE_CONFIG:
"serverName=hostname"  
# Otherwise start with docker run with -e
'PHP_IDE_CONFIG="serverName=hostname"'  
RUN echo "\nalias phpdebug='XDEBUG_CONFIG=\"idekey=$XDEBUG_KEY\" php'" >>
/root/.zshrc  
RUN echo "\nalias phpdebug='XDEBUG_CONFIG=\"idekey=$XDEBUG_KEY\" php'" >>
/root/.bashrc  
  
RUN usermod -u 1000 www-data  
  
WORKDIR /var/www  
  
# FPM PORT  
EXPOSE 9001  

