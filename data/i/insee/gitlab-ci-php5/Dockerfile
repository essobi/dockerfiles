FROM php:5  
MAINTAINER Michal Swietochowski <m.swietochowski@insee.pl>  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libbz2-dev \  
php-pear \  
curl \  
git \  
subversion \  
unzip \  
&& rm -r /var/lib/apt/lists/*  
  
# PHP Extensions  
RUN docker-php-ext-install mcrypt zip bz2 mbstring \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
# Memory Limit  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
  
# Time Zone  
RUN echo "date.timezone=Europe/Warsaw" > $PHP_INI_DIR/conf.d/date_timezone.ini  
  
VOLUME /root/composer  
  
# Environmental Variables  
ENV COMPOSER_HOME /root/composer  
ENV COMPOSER_GLOBAL /usr/share/php/composer  
ENV PATH $PATH:$COMPOSER_GLOBAL/vendor/bin  
  
# Display PHP version  
RUN php --version  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN composer --version  
  
COPY rulesets /root/  
COPY composer.json $COMPOSER_GLOBAL/  
  
RUN cd $COMPOSER_GLOBAL && composer install  
  
RUN phpcs --config-set installed_paths
$COMPOSER_GLOBAL/vendor/escapestudios/symfony2-coding-standard  
RUN phpcs -i  

