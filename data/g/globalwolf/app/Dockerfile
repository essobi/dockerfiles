FROM ubuntu:14.04  
  
MAINTAINER Edward Cho <echo@lwolf.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y --force-yes software-properties-common \  
&& LANG=C.UTF-8 add-apt-repository ppa:ondrej/php \  
&& apt-get clean \  
&& apt-get update \  
&& apt-get install -y --force-yes \  
openssh-server \  
curl \  
git \  
g++ \  
libicu-dev \  
libkrb5-dev \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libmcrypt-dev \  
libpng12-dev \  
libc-client2007e-dev \  
libgearman-dev \  
libxslt1-dev \  
freetds-dev \  
libsybdb5 \  
tdsodbc \  
unixODBC-dev \  
apache2 \  
php5.6 \  
php5.6-cli \  
libapache2-mod-php5.6 \  
php5.6-gd \  
php5.6-json \  
php5.6-curl \  
php5.6-mbstring \  
php5.6-mcrypt \  
php5.6-xsl \  
php5.6-intl \  
php5.6-mysqlnd \  
php5.6-imap \  
php5.6-odbc \  
php5.6-imagick \  
php5.6-redis \  
php5.6-gearman \  
php5.6-sybase \  
php5.6-xdebug \  
zip \  
unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/www/html \  
&& chown -R www-data:www-data /var/log/apache2 /var/www \  
&& a2dismod mpm_event \  
&& a2enmod mpm_prefork rewrite  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /var/log/php && chmod 777 /var/log/php \  
&& mkdir /THUMBNAILS && chown www-data:www-data /THUMBNAILS && chmod 777
/THUMBNAILS \  
&& mkdir /LISTINGMEDIA  
  
COPY freetds/* /etc/freetds/  
  
ENV COMPOSER_PROCESS_TIMEOUT=2000  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer global require hirak/prestissimo  
  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

