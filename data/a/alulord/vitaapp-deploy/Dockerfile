FROM php:7.1-fpm  
  
# Install required system packages  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y install \  
git \  
zlib1g-dev \  
libssl-dev \  
ca-certificates \  
bzip2 \  
libfontconfig \  
nano \  
curl \  
openssh-client \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libxml2-dev \  
libpq-dev \  
libpq5 \  
mysql-client \  
supervisor \  
\--no-install-recommends && \  
# Install dumb-init (to handle PID 1 correctly).  
# https://github.com/Yelp/dumb-init  
curl -Lo /tmp/dumb-init.deb https://github.com/Yelp/dumb-
init/releases/download/v1.1.3/dumb-init_1.1.3_amd64.deb && \  
dpkg -i /tmp/dumb-init.deb  
  
  
# Install php extensions  
RUN docker-php-ext-install \  
bcmath \  
zip  
  
# Install pecl extensions  
RUN pecl install mongodb xdebug && \  
docker-php-ext-enable mongodb && \  
docker-php-ext-install mysqli pdo_mysql && \  
docker-php-ext-enable xdebug  
  
# Configure php  
RUN echo "date.timezone = UTC" >> /usr/local/etc/php/php.ini && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) mbstring zip gd xml pdo pdo_mysql soap
mcrypt  
  
# Install composer  
ENV COMPOSER_ALLOW_SUPERUSER=1  
RUN curl -sS https://getcomposer.org/installer | php -- \  
\--filename=composer \  
\--install-dir=/usr/local/bin  
RUN composer global require --optimize-autoloader \  
"hirak/prestissimo"  
  
# Install official PhantomJS release  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl \  
&& mkdir /tmp/phantomjs \  
&& curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
| tar -xj --strip-components=1 -C /tmp/phantomjs \  
&& mv /tmp/phantomjs/bin/phantomjs /usr/local/bin \  
# Install dumb-init (to handle PID 1 correctly).  
# https://github.com/Yelp/dumb-init  
&& curl -Lo /tmp/dumb-init.deb https://github.com/Yelp/dumb-
init/releases/download/v1.1.3/dumb-init_1.1.3_amd64.deb \  
&& dpkg -i /tmp/dumb-init.deb \  
# Clean up  
&& apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/*  
# The end of the PhantomJS installation.  
# Clean up  
RUN apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/*  
  
## Prepare application  
#WORKDIR /repo  
#  
## Install vendor  
#COPY ./composer.json /repo/composer.json  
#RUN composer install --prefer-dist --optimize-autoloader  
#  
## Add source-code  
#COPY . /repo  
#  
#ENV PATH /repo:${PATH}  
# Setup Supervisor.  
RUN mkdir -p /var/log/supervisor \  
&& mkdir -p /etc/supervisor/conf.d  
  
RUN { \  
echo '[supervisord]'; \  
echo 'nodaemon=false'; \  
echo '[program:phantomjs]'; \  
echo 'command=/bin/bash -c "phantomjs --webdriver=4444"'; \  
echo 'autostart=true'; \  
echo 'autorestart=true'; \  
echo '[program:php-fpm7.1]'; \  
echo 'command=/usr/local/bin/php'; \  
echo 'autostart=true'; \  
echo 'autorestart=true'; \  
} > /etc/supervisor/conf.d/supervisord.conf  
  
  
EXPOSE 4444  
# Prepare host-volume working directory  
RUN mkdir /project  
WORKDIR /project  
  
ENTRYPOINT ["/usr/bin/supervisord"]  

