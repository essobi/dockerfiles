FROM debian:stretch  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
# For getting composer  
wget \  
# For editing configurations  
vim \  
# Apache stuff  
apache2-bin apache2 apache2-dev \  
# For converting TGA  
imagemagick \  
# For running 32 bit binaries  
lib32z1 lib32ncurses5 \  
# For composer fallback  
git \  
# PHP  
php-cgi \  
php-cli \  
php-memcached \  
php-gd \  
php-imagick \  
php-xml \  
php-zip \  
libapache2-mod-php \  
php-mysql \  
php-curl \  
php-mbstring \  
# For model viewer  
ruby \  
# For coffee-script and browserify  
npm \  
python-certbot-apache \  
&& apt-get clean \  
&& apt-get autoclean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Install composer  
RUN wget https://getcomposer.org/installer \  
&& php installer \  
&& mv composer.phar /usr/bin/composer \  
&& rm -f installer \  
# Install PHPUnit  
&& composer global require phpunit/phpunit \  
&& composer global require phpunit/dbunit \  
&& ln -s /root/.composer/vendor/bin/* /usr/bin/  
# Install coffee-script and browserify  
RUN npm install -g coffee-script browserify babel-cli  
  
COPY . /tmp/install  
  
RUN echo "" \  
# Symlink node  
&& ln -s $(which nodejs) /usr/bin/node \  
# Disable Apache mpm_event  
&& a2dismod mpm_event \  
&& a2enmod rewrite \  
&& a2enmod headers \  
&& a2enmod expires \  
&& a2enmod ssl \  
&& a2enmod socache_shmcb \  
&& a2enmod proxy_http \  
&& a2enmod proxy_wstunnel \  
&& a2dissite 000-default \  
# Install configuration addition  
&& cat /tmp/install/apache2.conf >> /etc/apache2/apache2.conf \  
# Install launch configure script  
&& mv /tmp/install/configure.sh /usr/bin/configure-base \  
&& chmod +x /usr/bin/configure-base \  
# Install certificate management script  
&& mv /tmp/install/check-certs.sh /usr/bin/check-certs \  
&& chmod +x /usr/bin/check-certs \  
# Install apache foreground script  
&& mv /tmp/install/apache2-foreground.sh /usr/bin/apache2-foreground \  
&& chmod +x /usr/bin/apache2-foreground \  
&& rm -rf /tmp/install  
  
EXPOSE 80 443  
  
VOLUME /etc/letsencrypt  
  
CMD configure-base > /etc/php/7.0/apache2/php.ini \  
&& check-certs \  
&& apache2-foreground  

