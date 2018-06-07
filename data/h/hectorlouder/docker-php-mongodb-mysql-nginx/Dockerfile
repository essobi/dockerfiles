################################################################################  
# Base image  
################################################################################  
FROM azukiapp/web-based  
  
################################################################################  
# Build instructions  
################################################################################  
  
# Install packages  
RUN apt-get update && apt-get install -y -qq \  
nginx \  
supervisor \  
curl \  
git \  
wget \  
unzip \  
subversion \  
libxml2 \  
libcurl4-openssl-dev \  
php5-dev \  
php5-cli \  
php5-mysql \  
php5-mcrypt \  
php5-curl \  
php5-json \  
php5-gd \  
php5-fpm \  
php-pear \  
php-apc \  
php5-intl \  
php5-xdebug \  
&& pecl install mongodb \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Remove default nginx configs.  
RUN rm -f /etc/nginx/conf.d/*  
  
# Ensure that PHP5 FPM is run as root.  
RUN sed -i "s/user = www-data/user = root/" /etc/php5/fpm/pool.d/www.conf  
RUN sed -i "s/group = www-data/group = root/" /etc/php5/fpm/pool.d/www.conf  
  
# Pass all docker environment  
RUN sed -i '/^;clear_env = no/s/^;//' /etc/php5/fpm/pool.d/www.conf  
  
# Get access to FPM-ping page /ping  
RUN sed -i '/^;ping\\.path/s/^;//' /etc/php5/fpm/pool.d/www.conf  
  
# Get access to FPM_Status page /status  
RUN sed -i '/^;pm\\.status_path/s/^;//' /etc/php5/fpm/pool.d/www.conf  
  
# Prevent PHP Warning: 'xdebug' already loaded.  
# XDebug loaded with the core  
RUN sed -i '/.*xdebug.so$/s/^/;/' /etc/php5/mods-available/xdebug.ini  
  
# Enable MongoDB PHP  
RUN echo "extension=mongodb.so" > /etc/php5/mods-available/mongodb.ini  
RUN php5enmod mcrypt mongodb  
  
# Add configuration files  
COPY conf/nginx.conf /etc/nginx/  
COPY conf/supervisord.conf /etc/supervisor/conf.d/  
COPY conf/php.ini /etc/php5/fpm/conf.d/40-custom.ini  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install phalcon  
RUN git clone --depth=1 git://github.com/phalcon/cphalcon.git  
RUN cd cphalcon/build && ./install 64bits  
RUN echo "extension=phalcon.so" > /etc/php5/fpm/conf.d/30-phalcon.ini  
  
################################################################################  
# Volumes  
################################################################################  
  
VOLUME ["/var/www", "/etc/nginx/conf.d"]  
  
################################################################################  
# Ports  
################################################################################  
  
EXPOSE 80 443 9000  
  
################################################################################  
# Entrypoint  
################################################################################  
  
ENTRYPOINT ["/usr/bin/supervisord"]  

