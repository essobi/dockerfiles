FROM php:5.6-apache  
  
  
COPY . /var/www/html  
  
RUN apt-get update && apt-get install -y \  
vim \  
libssl-dev \  
mysql-client \  
git  
  
# pdo_mysql  
RUN docker-php-ext-install pdo_mysql  
  
# zip  
RUN buildRequirements="zlib1g-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-install zip \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
# soap  
RUN buildRequirements="libxml2-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-install soap \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
#XDebug  
#RUN yes | pecl channel-update pecl.php.net  
# && yes | pecl install xdebug-2.5.0 \  
# && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
# && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
# && echo "xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/xdebug.ini \  
# && echo "xdebug.remote_connect_back=On" >>
/usr/local/etc/php/conf.d/xdebug.ini \  
# && echo "xdebug.remote_handler=dbgp" >> /usr/local/etc/php/conf.d/xdebug.ini
\  
# && echo "xdebug.profiler_enable=0" >> /usr/local/etc/php/conf.d/xdebug.ini \  
# && echo "xdebug.profiler_output_dir=\"/temp/profiledir\"" >>
/usr/local/etc/php/conf.d/xdebug.ini  
# Date  
RUN echo "date.timezone = Europe/Paris" > /usr/local/etc/php/conf.d/date.ini  
  
# Apache  
RUN echo "DocumentRoot /var/www/html/web" >> /etc/apache2/sites-
available/100-default.conf \  
&& ln /etc/apache2/sites-available/100-default.conf /etc/apache2/sites-
enabled/  
  
RUN chmod 777 -Rf /var/www/html/docker/  
RUN chmod 777 /var/www/html/docker/entrypoint.sh  
  
ENTRYPOINT ["/var/www/html/docker/entrypoint.sh"]  

