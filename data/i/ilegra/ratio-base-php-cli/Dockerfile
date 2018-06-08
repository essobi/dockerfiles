FROM ilegra/php:5.5-cli  
  
  
WORKDIR /var/www/html  
ENTRYPOINT [ "/entrypoint-base.sh" ]  
  
ENV DEBIAN_FRONTEND=noninteractive IMG_TYPE=base RATIO_ENVIRONMENT=dev  
  
RUN groupadd -g 1100 ratio \  
&& useradd -g 1100 -u 1100 -d /var/www -M ratio \  
&& mkdir -p /var/www/html /ratio_data/documentos || true \  
&& chown -Rv ratio. /var/www /ratio_data  
  
RUN apt-get update \  
&& apt-get install -y \  
libgearman-dev libicu-dev libcurl3-dev libmcrypt-dev \  
zlib1g-dev libmemcached-dev libxml2-dev git libxrender1 libpng-dev
libfontconfig  
  
# Remover quando puder!  
RUN apt-get install -y unoconv  
  
ADD https://github.com/jwilder/dockerize/releases/download/v0.0.3/dockerize-
linux-amd64-v0.0.3.tar.gz /tmp/  
ADD https://pecl.php.net/get/gearman-1.1.2.tgz /usr/src/php/ext/  
ADD https://s3.amazonaws.com/ratio-apt-
repos/jars/libjpeg8_8d-1deb7u1_amd64.deb /tmp/libjpeg8.deb  
ADD http://repo.zabbix.com/zabbix-official-repo.key /tmp/zabbix.key  
ADD https://getcomposer.org/installer /tmp/composer-installer.php  
  
RUN tar -C /usr/local/bin -xzvf /tmp/dockerize-linux-amd64-v0.0.3.tar.gz \  
&& rm -vf /tmp/dockerize-linux-amd64-v0.0.3.tar.gz \  
&& cat /tmp/zabbix.key | apt-key add - \  
&& echo 'deb http://repo.zabbix.com/zabbix/3.0/debian jessie main' >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y zabbix-sender \  
&& dpkg -i /tmp/libjpeg8.deb \  
&& rm -vf /tmp/libjpeg8.deb  
  
RUN php /tmp/composer-installer.php  
  
RUN mv composer.phar /usr/bin/composer \  
&& cd /usr/src/php/ext/ \  
&& for i in *.tgz; do tar -zxvf $i; done \  
&& mv gearman-1.1.2/ gearman/ \  
&& rm -vf *.tgz \  
&& ls -l /usr/src/php/ext/ \  
&& docker-php-ext-install pdo_mysql opcache gearman intl curl mcrypt soap zip
mbstring bcmath  
  
RUN apt-get clean \  
&& apt-get autoremove -y  
  
ADD templates /templates  
ADD entrypoint-base.sh /  
  
RUN chmod +x /entrypoint-base.sh \  
&& cp /templates/php.tmpl /usr/local/etc/php/php.ini  

