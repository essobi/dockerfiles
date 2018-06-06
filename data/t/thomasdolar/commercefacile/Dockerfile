FROM php:7.0-fpm  
  
MAINTAINER thomasdolar@gmail.com  
  
RUN apt-get update && apt-get install -y \  
git cron curl \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
mysql-client \  
libgmp-dev \  
libpq-dev \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt mbstring pdo_mysql pdo
pdo_pgsql bcmath gmp \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-enable bcmath  
  
# install supervisor  
RUN apt-get install -y supervisor && \  
mkdir -p /var/log/supervisor  
COPY .docker/conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | /usr/local/bin/php --
--install-dir=/usr/local/bin --filename=composer  
  
RUN apt-get update \  
&& apt-get -y autoremove && apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# add entry to crontab  
RUN (crontab -l 2>/dev/null; echo "* * * * * /usr/local/bin/php
/var/www/artisan schedule:run >> /dev/null 2>&1")| crontab -  
  
COPY . /var/www  
  
WORKDIR /var/www  
  
RUN /usr/local/bin/php /usr/local/bin/composer install  
  
RUN chown -R www-data ./storage && chmod -R 0770 ./storage  
  
# set container entrypoints  
ENTRYPOINT ["/bin/bash","-c"]  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

