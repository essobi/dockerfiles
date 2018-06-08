FROM php:apache  
  
WORKDIR /var/www/html  
  
RUN apt-get update && apt-get install -y libpng-dev libjpeg62-turbo-dev
libfreetype6-dev libmcrypt-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install mysqli mbstring gd zip  
  
ENV FLYSPRAY_VERSION v1.0-rc6  
  
RUN rm -rf /var/www/html/*  
RUN curl -L -O
https://github.com/Flyspray/flyspray/archive/${FLYSPRAY_VERSION}.tar.gz \  
&& tar -xf ${FLYSPRAY_VERSION}.tar.gz --strip 1 \  
&& rm ${FLYSPRAY_VERSION}.tar.gz  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer install  
  
# Set permissions  
RUN chmod a+w /var/www/html/cache /var/www/html/attachments  
  
# Move the configuration to a directory (exposed as a volume), plus remove
hacks  
RUN mkdir conf \  
&& sed -i "s,flyspray.conf.php,conf/flyspray.conf.php,g" $(grep -l -r
flyspray.conf.php) \  
&& sed -i "/display_errors/d" includes/fix.inc.php \  
&& sed -i "/error_reporting/d" includes/fix.inc.php  
  
COPY config/php.ini /usr/local/etc/php/  
  
VOLUME '/var/www/html/attachments' '/var/www/html/conf'  

