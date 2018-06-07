FROM psfoundation/webapp:php-5.6  
MAINTAINER Przemek Szalko <przemek@mobtitude.com>  
  
ENV XDEBUG_VERSION=2.4.1 \  
TERM="xterm" \  
APPLICATION_ENV="docker-development" \  
VIRTUAL_HOST=""  
# 1. Install xdebug  
# 2. Install additional packages  
RUN docker-php-source extract \  
&& ( \  
curl -sLo /tmp/xdebug.tgz http://xdebug.org/files/xdebug-$XDEBUG_VERSION.tgz \  
&& mkdir -p /tmp/xdebug \  
&& tar -zxvf /tmp/xdebug.tgz -C /tmp/xdebug --strip-components=1 \  
&& mv /tmp/xdebug /usr/src/php/ext/xdebug \  
&& docker-php-ext-install xdebug \  
) \  
&& rm -rf /tmp/xdebug* \  
&& rm -rf /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \  
&& apt-get update \  
&& apt-get install -y python \  
graphviz \  
pngquant \  
jpegoptim \  
python-scour \  
&& apt-get clean \  
&& docker-php-source delete \  
&& rm -rf /var/lib/apt/lists/*  
  
# Configure services  
COPY conf/php/* $PHP_INI_DIR/  
COPY bin/php-xdebug.sh /usr/local/bin/php-xdebug  
  
RUN chmod +x /usr/local/bin/php-xdebug  
  
CMD ["apache2-foreground"]

