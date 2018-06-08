FROM tomsowerby/php-5.3:cli  
  
# BASE  
# Packages  
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
&& rm -r /var/lib/apt/lists/*  
  
# Freetype 5.3 bug  
RUN mkdir /usr/include/freetype2/freetype \  
&& ln -s /usr/include/freetype2/freetype.h
/usr/include/freetype2/freetype/freetype.h  
  
# PHP Extensions  
RUN docker-php-ext-install mcrypt zip bz2 mbstring \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
# Memory Limit  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
  
# Time Zone  
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
$PHP_INI_DIR/conf.d/date_timezone.ini  
  
# Environmental Variables  
ENV COMPOSER_HOME /root/composer  
  
# Display PHP version  
RUN php --version  
  
# Set up the application directory  
VOLUME ["/app"]  
WORKDIR /app  
  
# Set up the command arguments  
CMD ["-"]  
ENTRYPOINT ["composer", "--ansi"]  
  
# COMPOSER  
ENV COMPOSER_VERSION 1.0.0-alpha11  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer --version=${COMPOSER_VERSION}  
  
# Display version information  
RUN composer --version  

