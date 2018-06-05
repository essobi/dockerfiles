FROM php:7.0.8-fpm  
MAINTAINER Duy <duy@dwork.vn>  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update \  
&& apt-get install -y \  
cron \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev \  
nodejs  
  
RUN docker-php-ext-configure \  
gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/  
  
RUN docker-php-ext-install \  
gd \  
intl \  
mbstring \  
mcrypt \  
pdo_mysql \  
soap \  
xsl \  
zip  
  
RUN curl -sS https://getcomposer.org/installer | \  
php -- \  
\--install-dir=/usr/local/bin \  
\--filename=composer \  
\--version=1.1.2  
  
RUN composer config -g repositories.magento '{ "type": "composer", "url":
"https://repo.magento.com/" }'  
RUN composer config -g http-basic.repo.magento.com
a2c82563ebbece3279b5b958b8174f71 c019af644525528b713ad362e76c86b6  
RUN composer global config minimum-stability alpha  
RUN composer global require "hirak/prestissimo:^0.3"  
  
RUN npm install -g grunt-cli  
  
ENV PHP_MEMORY_LIMIT 2G  
ENV PHP_PORT 9000  
ENV PHP_PM dynamic  
ENV PHP_PM_MAX_CHILDREN 10  
ENV PHP_PM_START_SERVERS 4  
ENV PHP_PM_MIN_SPARE_SERVERS 2  
ENV PHP_PM_MAX_SPARE_SERVERS 6  
ENV APP_MAGE_MODE default  
ENV COMPOSER_HOME /root/.composer/  
  
# COPY conf/www.conf /usr/local/etc/php-fpm.d/  
COPY conf/php.ini /usr/local/etc/php/  
COPY conf/php-fpm.conf /usr/local/etc/  
COPY bin/* /usr/local/bin/  
  
WORKDIR /srv/www  
  
RUN composer create-project --repository-url=https://repo.magento.com/
magento/project-community-edition  
RUN rm -rf ./project-community-edition  
  
RUN apt-get clean  
RUN rm -rf /root/.composer/cache/repo  
CMD ["/usr/local/bin/start"]  

