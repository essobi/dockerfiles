# PHP 7 with Supervisor for running Workers  
# Based on carlosbuenosvinos/php-with-supervisor-for-workers  
# Carlos Buenosvinos <carlos.buenosvinos@gmail.com>  
FROM php:cli  
  
RUN pecl install mysql redis  
  
# Install modules  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libpq-dev \  
apt-utils \  
mysql-client \  
zlib1g-dev \  
git \  
imagemagick \  
unzip \  
mailutils \  
ssmtp  
  
# Install required RabbitMQ modules  
RUN docker-php-ext-install -j$(nproc) bcmath  
  
# Install Drupal required modules  
RUN docker-php-ext-install -j$(nproc) pdo_mysql mbstring opcache \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install -j$(nproc) exif  
  
# imagemagick as PHP extension  
RUN apt-get install -y libmagickwand-6.q16-dev --no-install-recommends \  
&& pecl install imagick \  
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini  
  
# Set timezone  
RUN rm /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/Copenhagen /etc/localtime  
RUN "date"  
  
# Type docker-php-ext-install to see available extensions  
RUN docker-php-ext-install -j$(nproc) pdo pdo_mysql  
RUN echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini  
  
RUN apt-get update && apt-get install -y supervisor && apt-get clean  
RUN mkdir -p /var/log/supervisor /usr/src/app  
  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
VOLUME ["/etc/supervisor/conf.d", "/usr/src/app"]  
  
EXPOSE 9001  
CMD ["/usr/bin/supervisord"]

