FROM php:5-fpm-alpine  
  
RUN apk update \  
&& apk add icu-dev zlib-dev graphviz git openssh \  
&& docker-php-ext-install mysqli pdo pdo_mysql intl zip mbstring iconv  
  
RUN apk add gnu-libiconv --update-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing/ --allow-untrusted  
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
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
  
RUN apk update \  
&& apk add autoconf g++ make \  
&& pecl install xdebug-2.5.5 \  
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
  
RUN echo "date.timezone=Europe/London" > /usr/local/etc/php/conf.d/zz-
custom.ini \  
&& echo "error_reporting = E_ALL" >> /usr/local/etc/php/conf.d/zz-custom.ini \  
&& echo "display_errors = on" >> /usr/local/etc/php/conf.d/zz-custom.ini \  
&& echo "session.autostart=0" >> /usr/local/etc/php/conf.d/zz-custom.ini  
  
ENV PATH "$PATH:/var/www/html/vendor/bin"  
RUN echo "env[\"XDEBUG_CONFIG\"] = \$XDEBUG_CONFIG" >> /usr/local/etc/php-
fpm.d/zz-docker.conf  
  

