FROM php:7-apache  
  
WORKDIR /var/www/html  
  
RUN apt-get update \  
&& apt-get install -y \  
cron \  
libcurl4-openssl-dev \  
wget \  
unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& cd /tmp \  
&& wget https://github.com/graulund/tweetnest/archive/master.zip \  
&& unzip master.zip \  
&& mv tweetnest-master/* /var/www/html \  
&& rm -r tweetnest-master \  
&& rm master.zip \  
&& a2enmod rewrite \  
&& mkdir /config \  
&& mv /var/www/html/inc/config.php /config/config.php \  
&& cp /config/config.php /tmp/config.php \  
&& ln -s /config/config.php /var/www/html/inc/config.php \  
&& chown -R www-data:www-data /config  
  
RUN docker-php-ext-install -j$(nproc) curl \  
&& docker-php-ext-install -j$(nproc) json \  
&& docker-php-ext-install -j$(nproc) mysqli  
  
COPY run.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/run.sh  
COPY tweetnest-cron /etc/cron.d/  
  
EXPOSE 80  
ENTRYPOINT ["/usr/local/bin/run.sh"]  

