FROM php:apache  
  
MAINTAINER ODY <ody@gmail.com>  
  
RUN apt-get -y update && apt-get -y upgrade \  
&& echo 'Europe/Moscow' > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata \  
&& rm -frv /var/www/html/*  
  
COPY src/zabbix-2.2.10.tar.gz /tmp/  
COPY container-files /  
  
RUN a2enconf zabbix.conf \  
&& cd /tmp \  
&& tar -xvzf zabbix-2.2.10.tar.gz \  
&& rm -fv zabbix-2.2.10.tar.gz \  
&& cp -rv zabbix-2.2.10/frontends/php/* /var/www/html/ \  
&& rm -frv zabbix-2.2.10/ \  
&& docker-php-ext-install mysqli bcmath mbstring sockets \  
&& apt-get -y install libpng12-dev libjpeg-dev libfreetype6-dev libvpx-dev
libxpm-dev \  
&& docker-php-ext-configure gd --with-png-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \--with-freetype-dir=/usr/include/ \--with-vpx-
dir=/usr/include/ \--with-xpm-dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install gettext  
  

