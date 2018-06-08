FROM samtayuk/nginx-php:php7  
MAINTAINER Samuel Taylor "samtaylor.uk@gmail.com"  
ENV SOLDER_VERSION 0.7.3.1  
RUN curl -S https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
RUN cd /app && wget -qO-
https://github.com/TechnicPack/TechnicSolder/archive/v$SOLDER_VERSION.tar.gz |
tar xz \  
&& mv TechnicSolder-$SOLDER_VERSION solder \  
&& cd /app/solder \  
&& apt-get update && apt-get -y install git \  
&& composer install --no-dev --no-interaction \  
&& apt-get -y purge git \  
&& apt-get -y autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -f /app/solder/app/config/app.php \  
/app/solder/app/config/database.php \  
/app/solder/app/config/solder.php \  
&& mkdir -p /data /config \  
&& mv /app/solder/public/resources /app/resources \  
&& chown -R www-data:www-data /app/solder  
  
COPY default.app.php default.database.php default.solder.php /app/  
COPY 10-solder.sh /app/firstrun/  
COPY 10-pre_solder.sh /app/prerun/  
COPY default.conf /etc/nginx/conf.d/  
  
VOLUME ["/data", "/config", "/app/solder/app/storage"]

