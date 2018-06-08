FROM ubuntu:trusty  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common python-software-properties  
  
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php \  
&& apt-get update \  
&& apt-get install -y \  
git \  
unzip \  
curl \  
wget \  
apache2 \  
libapache2-mod-php7.1 \  
libapache2-mod-rpaf \  
libapache2-mod-fastcgi \  
php7.1-cli \  
php7.1-mbstring \  
php7.1-xml \  
php7.1-soap \  
php7.1-curl \  
php7.1-mcrypt \  
php7.1-gd \  
php7.1-bz2 \  
php7.1-zip \  
php7.1-mysql \  
php7.1-fpm \  
php7.1-sqlite3 \  
php7.1-bcmath \  
php7.1-intl \  
php7.1-opcache \  
php-xdebug \  
php-redis \  
mysql-client \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN a2enmod rewrite && \  
a2enmod rpaf && \  
a2enmod actions && \  
a2enmod fastcgi && \  
a2enmod vhost_alias && \  
a2enmod headers \  
&& a2enmod proxy_fcgi setenvif \  
&& a2enconf php7.1-fpm \  
&& phpenmod opcache \  
# Composer  
&& curl -fSL "https://getcomposer.org/installer" -o composer-setup.php \  
&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer \  
&& rm composer-setup.php \  
# Drush  
&& composer global require drush/drush:8.*; \  
ln -s /root/.composer/vendor/bin/drush /usr/local/bin/drush;  
  
COPY files/000-default.conf /etc/apache2/sites-enabled/  
  
EXPOSE 80  
  
WORKDIR /var/www/html  
  
CMD ["apache2ctl", "-D", "FOREGROUND"]  

