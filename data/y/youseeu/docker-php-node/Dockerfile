FROM ubuntu:16.04  
MAINTAINER Aleksandr Belous  
  
RUN apt-get update -y  
RUN apt-get install -y \  
vim \  
zip \  
curl \  
wget \  
git \  
imagemagick \  
apache2 \  
php7.0 \  
php7.0-cli \  
libapache2-mod-php7.0 \  
php7.0-intl \  
php7.0-gd \  
php7.0-curl \  
php7.0-mysql \  
php-pear \  
php7.0-dev \  
php-xdebug \  
php-mbstring \  
php7.0-mbstring \  
php-memcached \  
php-memcache  
  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Set the locale  
RUN apt-get clean && apt-get update && apt-get install -y locales  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
## install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
## install timezonedb  
RUN pecl install timezonedb  
RUN sed -i '$ a\extension=timezonedb.so' /etc/php/7.0/apache2/php.ini  
RUN sed -i '$ a\extension=timezonedb.so' /etc/php/7.0/cli/php.ini  
  
## install ffmpeg  
ADD ffmpeg-release-64bit-static.tar.xz /usr/local/bin  
RUN ln -s /usr/local/bin/ffmpeg-2.7-64bit-static/ffmpeg /usr/local/bin/ffmpeg
\  
&& ln -s /usr/local/bin/ffmpeg-2.7-64bit-static/ffprobe /usr/local/bin/ffprobe  
  
## config php  
RUN sed -i '$ a\xdebug.var_display_max_depth=4' /etc/php/7.0/mods-
available/xdebug.ini  
RUN sed -i '$ a\xdebug.max_nesting_level=500' /etc/php/7.0/mods-
available/xdebug.ini  
RUN sed -i '$ a\xdebug.var_display_max_data=-1' /etc/php/7.0/mods-
available/xdebug.ini  
RUN sed -i '$ a\xdebug.remote_enable=1' /etc/php/7.0/mods-available/xdebug.ini  
RUN sed -i '$ a\xdebug.remote_autostart=1' /etc/php/7.0/mods-
available/xdebug.ini  
RUN sed -i '$ a\xdebug.remote_connect_back=0' /etc/php/7.0/mods-
available/xdebug.ini  
RUN sed -i '$ a\xdebug.remote_handler=dbgp' /etc/php/7.0/mods-
available/xdebug.ini  
RUN sed -i '$ a\xdebug.profiler_enable=0' /etc/php/7.0/mods-
available/xdebug.ini  
RUN sed -i '$ a\xdebug.profiler_output_dir="/var/www/html"' /etc/php/7.0/mods-
available/xdebug.ini  
RUN sed -i '$ a\xdebug.remote_port=9000' /etc/php/7.0/mods-
available/xdebug.ini  
RUN sed -i '$ a\xdebug.remote_host="127.0.0.1"' /etc/php/7.0/mods-
available/xdebug.ini  
  
RUN sed -i '$ a\opcache.max_accelerated_files=20000' /etc/php/7.0/mods-
available/opcache.ini  
RUN sed -i '$ a\opcache.interned_strings_buffer=8' /etc/php/7.0/mods-
available/opcache.ini  
RUN sed -i '$ a\opcache.memory_consumption=384' /etc/php/7.0/mods-
available/opcache.ini  
RUN sed -i '$ a\opcache.revalidate_freq=0' /etc/php/7.0/mods-
available/opcache.ini  
#RUN sed -i '$ a\opcache.validate_timestamps=0' /etc/php/7.0/mods-
available/opcache.ini  
#RUN sed -i '$ a\opcache.fast_shutdown=1' /etc/php/7.0/mods-
available/opcache.ini  
RUN sed -i '$ a\opcache.enable_cli=0' /etc/php/7.0/mods-available/opcache.ini  
RUN sed -i '$ a\opcache.enable=1' /etc/php/7.0/mods-available/opcache.ini  
  
RUN sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g'
/etc/php/7.0/apache2/php.ini  
RUN sed -ri 's/^;date.timezone\s*=/date.timezone = UTC/g'
/etc/php/7.0/apache2/php.ini  
RUN sed -ri 's/^memory_limit\s*=\s*128M/memory_limit = 512M/g'
/etc/php/7.0/apache2/php.ini  
RUN sed -ri 's/^post_max_size\s*=\s*8M/post_max_size = 2048M/g'
/etc/php/7.0/apache2/php.ini  
RUN sed -ri 's/^upload_max_filesize\s*=\s*2M/upload_max_filesize = 2048M/g'
/etc/php/7.0/apache2/php.ini  
  
RUN sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g'
/etc/php/7.0/cli/php.ini  
RUN sed -ri 's/^;date.timezone\s*=/date.timezone = UTC/g'
/etc/php/7.0/cli/php.ini  
RUN sed -ri 's/^memory_limit\s*=\s*128M/memory_limit = 512M/g'
/etc/php/7.0/cli/php.ini  
RUN sed -ri 's/^post_max_size\s*=\s*8M/post_max_size = 2048M/g'
/etc/php/7.0/cli/php.ini  
RUN sed -ri 's/^upload_max_filesize\s*=\s*2M/upload_max_filesize = 2048M/g'
/etc/php/7.0/cli/php.ini  
  
## Disable xdebug for apache  
RUN rm -rf /etc/php/7.0/apache2/conf.d/20-xdebug.ini  
  
## config apache  
RUN a2enmod rewrite ssl headers proxy proxy_http proxy_wstunnel  
RUN mkdir /etc/apache2/ssl  
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout
/etc/apache2/ssl/app.key -out /etc/apache2/ssl/app.crt -subj /C=US/ST=New\
York/L=New\ York\ City/O=SuperDeveloper/OU=Developers/CN=localhost  
  
RUN a2dissite 000-default  
COPY app_vhost.conf /etc/apache2/sites-available/  
COPY app_vhost_ssl.conf /etc/apache2/sites-available/  
RUN a2ensite app_vhost app_vhost_ssl  
  
RUN mkdir -p /usr/local/openssl/include/openssl/ && \  
ln -s /usr/include/openssl/evp.h /usr/local/openssl/include/openssl/evp.h && \  
mkdir -p /usr/local/openssl/lib/ && \  
ln -s /usr/lib/x86_64-linux-gnu/libssl.a /usr/local/openssl/lib/libssl.a && \  
ln -s /usr/lib/x86_64-linux-gnu/libssl.so /usr/local/openssl/lib/  
  
RUN pecl install mongodb  
  
RUN echo "extension=mongodb.so" > /etc/php/7.0/mods-available/mongodb.ini  
RUN ln -s /etc/php/7.0/mods-available/mongodb.ini
/etc/php/7.0/cli/conf.d/20-mongodb.ini  
RUN ln -s /etc/php/7.0/mods-available/mongodb.ini
/etc/php/7.0/apache2/conf.d/20-mongodb.ini  
  
EXPOSE 80 443  
#RUN mkdir -p /home/webapp/htdocs/web/  
#COPY index.php /home/webapp/htdocs/web/  
#  
#RUN mkdir -p /home/webapp/htdocs/app/cache  
#RUN chown www-data:www-data /home/webapp/htdocs/app/cache  
#VOLUME /home/webapp/htdocs/app/cache  
#  
#RUN mkdir /home/webapp/htdocs/app/logs  
#RUN chown www-data:www-data /home/webapp/htdocs/app/logs  
#VOLUME /home/webapp/htdocs/app/logs  
RUN mkdir /unison  
RUN mkdir -p /home/webapp  
  
RUN ln -s /unison /home/webapp/htdocs  
  
RUN mkdir /unison/web  
COPY index.php /unison/web/  
  
VOLUME /unison  
  
COPY app_start.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/app_start.sh  
  
CMD ["/usr/local/bin/app_start.sh"]  

