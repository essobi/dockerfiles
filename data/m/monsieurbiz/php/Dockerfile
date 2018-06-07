FROM php:5-apache  
  
LABEL maintainer "Monsieur Biz <docker@monsieurbiz.com>"  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
libmcrypt4 \  
libcurl3-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev libicu-dev \  
libxml2-dev \  
libpcre3-dev \  
libxslt-dev \  
zip unzip git vim mysql-client ssmtp cron wget \  
&& docker-php-ext-configure gd --with-gd --with-freetype-dir=/usr/include/
--with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/ \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install -j$(nproc) pdo_mysql mcrypt gd exif intl soap
opcache calendar zip xsl bcmath \  
&& rm -rf /var/lib/apt/lists/*  
  
# Use composer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --snapshot \  
&& rm -f /tmp/composer-setup.*  
  
# Blackfire  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini  
  
# Set timezone to UTC (as always)  
RUN rm /etc/localtime \  
&& ln -s /usr/share/zoneinfo/UTC /etc/localtime \  
&& date \  
&& printf "date.timezone=UTC\n" > $PHP_INI_DIR/conf.d/timezone.ini  
  
# Enable modules  
RUN a2enmod rewrite headers ssl deflate  
  
# Remove default vhost  
# If you want a vhost, add it with your own configuration  
RUN rm -f /etc/apache2/sites-enabled/000-default.conf  
  
# Change working directory  
WORKDIR /var/www  
  
# Change CMD to have cron running  
RUN echo "#!/bin/sh\ncron\n/usr/local/bin/apache2-foreground" > /usr/bin/run  
RUN chmod u+x /usr/bin/run  
CMD ["run"]  

