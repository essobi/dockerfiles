FROM phusion/baseimage  
  
# Add the "PHP 7" ppa  
RUN apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:ondrej/php  
  
# Docker-friendly trivial templating for configuration files using environment
keys  
# https://github.com/kreuzwerker/envplate  
RUN curl -sLo /usr/local/bin/ep
https://github.com/kreuzwerker/envplate/releases/download/v0.0.8/ep-linux &&
chmod +x /usr/local/bin/ep  
  
# Install "PHP Extentions", "libraries", "Software's"  
RUN apt-get update && \  
apt-get install -y --force-yes \  
software-properties-common \  
ant \  
libmcrypt-dev \  
libssl-dev \  
pkg-config \  
libpng12-dev \  
libjpeg-dev \  
libpq-dev \  
postgresql \  
curl \  
nano \  
htop \  
wget \  
sed \  
zlib1g-dev \  
git \  
nginx \  
php-memcached \  
php7.1-cli \  
php7.1-common \  
php7.1-curl \  
php7.1-json \  
php7.1-xml \  
php7.1-zip \  
php7.1-mysql \  
php7.1-pgsql \  
php7.1-mcrypt \  
php7.1-mbstring \  
php7.1-bcmath \  
php7.1-gd \  
php7.1-gmp \  
php7.1-dev \  
php7.1-fpm \  
&& apt-get clean  
  
# Nodejs  
ENV NODEJS_VERSION "8.x"  
RUN curl -sL "https://deb.nodesource.com/setup_$NODEJS_VERSION" | bash - && \  
apt-get -y install nodejs  
  
# Postgres install  
RUN add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ xenial-
pgdg main" && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add - && \  
apt-get update && apt-get -y install postgresql-9.6  
  
# Redis install  
RUN apt-get -y --force-yes install php-redis  
  
# Mongodb  
RUN pecl install mongodb && echo "extension=mongodb.so" >>
/etc/php/7.1/cli/conf.d/30-mongodb.ini  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer config -g github-oauth.github.com
"b6234a017e3c7ae770cee6766d07960d61ec4880" \  
&& composer global require "fxp/composer-asset-plugin:^1.2.0" \  
&& composer global require hirak/prestissimo  
  
# Yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install yarn  
  
# Services  
COPY service/nginx /etc/service/nginx  
COPY service/phpfpm /etc/service/phpfpm  
  
# Configs  
ENV PM dynamic  
ENV PM_MAX_CHILDREN 1000  
ENV PM_START_SERVERS 4  
ENV PM_MIN_SPARE_SERVERS 2  
ENV PM_MAX_SPARE_SERVERS 4  
ENV PM_MAX_REQUESTS 0  
ENV PM_STATUS_PATH /fpm_status  
COPY fpm/php.ini /etc/php/7.1/fpm/php.ini  
COPY fpm/php-fpm.conf /etc/php/7.1/fpm/php-fpm.conf  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 80

