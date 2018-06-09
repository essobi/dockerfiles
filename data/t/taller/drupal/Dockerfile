FROM nginx:latest  
MAINTAINER Taller Development Team <dev@taller.net.br>  
  
# Configure Debian environment.  
# -----------------------------  
  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# Install dependencies.  
# ---------------------  
  
RUN apt-get update -y \  
&& apt-get install -y \  
bash-completion \  
build-essential \  
bzip2 \  
ca-certificates \  
curl \  
git \  
gzip \  
htop \  
imagemagick \  
libfontconfig1 \  
libjpeg-dev \  
libpng12-dev \  
libpq-dev \  
locales \  
mysql-client \  
nano \  
netcat \  
openconnect \  
php-apc \  
php5-curl \  
php5-fpm \  
php5-gd \  
php5-geoip \  
php5-imagick \  
php5-imap \  
php5-json \  
php5-ldap \  
php5-mcrypt \  
php5-memcached \  
php5-memcache \  
php5-mysqlnd \  
php5-sqlite \  
php5-xdebug \  
php5-xmlrpc \  
python-software-properties \  
rsync \  
sudo \  
ssh \  
tig \  
vim \  
xz-utils \  
wget \  
\--no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* \  
&& rm -rf /var/tmp/*  
  
  
# Configure Composer related environment.  
# ---------------------------------------  
### INSTALL COMPOSER  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_DISABLE_XDEBUG_WARN 1  
# Install Composer.  
# -----------------  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& composer self-update \  
&& composer global require "hirak/prestissimo:^0.3"  
  
# Make sure any sudoer can control libs.  
# --------------------------------------  
  
RUN sudo chmod a+w -R /usr/local  
  
  
# Copy configuration files.  
# -------------------------  
  
COPY ./files/nginx.conf /etc/nginx/nginx.conf  
COPY ./files/fastcgi.conf /etc/nginx/fastcgi.conf  
COPY ./files/fpm.conf /etc/php5/fpm/php-fpm.conf  
COPY ./files/www.conf /etc/php5/fpm/pool.d/www.conf  
COPY ./files/fpm.ini /etc/php5/fpm/php.ini  
COPY ./files/cli.ini /etc/php5/cli/php.ini  
COPY ./files/xdebug.ini /etc/php5/mods-available/xdebug.ini  
COPY ./files/web /var/www/drupal  
  
RUN echo "\n# Start NGINX\nsudo service nginx start" >> /etc/bash.bashrc  

