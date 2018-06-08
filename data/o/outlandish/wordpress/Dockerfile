FROM php:7.1-fpm  
  
  
RUN echo "date.timezone=Europe/London" > /usr/local/etc/php/conf.d/zz-
custom.ini \  
&& echo "error_reporting = E_ALL" >> /usr/local/etc/php/conf.d/zz-custom.ini \  
&& echo "display_errors = on" >> /usr/local/etc/php/conf.d/zz-custom.ini \  
&& echo "session.autostart=0" >> /usr/local/etc/php/conf.d/zz-custom.ini  
  
ENV PATH "$PATH:/var/www/html/vendor/bin"  
RUN apt-get update \  
&& apt-get install -y \  
&& docker-php-ext-install mysqli pdo pdo_mysql  
  
# RUN apt-get update \  
# && apt-get install -y \  
# libicu-dev \  
# && rm -rf /var/lib/apt/lists/* \  
# && docker-php-ext-install intl \  
# && apt-get remove -y \  
# libicu-dev \  
# && apt-get install -y \  
# libicu52 \  
# && apt-get autoremove -y  
RUN apt-get update \  
&& apt-get install libcurl4-openssl-dev -y \  
&& docker-php-ext-install curl \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false libcurl4-openssl-dev -y  
  
RUN apt-get update \  
&& apt-get install libxml2-dev -y \  
&& docker-php-ext-install xml \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false libxml2-dev -y  
  
RUN apt-get update \  
&& apt-get install -y \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install zip \  
&& apt-get remove -y \  
zlib1g-dev \  
&& apt-get install -y \  
zlib1g \  
&& apt-get autoremove -y  
  
RUN apt-get update \  
&& apt-get install -y \  
libmcrypt-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install mcrypt \  
&& apt-get remove -y \  
libmcrypt-dev \  
&& apt-get install -y \  
libmcrypt4 \  
&& apt-get autoremove -  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends libmagickwand-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& pecl install imagick-3.4.3 \  
&& docker-php-ext-enable imagick  
  
RUN apt-get update && \  
apt-get install -y git zip && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \  
php -r "unlink('composer-setup.php');"  
  
RUN curl -OL
https://github.com/phpmetrics/PhpMetrics/releases/download/v2.3.2/phpmetrics.phar
&& \  
chmod +x phpmetrics.phar && \  
mv phpmetrics.phar /usr/local/bin/phpmetrics  
  
RUN curl -OL http://www.phpdoc.org/phpDocumentor.phar && \  
chmod +x phpDocumentor.phar && \  
mv phpDocumentor.phar /usr/local/bin/phpdoc  
  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar && \  
chmod +x wp-cli.phar && \  
mv wp-cli.phar /usr/local/bin/wp  
  
RUN apt-get update \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_port=9001" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.profiler_enable=1" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.profiler_enable_trigger=1" >>
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \  
&& echo "xdebug.profiler_output_dir=/app/profiling" >>
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  

